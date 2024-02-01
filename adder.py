from circuit import CircuitBehaviour

class AdderCircuit(CircuitBehaviour):    


    def __fullAdder(self, a: int, b: int, cin: int):
        '''
        This function simulates a full adder. a, b are bits and
        cin is the carry in bit.
        '''
        # XOR gate for sum
        sum_bit = a ^ b ^ cin

        # AND gate for carry-out
        carry_out = (a & b) | ((a ^ b) & cin)

        return sum_bit, carry_out

    def fire(self, operand1: int, operand2: int) -> (int):
        '''
        This function defines the configuration of the adder ciruit.
        The function internally uses the self.__fullAdder function repeatedly
        to add the two operands.
        '''
        if operand1 < 0 or operand2 < 0:
            raise Exception("The numbers must be non-negative")

        result = carry = shift = 0

        while operand1 > 0 or operand2 > 0 or carry > 0:
            bit1 = operand1 & 1
            bit2 = operand2 & 1

            sum_bit, carry = self.__fullAdder(bit1, bit2, carry)

            # Set the sum bit in the result
            result |= (sum_bit << shift)

            # Right shift both numbers
            operand1 >>= 1
            operand2 >>= 1
            shift += 1

        return result