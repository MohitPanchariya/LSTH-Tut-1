from plugboard import Plugboard
from wired_circuits.divider import DividerCircuit
from calculator import Calculator

def main():

    # instantiate an divider circuit
    dividerCircuit = DividerCircuit()

    # instantiate a plugboard with the divider circuit
    plugboardInstance = Plugboard(dividerCircuit)

    # specify the path for instructions
    instructionsPath = "./input_scripts/division.scl"

    # use the plugboard instance as the calculator
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()