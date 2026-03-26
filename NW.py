"""Needleman-Wunsch sequence alignment"""


# Load the query sequence
with open("DNA_query.txt", "r") as f:
    query_sequence = "".join(line.strip() for line in f)


# Load stored sequences storing each as a tuple: (name, sequence)
stored_sequences = []
with open("DNA_sequences.txt", "r") as f:
    current_name = None
    current_sequence_lines = []

    for line in f:
        line = line.strip()

        if line.startswith(">"):
            # Save the previous entry before starting a new one
            if current_name is not None:
                sequence = "".join(current_sequence_lines)
                stored_sequences.append((current_name, sequence))

            # The name is everything after the ">"
            current_name = line[1:]
            current_sequence_lines = []

        elif line:
            current_sequence_lines.append(line)

    # Save the last entry in the file
    if current_name is not None:
        sequence = "".join(current_sequence_lines)
        stored_sequences.append((current_name, sequence))


# Scoring settings (https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm#Basic_scoring_schemes)
d = -1          # gap penalty
MATCH = 0       # length when two bases are the same
MISMATCH = -1   # length when two bases differ


def S(base_a, base_b):
    # Substitution length: reward a match, penalize a mismatch
    if base_a == base_b:
        return MATCH
    else:
        return MISMATCH


# Needleman-Wunsch scoring matrix
def needleman_wunsch(A, B):
    rows = len(A) + 1
    cols = len(B) + 1

    # Build an empty rows x cols grid filled with zeros
    F = [[0] * cols for _ in range(rows)]

    # Fill the first column: aligning A[0..i] against an empty string
    for i in range(rows):
        F[i][0] = d * i

    # Fill the first row: aligning an empty string against B[0..j]
    for j in range(cols):
        F[0][j] = d * j

    # Fill the rest of the grid
    for i in range(1, rows):
        for j in range(1, cols):
            match  = F[i-1][j-1] + S(A[i-1], B[j-1])    # diagonal: align Ai with Bj
            delete = F[i-1][j]   + d                    # up:       gap in B
            insert = F[i][j-1]   + d                    # left:     gap in A
            F[i][j] = max(match, delete, insert)

    # The bottom-right cell holds the final alignment length
    # return F[rows-1][cols-1]
    return F #return whole grid instead


# Compare query against every stored sequence

print(f"Query length: {len(query_sequence)} bases")
print(f"Scoring: match={MATCH}, mismatch={MISMATCH}, gap={d}")
print()
print("Aligning query against all stored sequences...")
print()

best_length = None
best_name  = None

for name, sequence in stored_sequences:
    F = needleman_wunsch(query_sequence, sequence)
    length = F[len(query_sequence)][len(sequence)]
    print(f"  length {length:>8}  |  {name[:70]}")

    if best_length is None or length > best_length:
        best_length = length
        best_name  = name

print()
print(f"Best match (length {best_length}):")
print(f"  {best_name}")


def run(query_path, sequences_path):
    with open(query_path, "r") as f:
        query = "".join(line.strip() for line in f)

    stored = []
    # sequence processing step
    with open(sequences_path, "r") as f:
        current_name = None
        current_lines = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_name:
                    stored.append((current_name, "".join(current_lines)))
                current_name = line[1:]
                current_lines = []
            elif line:
                current_lines.append(line)
        if current_name:
            stored.append((current_name, "".join(current_lines)))

    best_length = None
    best_name = None
    best_seq = ""

    for name, seq in stored:
        F = needleman_wunsch(query, seq)
        length = F[len(query)][len(seq)]
        if best_length is None or length > best_length:
            best_length = length
            best_name = name

            # backtracking starting in bottom right
            i, j = len(query), len(seq)
            result = ""
            while i > 0 and j > 0:
                if F[i][j] == F[i-1][j-1] + S(query[i-1], seq[j-1]):
                    result += query[i-1]
                    i -= 1
                    j -= 1
                elif F[i][j] == F[i-1][j] + d:
                    i -= 1
                else:
                    j -= 1
            best_seq = result[::-1]

    return best_name, best_length, best_seq