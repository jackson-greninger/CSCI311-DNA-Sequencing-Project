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

        return dp[m][n]


if __name__ == "__main__":
    # call LCS function
    target = "DNA_query.txt"
    database = "DNA_sequences.txt"
    clean_database = clean_file(database)

    print("heloo")
    #print(clean_database)

    print(lcs(target, clean_database))

    
        