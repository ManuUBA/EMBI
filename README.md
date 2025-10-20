# 📊 EMBI – Country Risk Index

**Repository:** [EMBI](https://github.com/ManuUBA/EMBI)  
**Language:** Python  

---

## Description

This repository provides scripts to automate web scraping of the current **EMBI** (Emerging Markets Bond Index) values from the Rava website (note: legality unknown). It is ideal for financial analysts, economists, and data enthusiasts who want to keep this value updated in real time.

The project allows users to extract, process, and save EMBI data in a structured format for analysis or visualization.

---

## Features

- Automates retrieval of current EMBI values.
- Saves data in JSON format for further analysis.
- Easy to integrate into personal finance or economic monitoring tools.

---

## Repository Structure

- `EMBI.py` → Main script to extract current EMBI values from Rava
- `EMBI.json` → Processed JSON file storing the latest EMBI value
- `requirements.txt` → Librerías necesarias para ejecutar el script.  
- `README.md` → Documentación del repositorio

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ManuUBA/EMBI.git
cd EMBI
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Usage:

Run the main script to extract the current EMBI data:

```bash
python extraer_riesgo_pais.py
```

The extracted data will be saved in riesgo_pais.json.
