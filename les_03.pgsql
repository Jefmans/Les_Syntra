-- -- SELECT id, author FROM proglang_tbl;

-- -- SELECT * FROM proglang_tbluk;

-- -- CREATE TABLE proglang_tbl_2
-- --         AS
-- --         SELECT id FROM proglang_tbluk;

-- -- SELECT * FROM proglang_tbl_2;        


-- -- SELECT language,
-- --         year
-- -- FROM proglang_tbl ORDER BY year DESC;


-- -- SELECT language,
-- --         year
-- -- FROM proglang_tbl
-- -- ORDER BY year DESC, language ASC;

-- -- SELECT * FROM proglang_tbl;


-- -- SELECT language,
-- --         author
-- -- FROM proglang_tbl
-- -- WHERE standard = 'ANSI';


-- -- INSERT INTO
-- -- proglang_tbl 
-- --     (id, language, author, year, standard)
-- -- VALUES
-- -- (1, ....),
-- -- (1, ....),
-- -- (1, ....),

-- -- UPDATE proglang_tbl SET
-- -- standard ='ISO'
-- -- WHere id = 1;

-- -- DELETE FROM test;

-- -- CREATE TABLE test
-- -- AS
-- -- SELECT * FROM proglang_tbl;

-- -- SELECT * FROM test;


-- SELECT * FROM proglang_tbl;

-- CREATE TABLE stdlang_tbl
-- (language varchar(20), 
-- standard varchar(10));

-- INSERT INTO stdlang_tbl
-- SELECT language, standard
-- FROM proglang_tbl
-- WHERE standard IS NOT NULL;

-- SELECT * FROM proglang_tbl;
-- SELECT * FROM stdlang_tbl;

-- DROP TABLE stdlang_tbl;


-- CREATE TABLE stdlang_tbl
-- (language varchar(20) PRIMARY KEY, 
-- standard varchar(10));

-- INSERT INTO stdlang_tbl
-- SELECT language, standard
-- FROM proglang_tbl
-- WHERE standard IS NOT NULL;

-- SELECT * FROM proglang_tbl;
-- SELECT * FROM stdlang_tbl;

-- DELETE FROM proglang_tbl;

-- INSERT INTO proglang_tbl
-- (id, language, author, year, standard)
-- VALUES
--     (2, 'Perl', 'Wall', '1987', NULL),
--     (6, 'JJJ', 'Schwartz', '1959', 'US-DOD'),
--     (3, 'APL', 'Iverson', '1964', 'ANSI'),
--     (1, 'Prolog', 'Comeruer', '1972', 'ISO'),
--     (4, 'JVIAL', 'Schwartz', '1959', 'US-DOD'),
--     (5, 'APT', 'Ross', '1959', 'ISO')
--     ;

-- DROP TABLE stdlang_tbl;

-- CREATE TABLE stdlang_tbl
-- (language varchar(20) PRIMARY KEY, 
-- standard varchar(10));

-- INSERT INTO stdlang_tbl
-- SELECT language, standard
-- FROM proglang_tbl
-- WHERE standard IS NOT NULL;

-- CREATE TABLE standardizing_bodies 
--     (name varchar(10) UNIQUE)

-- INSERT INTO standardizing_bodies
-- SELECT standard FROM proglang_tbl
-- WHERE standard IS NOT NULL;

-- SELECT * FROM standardizing_bodies;

-- DROP TABLE proglang_tbl;

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
--         (5, 'APT', 'Ross', 1959, 'ISO')
--                 ;        

-- SELECT * FROM proglang_tbl;

-- DROP TABLE stdlang_tbl;

-- CREATE TABLE stdlang_tbl
--         (language varchar(20) PRIMARY KEY,
--         standard varchar (10));

-- INSERT INTO stdlang_tbl
--         SELECT language,
--                 standard
--         FROM proglang_tbl
--         WHERE standard IS NOT NULL;

-- SELECT * FROM proglang_tbl;

-- SELECT * FROM stdlang_tbl;


-- CREATE TABLE standardizing_bodies
--         ( name varchar(10) UNIQUE );

-- INSERT INTO standardizing_bodies
--         SELECT standard FROM proglang_tbl
--         WHERE standard IS NOT NULL;        

-- INSERT INTO proglang_tbl
-- (id, language, author, year, standard)        
-- VALUES
-- (6, 'Forth', 'Moore', 1973, NULL),
-- (7, 'Tcl', 'Ousterhout', 1988, NULL);

-- SELECT * FROM proglang_tbl;

-- UPDATE proglang_tbl SET
-- year = year + 10;

-- SELECT * FROM proglang_tbl;

-- UPDATE proglang_tbl SET
-- year = year - 10;

-- SELECT * FROM proglang_tbl;


-- UPDATE proglang_tbl SET
-- year = 1972
-- WHere language = 'Forth';

-- SELECT * FROM proglang_tbl;

-- CREATE TABLE test_tbl
-- AS
-- SELECT * FROM proglang_tbl;

-- UPDATE test_tbl SET
-- year = 1972;

-- SELECT * FROM test_tbl;

-- UPDATE proglang_tbl SET
-- year = 1973,
-- standard = 'ANSI'
-- Where language = 'Forth';

-- SELECT * FROM proglang_tbl;


-- DELETE FROM stdlang_tbl;

-- SELECT * FROM stdlang_tbl;

-- SELECT * FROM proglang_tbl;

