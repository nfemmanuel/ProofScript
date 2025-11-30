from lark import Token, Tree
from src.parser import parse

class Interpreter:
    """ProodScript interpreter with variable support"""
    
    def __init__(self):
        self.variables = {}

    def evaluate(self, tree):
        """
        Evaluate an Abstract Syntax Tree and return the result
        
        Args:
            tree: Lark Tree object
            
        Returns:
            int/float: Result of evaluating the expression
        """
        # Base case: It's a number or variable name
        if isinstance(tree, Token):
            if tree.type == "NUMBER":
                return int(tree.value)
            elif tree.type == "NAME":
                # variable lookup
                if tree.value not in self.variables:
                    raise NameError(f"Variable '{tree.value}' is not defined")
                return self.variables[tree.value]
            
        # Handle Assignment
        if tree.data == "assignment":
            var_name = tree.children[0].value #NAME token
            value = self.evaluate(tree.children[1]) # evaluate expression
            self.variables[var_name] = value # store in symbol table
            return None
        
        # Recursive case: It's an operation
        # Evaluate left and right children first
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        
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
    
    def run(self, tree):
        """
        Execute a program (multiple statements)
        
        Args:
            tree: Parsed AST
            
        Returns:
            Result of last expression (or None)
        """
        result = None
        
        # if tree is one statement, wrap in list
        statements = tree.children if isinstance (tree, Tree) else [tree]
        
        # execute each statment
        for statement in statements:
            result = self.evaluate(statement)
            
        return result

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
    tree = parse(code)# Parse code into tree
    interpreter = Interpreter() # create instance of interpreter
    
    result = interpreter.run(tree) # run interpreter
    
    return result