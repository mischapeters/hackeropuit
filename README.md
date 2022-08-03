# HackErOpUit

Een overzicht van hacker-events in en rond Nederland.

Patches welcome ;) (Zowel code als data)

## Contributing:

https://github.com/revspace/hackeropuit/


## Convert yaml to json
```python3 -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=4)' < events.yaml > events.json```

## Start local server for testing
```python3 -m http.server```

## Example event data:

- Name: Event Name/Title
  Location: City, Country
  StartDate: 2022-07-22
  EndDate: 2022-07-26
  Comment: Something optional
  URL: https://hackeropuit.nl

If no date is known yet, just put in an approximate date, but have the end-date be befor
ethe start-date, then the entry will be ignored.
