import sqlite3


# Запитання 1. Інформація про скількох художників представлена у базі даних?

conn = sqlite3.connect('Artistc.db')
cursor = conn.cursor()

cursor.execute('''SELECT * FROM artists''')
data = cursor.fetchall()

print(len(data))



# Запитання 2. Скільки жінок (Female) у базі?

cursor.execute('''SELECT * FROM artists WHERE Gender == "Female"''')
dat = cursor.fetchall()
print(len(dat))

# Запитання 3. Скільки людей у базі даних народилися до 1900 року?

cursor.execute('''SELECT * FROM artists WHERE "Birth Year" < 1900''')
dat = cursor.fetchall()
print(len(dat))

# Запитання 4*. Як звати найстаршого художника?

cursor.execute('''SELECT * FROM artists WHERE "Birth Year" < 1900 ORDER BY "Birth Year"''')
dat = cursor.fetchall()
print(len(dat))

conn.commit()
conn.close()