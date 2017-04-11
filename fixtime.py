from urllib import request
from datetime import datetime
from subprocess import call
import pytz

def main():
	req_dt = request.urlopen("http://just-the-time.appspot.com").read().decode("utf-8").strip()
	local = pytz.timezone("Brazil/East")
	naive = datetime.strptime(req_dt, "%Y-%m-%d %H:%M:%S")
	utc_dt = pytz.utc.localize(naive)
	local_dt = utc_dt.astimezone(local)
	
	local_date = local_dt.strftime("%d/%m/%Y")
	local_time = local_dt.strftime("%H:%M:%S")
	
	#local_date = local_dt.strftime("%x")
	#local_time = local_dt.strftime("%X")
	
	print("\nDate set to: " + local_date + "\nTime set to: " + local_time)
	
	call("date " + local_date, shell=True)
	call("time " + local_time, shell=True)
	
	
	
	return

if (__name__ == "__main__"):
	main()
