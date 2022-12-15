-- 1.
-- Geef de naam van klanten die in Spanje wonen.
SELECT last_name, country, city
FROM customer
JOIN address
ON customer.address_id = address.address_id
JOIN city
On address.city_id = city.city_id
JOIN country
ON country.country_id = city.country_id
WHERE country = 'Spain';

-- Geef naam en adres van klanten die in Madrid wonen.
SELECT last_name, address
FROM customer
JOIN address
ON customer.address_id = address.address_id
JOIN city
On address.city_id = city.city_id
WHERE city = 'Madrid';


-- Geef het aantal klanten per stad in Spanje.
SELECT city.city, COUNT(customer) 
FROM customer
JOIN address ON customer.address_id=address.address_id
JOIN city ON address.city_id=city.city_id
JOIN country ON city.country_id=country.country_id
WHERE country = 'Spain'
GROUP BY city.city;
---------------

SELECT city.city, COUNT(customer) 
FROM customer
JOIN address ON customer.address_id=address.address_id
JOIN city ON address.city_id=city.city_id
JOIN country ON city.country_id=country.country_id
GROUP BY city.city, country
HAVING country = 'Spain';

-- 2.
-- Wat is de voornaam en naam van de klant met de het langste email adres?

SELECT first_name, last_name, email
FROM customer
WHERE length(email) = (
    SELECT MAX(length(email)) 
    FROM customer
);
--------------------

SELECT customer.first_name, customer.last_name, email, length(email)
FROM customer
WHERE length(email) >= ALL (
    SELECT length(email) 
    FROM customer
    );

SELECT first_name, last_name, email
FROM customer
WHERE length(email) = (
    SELECT MAX(length(email)) 
    FROM customer
);

SELECT first_name, last_name, email
FROM customer
WHERE length(email) = 33;

SELECT length(email)
FROM customer
ORDER BY length(email) DESC;

-- Wat is de voornaam en naam van de klant met de het kortste email adres?

SELECT first_name, last_name, email
FROM customer
WHERE length(email) = (
    SELECT MIN(length(email)) 
    FROM customer
);


-- 3.
-- Geef al de categorieën die niet op een "y" eindigen.

SELECT category.name 
FROM category
WHERE category.name NOT LIKE '%y';


-- Geef het aantal films per categorie. Soorteer op aantal films van groot naar klein.

SELECT COUNT(*) aantal_films, category.name
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
GROUP BY category.name
ORDER BY aantal_films DESC;

SELECT COUNT(film_id) FROM film_category 
GROUP BY category_id
ORDER BY category_id DESC


SELECT COUNT(category_id) FROM film_category 
GROUP BY film_id
ORDER BY film_id DESC

-- Geef de gemiddelde prijs per categorie.
SELECT category.name, ROUND(AVG(film.rental_rate), 2) as gemiddelde_prijs
FROM category
JOIN film_category
ON category.category_id = film_category.category_id
JOIN film
ON film_category.film_id = film.film_id
GROUP BY category.name
ORDER BY AVG(film.rental_rate);

-- Geef de gemiddelde betaling per categorie.

SELECT ROUND(AVG(payment.amount), 2) as Gemiddelde_Prijs, category.name as CATEGORY 
FROM category
JOIN film_category
ON category.category_id =  film_category.category_id
JOIN film
ON film_category.film_id = film.film_id
JOIN inventory
ON film.film_id = inventory.film_id
JOIN rental
ON inventory.inventory_id = rental.inventory_id
JOIN payment
ON rental.rental_id =  payment.rental_id
GROUP BY category.name
ORDER BY Gemiddelde_Prijs

-- Geef de naam van de film die het meeste opbracht.


-- Geef de top 10 van films die het minste opbrachten.

-- 4.
-- Welke store heeft het meeste ACTIE films.
-- Geef het adres van de store met het meeste DRAMA films.
-- In welk land ligt de store met de minste HORROR films?

-- 5.
-- Geef de naam van de film en de bijhorende categorie.
-- Soorteer op categorie.
-- Geef de naam van de klant en naam van de gehuurde filmen voor alle verhuurbeurten met een bedrag groter dan 5.

-- 6.
-- Geef de naam van de klant die het meeste heeft gehuurd.
-- Geef de naam van landen en hun totale omzet.
-- Geef de naam van de steden, bijhorende land en de total opbrengst voor deze stad.
