CREATE TABLE employes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    salaire DECIMAL(10,2),
    id_service INT
);

INSERT INTO employes (nom, prenom, salaire, id_service)
VALUES ('Doe', 'John', 4000.00, 1),
       ('Smith', 'Jane', 2500.00, 2),
       ('Williams', 'Bob', 3500.50, 1),
       ('Jones', 'Mary', 2800.00, 3),
       ('Taylor', 'David', 4200.75, 2);

SELECT * FROM employes WHERE salaire > 3000.00;

#CREATE TABLE services (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50)
);

INSERT INTO services (nom)
VALUES ('Marketing'),
       ('Sales'),
       ('IT');

SELECT e.nom, e.prenom, e.salaire, s.nom as service
FROM employes e
INNER JOIN services s ON e.id_service = s.id;