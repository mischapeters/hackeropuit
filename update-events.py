#!/usr/bin/python3

import sys
import glob
import ruamel.yaml as yaml
import simplejson as json
from datetime import datetime, date

def eventdate(elem):
  return elem['StartDate']

today=date.today()
okevents = []

with open("/dev/stdin") as stream:
  try:
    events = yaml.safe_load(stream)
  except yaml.YAMLError as exc:
    print(exc)

#print(events)

for event in events:
  # print(f"Parsing event: {event['Name']}" )
  if ( event['EndDate'] >= event['StartDate'] and today <= event['EndDate'] ):
    okevents.append(event)
    #print(f"Future Event: {event['Name']}, added to list" )

okevents.sort(key=eventdate)
output = open("events.json", "w", encoding='utf8' )
json.dump( okevents, output, indent=4, default=str, ensure_ascii=False, encoding="utf-8")
