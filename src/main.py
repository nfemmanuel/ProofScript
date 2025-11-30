from src.interpreter import interpret

import sys

def read_file(filename):
    """
    Read contents of a .proof file
    
    Args:
        filename (str): Path to the .proof file
        
    Returns:
        str: Contents of the file
        
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    
    # only read ".proof" and ".txt" files
    if not filename.endswith('.proof'):
        raise ValueError(f"Error: Expected .proof file, got {filename}")
    
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file: {filename}")

def main():
    """
    Main entry point for ProofScript interpreter
    
    Reads and executes a .proof file provided as command-line argument.
    
    Usage:
        python -m src.main <filename.proof>
    """
    # Check if filename was provided
    if len(sys.argv) < 2:
        print("Error: No input file provided")
        print("Usage: python -m src.main <filename.proof>")
        sys.exit(1)
    
    # Get filename from command-line arguments
    filename = sys.argv[1]
    
    try:
        code=read_file(filename)
        result = interpret(code)
        print(result)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()