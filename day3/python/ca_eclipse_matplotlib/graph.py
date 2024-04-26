#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

from glob import glob

import helpers as h

# CSV file has time in HH:SS notation. We need a floating-point time between [0,24)
# Furthermore, CSV file is in 5 minute intervals, or 12 samples per hour.
x = np.linspace(0, 24, 24 * 12, endpoint=False)

fig, ax = plt.subplots()

ax.set_title("Solar power generation in CA on April Mondays")
ax.set_xlabel("Time of day (24h)")
ax.set_ylabel("Solar power supply (MW)")

# Assume any *.csv file in the same directory is CAISO solar data.
# Sort for better legend readability
csv_list = glob("*.csv")
csv_list.sort()

# Process each CSV we find
for c in csv_list:
    solar_row = h.get_solar_row(c)
    date = h.parse_date_from_ymd(h.get_ymd_from_filename(c))
    us_date = f"{date['month']} {date['day']}, {date['year']}"

    y = np.array(solar_row)
    ax.plot(x, y, label=us_date)

# Finish the graph and show the result
ax.legend()
plt.show()
