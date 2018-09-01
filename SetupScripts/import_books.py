import database_scripts as dbs
import csv

def populateBooks(filepath):
    file = open(filepath)
    reader = csv.reader(file)
    headers = next(reader,None)
    db = dbs.get_database_connection()
    for isbn,title,author,year in reader:
        print(f"{isbn} {title} {author} {year}")
        if db.execute("SELECT * FROM books WHERE isbn = :isbn",{"isbn":isbn}).rowcount == 0:
            db.execute("INSERT INTO books(isbn, title,author,year) VALUES (:isbn,:title,:author,:year)",{"isbn":isbn,"title":title,"author":author,"year":int(year)})
            print(f"{isbn} {title} {author} {year} Added to books.")
        else:
            print(f"{isbn} {title} {author} {year} already exists in the database.")
    db.commit()
    print("Changes Commited.")

populateBooks("books.csv")
