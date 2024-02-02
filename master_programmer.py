from calculator import Calculator
from calculator_builder import CalculatorBuilder

def main():

    # Greet the user
    print("Welcome to the ENIAC Simulator")
    
    # Create a calculator instance
    calculator = Calculator()

    # Prompt the user for circuit type
    circuit_type = input("Please enter the circuit type: ")

    # Prompt the user to set input accumulators
    operand1 = input("Please set the value for operand 1: ")
    operand2 = input("Please set the value for operand 2: ")

    # Convert operand1 and operand2 to integers
    try:
        operand1 = int(operand1)
        operand2 = int(operand2)
    except ValueError:
        print("Please enter valid integer values for operands.")

    # Build the calculator and run it
    try:
        result = CalculatorBuilder(calculator).build_circuit(circuit_type).build_plugboard().build() \
                .set_input(operand1, operand2) \
                .run() \
                .get_output()
        
        print(f'Final result: {result}')
        return 0
    except Exception as e:
        print(e)
        return -1

main()