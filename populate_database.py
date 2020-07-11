#!/usr/bin/python

import psycopg2


def populate():
    """ populate tables in the PostgreSQL database"""
    conn = None
    try:
        conn = psycopg2.connect(dbname="varejo", user="docker", password="docker", host='127.0.0.1', port='5431')
        cur = conn.cursor()
        cur.execute("truncate users;")
        with open('data/users.csv', 'r') as f:
            next(f)  # Skip the header row.
            cur.copy_from(f, 'users', sep=',')

        conn.commit()
        cur.execute("SELECT setval('users_id_seq', coalesce(max(id)+1,1), false) FROM users;")
        conn.commit()
        cur.execute("truncate products;")
        with open('data/products.csv', 'r') as f:
            next(f)
            cur.copy_from(f, 'products', sep=',')

        conn.commit()
        cur.execute("SELECT setval('products_id_seq', coalesce(max(id)+1,1), false) FROM products;")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    populate()
