# Collatz Class

A Python class to generate and manipulate Collatz sequences with modified rules.

In this context, the modified Collatz equation takes the form ((3^log3) * m + n) / (2^log2), where:
- `m` represents the initial number,
- `n` denotes a series that emerges during the cycle calculation.

## Author
- Braulio Silveira <bosilveira@gmail.com>

## Attributes
- `m` (int): The initial number for the modified Collatz sequence.
- `log2` (int): The exponent of 2 in the modified Collatz equation.
- `log3` (int): The exponent of 3 in the modified Collatz equation.
- `n` (list): List of exponents of 3 in the modified Collatz equation.
- `cycle` (list): The modified Collatz sequence.

## Methods
- `eq_factored()`: Returns the equation representing the modified Collatz equation in factored form.
- `eq_numeric()`: Returns the equation representing the modified Collatz equation in numeric form.
- `calculate()`: Calculates the modified Collatz sequence and its attributes.

## Example Usage

```python
# Create a Collatz object with initial number 10
collatz_sequence = Collatz(10)

# Print the modified Collatz sequence
print(collatz_sequence)

# Print the equation associated to the modified Collatz sequence in factored form
print(collatz_sequence.eq_factored())

# Print the equation associated to the modified Collatz sequence in numeric form
print(collatz_sequence.eq_numeric())
