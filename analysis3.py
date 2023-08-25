import sqlite3
import json
import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect('pyadina-24-08-23.db')
cursor = conn.execute("SELECT * FROM orders where date = '19.08.2023'")
rows = cursor.fetchall()

print(rows)

x = []
y = []

x1 = []
x2 = []

for row in rows:
    jsn = json.loads(row[5])
    print(jsn)
    x.append(jsn['0'])
    x1.append(jsn['1'])
    x2.append(jsn['2'])

    y.append(row[6])

# plot
fig, ax = plt.subplots()

df = pd.DataFrame({
    'period': y,
    'de_eint': x,
    'de_scharf': x1,
    'de_vegi': x2
})

plt.plot(df['de_eint'], label='De Eint', color='blue', linewidth=.5)
plt.plot(df['de_scharf'], label='De Scharf', color='red', linewidth=.5)
plt.plot(df['de_vegi'], label='De Vegi', color='green', linewidth=.5)

plt.legend()
plt.title('Piadina Sales per Type per Order', fontsize=16)


plt.show()
