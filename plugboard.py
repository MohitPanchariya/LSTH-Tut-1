from circuit import CircuitBehaviour

class Plugboard:
    '''
    This class models a Plugboard found in older computers.
    A plugboard has a Circuit with a certain configuration.
    The plugboard has two accumulators to store the inputs and
    another accumulator to store the output of the operation performed by the
    circuit.
    The circuit doesn't have direct access to the accumulators, instead
    the values stored in the accumulator are passed to the circuit and the
    output returned from the circuit is stored in the accumulator
    '''
    
    # The circuit is to be used by the plugboard
    __circuit: CircuitBehaviour

    # The accumulators used to store the operands
    __acc1: int = 0
    __acc2: int = 0

    # The accumulator used to store the output after execution
    __acc3: int = 0


    def set_circuit(self, circuit: CircuitBehaviour):
        '''
        Used to set the circuit for the plugboard
        '''
        self.__circuit = circuit

    def set_accumulator(self, op1: int, op2: int):
        '''
        Used to set the values of the accumulators
        '''
        self.__acc1 = op1
        self.__acc2 = op2

    def exec(self):
        '''
        Used to fire the circuit
        '''
        self.__acc3 = self.__circuit.fire(self.__acc1, self.__acc2)

        print(f"Program execution done.")

    def get_accumulator(self):
        '''
        Used to get the output of the operation
        '''
        return self.__acc3