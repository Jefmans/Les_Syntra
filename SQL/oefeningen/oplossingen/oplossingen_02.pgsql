-- 1.
-- Geef naam en voornaam van alle klanten
-- zet alfabetisch op naam 
SELECT last_name, first_name
FROM customer
ORDER BY last_name

-- 2.
-- Geef naam en voornaam van alle klanten
-- waarvan de naam begint met een L
-- en zet alfabetisch op voornaam
SELECT last_name, first_name
FROM customer
WHERE last_name LIKE 'L%'
ORDER BY first_name;

-- 3.
-- Hoeveel landen zijn er in de db ?
SELECT COUNT(country)
FROM country

-- 4.
-- Hoeveel films zijn er die met een "A" beginnen?
SELECT COUNT(title)
FROM film
WHERE title LIKE 'A%';
-- Hoeveel hiervan hebben een rental_rate hoger dan 3?
SELECT COUNT(title)
FROM film
WHERE title LIKE 'A%'
    AND rental_rate > 3;
-- En hoeveel hiervan duren minder lang dan 60 minuten?
SELECT COUNT(title)
FROM film
WHERE title LIKE 'A%'
    AND rental_rate > 3
    AND length < 60;

-- 5.
-- Welke categorieën beginnen met een "G" beginnen? 
SELECT name
FROM category
WHERE name LIKE 'G%';

-- 6.
-- Verhoog de verhuurprijs met 10%.
SELECT title, rental_rate 
FROM film

UPDATE film
SET rental_rate = rental_rate * 1.1;

SELECT title, rental_rate 
FROM film
-- 7.
-- Voeg een column toe in de tabel bij film waarin je het jaar van aankoop (2020) zet.
ALTER TABLE film
ADD COLUMN purchase_year INTEGER;

UPDATE film SET
purchase_year = 2020;

SELECT *
FROM film;