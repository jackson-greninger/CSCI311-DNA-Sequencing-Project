def clean_file(database):
    genes = {}
    current_name = None
    current_seq = []
    
    with open(database, "r") as file:
        for line in file:
            line = line.strip()
            
            if line.startswith(">"):
                if current_name:
                    genes[current_name] = "".join(current_seq)
                
                # remove '>'
                current_name = line[1:] 
                current_seq = []
            else:
                current_seq.append(line)

        # Save the very last gene in the file
        if current_name:
            genes[current_name] = "".join(current_seq)

    return genes

# dp solution we did in class
def LCS(query, database):
    with open(query, "r") as file:
        contents = file.read()

    m = len(contents)
    solutions = []

    for sequence in database.values():
        n = len(sequence)
        dp_table = [[0]*(n+1) for _ in range(m+1)]
        res = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if they equal
                if contents[i-1] == sequence[j-1]:
                    # add to table, then take diagonal bottom right and add one
                    dp_table[i][j] = dp_table[i-1][j-1] + 1
                    res = max(res, dp_table[i][j])
                else:
                    # otherwise, take the maximum between the left and below
                    dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
        solutions.append(res)
    
    index = solutions.index(max(solutions))
    names = list(database.keys())
    name = names[index]
    
    print(f"The closest match to your query is: |{name}| with a common nucloetide string of {max(solutions)}.")
    
    return
        
if __name__ == "__main__":
    query = "DNA_query.txt"
    database = "DNA_sequences.txt"
    
    cleaned_database = clean_file("DNA_sequences.txt")
    
    LCS(query, cleaned_database)

