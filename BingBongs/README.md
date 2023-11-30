# Usage

## Getting ESPN Fantasy Credentials

### Creds needed

* SWID - stored in cookies for espn fantasy
* S2_ID - stored in cookies for espn fantasy
* League_ID - in the url of the espn fantasy league web page

## Using a Secrets file

*I have my secrets file locally and in the .gitignore*
* create a file named `secrets.ini` in the same dir as the script using it
*  Example:

[credentials]
L_ID  = ########
SWID_VAL  = '{<VALUE>}'
S2_KEY = '<KEY>'


## Current Status

Right now it writes a json file with all recent activity data in the BingBongs dir

## Future Plans

- expand functionality to facilitate add/drop charges for next year



