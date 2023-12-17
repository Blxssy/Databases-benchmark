#Name of file with table
file_name = "data.csv"

#Data for postgres
host = "localhost"
user = "postgres"
password = "postgres"
db_name = "postgres"
port = "5432"

#Count of tests
testCount = 10

#Queries
queries = [
    "SELECT VendorID, count(*) FROM trips GROUP BY 1;",
    "SELECT passenger_count, avg(fare_amount) FROM trips GROUP BY 1;",
    "SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;",
    "SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;"
]