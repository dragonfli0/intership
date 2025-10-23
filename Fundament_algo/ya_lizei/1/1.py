import pandas as pd


df = pd.read_csv('data.csv', sep=';')


def name_case(name):
    name = name.replace(' ', '_').replace('-', '_').lower()
    return name


df.columns = [name_case(col) for col in df.columns]

dict0 = {'дальнее_путешествие': 0, 'домашний_регион': 1, 'не_так_далеко': 2}
dict1 = {'да': 0, 'нет': 1}

result = (
    df.groupby('расстояние_кат')['путешествует_с_детьми']
    .value_counts(normalize=True)
    .mul(100)
    .round(1)
)

result = result.reindex(sorted(result.index, key=lambda x: (dict0[x[0]], dict1[x[1]])))

result = result.to_frame('0')

print(result)
