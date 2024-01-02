#!/usr/bin/python3

import sys
import glob
import ruamel.yaml as yaml
import simplejson as json
from datetime import datetime, date, timedelta
from icalendar import Calendar, Event

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
with open("events.json", "w", encoding='utf8' ) as output:
  json.dump( okevents, output, indent=4, default=str, ensure_ascii=False, encoding="utf-8")

cal = Calendar()
cal.add('prodid', '-//Hack er op uit//hackeropuit.nl//')
cal.add('version', '2.0')
baseicalevent = Event()
baseicalevent.add('transp', 'TRANSPARENT')
baseicalevent.add('dtstamp', datetime.now())

for source_event in events:
  event = baseicalevent.copy()
  event.add('uid', f"/{source_event['Name']}/{source_event['StartDate']}")
  event.add('summary', source_event['Name'])
  event.add('dtstart', source_event['StartDate'])
  event.add('dtend', source_event['EndDate'] + timedelta(days=1))
  event.add('location', source_event['Location'])
  event.add('description', source_event['Comment'])
  event.add('url', source_event['URL'])

  cal.add_component(event)

with open('events.ics', 'wb') as f:
  f.write(cal.to_ical())
