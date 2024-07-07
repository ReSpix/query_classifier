import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer

# Загрузка стоп-слов и инициализация лемматизатора
stop_words = set(stopwords.words('russian'))
lemmatizer = WordNetLemmatizer()

# Функция очистки текста
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

# Функция токенизации текста
def tokenize(text):
    tokens = word_tokenize(text)
    return tokens

# Функция удаления стоп-слов
def remove_stopwords(tokens):
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

# Функция лемматизации токенов
def lemmatize_tokens(tokens):
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

# Обработка текста
def preprocess_text(text):
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    return ' '.join(tokens)

# Пример использования
texts = ["Ищу работу программистом в Москве", "Ищу удаленную работу в сфере IT"]
processed_texts = [preprocess_text(text) for text in texts]

# Преобразование в TF-IDF векторы
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_texts)

# Нормализация векторов
normalizer = Normalizer()
normalized_vectors = normalizer.fit_transform(tfidf_matrix)

print(normalized_vectors)
