from circuit import CircuitBehaviour


class DividerCircuit(CircuitBehaviour):

    def __subtract(self, dividend: int, divisor: int) -> int:
        """
        This function simulates subtraction. It subtracts the divisor from the dividend.
        Here repeated subtraction is done in order to do the division.
        """
        while dividend >= divisor:
            dividend -= divisor
        return dividend

    def fire(self, dividend: int, divisor: int) -> int:
        """
        This function defines the configuration of the divider circuit.
        The function internally uses the self.__subtract function repeatedly
        to perform integer division using bitwise operations and return the quotient.
        """
        if divisor <= 0:
            raise ValueError("The divisor must be a positive integer")

        if dividend < 0:
            raise ValueError("The dividend must be a non-negative integer")

        quotient = 0
        remainder = 0

        # Assuming the integer bit representation as 32 bit.

        for _ in range(31, -1, -1):
            remainder = (remainder << 1) | ((dividend >> _) & 1)
            if remainder >= divisor:
                remainder = self.__subtract(remainder, divisor)
                quotient = (quotient << 1) | 1
            else:
                quotient = quotient << 1

        return quotient
