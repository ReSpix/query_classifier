import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Пример создания dataframe
data = pd.DataFrame({
    'query': ['query1', 'query2', 'query3'],
    'занятость': ['full-time', 'part-time', 'full-time'],
    'по должности-лемме': ['developer', 'manager', 'tester'],
    'по дополнительному признаку': ['feature1', 'feature2', 'feature3'],
    'по условиям': ['condition1', 'condition2', 'condition3'],
    'общая фраза': ['phrase1', 'phrase2', 'phrase3']
})

# Определение столбцов для различных преобразований
countvectorizer_columns = ['query', 'занятость', 'по дополнительному признаку']
onehotencoder_columns = ['по должности-лемме', 'по условиям', 'общая фраза']

# Создание трансформеров
countvectorizer_transformer = Pipeline(steps=[
    ('countvectorizer', CountVectorizer())
])

onehotencoder_transformer = Pipeline(steps=[
    ('onehotencoder', OneHotEncoder())
])

# Создание ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('countvectorizer', CountVectorizer(), countvectorizer_columns),
        ('onehotencoder', OneHotEncoder(), onehotencoder_columns)
    ]
)

# Разделение на X и y
X = data.drop(columns=['query'])  # Убираем 'query' из X
y = data['query']  # Используем 'query' как target

# Разделение на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание полного Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# Обучение модели
model.fit(X_train, y_train)

# Оценка модели
score = model.score(X_test, y_test)
print(f'Model accuracy: {score}')
