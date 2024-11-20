import gps
import time

session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

try:
    while True:
        report = session.next()

        #print("Raw GPS Report:")
        #print(report)

        # Check if the report contains position data (class 'TPV')
        if report['class'] == 'TPV':
            latitude = report.lat if hasattr(report, 'lat') else 'No Data'
            longitude = report.lon if hasattr(report, 'lon') else 'No Data'
            elevation = report.altMSL if hasattr(report, 'altMSL') else 'No Data'

            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Elevation: {elevation} meters")

        # Check if the report contains satellite data (class 'SKY')
        elif report['class'] == 'SKY':
            nSat = report.nSat if hasattr(report, 'nSat') else 'No Data'  # Number of locked satellites

            print(f"Number of locked satellites: {nSat}")
            satellites = report.satellites if hasattr(report, 'satellites') else 'No Data'


        print("===================================")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program interrupted")
except Exception as e:
    print(f"Error: {e}")
