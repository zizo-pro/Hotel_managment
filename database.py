import sqlite3
from random import choice , random

db = sqlite3.connect("hotel.db")
cr = db.cursor()
room_typ = ["Single","Double","Triple","Quad","Suite"]
room_view = ["Sea","Pool","Street"]


num = 1
# while num < 401:
    # typ = choice(room_typ)
    # view = choice(room_view)

    # if typ == "Single" and view == "Sea":
    #     price = 500

    # elif typ == "Single" and view == "Pool":
    #     price = 400

    # elif typ == "Single" and view == "Street":
    #     price = 325

    # elif typ == "Double" and view == "Pool":
    #     price = 550

    # elif typ == "Double" and view == "Sea":
    #     price = 700

    # elif typ == "Double" and view == "Street":
    #     price = 475

    # elif typ == "Triple" and view == "Sea":
    #     price = 900

    # elif typ == "Triple" and view == "Pool":
    #     price = 750

    # elif typ == "Triple" and view == "Street":
    #     price = 600

    # elif typ == "Quad" and view == "Sea":
    #     price = 1150

    # elif typ == "Quad" and view == "Pool":
    #     price = 900

    # elif typ == "Quad" and view == "Street":
    #     price = 750

    # elif typ == "Suite" and view == "Sea":
    #     price = 1750

    # elif typ == "Suite" and view == "Pool":
    #     price = 1500

    # elif typ == "Suite" and view == "Street":
    #     price = 1250
    # num += 1
cr.execute("update hotel_rooms set occupied = 'False'")

db.commit()
db.close()