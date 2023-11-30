from espn_api.football import League
from datetime import datetime
import configparser
import json
import os

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
    
def serialize_activity(activity):
    return {
        "team": activity.actions[0][0].team_name,
        "action": activity.actions[0][1],
        "player": {
            "name": activity.actions[0][2].name,
            "position": activity.actions[0][2].position,
            # Include other player attributes as needed
        }
    }


def main():
    # Read authentication credentials
    l_id, S2_key, swid_val = read_auth()

    # Set the current date to get the season year
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year

    # Get the league year based on the current date
    league_year = getLeagueYear(current_month, current_year)

    # Create the League object with the obtained credentials and league year
    league = League(
        league_id=l_id,
        year=league_year,
        espn_s2=S2_key,
        swid=swid_val
    )

    # Now you can use the 'league' object for further processing
    # For example, print league details
    # print(f"League ID: {l_id}")
    # print(f"League Year: {league_year}")
    # print(f"Number of Teams: {len(league.teams)}")
    
    activity = league.recent_activity()
    activity_len = len(activity)
    json_activity = [serialize_activity(act) for act in activity]

    # activity_json = json.dumps(activity, indent=2)
    # print(f"Recent Activity: {activity_json}")
    # print(activity.type())
    file_path = "recent_activity.json"
    with open(file_path, "w") as file:
    # Convert the list of dictionaries to a JSON-formatted string and write it to the file
        json.dump(json_activity, file, indent=2)

    print(f"Activity has been written to '{file_path}'")

if __name__ == "__main__":
    main()
