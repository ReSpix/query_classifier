import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans

# Загрузка необходимых ресурсов NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Загрузка стоп-слов и инициализация лемматизатора
stop_words = set(stopwords.words('english'))
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

# Пример данных
texts = [
    "Looking for a job as a software developer in Moscow",
    "Looking for remote work in IT field",
    "Seeking a data scientist position with flexible hours",
    "Need a part-time role in machine learning"
]

# Предобработка данных
processed_texts = [preprocess_text(text) for text in texts]

# Преобразование в TF-IDF векторы
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_texts)

# Нормализация векторов
normalizer = Normalizer()
normalized_vectors = normalizer.fit_transform(tfidf_matrix)

# Обучение модели K-means
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(normalized_vectors)

def predict_cluster(new_text):
    # Предобработка нового текста
    processed_text = preprocess_text(new_text)
    
    # Преобразование в TF-IDF вектор
    new_tfidf_vector = vectorizer.transform([processed_text])
    
    # Нормализация вектора
    new_normalized_vector = normalizer.transform(new_tfidf_vector)
    
    # Предсказание кластера
    predicted_cluster = kmeans.predict(new_normalized_vector)
    
    return predicted_cluster[0]

# Пример использования
new_request = "Looking for a part-time job in data analysis"
predicted_cluster = predict_cluster(new_request)
print(f"The new request belongs to cluster {predicted_cluster}")
