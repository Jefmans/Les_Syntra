
-- SELECT * FROM newlang_tbl;
-- SELECT * FROM authors_tbl;
-- SELECT * FROM proglang_tbl;




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
--         (9, 'Fortran', 'Backus', 1957, 'ANSI')
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

SELECT * FROM authors_tbl;

SELECT author FROM authors_tbl
WHERE language_id IN (
    SELECT id FROM newlang_tbl
    WHERE language='Tcl'
    OR language = 'Prolog'
)

SELECT * FROM newlang_tbl;

SELECT author, language
        FROM authors_tbl a,
            (
                SELECT id, language
                FROM newlang_tbl
                WHERE year > 1980
            ) new
WHERE a.language_id = new.id;



SELECT language,
        year
FROM newlang_tbl
WHERE EXISTS (
    SELECT * FROM authors_tbl
    WHERE newlang_tbl.id = language_id
    AND year > 1975
);

    SELECT language,
        year
FROM newlang_tbl;

    SELECT * FROM authors_tbl, newlang_tbl
    WHERE newlang_tbl.id = language_id
    AND year > 1975


SELECT language,
        year
FROM newlang_tbl
WHERE NOT EXISTS (
    SELECT * FROM authors_tbl
    WHERE newlang_tbl.id = language_id
);    

SELECT * FROM newlang_tbl;
SELECT * FROM authors_tbl;



INSERT INTO newlang_tbl
(id, language, year, standard)
VALUES (7, 'Pascal', 1970, 'ISO');



INSERT INTO authors_tbl
(author_id, author, language_id)
VALUES (7, 'Wirth',
        (
            SELECT id FROM newlang_tbl WHERE language='Pascal')
        );

SELECT * FROM newlang_tbl;
SELECT * FROM authors_tbl;


INSERT INTO newlang_tbl
(id, language, year, standard)
VALUES (9, 'Lisp', 'ISO');

SELECT language FROM newlang_tbl
WHERE year > ANY (SELECT year FROM newlang_tbl);


SELECT * FROM newlang_tbl;

SELECT language FROM newlang_tbl
WHERE year < ANY (SELECT year FROM newlang_tbl);


SELECT * FROM newlang_tbl;

SELECT language
FROM newlang_tbl
WHERE year <= ALL (
    SELECT year FROM newlang_tbl
    )