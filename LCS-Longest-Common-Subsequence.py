"""
TODO: Switch to dictionary format
    - maybe make a global file to be used with the 3 algorithms
        - Then change dictionary in each individual file to save
        - dosctrings and comments please
"""

import SequenceDictionary as sd

def find_most_similar_seq(t, dna_sequence, headers):
    """
    TODO:
    docstring and comments
    Implementation of algorithm 1 to find the most similar seq
    returns the name of the sequence aswell as the sequence itself
    """

    best_sim = float("-inf")
    best_seq_index = None
    
    for i in range(len(dna_sequence)):
        s_i = dna_sequence[i]

        sim = LCS(s_i, t) # calling function 

        if sim > best_sim:
            best_sim = sim
            best_seq_index = i
        
    return headers[best_seq_index], best_sim

def LCS(query, full_sequence):
    """
    TODO:
    dosctrings and comments please
    """
    m = len(query)
    n = len(full_sequence)
    sequence_string = ""

    # initialize  a matrix with base cases 0
    dp = [[0] * (n+1) for x in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n+1):
            if query[i - 1] == full_sequence[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n] # return the length of the longest sequence

if __name__ == "__main__":
    # call LCS function
    target = "DNA_query.txt"
    database = "DNA_sequences.txt"
    
    target_dna = sd.open_qery_file(target)
    headers, sequences = sd.clean_dna_sequence_dict(database)

    best_name, best_score = find_most_similar_seq(target_dna, sequences, headers)
    print(f"The most similar sequence is: {best_name}")
    print(f"The Longest Common Subsequence length is: {best_score}")


    





# def clean_file (DNA_sequences):
#     sequences = []
#     current_seq = []
    
#     file = open(DNA_sequences, "r")

#     for line in file:
#         line = line.strip()
            
#         if line.startswith(">"):
#             if current_seq:
#                 sequences.append("".join(current_seq))
#                 current_seq = []
#         else:
#             current_seq.append(line)
        
#     return sequences

# def clean_file_dict(DNA_sequence):
#     sequence_dict = {}
#     curr_header = None

    
#     file = open(DNA_sequence, "r")

#     for line in file:
#         line = line.strip()

#         if line.startswith(">"):
#             curr_header = line[1:]
#             sequence_dict[curr_header] = []
#         else:
#             sequence_dict[curr_header].append(line.upper())
    
#     for header in sequence_dict:
#         sequence_dict[header] = "".join(sequence_dict[header])

#     return sequence_dict

#def find_most_similar_seq(t, dna_sequences):