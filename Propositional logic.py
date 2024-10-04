# library for generating truth table combinations
import itertools

# print the truth table for a logical expression
def print_truth_table(variables, expression):
    # Generating all combinations of True and False for given variables
    combinations = list(itertools.product([False, True], repeat=len(variables)))

    # Print the header of the truth table
    print(f"{' | '.join(variables)} | Expression ({expression})")
    print('-' * (len(variables) * 6 + 15))
    
    # Loop through each combination of truth values
    for combination in combinations:
        # Create a dictionary to map variables to their respective truth values
        env = dict(zip(variables, combination))
        
        # Evaluate the expression in the current environment (combination of truth values)
        result = eval(expression, {}, env)
        
        # Print the result row in the truth table
        truth_values = " | ".join([f'{str(value):^5}' for value in combination])
        print(f"{truth_values} | {str(result):^15}")

# 1. Logical Operators - AND, OR, NOT
def demonstrate_logical_operators():
    a = True
    b = False

    print("Demonstrating Logical Operators:")
    print(f"a AND b: {a and b}")  # Logical AND
    print(f"a OR b: {a or b}")    # Logical OR
    print(f"NOT a: {not a}")      # Logical NOT
    print()

# 2. Atomic and Compound Propositions
def demonstrate_atomic_and_compound():
    p = True  # Atomic proposition p
    q = False  # Atomic proposition q

    # Compound proposition: p AND (NOT q)
    compound = p and not q

    print("Atomic and Compound Propositions:")
    print(f"Atomic p: {p}, Atomic q: {q}")
    print(f"Compound Proposition (p AND (NOT q)): {compound}")
    print()

# 3. Truth Tables
def demonstrate_truth_table():
    print("Truth Table for (p AND q) OR NOT r:")
    variables = ['p', 'q', 'r']
    expression = "(p and q) or not r"
    print_truth_table(variables, expression)
    print()

# 4. Boolean Algebra 
def demonstrate_boolean_algebra():
    p = True
    q = False

    # Simplifying (p AND True) OR (q AND False)
    simplified_expr = (p and True) or (q and False)

    print("Boolean Algebra Simplification:")
    print(f"Original Expression: (p AND True) OR (q AND False)")
    print(f"Simplified Expression: {simplified_expr} (since p AND True is p, and q AND False is False)")
    print()


if __name__ == "__main__":
    demonstrate_logical_operators()
    demonstrate_atomic_and_compound()
    demonstrate_truth_table()
    demonstrate_boolean_algebra()