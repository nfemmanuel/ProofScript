from lark import Lark

# Grammar definition
grammar = """
    ?start: expression

    ?expression: term
        | expression "+" term   -> add
        | expression "-" term   -> sub
    
    ?term: factor
        | term "*" factor    -> mul
        | term "/" factor    -> div
        | term "^" factor    -> pow
        | term "//" factor   -> floordiv
    
    ?factor: NUMBER
        | "(" expression ")"
    
    NUMBER: /[0-9]+/
    
    %import common.WS
    %ignore WS
"""

def parse(code):
    """
    Parse ProofScript source code into Abstract Syntax Tree
    
    Args:
        code (str): Source code to parse
        
    Returns:
        Tree: Lark tree object representing the code structure
        
    Example:
        >>> tree = parse("5 + 3")
        >>> print(tree.pretty())
    """

    # create parser with grammer
    parser = Lark(grammar, start='start')
    
    # parse the code
    tree = parser.parse(code)
    
    return tree