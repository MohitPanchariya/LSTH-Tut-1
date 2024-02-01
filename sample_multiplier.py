from calculator import Calculator
from multiplier import MultiplierCircuit
from plugboard import Plugboard


def main():
    # instantiate an adder circuit
    multiplierCircuit = MultiplierCircuit()
    # instantiate a plugboard with the adder circuit
    plugboardInstance = Plugboard(multiplierCircuit)

    instructionsPath = "./sample_multiplier.scl"
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()