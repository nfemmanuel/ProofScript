from lark import Token, Tree
from src.parser import parse

class Interpreter:
    """ProofScript interpreter with variable support"""
    
    def __init__(self):
        self.variables = {}
        self.max_iterations = 10000
        self._iteration_count = 0  # Track current loop iterations
    
    def evaluate(self, tree):
        """
        Main evaluation dispatcher - routes to specific handlers
        
        Args:
            tree: Lark Tree or Token object
            
        Returns:
            Result of evaluation
        """
        # Handle tokens (numbers and variables)
        if isinstance(tree, Token):
            if tree.type == "NUMBER":
                return self._eval_number(tree)
            elif tree.type == "NAME":
                return self._eval_variable(tree)
        
        # Dispatch based on node type
        handlers = {
            # Statements
            "assignment": self._eval_assignment,
            "if_stmt": self._eval_if,
            "while_stmt": self._eval_while,
            "for_stmt": self._eval_for,
            
            # Blocks (containers)
            "if_block": self._execute_block,
            "else_block": self._execute_block,
            "while_block": self._execute_block,
            "for_block": self._execute_block,
            
            # Boolean literals
            "true": lambda t: True,
            "false": lambda t: False,
            
            # Boolean operators
            "and_op": self._eval_and,
            "or_op": self._eval_or,
            "not_op": self._eval_not,
            
            # Comparison operators
            "eq": self._eval_eq,
            "neq": self._eval_neq,
            "lt": self._eval_lt,
            "gt": self._eval_gt,
            "lte": self._eval_lte,
            "gte": self._eval_gte,
            
            # Arithmetic operators
            "add": self._eval_add,
            "sub": self._eval_sub,
            "mul": self._eval_mul,
            "div": self._eval_div,
            "pow": self._eval_pow,
            "floordiv": self._eval_floordiv,
        }
        
        handler = handlers.get(tree.data)
        if handler:
            return handler(tree)
        
        raise ValueError(f"Unknown operation: {tree.data}")
    
    # ==================== TOKEN HANDLERS ====================
    
    def _eval_number(self, token):
        """Evaluate a number token"""
        return int(token.value)
    
    def _eval_variable(self, token):
        """Look up a variable in the symbol table"""
        if token.value not in self.variables:
            raise NameError(f"Variable '{token.value}' is not defined")
        return self.variables[token.value]
    
    # ==================== STATEMENT HANDLERS ====================
    
    def _eval_assignment(self, tree):
        """Handle variable assignment: x = 5"""
        var_name = tree.children[0].value  # NAME token
        value = self.evaluate(tree.children[1])  # Evaluate expression
        self.variables[var_name] = value
        return None
    
    def _eval_if(self, tree):
        """Handle if/else statements"""
        condition = self.evaluate(tree.children[0])
        
        if condition:
            # Execute if block
            if_block = tree.children[1]
            return self._execute_block(if_block)
        else:
            # Execute else block if it exists
            if len(tree.children) > 2:
                else_block = tree.children[2]
                return self._execute_block(else_block)
        
        return None
    
    def _eval_while(self, tree):
        """Handle while loops with infinite loop protection"""
        condition_expr = tree.children[0]
        while_block = tree.children[1]
        
        iterations = 0
        result = None
        
        while self.evaluate(condition_expr):
            iterations += 1
            self._check_loop_limit(iterations)
            
            result = self._execute_block(while_block)
        
        return result
    
    def _eval_for(self, tree):
        """Handle for loops: for i in 0 to 10 { }"""
        loop_var = tree.children[0].value  # NAME token
        start_value = self.evaluate(tree.children[1])
        end_value = self.evaluate(tree.children[2])
        for_block = tree.children[3]
        
        iterations = 0
        result = None
        
        # Loop from start to end (inclusive)
        for i in range(int(start_value), int(end_value) + 1):
            iterations += 1
            self._check_loop_limit(iterations)
            
            self.variables[loop_var] = i
            result = self._execute_block(for_block)
        
        return result
    
    # ==================== TOKEN HANDLERS ====================
    
    def _eval_number(self, token):
        """Evaluate a number token"""
        return int(token.value)
    
    def _eval_variable(self, token):
        """Look up a variable in the symbol table"""
        if token.value not in self.variables:
            raise NameError(f"Variable '{token.value}' is not defined")
        return self.variables[token.value]
    
    # ==================== STATEMENT HANDLERS ====================
    
    def _eval_assignment(self, tree):
        """Handle variable assignment: x = 5"""
        var_name = tree.children[0].value  # NAME token
        value = self.evaluate(tree.children[1])  # Evaluate expression
        self.variables[var_name] = value
        return None
    
    def _eval_if(self, tree):
        """Handle if/else statements"""
        condition = self.evaluate(tree.children[0])
        
        if condition:
            # Execute if block
            if_block = tree.children[1]
            return self._execute_block(if_block)
        else:
            # Execute else block if it exists
            if len(tree.children) > 2:
                else_block = tree.children[2]
                return self._execute_block(else_block)
        
        return None
    
    def _eval_while(self, tree):
        """Handle while loops with infinite loop protection"""
        condition_expr = tree.children[0]
        while_block = tree.children[1]
        
        iterations = 0
        result = None
        
        while self.evaluate(condition_expr):
            iterations += 1
            self._check_loop_limit(iterations)
            
            result = self._execute_block(while_block)
        
        return result
    
    def _eval_for(self, tree):
        """Handle for loops: for i in 0 to 10 { }"""
        loop_var = tree.children[0].value  # NAME token
        start_value = self.evaluate(tree.children[1])
        end_value = self.evaluate(tree.children[2])
        for_block = tree.children[3]
        
        iterations = 0
        result = None
        
        # Loop from start to end (inclusive)
        for i in range(int(start_value), int(end_value) + 1):
            iterations += 1
            self._check_loop_limit(iterations)
            
            self.variables[loop_var] = i
            result = self._execute_block(for_block)
        
        return result
    
    # ==================== BOOLEAN OPERATORS ====================
    
    def _eval_and(self, tree):
        """Handle 'and' operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left and right
    
    def _eval_or(self, tree):
        """Handle 'or' operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left or right
    
    def _eval_not(self, tree):
        """Handle 'not' operator"""
        value = self.evaluate(tree.children[0])
        return not value
    
    # ==================== COMPARISON OPERATORS ====================
    
    def _eval_eq(self, tree):
        """Handle == operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left == right
    
    def _eval_neq(self, tree):
        """Handle != operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left != right
    
    def _eval_lt(self, tree):
        """Handle < operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left < right
    
    def _eval_gt(self, tree):
        """Handle > operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left > right
    
    def _eval_lte(self, tree):
        """Handle <= operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left <= right
    
    def _eval_gte(self, tree):
        """Handle >= operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left >= right
    
# ==================== ARITHMETIC OPERATORS ====================
    
    def _eval_add(self, tree):
        """Handle + operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left + right
    
    def _eval_sub(self, tree):
        """Handle - operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left - right
    
    def _eval_mul(self, tree):
        """Handle * operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left * right
    
    def _eval_div(self, tree):
        """Handle / operator"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left / right
    
    def _eval_pow(self, tree):
        """Handle ^ operator (power)"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left ** right
    
    def _eval_floordiv(self, tree):
        """Handle // operator (floor division)"""
        left = self.evaluate(tree.children[0])
        right = self.evaluate(tree.children[1])
        return left // right
    
    # ==================== HELPER METHODS ====================
    
    def _execute_block(self, block):
        """Execute a block of statements (if_block, while_block, etc.)"""
        result = None
        for statement in block.children:
            result = self.evaluate(statement)
        return result
    
    def _check_loop_limit(self, iterations):
        """Check if loop has exceeded maximum iterations"""
        if iterations > self.max_iterations:
            raise RuntimeError(
                f"Loop exceeded maximum iterations ({self.max_iterations}). "
                f"Possible infinite loop!"
            )
    
    def run(self, tree):
        """
        Execute a program (multiple statements)
        
        Args:
            tree: Parsed AST
            
        Returns:
            Result of last expression (or None)
        """
        result = None
        
        # If tree is one statement, wrap in list
        statements = tree.children if isinstance(tree, Tree) else [tree]
        
        # Execute each statement
        for statement in statements:
            result = self.evaluate(statement)
        
        return result


# ==================== PUBLIC API ====================

def interpret(code):
    """
    Parse and execute ProofScript code
    
    Args:
        code (str): Source code to execute
        
    Returns:
        Result of last expression
        
    Example:
        >>> interpret("x = 5\\nx + 3")
        8
    """
    tree = parse(code)
    interpreter = Interpreter()
    result = interpreter.run(tree)
    return result