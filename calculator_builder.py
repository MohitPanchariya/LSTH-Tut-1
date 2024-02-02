from calculator import Calculator
from plugboard import Plugboard
from circuit_factory import CircuitFactory

class CalculatorBuilder():
    
    def __init__(self, calculator: Calculator):
        self.calculator = calculator
        self.plugboard = Plugboard()
        self.circuit = None
        self.circuit_factory = CircuitFactory()

    def build(self):
        self.calculator.set_plugboard(self.plugboard)
        return self.calculator
    
    def build_plugboard(self):
        self.plugboard.set_circuit(self.circuit)
        return self

    def build_circuit(self, circuit_type = 'default'):
        self.circuit = self.circuit_factory.create_circuit(circuit_type)
        return self
    
