import dill
import pandas as pd
from pymorphy3 import MorphAnalyzer


def load_pipe_data():
    model_filename = "model.pkl"
    with open(model_filename, "rb") as file:
        data = dill.load(file)
    return data["pipeline"], data["inverser"]


pipeline, inverser = load_pipe_data()


def predict(query):
    frame = pd.DataFrame({"query": [query]})

    try:
        prediction_raw = pipeline.predict(frame)
        prediction = inverser.transform(prediction_raw)
    except:
        return {'по должности-лемме': 'Нет', 'общие фразы': 'общая фраза', 'занятость': ['Нет'], 'по дополнительному признаку': ['Нет'], 'по условиям': ['Нет']}

    return prediction


if __name__ == "__main__":
    print(predict(input("Введите запрос:")))
