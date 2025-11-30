from lark import Lark

# Grammar definition
grammar = """
    ?start: statement+
    
    ?statement: assignment
        | if_stmt
        | while_stmt
        | for_stmt
        | expression
    
    assignment: NAME "=" expression
    
    if_stmt: "if" expression if_block ("else" else_block)?
    if_block: "{" statement+ "}"
    else_block: "{" statement+ "}"
    
    while_stmt: "while" expression while_block
    while_block: "{" statement+ "}"
    
    for_stmt: "for" NAME "in" expression "to" expression for_block
    for_block: "{" statement+ "}"
    
    ?expression: or_expr
    
    ?or_expr: and_expr
        | or_expr "or" and_expr    -> or_op
    
    ?and_expr: not_expr
        | and_expr "and" not_expr -> and_op
    
    ?not_expr: comparison
        | "not" not_expr          -> not_op
    
    ?comparison: arith_expr
        | arith_expr "==" arith_expr  -> eq
        | arith_expr "!=" arith_expr  -> neq
        | arith_expr "<" arith_expr   -> lt
        | arith_expr ">" arith_expr   -> gt
        | arith_expr "<=" arith_expr  -> lte
        | arith_expr ">=" arith_expr  -> gte
    
    ?arith_expr: term
        | arith_expr "+" term   -> add
        | arith_expr "-" term   -> sub
    
    ?term: factor
        | term "*" factor  -> mul
        | term "/" factor  -> div
        | term "^" factor  -> pow
        | term "//" factor -> floordiv
    
    ?factor: atom
        | "(" expression ")"
    
    ?atom: NUMBER
        | "true"   -> true
        | "false"  -> false
        | NAME
    
    NAME: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMBER: /[0-9]+/
    
    %import common.CPP_COMMENT
    %import common.WS
    %ignore CPP_COMMENT
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