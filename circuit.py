from abc import ABC, abstractclassmethod

'''
The Circuit interface is used to implement circuits with varying purposes.
E.g. An adder circuit, a multiplier circuit etc.
'''
class CircuitBehaviour(ABC):
    @abstractclassmethod
    def fire(self, operand1: int, operand2: int) ->(int) :
        '''
        The fire method "fires" the circuit. Thereby, performing the defined
        operation on the operands.
        '''
        pass