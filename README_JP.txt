# **Jacobsthal正規化スピノル表現にる Collatz 型写像（3n+5問題）の再構成**
## **(Reconstruction of the Collatz-type Map ($3n+5$ Problem) via Jacobsthal Normalized Spinor Representation)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Hiroshi Harada - September 1, 2026**

---

## **概要 (Overview)**
本リポジトリは、一般化Collatz写像（$3n+5$問題）における奇数核軌道を、Jacobsthal数列を用いた2成分離散スピノル（**J-spinor**）として再構成し、その線形遷移とトポロジー的閉包（アトラクター）を証明する研究データおよびソースコードを公開するものです。

従来の「$3n+5$して2で割る」という算術的な手続きを排除し、奇数核のダイナミクスを **「J空間における定在波の線形シフト」** として視覚的かつ代数的に解明しました。

本研究は、$3n+5$空間に存在する6系統のすべてのアトラクター（$1, 5, 19, 23, 187, 347$）が、外部ポータルからの突入と波源への完全な回帰として記述できることを明らかにしています。

---

## **リポジトリ構成 (Repository Structure)**
- `REPORT_EN.pdf`
  - 英語版の研究レポート。
  - J-spinor理論の数式展開と、6系統すべてのアトラクターのトポロジー的閉包の証明を収録。
- `REPORT_JP.pdf`
  - 日本語版の研究レポート。
- `code_01_collatz_3n5_jacobsthal_spinor.py`
  - 任意の初期値 $n$ から$3n+5$の奇数核軌道を計算し、J-spinorの波源を逆算して対数螺旋空間（Logarithmic Spiral Space）にマップするPythonスクリプト。

---

## **理論の核心 (Key Concepts)**
本研究の最大のブレイクスルーは、以下の3つの関係式が常に成立することを示した点にあります。

1. **J-spinor表現:** 任意の奇数核 $N_{\text{current}}$ は、シフト数 $c$ と波源 $(a,b)$ を用いて $J_c(a,b)$ として一意に定まる。
2. **次項への線形遷移:** 次の奇数核 $N_{\text{next}}$ は、波源の和 $a+b$ に等しい。
3. **3n+5写像との同値性:** $N_{\text{next}} = \frac{3J_c(a,b) + 5}{2^c}$

さらに本研究は、$3n+5$空間における真の基底状態が「$5$」すなわち $J(0,5)$ であり、$3n+1$世界で特権的とされた「$1$」が、局所的な定在波モード $J(2,-1)$ に過ぎないことを明らかにしています。

---

## **スクリプトの使用方法 (How to Use)**
Python 3.x環境で、以下のライブラリを使用して視覚化アーティファクトを生成できます。

### **依存ライブラリ (Dependencies)**
```bash
pip install numpy matplotlib

```

### **実行 (Execution)**

コード末尾の `generate_artifacts(n)` の引数に任意の初期値（例: 121, 25, 1849 など）を与えて実行してください。

```bash
python code_01_collatz_3n5_jacobsthal_spinor.py

```

実行後、スクリプトと同じディレクトリに、高解像度の対数螺旋プロット（PNG）と、各ステップの波源・シフト数を記録した構造データ（CSV）が出力されます。

---

## **ライセンス (License)**

本リポジトリに含まれる成果物は、以下のライセンスの下で公開されています。

* **Research Documents (PDF, MD):** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
* **Python Source Code:** [MIT License](https://opensource.org/licenses/MIT)

Copyright (c) 2026 Hiroshi Harada

---