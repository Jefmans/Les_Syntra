
CREATE FUNCTION get_film_count(len_from int, len_to int)
RETURNS int
LANGUAGE plpgsql
AS
$$
DECLARE 
    film_count integer;
BEGIN
    SELECT count(*) 
    into film_count
    from film
    WHERE length BETWEEN len_from AND len_to;
    RETURN film_count;
END;    
$$;

SELECT get_film_count(40, 90)




CREATE OR REPLACE FUNCTION get_film (p_pattern VARCHAR) 
    RETURNS TABLE (
        film_title VARCHAR,
        film_release_year INT
) 
AS $$
BEGIN
    RETURN QUERY SELECT
        title,
        cast( release_year as integer)
    FROM
        film
    WHERE
        title ILIKE p_pattern ;
END; $$ 

LANGUAGE 'plpgsql';

SELECT get_film('%a%');
SELECT * FROM get_film('%a%');