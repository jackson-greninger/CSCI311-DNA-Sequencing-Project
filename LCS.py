""""
TODO: MAYBE ADD MORE COMMENTS IN ALGORITHM
"""
import SequenceDictionary as sd

def find_most_similar_seq(t, dna_sequence, headers):
    """
    Searches for the closest DNA sequence to a target sequence (query) using lcs.

    Params:
            t (str) - Target DNA sequence (query).
            dna_sequence (list[str]) - List of DNA sequences from database.
            headers (list[str]) - List of sequences' headers.

    Returns:
            tuple:
                    str - header of the closest DNA sequence.
                    int - index of the closest DNA sequence.
                    str - sequence of the closest DNA sequence.
    """
    # initialize to ensure first comparison always updates
    best_sim = float("-inf")
    best_seq_index = None
    best_seq = ""
    
    for i in range(len(dna_sequence)):
        s_i = dna_sequence[i]
        # call LCS
        sim, seq = lcs(s_i, t)

        # update global best if current sequence is more similar
        if sim > best_sim:
            best_sim = sim
            best_seq_index = i
            best_seq = seq
        
    return headers[best_seq_index], best_sim, best_seq

def lcs(query, full_sequence):
    """
    Calculates the longest common subsequence between two sequences.

    Params:
            query (str) - Target DNA sequence.
            full_sequence (str) - DNA database.

    Returns:
            tuple:
                    int - length of the closest DNA sequence.
                    str - sequence of the closest DNA sequence.
    """
    m = len(query)
    n = len(full_sequence)

    # 1. initialize  a matrix with base cases 0
    # (m+1) x (n+1) table filled with 0s
    dp = [[0] * (n + 1) for _ in range(m+1)]

    # 2. filling in the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the characters match, increment the value from the top-left diagonal 
            if query[i - 1].upper() == full_sequence[j - 1].upper():
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # if they don't match, keep the best score form above or the left
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 3. ACTUAL subsequence
    # start at the bottom-right corener and worl our way back to (0, 0)
    sequence_string = ""
    i = m
    j = n

    while i > 0 and j > 0:
        # if match, it was part of the LCS, move diagonally up-left
        if query[i - 1].upper() == full_sequence[j - 1].upper(): # if the characters match in the query
            sequence_string += query[i - 1] # backtrack to create the string in order; addinging to the sequence string
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            # if not match, move in the direction of the higher score
            # move up
            i -= 1
        else:
            # move left 
            j -= 1

    return dp[m][n], sequence_string[::-1] # return the length of the longest sequence

def run(query_path, database_path):
    """Runs algorithm for GUI"""
    target_dna = sd.open_qery_file(query_path)
    headers, sequences = sd.clean_dna_sequence_dict(database_path)
    best_name, best_score, best_sequence = find_most_similar_seq(target_dna, sequences, headers)
    return best_name, best_score, best_sequence

if __name__ == "__main__":
    # call lcs function
    target = "DNA_query.txt"
    database = "DNA_sequences.txt"
    
    target_dna = sd.open_qery_file(target)
    headers, sequences = sd.clean_dna_sequence_dict(database)

    best_name, best_score, best_sequence = find_most_similar_seq(target_dna, sequences, headers)
    print(f"The most similar sequence is: {best_name}")
    print(f"The Longest Common Subsequence length is: {best_score}")
    print(f"The Sequence String is: {best_sequence}")
