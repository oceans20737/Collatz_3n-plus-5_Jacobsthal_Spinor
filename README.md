# **Reconstruction of the Collatz-type Map ($3n+5$ Problem) via Jacobsthal Normalized Spinor Representation**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Hiroshi Harada - September 1, 2026**

---

## **Overview**
This repository provides research data and source code that reconstruct the odd-nucleus trajectories in the generalized Collatz map ($3n+5$ problem) as two-component discrete spinors (**J-spinors**) using the Jacobsthal sequence, proving their linear transitions and topological closures (attractors).

By eliminating the conventional arithmetic procedure of "multiplying by 3, adding 5, and dividing by 2," this study visually and algebraically elucidates the dynamics of odd nuclei as **"linear shifts of standing waves in J-space."**

This research demonstrates that all six attractor systems ($1, 5, 19, 23, 187, 347$) existing in the $3n+5$ space can be described as an entry from an external portal followed by a perfect return to the wave source.

---

## **Repository Structure**
- `REPORT_EN.pdf`
  - Research report in English.
  - Contains the mathematical development of the J-spinor theory and the proof of topological closure for all six attractor systems.
- `REPORT_JP.pdf`
  - Research report in Japanese.
- `code_01_collatz_3n5_jacobsthal_spinor.py`
  - A Python script that calculates the $3n+5$ odd-nucleus trajectory from an arbitrary initial value $n$, reverse-engineers the J-spinor wave source, and maps it onto a Logarithmic Spiral Space.

---

## **Key Concepts**
The greatest breakthrough of this research lies in demonstrating that the following three relations universally hold:

1. **J-spinor Representation:** An arbitrary odd nucleus $N_{\text{current}}$ is uniquely determined as $J_c(a,b)$ using the shift count $c$ and the wave source $(a,b)$.
2. **Linear Transition to the Next Term:** The next odd nucleus $N_{\text{next}}$ is equal to the sum of the wave source $a+b$.
3. **Equivalence with the $3n+5$ Map:** $N_{\text{next}} = \frac{3J_c(a,b) + 5}{2^c}$

Furthermore, this research demonstrates that the true ground state in the $3n+5$ space is "$5$" (i.e., $J(0,5)$), and that "$1$", which was considered privileged in the $3n+1$ world, is merely a localized standing wave mode $J(2,-1)$.

---

## **How to Use**
You can generate visualization artifacts using the following libraries in a Python 3.x environment.

### **Dependencies**
```bash
pip install numpy matplotlib

```

### **Execution**

Run the script by passing an arbitrary initial value (e.g., 121, 25, 1849) to the `generate_artifacts(n)` function at the end of the code.

```bash
python code_01_collatz_3n5_jacobsthal_spinor.py

```

Upon execution, a high-resolution logarithmic spiral plot (PNG) and structural data recording the wave source and shift count for each step (CSV) will be generated in the same directory as the script.

---

## **License**

The artifacts included in this repository are published under the following licenses:

* **Research Documents (PDF, MD):** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
* **Python Source Code:** [MIT License](https://opensource.org/licenses/MIT)

Copyright (c) 2026 Hiroshi Harada

---
