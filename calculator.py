from plugboard import Plugboard

class Calculator:
    '''
    A Calculator consists of a plugboard. This plugboard will have a 
    '''
    __plugboard: Plugboard

    def __init__(self, plugboard: Plugboard) -> None:
        self.__plugboard = plugboard

    def run(self, instructions: str):
        '''
        The run method is used to execute the instructions using the 
        current configuration of the plugboard.
        The argument instructions expects a path to file where instructions
        are stored.
        '''
        self.__plugboard.exec(instructions)
