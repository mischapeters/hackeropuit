#!/usr/bin/python3

import sys
import yaml
import glob
import json
from yamlreader import yaml_load
from datetime import datetime, date

today=date.today()

events = yaml_load("events/*.yaml")
output = open("events.json", "w" )

okevents = {}

def eventdate(elem):
  return elem['StartDate']

# Ugly, we loop over events multiple times,
# but I couldn't get it working in 1 pass...

for event in events:
  if event['EndDate'] < event['StartDate']:
    print( "Event ends before it starts\n" )
    events.remove(event)

for event in events:
  if today > event['EndDate']:
    print( "Skipping event, already passed\n" )
    events.remove(event)

events.sort(key=eventdate);
json.dump( events, output, indent=4, default=str )
