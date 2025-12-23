# AI-Data-analyst
A data analyst project that handles data , perform analysis using pandas and for visualization - matplotlib and seaborn but inbuilt with an llm based ai which acts like a brain and morphs the output based on the dataset given.


![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![NumPy](https://img.shields.io/badge/NumPy-Scientific-lightgrey)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-lightblue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green)
![LLM](https://img.shields.io/badge/LLM-AI%20Reasoning-purple)
![EDA](https://img.shields.io/badge/EDA-Automated-success)

---

## 🚀 Overview

This project is a **local, LLM-powered AI data analyst** that reasons about a dataset *before* analyzing it.

Instead of running fixed plots or hardcoded statistics, an AI analyst (powered by **llama3 via Ollama**) decides:

- what kind of dataset this is  
- what analysis actually makes sense  
- which visualizations are meaningful  
- what conclusions are safe  
- what limitations must be stated  

The result is a **self-adapting data analysis pipeline** that behaves like a human analyst inside the system.

No cloud APIs. No blind automation.

---
## 🧠 Why This Is Not Just “Using an LLM”

The LLM in this project does **not** generate code, plots, or statistics.

Instead, it acts as a **reasoning layer** that:
- interprets dataset structure
- classifies dataset type
- decides what analysis is meaningful
- selects appropriate visualizations
- states limitations explicitly

All execution is handled by Python code.

This ensures:
- explainability
- safety
- reproducible results
- realistic AI system design

The goal is not automation, but **decision-making intelligence**.

 ---
## 🧠 Core Idea

The ai-intelligence is separated from execution.

- The **LLM reasons and decides**
- The **code executes safely**
- The AI never writes plotting code or touches raw data
- Every dataset produces different analysis behavior
---
##  Features

- Automatic data cleaning & quality checks  
- Automated EDA report generation  
- **LLM-based dataset type classification**  
- **LLM-driven visualization selection**  
- Summary written by AI    
- local LLM (no API keys)  

---

## 🛠 Tools Used

- **Python 3.10+**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **ydata-profiling (EDA)**
- **Ollama (llama3 local LLM)**
---
## Setup environmemt(Windows)

python -m venv venv
venv\Scripts\activate   
pip install -r requirements.txt
---
### Install Ollama
Download from:
https://ollama.com

After installation, pull the model:

```bash
ollama pull llama3

```
---
## To Run:

python run_pipeline.py
(this file runs the project in the correct order)
---
## Outputs:

reports/
├── eda_profile.html   (using automated eda)
├── visuals/
│   └── *.png         ( using matplotlib and seaborn)
└── ai_insights.md   (written by the LLM)


