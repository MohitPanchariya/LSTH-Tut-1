from plugboard import Plugboard
from wired_circuits.multiplier import MultiplierCircuit
from calculator import Calculator

def main():

    # instantiate an multiplier circuit
    multiplierCircuit = MultiplierCircuit()

    # instantiate a plugboard with the divider circuit
    plugboardInstance = Plugboard(multiplierCircuit)

    # specify the path for instructions
    instructionsPath = "./input_scripts/multiplication.scl"

    # use the plugboard instance as the calculator
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()