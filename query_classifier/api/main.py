from fastapi import FastAPI
import nltk
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Позволяет всем источникам, можно указать конкретные
    allow_credentials=True,
    allow_methods=["*"],  # Позволяет все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Позволяет все заголовки
)

nltk.download('stopwords')


@app.get("/status")
async def root():
    return 'im ok'


import dill
import pandas as pd


def load_pipe_data():
    model_filename = "/code/app/model.pkl"
    with open(model_filename, "rb") as file:
        data = dill.load(file)
    return data["pipeline"], data["inverser"]


pipeline, inverser = load_pipe_data()


def get_prediction(query):
    frame = pd.DataFrame({"query": [query]})

    try:
        prediction_raw = pipeline.predict(frame)
        prediction = inverser.transform(prediction_raw)
    except Exception as e:
        print(e)
        return {'по должности-лемме': 'Нет', 'общие фразы': 'общая фраза', 'занятость': ['Нет'], 'по дополнительному признаку': ['Нет'], 'по условиям': ['Нет']}

    return prediction


@app.get("/classification/{query}")
async def root(query):
    prediction = get_prediction(query)
    return {"query": query, "result": prediction}