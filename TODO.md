# ProofScript Development TODO

A domain-specific language for verified algorithm development.

## Progress Tracking
- [ ] Phase 1: Foundation
- [ ] Phase 2: Variables & Statements  
- [ ] Phase 3: Control Flow
- [ ] Phase 4: Arrays & Functions
- [ ] Phase 5: Specifications
- [ ] Phase 6: Test Generation
- [ ] Phase 7: LaTeX Output
- [ ] Phase 8: Execution Protection
- [ ] Phase 9: Visualization
- [ ] Phase 10: Polish & Publish

---

## PHASE 1: FOUNDATION (Week 1)
**Goal: Parse and execute the simplest possible program**

### 1.1 Project Setup ✓
- [x] Create project structure (folders, files)
- [ ] Choose and install parser library
- [ ] Set up basic CLI (run a .proof file)
- [ ] Create first test file to work towards

### 1.2 Lexer/Tokenizer
- [ ] Define tokens (numbers, operators, identifiers, keywords)
- [ ] Implement/configure lexer
- [ ] Test: "5 + 3" → tokens

### 1.3 Simple Expression Parser
- [ ] Define grammar for math expressions
- [ ] Build/configure parser
- [ ] Test: "5 + 3" → AST

### 1.4 Expression Evaluator
- [ ] Implement interpreter for numbers
- [ ] Implement arithmetic operators (+, -, *, /)
- [ ] Test: "5 + 3" → 8

**✅ Milestone: Calculator works**

---

## PHASE 2: VARIABLES & STATEMENTS (Week 1-2)
**Goal: Store and manipulate data**

### 2.1 Variable Assignment
- [ ] Add assignment to grammar (x = 5)
- [ ] Implement symbol table (stores variables)
- [ ] Test: "x = 5; x + 3" → 8

### 2.2 Variable References
- [ ] Handle variable lookup in expressions
- [ ] Error handling (undefined variable)
- [ ] Test: "y = 10; z = y + 5" → z is 15

### 2.3 Statement Sequencing
- [ ] Support multiple statements
- [ ] Test: Three statements in sequence

**✅ Milestone: Variables work**

---

## PHASE 3: CONTROL FLOW (Week 2-3)
**Goal: Conditional logic and loops**

### 3.1 Boolean Expressions
- [ ] Add comparison operators (<, >, ==, !=)
- [ ] Add boolean operators (and, or, not)
- [ ] Test: "5 > 3" → true

### 3.2 If Statements
- [ ] Add if/else to grammar
- [ ] Implement conditional execution
- [ ] Test: Simple if/else logic

### 3.3 While Loops
- [ ] Add while to grammar
- [ ] Implement loop execution
- [ ] Add step counter (infinite loop protection)
- [ ] Test: "i = 0; while i < 5: i = i + 1" → i is 5

### 3.4 For Loops
- [ ] Add for loop to grammar
- [ ] Implement iteration
- [ ] Test: "for i in 0..5: sum = sum + i"

**✅ Milestone: Control flow works**

---

## PHASE 4: ARRAYS & FUNCTIONS (Week 3)
**Goal: Data structures and code organization**

### 4.1 Arrays/Lists
- [ ] Add list literal syntax [1, 2, 3]
- [ ] Implement array indexing (arr[0])
- [ ] Implement array assignment (arr[0] = 5)
- [ ] Test: Create, read, modify array

### 4.2 Function Definitions
- [ ] Add function syntax to grammar
- [ ] Implement function storage
- [ ] Test: Define simple function

### 4.3 Function Calls
- [ ] Implement call stack
- [ ] Handle parameters and return values
- [ ] Test: Call function with arguments

### 4.4 Recursion
- [ ] Add recursion depth limit
- [ ] Test: Factorial function

**✅ Milestone: Can write real algorithms**

---

## PHASE 5: SPECIFICATIONS (Week 4)
**Goal: Add verification features**

### 5.1 Algorithm Declaration Syntax
- [ ] Add algorithm keyword to grammar
- [ ] Parse type annotations (arr: List[int])
- [ ] Parse return type
- [ ] Test: Parse algorithm signature

### 5.2 Requires Clauses
- [ ] Add requires to grammar
- [ ] Store preconditions
- [ ] Validate before execution
- [ ] Test: Reject invalid inputs

### 5.3 Ensures Clauses
- [ ] Add ensures to grammar
- [ ] Store postconditions
- [ ] Validate after execution
- [ ] Test: Detect when output violates spec

### 5.4 Complexity Annotations
- [ ] Parse complexity: O(n²)
- [ ] Store complexity metadata
- [ ] Test: Parse various complexities

**✅ Milestone: Specifications parse and check**

---

## PHASE 6: TEST GENERATION (Week 4-5)
**Goal: Automatic testing**

### 6.1 Simple Test Case Generation
- [ ] Generate random inputs from types
- [ ] Respect requires clauses
- [ ] Test: Generate 10 valid inputs

### 6.2 Test Execution
- [ ] Run algorithm on test cases
- [ ] Check ensures clauses
- [ ] Report pass/fail
- [ ] Test: Run bubble_sort with generated tests

### 6.3 Edge Case Generation
- [ ] Empty arrays, zero, negative numbers
- [ ] Boundary conditions
- [ ] Test: Generate edge cases automatically

### 6.4 Test Reports
- [ ] Format test results nicely
- [ ] Show which tests passed/failed
- [ ] Show which ensures clause failed
- [ ] Test: Readable test output

**✅ Milestone: Automatic testing works**

---

## PHASE 7: LATEX OUTPUT (Week 5)
**Goal: Documentation generation**

### 7.1 Basic LaTeX Structure
- [ ] Generate LaTeX document skeleton
- [ ] Format algorithm signature
- [ ] Test: Valid .tex file output

### 7.2 Algorithm Pseudocode
- [ ] Convert your AST to LaTeX algorithmic notation
- [ ] Handle if/while/for formatting
- [ ] Test: Bubble sort → pretty LaTeX

### 7.3 Specifications Documentation
- [ ] Format requires/ensures nicely
- [ ] Add complexity notation
- [ ] Test: Complete algorithm documentation

### 7.4 Test Results in LaTeX
- [ ] Include test summary
- [ ] Show example runs
- [ ] Test: Full document with tests

**✅ Milestone: Can generate papers/homework**

---

## PHASE 8: EXECUTION PROTECTION (Week 5-6)
**Goal: Safety features**

### 8.1 Timeout Implementation
- [ ] Add timeout to interpreter
- [ ] Handle timeout gracefully
- [ ] Test: Detect infinite while loop

### 8.2 Step Counter
- [ ] Count operations during execution
- [ ] Calculate limit from input size + complexity
- [ ] Test: Detect when steps exceed O(n²) for size n

### 8.3 Better Error Messages
- [ ] Line numbers in errors
- [ ] Helpful suggestions
- [ ] Test: Various error cases give good feedback

**✅ Milestone: Safe to run untrusted code**

---

## PHASE 9: VISUALIZATION (Week 6)
**Goal: Show execution steps**

### 9.1 Step Tracing
- [ ] Log each statement executed
- [ ] Show variable values at each step
- [ ] Test: Trace through simple algorithm

### 9.2 Array Visualization
- [ ] Pretty-print arrays at each step
- [ ] Highlight what changed
- [ ] Test: Bubble sort shows swaps

### 9.3 Trace Output Options
- [ ] Text format for terminal
- [ ] Optional HTML output
- [ ] Test: Both formats work

**✅ Milestone: Learners can see execution**

---

## PHASE 10: POLISH & PUBLISH (Week 6)
**Goal: Make it distributable**

### 10.1 Package Structure
- [ ] Create setup.py / pyproject.toml
- [ ] Make installable with pip
- [ ] Test: Install in fresh environment

### 10.2 Command-Line Interface
- [ ] Good help messages
- [ ] Multiple output formats (--latex, --visualize)
- [ ] Test: CLI is intuitive

### 10.3 Documentation
- [ ] README with examples
- [ ] Getting started guide
- [ ] Test: Roommate can use it

### 10.4 Examples & Stdlib
- [ ] 5-10 example algorithms
- [ ] Test files for common algorithms
- [ ] Test: All examples work

### 10.5 GitHub & PyPI
- [ ] Push to GitHub
- [ ] Publish to PyPI
- [ ] Test: Fresh install from PyPI works

**✅ Milestone: Publicly available**

---

## BONUS: COMBO 3 FEATURES (Post Week 6)
**Goal: Advanced verification**

### B.1 Loop Invariants
- [ ] Parse invariant clauses
- [ ] Check at loop start/end
- [ ] Test: Verify bubble sort invariants

### B.2 Loop Variants
- [ ] Parse variant clauses
- [ ] Check decreases each iteration
- [ ] Test: Prove termination

### B.3 Complexity Measurement
- [ ] Count actual operations
- [ ] Compare to claimed complexity
- [ ] Test: Detect O(n³) claimed as O(n²)

### B.4 Proof Sketches
- [ ] Generate informal proofs in LaTeX
- [ ] Explain why properties hold
- [ ] Test: Readable proof output

---

## Notes

**Design Decisions:**
- Static typing with type annotations
- C-style comments (`//` and `/* */`)
- Turing complete with input-based safety bounds
- Hybrid implementation (specs + control flow in custom syntax)

**Current Phase:** Phase 1.1 - Project Setup
**Next Up:** Choose parser library

**Repository:** https://github.com/nfemmanuel/ProofScript
