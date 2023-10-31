import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from tabulate import tabulate
import numbers
import statsmodels.api as sm




datos = pd.read_csv("/Users/spide/OneDrive/Documents/Mineria/games-data-limpio.csv")
df = pd.DataFrame(datos)

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] 
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df_anio[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.savefig(f'/Users/spide/OneDrive/Documents/Mineria/Tarea6/lr_{y}_{x}.png')
    plt.close()

df_anio = df.groupby("Anio").aggregate(Score_Prom=pd.NamedAgg(column="Score", aggfunc=pd.DataFrame.mean))
df_anio.reset_index(inplace=True)
print_tabulate(df_anio)

linear_regression(df_anio, "Anio", "Score_Prom")


