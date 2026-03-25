def clean_dna_sequence_dict(DNA_sequence):
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

    file.close()
    
    for header in sequence_dict:
        sequence_dict[header] = "".join(sequence_dict[header])

    return list(sequence_dict.keys()), list(sequence_dict.values())

def open_qery_file(query_file):
    with open(query_file, 'r') as f:
        target_dna = f.read().replace("\n", "").strip().upper()
    
    return target_dna