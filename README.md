# GenAI-Automated Market Intelligence Pipeline 🚀

## Overview
This project is an automated data pipeline designed to streamline competitor analysis and market research. Built for high-level strategic decision-making, it ingests unstructured customer feedback, cleans the data, and utilizes Generative AI to extract actionable business insights.

## Features
* **Automated Data Cleaning:** Uses Pandas to handle duplicates and missing values from raw data streams.
* **LLM Integration:** Connects to the Google Gemini API to perform sentiment analysis, identify product bottlenecks, and generate strategic recommendations.
* **Interactive Dashboard:** Deployed via Streamlit to provide stakeholders with a clean, one-click interface for generating executive summaries.
* **Failsafe Engineering:** Includes error-handling logic (try/except blocks) to deploy local backup data if the live API server experiences rate-limiting (HTTP 429).

## Tech Stack
* **Python** (Core Logic)
* **Pandas** (Data Manipulation)
* **Streamlit** (Frontend Dashboard)
* **Google Generative AI** (Gemini 1.5 Flash Model)

## How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install pandas google-generativeai streamlit`
3. Add your own Google Gemini API key to `app.py`.
4. Run the application: `streamlit run app.py`
