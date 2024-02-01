from plugboard import Plugboard
from wired_circuits.subtractor import SubtractorCircuit
from calculator import Calculator

def main():

    # instantiate an divider circuit
    subtractorCircuit = SubtractorCircuit()

    # instantiate a plugboard with the divider circuit
    plugboardInstance = Plugboard(subtractorCircuit)

    # specify the path for instructions
    instructionsPath = "./input_scripts/subtraction.scl"

    # use the plugboard instance as the calculator
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()