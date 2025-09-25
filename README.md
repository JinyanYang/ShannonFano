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

```bash
python scripts/shannon_fano.py
```

This will print the generated codebook and the average code length for a demo symbol set.

---

## Notes

- The original coursework report is included in `report/ShannonFano_Report.pdf` (with personal identifiers removed).  
- This repository is intended as a **portfolio + educational project**.  
- You can extend it with **Huffman coding** for comparison.  

---

## Author

**Jinyan Yang** — MSc in Renewable Energy Systems
