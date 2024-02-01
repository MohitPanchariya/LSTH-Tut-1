from circuit import CircuitBehaviour

class SubCircuit(CircuitBehaviour):    
    def fire(self, operand1: int, operand2: int) -> (int):
        '''
        This function defines the configuration of the ciruit.
        '''
        return operand1 - operand2