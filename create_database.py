#!/usr/bin/python

import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            birthdate DATE NOT NULL
        )
        """,
        """ CREATE TABLE products (
                id SERIAL PRIMARY KEY,
                title VARCHAR(150) NOT NULL,
                description VARCHAR(255),
                price NUMERIC (5, 2) NOT NULL,
                base_discount_percent FLOAT NOT NULL DEFAULT 0
                )
        """,
        )
    conn = None
    try:
        conn = psycopg2.connect(dbname="varejo", user="docker", password="docker", host='127.0.0.1', port='5431')
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
