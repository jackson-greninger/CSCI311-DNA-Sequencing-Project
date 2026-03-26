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
MATCH = 0       # score when two bases are the same
MISMATCH = -1   # score when two bases differ


def S(base_a, base_b):
    # Substitution score: reward a match, penalize a mismatch
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

    # The bottom-right cell holds the final alignment score
    return F[rows-1][cols-1]


# Compare query against every stored sequence

print(f"Query length: {len(query_sequence)} bases")
print(f"Scoring: match={MATCH}, mismatch={MISMATCH}, gap={d}")
print()
print("Aligning query against all stored sequences...")
print()

best_score = None
best_name  = None

for name, sequence in stored_sequences:
    score = needleman_wunsch(query_sequence, sequence)
    print(f"  Score {score:>8}  |  {name[:70]}")

    if best_score is None or score > best_score:
        best_score = score
        best_name  = name

print()
print(f"Best match (score {best_score}):")
print(f"  {best_name}")
