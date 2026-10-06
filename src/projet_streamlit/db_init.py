import psycopg
import getpass



DB_NAME = "sncf_c_gro_nul"
USER = getpass.getuser()
MDP = "secret1"


def main():

    # Connexion à une base qui existe déjà
    conn = psycopg.connect(
        f"dbname=postgres user={USER} password={MDP}",
        autocommit=True
    )

    cur = conn.cursor()

    # Vérifie si notre base existe
    cur.execute(
        "SELECT 1 FROM pg_database WHERE datname = %s",
        (DB_NAME,)
    )

    existe = cur.fetchone()

    if not existe:
        cur.execute(f'CREATE DATABASE "{DB_NAME}"')
        print(f"Base {DB_NAME} créée")
    else:
        print(f"Base {DB_NAME} existe déjà")

    cur.close()
    conn.close()

    # Maintenant la base existe, donc on peut s'y connecter
    conn = psycopg.connect(
        f"dbname={DB_NAME} user={USER} password={MDP}"
    )

    cur = conn.cursor()

    # Lecture du schema SQL
    with open("Database/shema.sql", "r") as fichier:
        sql = fichier.read()

    cur.execute(sql)

    conn.commit()

    print("Tables créées")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()