import sqlite3
import time
import numpy

from config import testCount

def query_sqlite():
    try:
        connection = sqlite3.connect('identifier.sqlite')
        cursor = connection.cursor()

        res = []

        times = []
        for i in range(testCount):
            startTime = time.time()
            cursor.execute(queries[0])
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            cursor.execute(queries[1])
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            cursor.execute(queries[2])
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        times = []
        for i in range(testCount):
            startTime = time.time()
            cursor.execute(queries[3])
            endTime = time.time()
            times.append(endTime - startTime)
        res.append(numpy.mean(times))

        cursor.close()
        connection.close()

        return res

    except sqlite3.Error as err:
        print("SQLite error")
        print(err)
        return []

queries = [
        "SELECT VendorID, count(*) FROM nyc_yellow_tiny GROUP BY 1;",
    "SELECT passenger_count, avg(fare_amount) FROM nyc_yellow_tiny GROUP BY 1;",
    "SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM nyc_yellow_tiny GROUP BY 1, 2;",
    "SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM nyc_yellow_tiny GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;"
]