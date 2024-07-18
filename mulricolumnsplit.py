# import pandas as pd
# from sklearn.preprocessing import MultiLabelBinarizer

# # Данные
# data = {
#     'занятость': [
#         'на неполный день,Удаленная',
#         'на неполный день',
#         'на неполный день',
#         'на неполный день',
#         'на неполный день,Удаленная',
#         'на неполный день',
#         'по выходным,на неполный день',
#         'на неполный день',
#         'на неполный день',
#         'по выходным,на неполный день,Удаленная',
#         'на неполный день',
#         'на неполный день,на неполный день'
#     ]
# }

# df = pd.read_csv("answers.csv")

# # Разделение строк с множественными метками на отдельные элементы
# df['занятость'] = df['занятость'].fillna(value='Нет')
# df['занятость'] = df['занятость'].apply(lambda x: x.split(','))

# # Создание и применение MultiLabelBinarizer
# mlb = MultiLabelBinarizer()
# df_encoded = pd.DataFrame(mlb.fit_transform(df['занятость']), columns=mlb.classes_)

# # Объединение закодированных столбцов с оригинальными данными
# df = df.join(df_encoded)

# print(df.columns)


from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd

# Пример DataFrame
data = {
    'query': ['q1', 'q2', 'q3'],
    'options': [['opt1', 'opt2'], ['opt2', 'opt3'], ['opt1']],
    'statement': [['st1', 'st2'], ['st2'], ['st1', 'st3']]
}

df = pd.DataFrame(data)

# Инициализация MultiLabelBinarizer для столбцов options и statement
from sklearn.feature_extraction.text import CountVectorizer

mlb_options = CountVectorizer(analyzer=set)
mlb_statement = CountVectorizer(analyzer=set)

# Преобразование списков в список списков (двумерный массив)
options_transformed = mlb_options.fit_transform(df['options'])
statement_transformed = mlb_statement.fit_transform(df['statement'])

# Создание DataFrame для закодированных значений
df_options_encoded = pd.DataFrame(options_transformed.todense(), columns=mlb_options.get_feature_names_out())
df_statement_encoded = pd.DataFrame(statement_transformed.todense(), columns=mlb_statement.get_feature_names_out())

# Соединение закодированных данных с исходным DataFrame
df_encoded = pd.concat([df, df_options_encoded, df_statement_encoded], axis=1)

# Пример обратного преобразования
decoded_options = mlb_options.inverse_transform(df_options_encoded.values)
decoded_statement = mlb_statement.inverse_transform(df_statement_encoded.values)

# Результат
print(df)
print(df_encoded)
print(decoded_options)
print(decoded_statement)


