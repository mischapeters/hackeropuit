#!/usr/bin/python3

import sys
import yaml
import glob
import simplejson as json
import yaml
from datetime import datetime, date

today=date.today()

with open(r'/dev/stdin') as infile:
    events = yaml.load( infile, Loader=yaml.BaseLoader )

output = open("events.json", "w", encoding='utf8' )

okevents = {}

def eventdate(elem):
  return elem['StartDate']

# Ugly, we loop over events multiple times,
# but I couldn't get it working in 1 pass...

for event in events:
  sdate = datetime.strptime( event['StartDate'], "%Y-%m-%d" ).date()
  edate = datetime.strptime( event['EndDate'], "%Y-%m-%d" ).date()

  if edate < sdate:
    print(f"Event {event['Name']}, end time before start time\n" )
    events.remove(event)
  elif today > edate:
    print(f"Skipping event {event['Name']}, already passed\n" )
    events.remove(event)
  else:
    print(f"Event {event['Name']}, looks ok.\n" )

events.sort(key=eventdate);
json.dump( events, output, indent=4, default=str, ensure_ascii=False, encoding="utf-8")

