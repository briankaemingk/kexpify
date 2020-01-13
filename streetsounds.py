import kexp
import pytz, datetime
from datetime import timedelta
###
### A script that is run every Friday night to pull down the latest Street Sounds show from KEXP
###
if __name__ == '__main__':

    #Get the date this is being run
    utc_datetime = datetime.datetime.utcnow() - timedelta(days=1)

    #Show starts at 5 UTC time
    start_date = utc_datetime.strftime("%Y-%m-%dT05:00:00Z")

    #Show ends at 8 UTC time
    end_date = (datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ")

    name = "Street Sounds on KEXP"
    description = "Streetsounds is Seattle's longest running mixshow."
    args = [name,start_date, end_date, description]
    kexp.main(args)

