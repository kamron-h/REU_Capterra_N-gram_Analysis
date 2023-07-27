import nltk
import pandas as pd
from nltk import ngrams, FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Used for review dates
import pandas as pd
import re
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

# TODO: Uncomment the following lines if you are running this for the first time
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

def ngram_analysis(file_path, n):
    # 1. Read the data from excel file
    df = pd.read_excel(file_path)

    # Convert the "Cons" column into a single string
    text = ' '.join(df['All NCSS Capterra Cons'])

    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Perform Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Generate n-grams
    n_grams = list(ngrams(tokens, n))

    # Calculate frequency distribution
    freq_dist = FreqDist(n_grams)

    # Calculate total number of n-grams
    freq_count = len(freq_dist)

    # Print the n most common n-grams and their counts
    for gram, count in freq_dist.most_common(100):
        print(f'{" ".join(gram)}: {count}')

    print(f'\nTotal Token Count: {freq_count}')


# Usage
print('\n\nUsing the N-gram model to calculate word and word pair frequencies.')
file_path = 'Capterra_Cons_Excel.xlsx'
ngram_analysis(file_path, 3)  # Change 2 to whatever 'n' you want

def process_date_data(file_name):
    # Read data
    df = pd.read_csv(file_name)

    # Convert the dataframe into a single string
    text = " ".join(df.values.flatten().astype(str))

    # Extract only four-digit numbers
    cleaned_text = " ".join(re.findall(r'\b\d{4}\b', text))

    if cleaned_text:
        # Use the N-gram model to calculate the number of occurrences for each 4-digit year
        vectorizer = CountVectorizer(ngram_range=(1, 1), token_pattern=r'\b\w+\b', min_df=1)
        X = vectorizer.fit_transform(cleaned_text.split())

        try:
            vocab = list(vectorizer.get_feature_names_out())
        except AttributeError:
            vocab = list(vectorizer.get_feature_names())

        counts = X.sum(axis=0).A1
        freq_distribution = Counter(dict(zip(vocab, counts)))

        # Print out the results
        for word, freq in freq_distribution.items():
            print(f"Word: {word}, Frequency: {freq}")
    else:
        print("No four-digit numbers found in the dataset.")


# Use the function
print('\n\nUsing the N-gram model to calculate the number of occurrences for each 4-digit year.')
process_date_data("Capterra_Review_Dates.csv")
