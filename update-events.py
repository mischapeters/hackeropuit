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

okevents = []

def eventdate(elem):
  return elem['StartDate']

# Ugly, we loop over events multiple times,
# but I couldn't get it working in 1 pass...

for event in events:
#  print(f"Parsing event: {event['Name']}" )
  sdate = datetime.strptime( event['StartDate'], "%Y-%m-%d" ).date()
  edate = datetime.strptime( event['EndDate'], "%Y-%m-%d" ).date()

  if edate < sdate:
    print(f"Disabled Event: {event['Name']}, end time before start time" )
    events.remove(event)
  elif today > edate:
    print(f"Passed Event: {event['Name']}, already passed" )
    events.remove(event)
  else:
    print(f"Future Event: {event['Name']}, added to list" )
    okevents.append(event)

okevents.sort(key=eventdate)
output = open("events.json", "w", encoding='utf8' )
json.dump( okevents, output, indent=4, default=str, ensure_ascii=False, encoding="utf-8")

