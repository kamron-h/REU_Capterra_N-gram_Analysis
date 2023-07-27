# N-gram Analysis of Software Reviews

<br>

This repository contains Python scripts for conducting N-gram analysis on software reviews.

<br>

## Dependencies

The following Python libraries are required:

- NLTK
- pandas
- scikit-learn
- collections
- re
- openpyxl

<br>

If you're running the script for the first time, uncomment the following lines to download the necessary NLTK corpora:

```python
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```
<br>

## Usage
The script contains two main functions: ngram_analysis and process_date_data.

<br>

ngram_analysis
The ngram_analysis function reads in an Excel file containing software review data, tokenizes the "All NCSS Capterra Cons" column, removes stopwords, performs lemmatization, generates N-grams, and calculates and prints the frequency distribution of these N-grams.

```python
# Usage
file_path = 'Capterra_Cons_Excel.xlsx'
ngram_analysis(file_path, 3)  # Change 3 to whatever 'n' you want for the N-gram
```

<br>

process_date_data
The process_date_data function reads in a CSV file, converts the dataframe into a single string, extracts all four-digit numbers (intended for years), and then uses the N-gram model to calculate and print the number of occurrences for each 4-digit year.

```python
# Usage
file_name = 'Review_Dates.csv'
process_date_data(file_name)
```

<br>

Please ensure the data files are in the same directory as the script when running it.