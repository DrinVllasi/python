from optparse import Option
from typing import List, Optional
import sqlite3

from Module24.join_example import cursor
from lesson2.lesson2 import items
from models import Item
from database import get_db_connection

def create_item(item: Item) -> Item:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items(name, description) VALUES (?,?)", (item.name, item.description))
    conn.commit()
    item.id = cursor.lastrowid
    conn.close()
    return item

def get_items() -> List[Item]:
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return [Item(**dict(item)for item in items)]

def get_item(item_id: int) ->Option[Item]:
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id=?",(item_id,)).fetchall()
    conn.close()
    if item is None:
        return None
    else:
        return Item(**dict(item))

def update_item(item_id: int, item: Item) -> Optional[Item]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE items set name = ?, description = ? WHERE id = ?", (item.name, item.description. item_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    if updated = 0:
        return None
    item.id = item_id
    return item

def delete_item(item_id:int) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted >0