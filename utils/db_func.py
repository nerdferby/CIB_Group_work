"""
database functionality common to both flask and tkinter
"""
import datetime

import mysql.connector

import utils.db_init


def insert_vehicle(username, is_electric, vehicle_reg, vehicle_make):
    creds = utils.db_init.load_credentials()

    sql_insert_query = """ 
    INSERT INTO `vehicles`
    (`username`, `electric_vehicle`, `vehicle_registration`, `vehicle_make`) VALUES (%s,%s,%s,%s)
"""
    try:
        connection = utils.db_init.connect(creds['user'], creds['database'], creds['password'], creds['host'])
        cursor = connection.cursor()
        cursor.execute(sql_insert_query, (username, is_electric, vehicle_reg, vehicle_make))
        print("Row inserted into vehicle table")
        return True

    except mysql.connector.Error as e:
        print("Failed to insert", e)
        return False

    finally:
        return False


def insert_booking(username, booking_date, vehicle_reg):
    creds = utils.db_init.load_credentials()
    sql_insert_query = """
    INSERT INTO `bookings`
    (`username`, `booking_date`, `vehicle_registration`) VALUES (%s,%s,%s)
    """
    try:
        connection = utils.db_init.connect(creds['user'], creds['database'], creds['password'], creds['host'])
        cursor = connection.cursor()
        cursor.execute(sql_insert_query, (username, booking_date, vehicle_reg))
        print("Row inserted into booking table")
        return True

    except mysql.connector.Error as e:
        print("Failed to insert", e)
        return False

    finally:
        return False


def give_user_badge(username, badge_colour):
    creds = utils.db_init.load_credentials()
    sql_insert_query = """
    UPDATE users
    SET badge = %s
    WHERE username = %s
    """
    try:
        connection = utils.db_init.connect(creds['user'], creds['database'], creds['password'], creds['host'])
        cursor = connection.cursor()
        cursor.execute(sql_insert_query, (username, badge_colour))
        print("Print badge colour for "+username+" set to "+badge_colour)
        return True

    except mysql.connector.Error as e:
        print("Failed to update", e)
        return False

    finally:
        return False


if __name__ == "__main__":
    give_user_badge("jacob.smith@gmail.com", "RED")
