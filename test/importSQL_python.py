import pandas as pd
import psycopg
import getpass

conn = psycopg.connect(
    dbname="sncf_c_gro_nul",
    user=getpass.getuser(),
    password="secret1",
    host="localhost"
)

requete = """
SELECT COUNT(*)
FROM regularite_tgv;
"""

df = pd.read_sql(requete, conn)

print(df)

print(df)

conn.close()