# 📊 WordScope
### Interactive Multi-Document Word Frequency Analyzer

[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-red?logo=streamlit)](https://wordscope-kec4pgcnsgstlutyieswuw.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)

## 🌐 Live Application

**Try WordScope:** https://wordscope-kec4pgcnsgstlutyieswuw.streamlit.app/

## 📌 Project Overview

WordScope is an interactive web-based application designed to analyze and visualize word frequency across multiple text documents.

Users can upload TXT and PDF files, extract their text, remove common stopwords, calculate word frequencies, and explore visual comparisons through interactive charts.

## 🎯 Objectives

- Extract text from multiple documents.
- Remove common stopwords and unnecessary words.
- Calculate word frequency in each document.
- Visualize the most frequently used words.
- Compare word frequencies across multiple documents.
- Provide downloadable frequency analysis results.

## ✨ Key Features

- **Multiple Document Upload:** Supports TXT and PDF files.
- **Text Processing:** Converts text to lowercase and removes stopwords.
- **Word Frequency Analysis:** Counts occurrences of meaningful words.
- **Combined Visualization:** Displays word frequency across all uploaded documents.
- **Individual Analysis:** Visualizes word frequencies for each document separately.
- **Document Comparison:** Compares word usage across documents.
- **Interactive Charts:** Uses Plotly for data visualization.
- **CSV Export:** Allows users to download frequency results.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming and text processing |
| Streamlit | Interactive web application |
| Pandas | Data handling |
| Plotly | Interactive visualizations |
| PyPDF | PDF text extraction |
| Regular Expressions | Text cleaning and tokenization |

## ⚙️ Application Workflow

1. Upload multiple TXT or PDF documents.
2. Extract text from the uploaded documents.
3. Convert text into lowercase.
4. Tokenize the text into individual words.
5. Remove stopwords and short words.
6. Calculate word frequencies.
7. Generate combined and individual visualizations.
8. Compare document frequencies.
9. Download the results as a CSV file.

## 🖥️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ajmal-D/WordScope.git
```

### 2. Navigate to the project folder

```bash
cd WordScope
```

### 3. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## 📁 Project Structure

```text
WordScope/
│
├── app.py
├── processor.py
├── requirements.txt
└── sample_documents/
    ├── document1.txt
    ├── document2.txt
    └── document3.txt
```

## 🎓 Academic Information

**Course:** Information Visualization  
**Course Code:** 21CSE481T  
**Semester:** VII  
**Academic Year:** 2026–2027

## 🚀 Deployment

The application is deployed using **Streamlit Community Cloud** and is accessible through the public live application link.

## 📄 License

This project is developed for academic purposes as part of the Information Visualization course assignment.
