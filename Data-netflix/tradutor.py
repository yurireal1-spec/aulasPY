import pandas as pd

df=pd.read_json('netflix_titles.json')

traducao={
    'show_id': 'id',
    'type':'tipo',
    'title': 'titulo',
    'director': 'diretor',
    'cast': 'elenco',
    'country': 'pais',
    'date_added':'data_adicionada',
    'release_year': 'ano_lancamento',
    'rating': 'avaliacao',
    'duration':'duracao',
    'listed_in': 'categoria',
    "description": 'descricao',
}   

df=df.rename(columns=traducao)

print(df.columns)