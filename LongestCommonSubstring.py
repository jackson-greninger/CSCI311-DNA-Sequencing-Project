"""
TODO: Switch to dictionary format
    - maybe make a global file to be used with the 3 algorithms
        - Then change dictionary in each individual file to save
        - dosctrings and comments please
"""
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

    if current_seq:
        sequences.append("".join(current_seq))

    return sequences

def LCS(target, database):
    matches = []
    current_match = ""

    for sequence in database:
        for x in target:
            for y in sequence:
                # if we get matching characters (in progress)
                if x == y:
                    current_match += x
                else:
                    continue
        


if __name__ == "__main__":
    target = "DNA_query.txt"
    database = "DNA_sequences.txt"
    
    cleaned_database = clean_file(database)
    print(cleaned_database)

