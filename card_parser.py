def parse_card(instruction_path):

    with open(instruction_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 6:
                if parts[0] == 'ACC1' and parts[2] == 'ACC2' and parts[4] == 'CIRCUIT':
                    acc1 = parts[1]
                    acc2 = parts[3]
                    circuit_name = parts[5]
                    break
                else: 
                    raise Exception("Punch card corrupted!")
            else: 
                raise Exception("Punch card corrupted!")

    return acc1, acc2, circuit_name