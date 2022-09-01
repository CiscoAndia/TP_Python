""" Archivo principal del programa"""

import menu
import DB

DB.crear_db()

def main():
    menu.loop()

if __name__ == "__main__":
    main()
    
