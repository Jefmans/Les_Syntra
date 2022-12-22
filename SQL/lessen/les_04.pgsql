-- DROP TABLE proglang_tbl;
-- DELETE FROM proglang_tbl;

-- CREATE TABLE proglang_tbl (
--         id              INTEGER         NOT NULL        PRIMARY KEY,
--         language        VARCHAR(20)     NOT NULL        UNIQUE,
--         author          VARCHAR(25)     NOT NULL,
--         year            INTEGER         NOT NULL,
--         standard        VARCHAR(10)     NULL);

-- INSERT INTO proglang_tbl
--         (id, language, author, year, standard)
--         VALUES
--         (1, 'Prolog', 'Colmerauer', 1972, 'ISO'),
--         (2, 'Perl', 'Wall', 1987, null),
--         (3, 'ANSI', 'Iverson', '1964', 'APL'),
--         (4, 'JOVIAL', 'Schwartz', 1959, 'US-DOD'),
--         (5, 'APT', 'Ross', 1959, 'ISO'),
--         (6, 'Forth', 'Moore', 1973, NULL),
--         (7, 'Tcl', 'Ousterhout', 1988, NULL)
--                 ;     

-- SELECT * FROM proglang_tbl;


-- CREATE TABLE newlang_tbl (
--     id INTEGER NOT NULL PRIMARY KEY,
--     language VARCHAR(20) NOT NULL,
--     year INTEGER NOT NULL,
--     standard VARCHAR(10) NULL
-- );

-- CREATE TABLE authors_tbl(
--     aurhor_id INTEGER NOT NULL,
--     author VARCHAR(25) NOT NULL,
--     language_id INTEGER REFERENCES newlang_tbl(id)
-- );

-- INSERT INTO authors_tbl 
--     (aurhor_id, author, language_id)
--     VALUES
--     (5, 'Kemeny', 5);

-- INSERT INTO newlang_tbl
--     (id, language, year, standard)
--     VALUES
--     (5, 'BASIC', 1964, 'ANSI');

-- INSERT INTO authors_tbl 
--     (aurhor_id, author, language_id)
--     VALUES
--     (5, 'Kemeny', 5);

-- select * FROM authors_tbl;

SELECT * FROM proglang_tbl;
SELECT COUNT(*) FROM proglang_tbl;
SELECT COUNT(standard) FROM proglang_tbl;

INSERT INTO proglang_tbl
(id, language, author, year, standard)
VALUES
(8, 'PL/I', 'IBM', 1964, 'ECMA');

SELECT DISTINCT (year)
FROM proglang_tbl;

SELECT COUNT(year) FROM proglang_tbl;

SELECT COUNT (DISTINCT year)
FROM proglang_tbl;

SELECT * FROM proglang_tbl;

SELECT DISTINCT (standard)
FROM proglang_tbl
ORDER BY standard DESC;

SELECT DISTINCT (standard)
FROM proglang_tbl
WHERE standard IS NOT NULL
; 

SELECT COUNT (DISTINCT standard)
        FROM proglang_tbl;

SELECT id,
language,
author as creator
FROM proglang_tbl;

ALTER TABLE proglang_tbl
RENAME COLUMN aut TO author;

ALTER TABLE proglang_tbl
RENAME TO prog;

ALTER TABLE prog
RENAME TO proglang_tbl;


SELECT  *
FROM INFORMATION_SCHEMA.TABLES
WHERE table_name = 'proglang_tbl';

SELECT id,
language,
author creator
FROM proglang_tbl
WHERE creator = 'Ross';

SELECT id,
language,
author creator
FROM proglang_tbl
ORDER BY creator;


SELECT * FROM proglang_tbl
WHERE language LIKE 'P%';

SELECT * FROM proglang_tbl
WHERE language LIKE '%l%';

SELECT * FROM proglang_tbl
WHERE CAST(year as TEXT) LIKE '%59';

SELECT * FROM proglang_tbl
WHERE language LIKE '__l';


SELECT * FROM proglang_tbl
WHERE language NOT LIKE '__l';


SELECT language,
        (year % 10) remainder
FROM proglang_tbl;

SELECT language,
        year - (year % 10) decade
FROM proglang_tbl;

SELECT language,
        (year / 10) * 10 decade
FROM proglang_tbl;

SELECT language,
        'The '||(year / 10) * 10||'s' decade
        FROM proglang_tbl;

SELECT language,
        CONCAT(
            'The ', (year / 10) * 10, 's' 
        ) decade
FROM proglang_tbl;        

SELECT SUBSTR(language, 2, 3),
        year
FROM proglang_tbl;

SELECT UPPER(language),
        LOWER(standard)
FROM proglang_tbl;

SELECT language,
        year,
        'AD' AD
FROM proglang_tbl;

SELECT AVG(year) FROM proglang_tbl;

SELECT CAST(AVG(year) as INTEGER)
FROm proglang_tbl;

SELECT CAST(language AS INTEGER)
        FROM proglang_tbl;

SELECT SUM(year) FROM proglang_tbl;

SELECT SUM(language)
FROM proglang_tbl;

SELECT MIN(year) FROM proglang_tbl;
SELECT MAX(year) FROM proglang_tbl;
SELECT MIN(year), MAX(year) FROM proglang_tbl;
SELECT MIN(language), MAX(year) FROM proglang_tbl;

INSERT INTO proglang_tbl
        (id, language, author, year, standard)
        VALUES
        (9, 'Fortran', 'Backus', 1957, 'ANSI');

SELECT * FROM proglang_tbl;

SELECT standard FROM proglang_tbl
WHERE standard IS NOT NULL
GROUP BY standard;

SELECT standard FROM proglang_tbl
WHERE standard IS NOT NULL;

SELECT standard,
        language
FROM proglang_tbl
WHERE standard IS NOT NULL
GROUP BY standard;


SELECT standard,
        language
FROM proglang_tbl
WHERE standard IS NOT NULL
GROUP BY standard, language;

SELECT standard,
COUNT(*)
FROM proglang_tbl
GROUP BY standard;

SELECT * FROM proglang_tbl;

SELECT year,
        MIN(language),
        COUNT(*)
FROM proglang_tbl
GROUP BY year;

SELECT language,
        standard,
        year
FROM proglang_tbl
GROUP BY standard, 
        year,
        language
HAVING year < 1980;

SELECT standard 
FROM proglang_tbl
WHERE COUNT(standard) > 1
GROUP BY standard;

SELECT standard 
FROM proglang_tbl
GROUP BY standard
HAVING COUNT(standard) > 1;

SELECT language,
        standard,
        year
FROM proglang_tbl
GROUP BY standard, 
        year,
        language
HAVING year < 1980;


SELECT language,
        standard,
        year
FROM proglang_tbl
where year < 1980
GROUP BY standard, 
        year,
        language
;

SELECT year,
        MIN(language),
        COUNT(*)
FROM proglang_tbl
GROUP BY year;



SELECT * FROM proglang_tbl;


SELECT standard
        FROM proglang_tbl
        GROUP BY standard
        HAVING COUNT(*) > 1;