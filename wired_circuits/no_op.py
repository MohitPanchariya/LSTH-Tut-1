from circuit import CircuitBehaviour

class NoOpCircuit(CircuitBehaviour):

    def fire(self, operand1: int, operand2: int) -> (int):
        pass