# Benford's Law Analysis Tool

A Python-based utility for analyzing numerical datasets to determine if they adhere to **Benford's Law** (the Law of Anomalous Numbers). Extracts leading digits and provides statistical verification plus visual distribution analysis.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Pandas](https://img.shields.io/badge/pandas-required-orange)

## Features

- **Load CSV Datasets** – Efficiently parse large data files using `pandas`.
- **Leading Digit Extraction** – Calculate the probability of digits 1–9 appearing as the first significant figure.
- **Handle Small Values** – Choose to ignore numbers between 0 and 1, or extract the first non‑zero digit (ideal for scientific data).
- **Visualize Results** – Generate horizontal bar charts comparing observed digit frequencies against the theoretical Benford distribution.
- **Verification** – Automatically check if a selected column respects Benford's Law.
- **Interactive CLI** – Change columns or toggle options without restarting.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Clone & Setup
```bash
git clone https://github.com/yourusername/DigitDrift.git
cd DigitDrift
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
Run the tool from the command line, passing the path to your CSV file:
```bash
python main.py Datasets/your_dataset.csv
```

### Navigation

Once the file is loaded, follow the on-screen prompts:

1.  **Column Selection**: Choose the numerical column you wish to analyze.
2.  **Zero Feature**: Toggle whether to skip numbers between 0 and 1 or find the first non-zero digit.

### Analysis Options

| Option | Action |
|--------|--------|
| `0` | Draw a frequency plot (horizontal bar chart) |
| `1` | Run a statistical check to see if the dataset respects Benford's Law |
| `2` | Toggle the leading‑zero logic dynamically |
| `3` | Change the active column for the current dataset |
| `4` | Exit the program |

---

## 🛠 Technical Details

The tool calculates the expected distribution using the standard Benford formula:

$$P(d) = \log_{10}\left(1 + \frac{1}{d}\right)$$

The extraction logic in `benfordsLaw.py` ensures that negative signs are handled and provides a toggle for scientific/decimal precision. Plotting is handled via the `multiprocessing` module in `plot.py` to allow the user to continue interacting with the CLI while the graph window is open.

### Example Datasets Included
The `Datasets/` folder contains several real-world examples to get you started:
*   `API_NY.GDP.MKTP.CD_DS2_en_csv_v2_126992.csv`
*   `Global Temperature.csv`
*   `pib_per_capita_countries_dataset.csv`

---

## Configuration & Notes

- **Large datasets** – `pandas` handles CSV files efficiently, but very large files may take a moment to load.
- **Negative numbers** – The tool automatically ignores the minus sign when extracting the leading digit.
- **Zero handling** – The “zero feature” toggles between:
  - *Skip*: numbers with absolute value < 1 are ignored.
  - *First non‑zero*: e.g., `0.0023` returns leading digit `2`.
- **Plotting** – If no graphical environment is available, plotting will fail gracefully (fallback to text output can be added if needed).

---

## Disclaimer

The `plot.py` modules (CLI menu and multiprocessing plotting) were partially generated with the assistance of an AI language model.

---

**Benford's Law Analysis Tool** – Uncover anomalies in your data, one digit at a time. 
