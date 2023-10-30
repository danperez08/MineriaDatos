import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols


datos = pd.read_csv("/Users/spide/OneDrive/Documents/Mineria/games-data-limpio.csv")
df = pd.DataFrame(datos)

df.boxplot("Score", by="Anio", figsize=(15,9))
plt.xticks(rotation=45)
plt.title("Scores dados por año", fontsize=16)
plt.xlabel("Años", fontsize=13)
plt.ylabel("Score", fontsize=13)
plt.savefig('/Users/spide/OneDrive/Documents/Mineria/Tarea5/score_año.jpeg', bbox_inches='tight')# , bbox_inches='tight')
plt.show()

mod = ols("Score ~ Año", data=df).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)

if aov_table["PR(>F)"][0] < 0.005:
    print("Hay diferencias")

    print(aov_table)

else:
    print("No hay diferencias")

