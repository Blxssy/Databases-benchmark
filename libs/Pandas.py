import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import URL
from config import user, password, host, db_name, port, testCount, queries
import time
import numpy

def query_pandas():
    try:
        urlObj = URL.create(
            "postgresql",
            username=user,
            password=password,
            host=host,
            port=port,
            database=db_name
        )

        engine = create_engine(urlObj)

        res = []

        times = []
        for i in range(testCount):
            startTime = time.time()
            pd.read_sql(queries[0], engine)
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            pd.read_sql(queries[1], engine)
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            pd.read_sql(queries[2], engine)
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            pd.read_sql(queries[3], engine)
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        engine.dispose()
        return res
    except create_engine.Error as err:
        print("Pandas error")
        print(err)