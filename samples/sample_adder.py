from plugboard import Plugboard
from wired_circuits.adder import AdderCircuit
from calculator import Calculator

def main():

    # instantiate an adder circuit
    adderCircuit = AdderCircuit()

    # instantiate a plugboard with the adder circuit
    plugboardInstance = Plugboard(adderCircuit)

    # specify the path for instructions
    instructionsPath = "./input_scripts/addition.scl"

    # use the plugboard instance as the calculator
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()