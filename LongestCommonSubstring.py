def clean_file(database):
    sequences = []
    current_seq = []
    
    file = open(database, "r")

    for line in file:
        line = line.strip()
            
        if line.startswith(">"):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            current_seq.append(line)
        
    return sequences

    if current_seq:
        sequences.append("".join(current_seq))




if __name__ == "__main__":
    # call LCS function
    target = "CSCI311-DNA-Sequencing-Project\DNA_query.txt"
    database = "CSCI311-DNA-Sequencing-Project\DNA_sequences.txt"
    clean_file(database)