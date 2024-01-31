from circuit import CircuitBehaviour


class Plugboard:
    '''
    This class models a Plugboard found in older computers.
    A plugboard has a Circuit with a certain configuration.
    The plugboard has two accumulators to store the inputs and
    a sink to store the output of the operation performed by the
    circuit.
    The circuit doesn't have direct access to the accumulators, instead
    the values stored in the accumulator are passed to the circuit and the
    output returned from the circuit is stored in the sink
    '''
    
    __circuit: CircuitBehaviour

    __acc1: int = 0
    __acc2: int = 0
    __sink: int = 0


    def __init__(self, circuit: CircuitBehaviour) -> None:
        self.__circuit = circuit

    def exec(self, instructions: str):
        '''
        Used to fire the circuit
        '''
        # parse the instruction file
        with open(instructions, "r") as file:
            for line in file:
                tokens = line.split()

                # Stop reading instructions after encountering END instruction
                if tokens[0] == "END":
                    break
                # SET instruction -> Used to set the values of ACC1, ACC2
                elif tokens[0] == "SET":
                    if tokens[1] == "ACC1":
                        self.__acc1 = int (tokens[2])
                    elif tokens[1] == "ACC2": 
                        self.__acc2 = int (tokens[2])
                    else:
                        raise Exception("Syntax error. Valid tokens for SET"/
                                        "instruction are: ACC1, ACC2")
                # EXEC instruction -> Used to fire the circuit
                elif tokens[0] == "EXEC":
                    self.__sink = self.__circuit.fire(self.__acc1, self.__acc2)
                # PRINT instruction -> Used to print the value stored in SINK
                elif tokens[0] == "PRINT":
                    print(self.__sink)
                # Unrecognised instruction
                else:
                    raise Exception(f"Unrecognised instruction: {tokens[0]}")

        print(f"Program Execution finished.")