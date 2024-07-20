import dill
import pandas as pd


def load_pipe_data():
    model_filename = "/app/model.pkl"
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
        return {'по должности-лемме': 'Нт', 'общие фразы': 'общая фраза', 'занятость': ['Нет'], 'по дополнительному признаку': ['Нет'], 'по условиям': ['Нет']}

    return prediction


if __name__ == "__main__":
    print(get_prediction(input("Введите запрос:")))
