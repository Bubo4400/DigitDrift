# Benford's Law Analysis Tool

A Python-based utility designed to analyze numerical datasets and determine if they adhere to **Benford's Law** (the Law of Anomalous Numbers). This tool extracts leading digits from data columns and provides both statistical verification and visual distribution analysis.

## 📊 Overview

Benford's Law predicts the frequency distribution of leading digits in many real-life sets of numerical data. This tool allows you to:
*   **Load CSV Datasets**: Efficiently parse large data files using `pandas`.
*   **Analyze Leading Digits**: Calculate the probability of digits 1 through 9 appearing as the first significant figure.
*   **Handle Small Values**: Choose whether to ignore numbers between 0 and 1 or extract the first non-zero digit (e.g., for scientific data).
*   **Visualize Results**: Generate horizontal bar charts showing the frequency of each digit compared to the theoretical expectation.
*   **Verification**: Automatically check if the selected data column respects Benford's Law patterns.

---

## 📂 Project Structure

The project is organized into modular components:

*   `main.py`: The entry point that manages the command-line interface and the main application loop.
*   `benfordsLaw.py`: Contains the mathematical logic for digit extraction and Benford's Law validation.
*   `loadDataset.py`: Handles file I/O, error checking, and column selection logic.
*   `plot.py`: Manages data visualization using `matplotlib` in a separate process.
*   **`Datasets/`**: Example datasets provided for testing, including:
    *   `API_NY.GDP.MKTP.CD_DS2_en_csv_v2_126992.csv` (World Bank GDP data)
    *   `Global Temperature.csv`
    *   `GlobalLandTemperaturesByCity.csv`
    *   `pib_per_capita_countries_dataset.csv`
    *   `PS_20174392719_1491204439457_log.csv` (Transaction logs)

---

## 🚀 Getting Started

### Prerequisites
You will need Python 3 and the following libraries installed:
```bash
pip install pandas matplotlib
```

---

## Usage

Run the `main.py` script from your terminal, passing the path to the dataset you wish to analyze as a command-line argument.

```bash
python main.py Datasets/pib_per_capita_countries_dataset.csv
```

---

### Navigation
Once the file is loaded, follow the on-screen prompts:
1.  **Column Selection**: Choose the numerical column you wish to analyze.
2.  **Zero Feature**: Toggle whether to skip numbers between 0 and 1 or find the first non-zero digit.
3.  **Analysis Options**:
    *   **0**: Draw a frequency plot.
    *   **1**: Run a check to see if the dataset respects Benford's Law.
    *   **2**: Toggle the leading-zero logic dynamically.
    *   **3**: Change the active column for the current dataset.
    *   **4**: Exit the program.

---

## 🛠 Technical Details

The tool calculates the expected distribution using the standard Benford formula:
$$P(d) = \log_{10}(1 + \frac{1}{d})$$

The extraction logic in `benfordsLaw.py` ensures that negative signs are handled and provides a toggle for scientific/decimal precision. Plotting is handled via the `multiprocessing` module in `plot.py` to allow the user to continue interacting with the CLI while the graph window is open.

### Example Datasets Included
The `Datasets/` folder contains several real-world examples to get you started:
*   `API_NY.GDP.MKTP.CD_DS2_en_csv_v2_126992.csv`
*   `Global Temperature.csv`
*   `pib_per_capita_countries_dataset.csv`
