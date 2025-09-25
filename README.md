# Shannon-Fano Encoding Algorithm (Data Compression Demo)

This repository demonstrates the **Shannon-Fano algorithm**, a classical lossless data compression technique.  
It provides both the **theoretical explanation** (report PDF) and a **Python implementation** of the algorithm, with examples and visualizations.

The project was originally prepared as part of coursework and has been adapted here into a reusable, educational GitHub project.

---

## Repository Structure

```
shannon-fano-demo/
├── README.md
├── LICENSE
├── .gitignore
├── report/
│   └── ShannonFano_Report.pdf    # Anonymized report (with student info removed)
├── scripts/
│   └── shannon_fano.py           # Python implementation of Shannon-Fano
└── figures/
    └── coding_tree.png           # Example encoding tree diagram
```

---

## Project Overview

- **Algorithm**: Shannon-Fano encoding, one of the earliest entropy coding methods.  
- **Goal**: Reduce the average codeword length compared to fixed-length coding.  
- **Approach**:
  1. Sort symbols by probability (highest first).  
  2. Split into two groups with total probability as equal as possible.  
  3. Assign `0` to one group and `1` to the other.  
  4. Repeat recursively until all symbols are uniquely coded.  

---

## Example Usage

python
def shannon_fano(symbols, code=''):
    if len(symbols) == 1:
        return {symbols[0][0]: code}
    
    # Split into two groups with probabilities balanced
    total = sum([p for _, p in symbols])
    accum, split = 0, 0
    for i, (_, p) in enumerate(symbols):
        accum += p
        if accum >= total/2:
            split = i + 1
            break

    left = shannon_fano(symbols[:split], code + '0')
    right = shannon_fano(symbols[split:], code + '1')
    return {**left, **right}

# Example usage
symbols = [('A', 0.4), ('B', 0.2), ('C', 0.15), ('D', 0.15), ('E', 0.1)]
codes = shannon_fano(symbols)
print(codes)

Example Result
Input symbols & probabilities:
Symbol	Probability
A	0.40
B	0.20
C	0.15
D	0.15
E	0.10
Generated Shannon-Fano codes:
Symbol	Code
A	0
B	10
C	110
D	111
E	101

## Notes

- The original coursework report is included in `report/ShannonFano_Report.pdf` (with personal identifiers removed).  
- This repository is intended as a **portfolio + educational project**.  
- You can extend it with **Huffman coding** for comparison.  

---

## Author

Jinyan Yang — MSc in Renewable Energy Systems
