from plugboard import Plugboard
from calculator import Calculator

# import any of the circuits - Adder, Subtractor, Multiplier, Divider

from wired_circuits.adder import AdderCircuit as Circuit
# from wired_circuits.subtractor import SubtractorCircuit as Circuit
# from wired_circuits.multiplier import MultiplierCircuit as Circuit
# from wired_circuits.divider import DividerCircuit as Circuit

def main():

    # instantiate the circuit
    circuitInstance = Circuit()

    # instantiate a plugboard with the adder circuit
    plugboardInstance = Plugboard(circuitInstance)

    # specify the path for instructions
    instructionsPath = "./input.scl"

    # use the plugboard instance as the calculator
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()