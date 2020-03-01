# HackErOpUit

Een overzicht van hacker-events in en rond Nederland.

Patches welcome ;) (Zowel code als data)

## Contributing:

https://github.com/revspace/hackeropuit/


## Convert yaml to json
```python3 -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=4)' < events.yaml > events.json```

## Start local server for testing
```python3 -m http.server```
