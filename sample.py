from adder import AdderCircuit
from plugboard import Plugboard
from calculator import Calculator

def main():
    # instantiate an adder circuit
    adderCircuit = AdderCircuit()
    # instantiate a plugboard with the adder circuit
    plugboardInstance = Plugboard(adderCircuit)

    instructionsPath = "./sample.scl"
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()