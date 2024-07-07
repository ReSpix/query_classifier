import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

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
data = [
    ["Looking for a job as a software developer in Moscow", "developer"],
    ["Looking for remote work in IT field", "developer"],
    ["Seeking a data scientist position with flexible hours", "data-scientist"],
    ["Need a part-time role in machine learning", "ml-engineer"]
]

# Разделение данных на тексты и метки
texts, labels = zip(*data)

# Предобработка текстов
processed_texts = [preprocess_text(text) for text in texts]

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(processed_texts, labels, test_size=0.2, random_state=42)

# Создание и обучение модели
pipeline = make_pipeline(
    TfidfVectorizer(),
    Normalizer(),
    LogisticRegression()
)

pipeline.fit(X_train, y_train)

# Оценка модели
accuracy = pipeline.score(X_test, y_test)
print(f"Model accuracy: {accuracy}")

# Функция для предсказания кластера нового запроса
def predict_cluster(new_text):
    processed_text = preprocess_text(new_text)
    predicted_cluster = pipeline.predict([processed_text])
    return predicted_cluster[0]

# Пример использования
new_request = "Looking for a part-time job in data analysis"
predicted_cluster = predict_cluster(new_request)
print(f"The new request belongs to cluster {predicted_cluster}")
