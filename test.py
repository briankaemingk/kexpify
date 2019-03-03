import kexp
import pytz, datetime
from datetime import timedelta
###
### An example script that is run every Wednesday night to pull down the latest Roadhouse show from KEXP
###
if __name__ == '__main__':

    #Get the date this is being run
    utc_datetime = datetime.datetime.utcnow()

    #Roadhouse starts at 2 UTC time
    start_date = utc_datetime.strftime("%Y-%m-%dT02:00:00Z")

    #Roudhouse ends at 5 UTC time
    end_date = (datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ")

    name = "Test Playlist"
    description = "A description for this playlist"
    args = [name,start_date, end_date, description]
    kexp.main(args)

