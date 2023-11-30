from espn_api.football import League
from datetime import datetime
import configparser


# ESPN Fantasy auth, abstract before pushing
def read_auth(file_path='secrets.ini'):
    config = configparser.RawConfigParser()
    config.read(file_path)

    l_id = config.get("credentials", "L_ID")
    S2_key = config.get("credentials", "S2_KEY")
    swid_val = config.get("credentials", "SWID_VAL")

    return l_id, S2_key, swid_val

def getLeagueYear(month, year):
    if 9 <= month <= 12:
        return year
    else:
        return year - 1


# Read authentication credentials
l_id, S2_key, swid_val = read_auth()

# Set the current date to get the season year
current_date = datetime.now()
current_month = current_date.month
current_year = current_date.year

# Get the league year based on the current date
league_year = getLeagueYear(current_month, current_year)


print(f"League ID: {l_id}")
print(f"League Year: {league_year}")
print(f"SWID: {swid_val}")