CREATE TABLE regularite_tgv (
    id SERIAL PRIMARY KEY,

    date TEXT,
    service TEXT,
    gare_depart TEXT,
    gare_arrivee TEXT,

    duree_moyenne INTEGER,
    nb_circulation_prevues INTEGER,
    nb_annulation INTEGER,

    commentaire_annulation TEXT,

    nb_train_depart_retard INTEGER,
    retard_moyen_depart DOUBLE PRECISION,
    retard_moyen_tous_trains_depart DOUBLE PRECISION,

    commentaire_retards_depart TEXT,

    nb_train_retard_arrivee INTEGER,
    retard_moyen_arrivee DOUBLE PRECISION,
    retard_moyen_tous_trains_arrivee DOUBLE PRECISION,

    commentaires_retard_arrivee TEXT,

    nb_train_retard_sup_15 INTEGER,
    retard_moyen_trains_retard_sup15 DOUBLE PRECISION,
    nb_train_retard_sup_30 INTEGER,
    nb_train_retard_sup_60 INTEGER,

    prct_cause_externe TEXT,
    prct_cause_infrastructure TEXT,
    prct_cause_gestion_trafic TEXT,
    prct_cause_matériel_roulant TEXT,
    prct_cause_matériel_gestion_et_matériel TEXT,
    prct_cause_voyageurs TEXT

);

