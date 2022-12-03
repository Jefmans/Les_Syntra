-- 1.
-- Voeg een kolom "iso_code" toe aan de landen. Zet in deze kolom de eerste 2 letters van de landen (in hoofdletters).
ALTER TABLE country
ADD COLUMN iso_code CHAR(2);

UPDATE country 
SET iso_code = UPPER(SUBSTRING(country, 1,2));

SELECT country, iso_code
FROM country;


-- 2.
-- Geef een lijst van alle steden met hun landen erbij.
-- Geef een lijst van alle steden in SPANJE
-- Voeg Belgie en Mechelen toe (link Belgie aan Mechelen). (stel dat je het id van Belgie niet weet)

SELECT city.city, country.country
FROM city, country
WHERE city.country_id = country.country_id;


SELECT city.city, country.country
FROM city, country
WHERE city.country_id = country.country_id
AND 
country.country = 'Spain';

INSERT INTO city
(city, country_id)
VALUES
('Mechelen', (SELECT country_id FROM country WHERE country = 'Belgium'));

SELECT *
FROM city
WHERE city = 'Mechelen';


-- 3.
-- Geef een lijst met naam, voornaam en stad voor alle klanten waarvan de achternaam begint met een B.

SELECT customer.first_name, customer.last_name, city.city
FROM customer JOIN address
ON customer.address_id = address.address_id
JOIN city 
ON address.city_id = city.city_id
WHERE customer.last_name LIKE 'B%';


-- 4. 
-- Naar welke store gaat "Elizabeth Brown"?
-- Waar (stad, land) is deze store gelegen?




SELECT customer.store_id, city.city, country.country
FROM customer
JOIN store
ON customer.store_id = store.store_id
JOIN address
ON store.address_id = address.address_id
JOIN city
ON address.city_id = city.city_id
JOIN country
ON city.country_id = country.country_id
WHERE customer.first_name = 'Elizabeth'
AND customer.last_name = 'Brown';





SELECT city.city, country.country
FROM store JOIN address
ON store.address_id = address.address_id
JOIN city
ON address.city_id = city.city_id
JOIN country
ON city.country_id = country.country_id
WHERE store_id = (
            SELECT store_id
            FROM customer
            WHERE first_name ='Elizabeth'
            AND last_name = 'Brown'
        )
;