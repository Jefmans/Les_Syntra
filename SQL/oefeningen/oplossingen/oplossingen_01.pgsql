-- 1.
-- a)
SELECT country FROM country;
-- b) 109
SELECT  COUNT(*)
FROM country;

-- c)
INSERT INTO country
VALUES (110, 'België');



-- d) 2022-11-16 20:29:18.209893  //  timestamp
SELECT  country, 
        last_update 
FROM country;

SELECT  column_name,
        data_type
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'country';


----------------------------------------


-- 2. 
-- a)

CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL
);

-- b)
INSERT INTO accounts
(username, password, email)
VALUES
('joske_vermeulen', 'dejosisdebeste', 'joske_vermeulen@trammelantlei.schoten');
-- c)
INSERT INTO accounts
(username, password, email)
VALUES
('jefferson', 'jefke', 'jefke@email.com');

INSERT INTO accounts
(username, password, email)
VALUES
('jeffeeersooooon', 'jeeefkeeke', 'jeeeefke@email.be');

-- d)
SELECT * FROM accounts;

----------------------------------------

-- 3.
-- a)
SELECT first_name FROM customer;
-- b)
SELECT first_name, last_name FROM customer;
-- c) 
SELECT first_name, last_name FROM actor;
-- d)
SELECT first_name, last_name FROM customer;
-- e) 10
SELECT * FROM customer;


