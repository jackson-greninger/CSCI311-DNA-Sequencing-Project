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