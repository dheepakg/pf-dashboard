from pyxirr import xirr

from datetime import date


dates = [
    date(2022, 6, 3),
    date(2022, 6, 17),
    date(2022, 8, 2),
    date(2022, 9, 2),
    date(2022, 9, 21),
    date(2022, 10, 4),
    date(2022, 11, 2),
    date(2022, 12, 2),
    date(2022, 12, 23),
]

values = [-5000, -10000, -5000, -5000, -5000, -5000, -5000, -5000, 46482]

roe = xirr(dates, values)

print(str(round(roe * 100, 2)) + "%")
