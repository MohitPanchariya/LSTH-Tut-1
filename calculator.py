from plugboard import Plugboard

class Calculator:
    '''
    A Calculator consists of a plugboard. This plugboard will have a 
    '''
    __plugboard: Plugboard

    def set_plugboard(self, plugboard: Plugboard):
        '''
        The set_plugboard method is used to set the plugboard for the calculator.
        '''
        self.__plugboard = plugboard

    def set_input(self, op1: int, op2: int):
        '''
        The set_input method is used to set the values of the accumulators
        '''
        self.__plugboard.set_accumulator(op1, op2)
        return self

    def run(self):
        '''
        The run method is used to execute the instructions using the 
        current configuration of the plugboard.
        The argument instructions expects a path to file where instructions
        are stored.
        '''
        self.__plugboard.exec()
        return self

    def get_output(self):
        '''
        The get_output method is used to get the output of the operation
        '''
        return self.__plugboard.get_accumulator()
