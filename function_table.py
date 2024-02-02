from circuit import CircuitBehaviour

from wired_circuits.adder import AdderCircuit
from wired_circuits.subtractor import SubtractorCircuit
from wired_circuits.multiplier import MultiplierCircuit
from wired_circuits.divider import DividerCircuit
from wired_circuits.no_op import NoOpCircuit

class function_table:

    table = {
        'default': NoOpCircuit
    }
    
    def __init__(self):
        self.add('adder', AdderCircuit)
        self.add('subtractor', SubtractorCircuit)
        self.add('multiplier', MultiplierCircuit)
        self.add('divider', DividerCircuit)

    def add(self, name, circuit_class: CircuitBehaviour):
        self.table[name] = circuit_class

    def get(self, name):
        return self.table.get(name, self.table['default'])