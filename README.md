# database-prosjekt

Train database project using SQLite and Python.

### Run the project:
- Make sure to have sqlite3 and Python installed on your computer.

**Type the following in your terminal (make sure you are in the same directory as the project):**
```
pip install tabulate
sqlite3 innlevering.db
.read schema.sql
.exit
```

- You will now have a database file called "innlevering.db" whith empty tables created from the "schema.sql" file.

**Type the following in your terminal:**
```
python -u brukerhistorie_a_b_f.py
```

- This initializes the database with the necessary information for the user stories to work. Trains depart on the 3rd- and 4th of april 2023 in the program.
- For the best experience, run the user stories in alphabetical order.

**Commands for running the different user stories:**
```
python -u brukerhistorie_c.py
python -u brukerhistorie_d.py
python -u brukerhistorie_e.py
python -u brukerhistorie_g.py
python -u brukerhistorie_h.py
```
