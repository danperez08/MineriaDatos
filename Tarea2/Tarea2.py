import os
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
import datetime


df = pd.read_csv('/Users/spide/OneDrive/Documents/Mineria/games-data.csv')


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))


df.columns = ['Nombre', 'Plataforma', 'Fecha_Salida', 'Score',
        'Score_Jugadores', 'Desarrollador', 'Genero', 'Jugadores',
        'Criticos', 'Usuarios']


def convert_anio(obj):
    dto = datetime.datetime.strptime(obj, '%B %d, %Y')
    return dto.year

def convert_mes(obj):
    dto = datetime.datetime.strptime(obj, '%B %d, %Y')
    return dto.month

def convert_dow(obj):
    dto = datetime.datetime.strptime(obj, '%B %d, %Y')
    return dto.weekday()

def convert_dia(obj):
    dto = datetime.datetime.strptime(obj, '%B %d, %Y')
    return dto.day

def convert_fecha(obj):
    dto = datetime.datetime.strptime(obj, '%B %d, %Y')
    return dto


df['Anio'] = df['Fecha_Salida'].apply(convert_anio)
df['Mes'] = df['Fecha_Salida'].apply(convert_mes)
df['Numero_Dia'] = df['Fecha_Salida'].apply(convert_dia)
df['Nombre_Dia'] = df['Fecha_Salida'].apply(convert_dow)
df['Fecha_Salida'] = df['Fecha_Salida'].apply(convert_fecha)


dmap = {0:'Lun',1:'Mar',2:'Mie',3:'Jue',4:'Vie',5:'Sab',6:'Dom'}
df['Nombre_Dia'] = df['Nombre_Dia'].map(dmap)


df['Score_Jugadores'] = df['Score_Jugadores'].apply(lambda score: 0 if score == 'tbd' else score)
df['Score_Jugadores'] = pd.to_numeric(df['Score_Jugadores'])
df['Score_Jugadores'] = df['Score_Jugadores']*10


df['Jugadores'] = df['Jugadores'].fillna('No info')


df['Jugadores'] = df['Jugadores'].apply(lambda x: str(x).strip())


df['Jugadores'].replace(['1 Player', 'No Online Multiplayer'], ['1','1'], inplace=True)
df['Jugadores'].replace(['2', '1-2', '2  Online'], ['2','2','2'], inplace=True)
df['Jugadores'].replace(['1-3', '3  Online', 'Up to 3'], ['3','3','3'], inplace=True)
df['Jugadores'].replace(['1-4', '4  Online', 'Up to 4'], ['4','4','4'], inplace=True)
df.loc[(df['Jugadores'] !='1') &
         (df['Jugadores'] !='2') &
         (df['Jugadores'] !='3') &
         (df['Jugadores'] !='4') &
         (df['Jugadores'] !='No info'),
             'Jugadores'
        ] = '>4'

num_de_jugadores = df.groupby(['Jugadores']).size().reset_index(name='counts')


df['Genero'] = df['Genero'].apply(lambda s: s.lower().replace(' ',''))


df['Lista_Generos'] = df['Genero'].apply(lambda s: list(set(s.split(','))))


print_tabulate(df.head(20))


df.to_csv('/Users/spide/OneDrive/Documents/Mineria/games-data-limpio.csv', index=False)