-- 1.
-- Geef een lijst van de steden waar onze klanten wonen.

SELECT DISTINCT(city.city)
FROM customer JOIN address
ON customer.address_id = address.address_id
JOIN city
ON address.city_id = city.city_id;


-- 2. 
-- Geef een lijst van films met een verhuurwaarde groter en gelijk dan 5
-- Geef de namen van de films met een duur tussen 80 en 90 minuten.

SELECT film.title, film.rental_rate FROM film
WHERE film.rental_rate >= 5;

SELECT film.title FROM film
WHERE film.length > 80
AND film.length < 90

SELECT film.title FROM film
WHERE film.length BETWEEN 81 AND 89


-- 3.
-- Geef alle landen die een "e" op positie 2 hebben.
-- Geef alle landen met minder dan 5 letters.

SELECT country FROM country
WHERE SUBSTRING(country, 2,1) = 'e';

SELECT country FROM country
WHERE length(country) < 5;


-- 4.
-- Geef het id van de films, van groot naar klein, waar die een verhuurwaarde hebben kleiner als 3 of groter als 6.

SELECT film.film_id
FROM film
WHERE film.rental_rate <3
OR film.rental_rate > 6
ORDER BY film.film_id DESC


-- 5.
-- Welke adressen hebben geen postcode?
-- Welke klanten hebben geen postcode?

SELECT address.address
FROM address 
WHERE address.postal_code = ''

SELECT address.address FROM address
WHERE postal_code IS NULL
OR LENGTH(postal_code) = 0;

SELECT address, postal_code FROM address;


SELECT customer.first_name, customer.last_name
FROM customer JOIN address
ON customer.address_id = address.address_id
WHERE address.postal_code = ''


-- 6.
-- Geef de namen van de films in de store met id = 1.
-- Geef het aantal films van deze store per categorie.
SELECT DISTINCT(title) FROM film
JOIN inventory
ON film.film_id = inventory.film_id
JOIN store
ON inventory.store_id = store.store_id
WHERE store.store_id = 1

SELECT DISTINCT inventory.store_id, film.title
FROM film
JOIN inventory
ON film.film_id = inventory.film_id
WHERE inventory.store_id = 1;



SELECT category.name, COUNT (*) as films_per_category
FROM inventory
JOIN film
ON film.film_id = inventory.film_id
JOIN film_category
ON film_category.film_id = film.film_id
JOIN category
ON film_category.category_id = category.category_id
GROUP BY inventory.store_id, category.name
HAVING inventory.store_id = 1
ORDER BY category.name;


-- 7.
-- Geef de naam en voornaam van de klanten die in totaal voor meer dan 10€ hebben gehuurd.



-- 8.
-- Geef hoeveel heeft elke verkoper in totaal verhuurd. aantal films + totaal bedrag.

