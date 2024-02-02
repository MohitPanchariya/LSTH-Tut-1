# ENIAC Simulator - Calculator

This project is an ENIAC simulator that allows you to perform simple mathematical operations using a plugboard and a circuit. The plugboard is directly connected to a set of accumulators, which can be set and retrieved using the provided class methods.

## Installation

1. Clone the repository: `git clone https://github.com/MohitPanchariya/LSTH-Tut-1.git`
2. Navigate to the project directory
3. Install the dependencies: `!pip install python-abc`

## Usage

1. Run inside the parent directory: `python master_programmer.py`
2. Define the requested operation inside the 'punch_card.scl' file
   Format: `ACC1 <first_operand> ACC2 <second_operand> CIRCUIT <circuit_name>` 
3. Specify the path to the punch card file when prompted
   Sample: `./punch_card.scl`

## Creating Custom Circuits

1. Add your circuit as a python module into the `/wired_circuits` directory
2. Add its entry into the function table file `function_table.py`
