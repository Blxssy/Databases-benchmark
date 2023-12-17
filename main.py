import time
import matplotlib.pyplot as plot
import numpy as np

from libs import Pandas, PostgreSQL, SQLAlchemy, SQLite, DuckDB

plot.title('Benchmark results')

width = 0.15
plot.grid()
x = [0, 1, 2, 3]
xInd = np.arange(len(x))
plot.xticks(xInd, ['Query1', 'Query2', 'Query3', 'Query4'])

res1 = SQLite.query_sqlite()
print("SQLite ", *res1)
plot.bar(xInd- (width), res1, label="SQLite", width=width)

res2 = Pandas.query_pandas()
print("Pandas ", *res2)
plot.bar(xInd + width, res2, label="Pandas", width=width)

res3 = PostgreSQL.query_Pg()
print("Postgre ", *res3)
plot.bar(xInd-(width*2), res3, label="Postgre", width=width)

res4 = SQLAlchemy.query_SQLAlchemy()
print("SQLAlchemy ", *res4)
plot.bar(xInd + (2*width), res4, label="SQLAlchemy", width=width)

res5 = DuckDB.query_duckdb()
print("DuckDB ", *res5)
plot.bar(xInd, res5, label="DuckDB", width=width)


plot.legend()
plot.show()
