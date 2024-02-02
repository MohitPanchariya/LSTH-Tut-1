from function_table import function_table

class CircuitFactory:
    
    def __init__(self):
        self.function_table = function_table()

    def create_circuit(self, circuit_type):
        return self.function_table.get(circuit_type)()
