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

def tokenize(code):
    """
    Tokenize ProofScript source code
    
    Args:
        code (str): Source code to tokenize
        
    Returns:
        List of tokens
    """
    # Create lexer with grammar
    lexer = Lark(grammar, start='start', lexer='basic')
    
    # Tokenize code
    tokens = list(lexer.lex(code))
    
    return tokens