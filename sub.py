from circuit import CircuitBehaviour

class SubCircuit(CircuitBehaviour):
    
    def __fullSubtractor(self, a: int, b: int, bin: int):
        '''
        This function simulates a full subtractor. a, b are bits and
        bin is the borrow-in bit.
        '''
        # XOR gate for difference
        diff_bit = a ^ b ^ bin

        # AND gate for borrow-out
        borrow_out = (~a & b) | ((~a ^ b) & bin)

        return diff_bit, borrow_out

    def fire(self, operand1: int, operand2: int) -> int:
        '''
        This function defines the configuration of the subtraction circuit.
        The function internally uses the self.__fullSubtractor function repeatedly
        to subtract operand2 from operand1.
        '''
        if operand1 < 0 or operand2 < 0:
            raise Exception("The numbers must be non-negative")

        # Swap operands if operand1 is less than operand2
        is_negative_result = False
        if operand1 < operand2:
            operand1, operand2 = operand2, operand1
            is_negative_result = True

        result = borrow = shift = 0

        while operand1 > 0 or operand2 > 0 or borrow > 0:
            bit1 = operand1 & 1
            bit2 = operand2 & 1

            diff_bit, borrow = self.__fullSubtractor(bit1, bit2, borrow)

            # Set the difference bit in the result
            result |= (diff_bit << shift)

            # Right shift both numbers
            operand1 >>= 1
            operand2 >>= 1
            shift += 1

        # If the result is negative, convert it to a negative value
        if is_negative_result:
            result = -result

        return result
