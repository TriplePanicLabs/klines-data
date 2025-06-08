import os
import pandas as pd

def merge(symbol: str, year: str):
    folder = f'./{symbol}/{year}'
    output_file = f'./{symbol}/{year}/{year}.csv'

    # Получаем список файлов
    csv_files = sorted([
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith('.csv')
    ])

    # Читаем и объединяем
    df_list = [pd.read_csv(file) for file in csv_files]

    merged_df = pd.concat(df_list, ignore_index=True)

    # Сохраняем результат
    merged_df.to_csv(output_file, index=False)

    print(f'✅ Объединено {len(csv_files)} файлов в {output_file}')


merge('ETHUSDT', '2022')