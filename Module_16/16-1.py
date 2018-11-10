import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    datetimes, highs, lows = [], [], []
    for row in reader:
        try:
            current_time = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print(current_time, "missing date")
        else:
            datetimes.append(current_time)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(datetimes, highs, c="red", linewidth=0.5)
plt.plot(datetimes,lows, c="blue", linewidth=0.5)
plt.fill_between(datetimes, highs, lows, facecolor="yellow",
                 alpha=0.1)

title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()
