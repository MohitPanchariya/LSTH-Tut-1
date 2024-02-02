from calculator import Calculator
from calculator_builder import CalculatorBuilder

from card_parser import parse_card

def main():

    # Greet the user
    print("Welcome to the ENIAC Simulator")
    
    # Create a calculator instance
    calculator = Calculator()

    # Prompt the user for the punch card file
    instruction_path = input("Please enter the path to your punch card file: ")

    # Parse the punch card file
    try: 
        operand1, operand2, circuit_type = parse_card(instruction_path)

        # Convert operand1 and operand2 to integers
        try:
            operand1 = int(operand1)
            operand2 = int(operand2)
        except ValueError:
            print("Please enter valid integer values for operands.")

        # Build the calculator and run it
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