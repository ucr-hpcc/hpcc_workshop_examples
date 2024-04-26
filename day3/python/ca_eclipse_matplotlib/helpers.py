import csv

# Opens a CSV file from CAISO and returns just the solar power readings row,
# converted to int.
def get_solar_row(csv_file):
    solar_row = None          # Initialize with value we can use to check for errors
    with open(csv_file, "r") as f:
        cr = csv.reader(f)
        for row in cr:
            if row[0] == "Solar": # Check for line with solar data
                tmp = row[1:]     # First item is "Solar", we don't want it
                solar_row = [ int(n) for n in tmp ] # Convert each string to int
                break             # Once we find what we're looking for, stop looping
    return solar_row

# Simple lookup dict for converting numeric months to English abbreviations
month_lookup = {"01" : "Jan",
                "02" : "Feb",
                "03" : "Mar",
                "04" : "Apr",
                "05" : "May",
                "06" : "Jun",
                "07" : "Jul",
                "08" : "Aug",
                "09" : "Sep",
                "10" : "Oct",
                "11" : "Nov",
                "12" : "Dec"}

# Interprets YYYYMMDD. Converts MM to English abbreviation
def parse_date_from_ymd(ymd):
    year = ymd[0:4]
    month = month_lookup[ymd[4:6]]
    day = ymd[6:8]

    return {"year": year, "month": month, "day": day}

# Gets the numeric date from filename by splitting at certain characters
def get_ymd_from_filename(filename):
    remove_ext = filename.rsplit('.', maxsplit=1)[0]
    remove_prefix = remove_ext.rsplit('-', maxsplit=1)[1]

    return remove_prefix
