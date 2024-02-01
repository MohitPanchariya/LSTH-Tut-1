from circuit import CircuitBehaviour
from wired_circuits.subtractor import SubtractorCircuit

class DividerCircuit(CircuitBehaviour):

    def __init__(self):
        super().__init__()
        # Create an instance of the SubCircuit class to access its subtraction method
        """
        This function simulates subtraction. It subtracts the divisor from the dividend.
        Here repeated subtraction is done in order to do the division.
        """

        self.sub_circuit = SubtractorCircuit()

    def fire(self, dividend: int, divisor: int) -> int:
        """
        This function defines the configuration of the divider circuit.
        The function internally uses the subtraction function from SubCircuit
        to perform integer division using bitwise operations and return the quotient.
        
        """
        if divisor <= 0:
            raise ValueError("The divisor must be a positive integer")

        if dividend < 0:
            raise ValueError("The dividend must be a non-negative integer")

        quotient = 0
        remainder = 0

        # Assuming the integer bit representation as 32 bit.
        for bit_position in range(31, -1, -1):
            remainder = (remainder << 1) | ((dividend >> bit_position) & 1)
            if remainder >= divisor:
                # Use the fire method from the SubCircuit class for subtraction
                diff = self.sub_circuit.fire(remainder, divisor)
                remainder = diff
                quotient = (quotient << 1) | 1
            else:
                quotient = quotient << 1

        return quotient
