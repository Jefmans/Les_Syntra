-- 1. Selecteer alle film, id en inventory_id

SELECT film.title, film.film_id, inventory.inventory_id
FROM film
LEFT JOIN inventory
ON film.film_id = inventory.film_id
ORDER BY film.film_id;


-- 2. Geef de films die niet in de inventory voorkomen

SELECT film.title, film.film_id, inventory.inventory_id
FROM film
LEFT JOIN inventory
ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IS NULL
ORDER BY film.film_id
;

-- 3. geef de films met een verhurprijs groter dab de gemiddelde verhuurprijs. (gebruik een subquery)
SELECT avg(rental_rate)
    FROM film


SELECT film.title, film.rental_rate
FROM film
WHERE film.rental_rate > (
    SELECT avg(rental_rate)
    FROM film
    );
    

-- 4. geef de id en titel van de films die zijn teruggebracht tussen '2005_05_29' en '2005_05_30' (gebruik subquery)

SELECT film_id
FROM rental
JOIN inventory
ON rental.inventory_id =  inventory.inventory_id
WHERE return_date 
BETWEEN '2005_05_29' AND '2005_05_30'


SELECT film_id, title
FROM film
WHERE film_id IN (    
    SELECT film_id
    FROM rental
    JOIN inventory
    ON rental.inventory_id =  inventory.inventory_id
    WHERE return_date 
    BETWEEN '2005_05_29' AND '2005_05_30'
)


SELECT film.film_id, film.title
FROM film
JOIN inventory
ON film.film_id = inventory.film_id
WHERE inventory_id IN (
    SELECT inventory_id
    FROM rental
    WHERE return_date
    BETWEEN '2005_05_29' AND '2005_05_30')

-- 5. Geef de voornaam + naam van de klanten die minstens 1 keer een film hebben gehuurd (gebuik subquery + EXISTS)