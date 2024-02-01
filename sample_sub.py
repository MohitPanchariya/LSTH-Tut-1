from sub import SubCircuit
from plugboard import Plugboard
from calculator import Calculator

def main():
    # instantiate an substraction circuit
    subCircuit = SubCircuit()
    # instantiate a plugboard with the substraction circuit
    plugboardInstance = Plugboard(subCircuit)

    instructionsPath = "./sample_sub.scl"
    calculator = Calculator(plugboardInstance)

    try:
        calculator.run(instructionsPath)
    except Exception as e:
        print(e)

main()