from calculator import Calculator
from divider import DividerCircuit
from plugboard import Plugboard


def main():
    # instantiate an adder circuit
    dividerCircuit = DividerCircuit()
    # instantiate a plugboard with the adder circuit
    plugboardInstance = Plugboard(dividerCircuit)

    instructionsPath = "./sample_divider.scl"
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()