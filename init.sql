CREATE TABLE ventes (
    id SERIAL PRIMARY KEY,
    produit TEXT NOT NULL,
    montant NUMERIC NOT NULL,
    date_vente TIMESTAMP DEFAULT NOW()
);

INSERT INTO ventes (produit, montant) VALUES
('Ordinateur', 1200),
('Clavier', 50),
('Souris', 25),
('Écran', 300),
('Casque', 75);
-- 🔁 Générer 500 lignes aléatoires de test au démarrage
DO $$
BEGIN
  FOR i IN 1..500 LOOP
    INSERT INTO ventes (produit, montant)
    VALUES (
      'Produit_' || i,
      round(random() * 1000 + 10, 2)
    );
  END LOOP;
END $$;
