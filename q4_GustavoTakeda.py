def generate_inner_join_query():
    """
    Generates SQL code for INNER JOIN between GAMES, VIDEOGAMES, and COMPANY tables.

    Returns:
        str: SQL code for INNER JOIN query.
    """
    return """
    SELECT GAMES.title, GAMES.genre, GAMES.release_date, COMPANY.name
    FROM GAMES
    INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
    INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company
    """


def generate_select_query():
    """
    Generates a SELECT command with attributes involved in the query.

    Returns:
        str: SELECT command with attributes.
    """
    return generate_inner_join_query()


def print_query(query):
    """
    Prints the generated SQL query.

    Args:
        query (str): The SQL query to print.
    """
    print("Generated SQL command:")
    print(query)


def main():
    query = generate_select_query()
    print_query(query)


if __name__ == "__main__":
    main()
