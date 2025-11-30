from lark import Token
from src.parser import parse

def evaluate(tree):
    """
    Evaluate an Abstract Syntax Tree and return the result
    
    Args:
        tree: Lark Tree object
        
    Returns:
        int/float: Result of evaluating the expression
    """
    # Base case: It's a number
    if isinstance(tree, Token):
        return int(tree.value)
    
    # Recursive case: It's an operation
    # Evaluate left and right children first
    left = evaluate(tree.children[0])
    right = evaluate(tree.children[1])
    
    # Apply the operation based on node type
    if tree.data == "add":
        return left + right
    elif tree.data == "sub":
        return left - right
    elif tree.data == "mul":
        return left * right
    elif tree.data == "div":
        return left / right
    elif tree.data == "pow":
        return left ** right
    elif tree.data == "floordiv":
        return left // right
    
    # If we get here, unknown node type
    raise ValueError(f"Unknown operation: {tree.data}")

def interpret(code):
    """
    Parse and evaluate ProofScript code
    
    Args:
        code (str): Source code to execute
        
    Returns:
        Result of execution
        
    Example:
        >>> interpret("5 + 3")
        8
    """
    # Parse code into tree
    tree = parse(code)
    
    # Evaluate the tree
    result = evaluate(tree)
    
    return result