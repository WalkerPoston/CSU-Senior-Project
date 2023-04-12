import serial
import time
import string
import pynmea2
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException

pnChannel = "raspi-tracker"

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-aeb29709-0d90-4695-8bfd-e6e7f5340b9b"
pnconfig.publish_key = "pub-c-6db0a33f-8510-4efa-a066-3feb81e94802"
pnconfig.user_id = "does-not-matter"
pnconfig.ssl = False

pubnub = PubNub(pnconfig)
pubnub.subscribe().channels(pnChannel).execute()

while True:
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata=ser.readline().decode('unicode_escape')

	if newdata[0:6] == "$GPRMC":
		newmsg=pynmea2.parse(newdata)
		lat=newmsg.latitude
		lng=newmsg.longitude
		try:
			envelope = pubnub.publish().channel(pnChannel).message({
				'lat':lat,
				'lng':lng
			}).sync()
			print("publish timetoken: %d" % envelope.result.timetoken)
		except PubNubException as e:
			handle_exception(e)

		#gps = "lat= " + str(lat) + " lng= " + str(lng)
		#print(gps)