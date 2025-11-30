# ProofScript

A domain-specific language for **verified algorithm development**. Write algorithms once with formal specifications—get automatic testing, correctness verification, and publication-quality documentation.

## Why ProofScript?

**The Problem:** Algorithm development requires separate workflows for coding, testing, verification, and documentation. Students copy-paste code without understanding correctness. Developers document algorithms that drift from implementation. Interviewees can't prove their solutions handle edge cases.

**The Solution:** ProofScript unifies specification, implementation, verification, and documentation in one language.

## Key Features

- ✅ **Formal Specifications** - Define preconditions, postconditions, complexity bounds
- 🧪 **Auto-Generated Tests** - Property-based testing from specs
- 📊 **Runtime Verification** - Validates correctness during execution
- 📄 **LaTeX Documentation** - Publication-quality output with proofs
- 🎓 **Educational Visualization** - Step-by-step execution traces
- 🔒 **Type Safety** - Static typing catches errors before runtime

## Use Cases

### For Students (DSA Learning)
Write algorithms with confidence. ProofScript generates comprehensive test cases, catches edge cases you missed, and helps you understand why implementations fail.

### For Interview Prep
Create portfolio-quality algorithm writeups. One .proof file generates working code + professional LaTeX documentation for your GitHub.

### For Educators
Auto-grade student submissions. Students submit .proof files with specs—system verifies correctness automatically.

### For Developers
Document core algorithms with executable specifications. Code serves as verified documentation that can't get out of sync.

### For Researchers
Develop and compare algorithm variants. Specify properties once, test multiple implementations, measure actual complexity.

## Quick Example
```proof
algorithm bubble_sort(arr: List[int]) -> List[int]:
    requires: len(arr) >= 0
    ensures: sorted(result)
    ensures: is_permutation(arr, result)
    complexity: O(n²)
    
    for i in 0..len(arr):
        for j in 0..len(arr)-i-1:
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr
```

**Run:** `proofscript bubble_sort.proof --test --latex`

**Outputs:**
- ✅ 50 auto-generated test results
- 📄 LaTeX document with algorithm + proof
- 🎓 Step-by-step execution trace

## Installation
```bash
pip install proofscript  # Coming soon!
```

## Current Status

🚧 **Active Development** - Week 1 of 20-week build timeline  
📋 [Project Roadmap](issues)  
🎯 Target: v1.0 by [Date]

## Contributing

This is currently a solo learning project but feedback welcome! See [issues](issues) for development progress.

## License

MIT License - See LICENSE file
