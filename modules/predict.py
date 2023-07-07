# <YOUR_IMPORTS>
import os
import pandas as pd
import json
from datetime import datetime

import dill


def predict():
    # <YOUR_CODE>
    path = os.environ.get('PROJECT_PATH', '..')

    # Считываем тестовые данные
    files = os.listdir(f'{path}/data/test')
    filtered_files = [file for file in files if file.endswith('.json')]
    df = pd.DataFrame()
    for file in filtered_files:
        file_name = os.path.join(f'{path}/data/test', file)
        with open(file_name, 'r') as f:
            data = json.load(f)
        data = pd.DataFrame([data])
        df = pd.concat([df, data], ignore_index=True)

    # считываем последнюю сохраненную модель
    files = os.listdir(f'{path}/data/models')
    filtered_files = [file for file in files if file.startswith('cars_pipe_') and file.endswith('.pkl')]
    # Сортировка файлов по времени создания
    sorted_files = sorted(filtered_files, key=lambda file: os.path.getctime(os.path.join(f'{path}/data/models', file)),
                          reverse=True)
    # Выбор последнего файла
    latest_file = sorted_files[0]
    pipe_filename = os.path.join(f'{path}/data/models', latest_file)
    # пока без обработки ошибки отсутствия файла...
    with open(pipe_filename, 'rb') as f:
        loaded_pipeline = dill.load(f)

    # предсказываем и сохраняем
    predicted = loaded_pipeline.predict(df)
    df['prediction'] = predicted
    file_name = f'{path}/data/predictions/{datetime.now().strftime("%Y%m%d%H%M")}.csv'
    df.to_csv(file_name)


if __name__ == '__main__':
    predict()
