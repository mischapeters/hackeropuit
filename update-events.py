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
    print( "Event ends before it starts\n" )
    events.remove(event)

for event in events:
  edate = datetime.strptime( event['EndDate'], "%Y-%m-%d" ).date()
  if today > edate:
    print( "Skipping event, already passed\n" )
    events.remove(event)

events.sort(key=eventdate);
#json.dump( events, output, indent=4, default=str, ensure_ascii=False )
json.dump( events, output, indent=4, default=str, ensure_ascii=False, encoding="utf-8")

