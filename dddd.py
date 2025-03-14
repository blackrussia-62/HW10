import sqlite3

conn = sqlite3.connect('DaTe.sl3')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE temperature (
        date DATE,
        time TIME,
        value REAL
    )
''')

data = [
    ('14.03.2025', '10:52:42', 23.5),
    ('15.03.2025', '10:52:42', 24.0),
    ('16.03.2025', '10:52:42', 22.8)
]

cursor.executemany('INSERT INTO temperature (date, time, value) VALUES (?, ?, ?)', data)

conn.commit()

cursor.execute('SELECT * FROM temperature')
print("tempertura:")
for row in cursor.fetchall():
    print(f"tarix: {row[0]}, vaxt: {row[1]}, ttteeemmmppp: {row[2]}°C")
    
cursor.execute('DROP TABLE temperature')

conn.close()
