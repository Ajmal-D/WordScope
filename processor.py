
import re
from collections import Counter

# Common English words to remove
STOP_WORDS = {
    "the", "is", "are", "was", "were", "a", "an",
    "and", "or", "but", "of", "in", "on", "at",
    "to", "for", "with", "from", "by", "as", "it",
    "this", "that", "these", "those", "be", "been",
    "being", "have", "has", "had", "do", "does",
    "did", "will", "would", "can", "could", "should",
    "i", "you", "he", "she", "we", "they", "them",
    "their", "our", "your", "my", "me", "his", "her",
    "its", "not", "so", "if", "then", "than", "which",
    "who", "what", "when", "where", "how", "all",
    "also", "more", "most", "such", "into", "about"
}

def clean_and_count(text):
    # Convert text to lowercase
    text = text.lower()

    # Extract words
    words = re.findall(r"\b[a-z]+\b", text)

    # Remove stopwords and very short words
    filtered_words = [
        word for word in words
        if word not in STOP_WORDS and len(word) > 2
    ]

    # Count word frequency
    return Counter(filtered_words)
