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



if __name__ == "__main__":
    # call LCS function
    target = "DNA_query.txt"
    database = "DNA_sequences.txt"
    clean_database = clean_file(database)

    print(clean_database)

    
        