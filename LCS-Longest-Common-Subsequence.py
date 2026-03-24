def clean_file (DNA_sequences):
    sequences = []
    current_seq = []
    
    file = open(DNA_sequences, "r")

    for line in file:
        line = line.strip()
            
        if line.startswith(">"):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            current_seq.append(line)
        
    return sequences

def clean_file_dict(DNA_sequence):
    sequence_dict = {}
    curr_header = None

    
    file = open(DNA_sequence, "r")

    for line in file:
        line = line.strip()

        if line.startswith(">"):
            curr_header = line[1:]
            sequence_dict[curr_header] = []
        else:
            sequence_dict[curr_header].append(line.upper())
    
    for header in sequence_dict:
        sequence_dict[header] = "".join(sequence_dict[header])

    return sequence_dict

#def find_most_similar_seq(t, dna_sequences):



def lcs(query, full_sequence):
    # do another loop to og through each quence in the full_sequence list 
    # ok so this is the algorithm technically
    m = len(query)
    n = len(full_sequence)

    # initialize  a matrix
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
    clean_database = clean_file(database)
    clean_database1 = clean_file_dict(database)

    print("heloo")
    #print(clean_database)

    #print(lcs(target, clean_database))
    print(clean_database1)

    
        