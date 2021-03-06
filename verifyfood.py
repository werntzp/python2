"""
Verify each animal eats at least one food
"""

import mysql.connector
from database import login_info

if __name__ =="__main__":

    db = mysql.connector.Connect(**login_info)
    cursor = db.cursor()

    # query for a summary report
    cursor.execute("select count(*) from animal where id not in (select distinct anid from food)")
    count = cursor.fetchone()[0]
    if count == 0:
        print("All animals have food...\n")
    else:
        print("At least one animal has no food!\n")

    # get all ids and names of animals
    print("Details:\n===============")
    cursor.execute("select id, name from animal")
    data = cursor.fetchall()
    for row in data:    
        # use the id to see if that animal eats food
        cursor.execute("select count(*) from food where anid=" + str(row[0]))
        count = cursor.fetchone()[0]
        print(row[1], "eats",count,"food(s)")
            
    print("===============")

 
