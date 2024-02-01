from circuit import CircuitBehaviour
from wired_circuits.adder import AdderCircuit

class MultiplierCircuit(CircuitBehaviour):    

    def __init__(self):
        super().__init__()
        # Create an instance of the AdderCircuit class to access its addition method
        """
        This function simulates addition. It adds the multiplicand to the product.
        Here repeated addition is done in order to do the multiplication.
        """

        self.add_circuit = AdderCircuit()

    def fire(self, multiplicand: int, multiplier: int) -> int:
        """
        This function defines the configuration of the multiplier circuit.
        The function internally uses the addition function from AdderCircuit
        to perform integer multiplication using bitwise operations and return the product.
        
        """

        if multiplicand < 0 or multiplier < 0:
            raise Exception("Both multiplicand and multiplier must be non-negative")

        product = 0
        shift = 0

        while multiplier > 0:
            bit = multiplier & 1
            if bit:
                # If the current bit of multiplier is 1, add the shifted multiplicand to the result
                # Use the fire method from the AdderCircuit class for addition
                product = self.add_circuit.fire(product, multiplicand << shift)

            # Right shift multiplier for next iteration
            multiplier >>= 1
            shift += 1

        return product
