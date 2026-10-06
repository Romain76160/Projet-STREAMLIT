import psycopg
import getpass


DB_NAME = "sncf_c_gro_nul"
USER = getpass.getuser()
MDP = "secret1"


def main():

    # --------------------------------------------------
    # 1. Connexion à PostgreSQL sur la base "postgres"
    # --------------------------------------------------

    conn = psycopg.connect(
        dbname="postgres",
        user=USER,
        password=MDP,
        host="localhost",
        autocommit=True
    )

    cur = conn.cursor()

    # --------------------------------------------------
    # 2. Vérifier si la base existe
    # --------------------------------------------------

    cur.execute(
        "SELECT 1 FROM pg_database WHERE datname = %s",
        (DB_NAME,)
    )

    existe = cur.fetchone()

    if existe is None:

        cur.execute(
            f'CREATE DATABASE "{DB_NAME}"'
        )

        print(f"Base {DB_NAME} créée")

    else:

        print(f"Base {DB_NAME} existe déjà")

    cur.close()
    conn.close()

    # --------------------------------------------------
    # 3. Connexion à notre base
    # --------------------------------------------------

    conn = psycopg.connect(
        dbname=DB_NAME,
        user=USER,
        password=MDP,
        host="localhost"
    )

    cur = conn.cursor()

    # --------------------------------------------------
    # 4. Création des tables avec shema.sql
    # --------------------------------------------------

    with open(
        "Database/shema.sql",
        "r",
        encoding="utf-8"
    ) as fichier:

        sql = fichier.read()

    cur.execute(sql)

    conn.commit()

    print("Tables créées")

    # --------------------------------------------------
    # 5. Vérifier si des données existent déjà
    # --------------------------------------------------

    cur.execute(
        "SELECT COUNT(*) FROM regularite_tgv"
    )

    nb_lignes = cur.fetchone()[0]

    # --------------------------------------------------
    # 6. Import du CSV si la table est vide
    # --------------------------------------------------

    if nb_lignes == 0:

        print("Import du CSV...")

        with open(
            "Data/regularite-mensuelle-tgv-aqst.csv",
            "r",
            encoding="utf-8"
        ) as fichier_csv, cur.copy("""
                COPY regularite_tgv (
                    date,
                    service,
                    gare_depart,
                    gare_arrivee,
                    duree_moyenne,
                    nb_circulation_prevues,
                    nb_annulation,
                    commentaire_annulation,
                    nb_train_depart_retard,
                    retard_moyen_depart,
                    retard_moyen_tous_trains_depart,
                    commentaire_retards_depart,
                    nb_train_retard_arrivee,
                    retard_moyen_arrivee,
                    retard_moyen_tous_trains_arrivee,
                    commentaires_retard_arrivee,
                    nb_train_retard_sup_15,
                    retard_moyen_trains_retard_sup15,
                    nb_train_retard_sup_30,
                    nb_train_retard_sup_60,
                    prct_cause_externe,
                    prct_cause_infrastructure,
                    prct_cause_gestion_trafic,
                    prct_cause_matériel_roulant,
                    prct_cause_matériel_gestion_et_matériel,
                    prct_cause_voyageurs
                )
                FROM STDIN
                WITH (
                    FORMAT CSV,
                    HEADER TRUE,
                    DELIMITER ';'
                )
            """) as copy:

            while data := fichier_csv.read(1024 * 1024):
                copy.write(data)

        conn.commit()

        # Vérification
        cur.execute(
            "SELECT COUNT(*) FROM regularite_tgv"
        )

        nb_lignes = cur.fetchone()[0]

        print(f"{nb_lignes} lignes importées")

    else:

        print(
            f"Les données sont déjà présentes : "
            f"{nb_lignes} lignes"
        )

    # --------------------------------------------------
    # 7. Fermeture
    # --------------------------------------------------

    cur.close()
    conn.close()

    print("Base de données prête.")


if __name__ == "__main__":
    main()