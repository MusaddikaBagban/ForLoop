import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# --- One-time Downloads for NLTK ---
# This corrected block ensures the necessary resources are available
try:
    # A more robust way to check if resources exist
    stopwords.words('english')
    nltk.data.find('tokenizers/punkt')
except LookupError:
    # If they don't exist, download them
    print("Downloading NLTK resources (stopwords, punkt)...")
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)
    print("Download complete.")

# --- 1. Data Loading & Preprocessing ---
# This section creates the sample dataset for demonstration.
data = {
    'text': [
        "This project is incredibly helpful and well-structured!",
        "I am very happy with the results.",
        "The system is efficient and lightweight.",
        "This is the worst experience I have ever had.",
        "The model's performance is disappointing and inaccurate.",
        "I am not satisfied with this product at all.",
        "It's an okay tool, neither good nor bad.",
        "The analysis provided valuable insights for our business."
    ],
    'sentiment': [
        'positive', 'positive', 'positive',
        'negative', 'negative', 'negative',
        'negative', 'positive'
    ]
}
df = pd.DataFrame(data)

print("--- Original Data ---")
print(df)

# This function cleans and prepares the text data.
def preprocess_text(text):
    """
    Cleans and prepares text data for feature extraction.
    - Converts to lowercase
    - Removes URLs and special characters
    - Tokenizes text
    - Removes stopwords
    """
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

# Apply the preprocessing function to the text column.
df['cleaned_text'] = df['text'].apply(preprocess_text)

print("\n--- Data After Preprocessing ---")
print(df[['text', 'cleaned_text']])

# --- 2. Feature Extraction & Data Splitting ---
# Define features (X) and the target label (y).
X = df['cleaned_text']
y = df['sentiment']

# Split data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Convert text data into numerical vectors using TF-IDF.
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# --- 3. Model Training & Evaluation ---
# Initialize and train the Logistic Regression model.
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Make predictions on the test data.
y_pred = model.predict(X_test_tfidf)

# Print the evaluation report.
print("\n--- Model Evaluation Report ---")
print(classification_report(y_test, y_pred))

# --- 4. Predicting New Text ---
# This section demonstrates how to use the trained model on new, unseen data.
print("\n--- Predicting on New Sentences ---")
new_sentences = [
    "The customer feedback is overwhelmingly positive.",
    "This is a complete failure and a waste of time."
]

# Clean and transform the new sentences.
new_sentences_cleaned = [preprocess_text(text) for text in new_sentences]
new_sentences_tfidf = tfidf_vectorizer.transform(new_sentences_cleaned)

# Predict the sentiment of the new sentences.
new_predictions = model.predict(new_sentences_tfidf)

# Display the results.
for text, sentiment in zip(new_sentences, new_predictions):
    print(f"'{text}' -> Predicted Sentiment: {sentiment.upper()}")