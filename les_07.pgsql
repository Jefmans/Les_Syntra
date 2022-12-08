




-- DROP TABLE  authors_tbl;
-- DROP TABLE  proglang_tbl;
-- DROP TABLE  newlang_tbl;

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
--         (7, 'Tcl', 'Ousterhout', 1988, NULL),
--         (8, 'PL/I', 'IBM', 1964, 'ECMA'),
--         (9, 'Fortran', 'Backus', 1957, 'ANSI'),
--         (10, 'APL', 'Iverson', 1964, 'ANSI')
--         ;   



-- CREATE TABLE newlang_tbl (
--     id INTEGER NOT NULL PRIMARY KEY,
--     language VARCHAR(20) NOT NULL,
--     year INTEGER NOT NULL,
--     standard VARCHAR(10) NULL
-- );

-- CREATE TABLE authors_tbl(
--     author_id INTEGER NOT NULL,
--     author VARCHAR(25) NOT NULL,
--     language_id INTEGER REFERENCES newlang_tbl(id)
-- );


-- INSERT INTO newlang_tbl
--     (id, language, year, standard)
--     VALUES
--     (1, 'Prolog', 1972, 'ISO');

-- INSERT INTO newlang_tbl
--     (id, language, year)
--     VALUES
--     (2, 'Perl', 1987);

-- INSERT INTO newlang_tbl
--     (id, language, year, standard)
--     VALUES
--     (3, 'APL', 1964, 'ANSI');

-- INSERT INTO newlang_tbl
--     (id, language, year)
--     VALUES
--     (4, 'Tcl', 1988);

-- INSERT INTO newlang_tbl
--     (id, language, year, standard)
--     VALUES
--     (5, 'BASIC', 1964, 'ANSI');

-- INSERT INTO authors_tbl
--     (author_id, author, language_id)
--     VALUES (6, 'Kurtz', 5);

-- INSERT INTO authors_tbl
--     (author_id, author, language_id)
--     VALUES (1, 'Colmerauer', 1);

-- INSERT INTO authors_tbl
--     (author_id, author, language_id)
--     VALUES (2, 'Wall', 2);

-- INSERT INTO authors_tbl
--     (author_id, author, language_id)
--     VALUES (3, 'Ousterhout', 4);

-- INSERT INTO authors_tbl
--     (author_id, author, language_id)
--     VALUES (4, 'Iverson', 3);

-- INSERT INTO authors_tbl 
--     (author_id, author, language_id)
--     VALUES
--     (5, 'Kemeny', 5); 

-- INSERT INTO newlang_tbl
-- (id, language, year, standard)
-- VALUES (7, 'Pascal', 1970, 'ISO');



-- INSERT INTO authors_tbl
-- (author_id, author, language_id)
-- VALUES (7, 'Wirth',
--         (
--             SELECT id FROM newlang_tbl WHERE language='Pascal')
--         );


SELECT * FROM newlang_tbl;
SELECT * FROM authors_tbl;
SELECT * FROM proglang_tbl;        


set1 = { 1, 3, 5 }

set2 = { 1, 2, 3 }

set1 UNION set2 = { 1, 3, 5, 2 }

SELECT * FROM proglang_tbl


SELECT year FROM proglang_tbl
WHERE standard='ANSI'
UNION
SELECT year FROM proglang_tbl
WHERE standard='ISO';

SELECT standard FROM proglang_tbl
WHERE language = 'Fortran'
UNION
SELECT standard FROM proglang_tbl
WHERE language = 'APL';  

SELECT standard FROM proglang_tbl
WHERE language = 'Fortran'
UNION
SELECT standard FROM proglang_tbl
WHERE language = 'APT';    

SELECT standard FROM proglang_tbl
WHERE language = 'Fortran'
UNION ALL
SELECT standard FROM proglang_tbl
WHERE language = 'APL';


set1 = { 1, 3, 5 }

set2 = { 1, 2, 3 }

set1 INTERSECTION set2 = { 1, 3 }

SELECT * FROM proglang_tbl;


SELECT standard FROM proglang_tbl
WHERE year=1964
INTERSECT
SELECT standard FROM proglang_tbl
WHERE year=1957;

SELECT standard FROM proglang_tbl
WHERE year=1964
UNION ALL
SELECT standard FROM proglang_tbl
WHERE year=1957;


set1 = { 1, 3, 5 }

set2 = { 1, 2, 3 }


set1 DIFFERENCE set2 = { 5 }

set2 DIFFERENCE set1 = { 2 }

INSERT INTO proglang_tbl
        (id, language, author, year, standard)
        VALUES
        (11, 'RPG', 'IBM', 1964, 'ISO');

SELECT * FROM proglang_tbl;         

SELECT language, year, standard FROM proglang_tbl
WHERE standard IN ('ISO');
SELECT language, year, standard FROM proglang_tbl
where standard NOT IN ('ANSI');  

-- geen exacte waarde
SELECT year FROM proglang_tbl
WHERE standard IN ('ISO')
AND standard NOT IN ('ANSI');   


SELECT year FROM proglang_tbl WHERE standard IN ('ISO')
EXCEPT
SELECT year FROM proglang_tbl WHERE standard IN ('ANSI');


CREATE VIEW language_chronology AS
SELECT language, year
FROM proglang_tbl
ORDER BY year ASC;

SELECT * FROM language_chronology;

INSERT INTO proglang_tbl
        (id, language, author, year, standard)
        VALUES
        (12, 'RPGA', 'IBMA', 1964, 'ISA');

CREATE VIEW language_decade AS
SELECT language,
'The '||((year/10)*10)||'s' decade
FROM proglang_tbl;        

SELECT * FROM language_decade;

SELECT * FROM language_chronology;


UPDATE language_chronology
SET year=1977
WHERE language='Fortran';

SELECT * FROM proglang_tbl
WHERE language='Fortran';


UPDATE language_decade 
SET decade='The 1960s'
WHERE language='JOVIAL';

CREATE VIEW standards AS
SELECT standard, count(*)
FROM proglang_tbl
GROUP BY standard;

SELECT * FROM standards;

UPDATE standards 
SET standard='IS'
WHERE standard='ISO';

DROP VIEW standards;

DROP VIEW proglang_tbl;

select *
from information_schema.columns
where table_name = 'language_chronology';

select definition from pg_views where viewname = 'language_chronology'


CREATE INDEX <index name> ON <table name> (<column list>);

CREATE INDEX language_idx 
ON proglang_tbl(language);

SELECT a.language,
        b.author,
        c.year,
        d.standard,
        e.id
INTO biglang_tbl
FROM proglang_tbl a, proglang_tbl b, proglang_tbl c, proglang_tbl d, proglang_tbl e;

EXPLAIN 
SELECT * FROM biglang_tbl 
WHERE language='Fortran'

CREATE INDEX biglang_idx
ON biglang_tbl (language)

EXPLAIN 
SELECT * FROM biglang_tbl 
WHERE language='Fortran'

SELECT pg_size_pretty(pg_total_relation_size('biglang_tbl'))

SELECT pg_size_pretty(pg_relation_size('biglang_idx'));$

DROP INDEX biglang_idx;

SELECT COUNT(*) FROM biglang_tbl;