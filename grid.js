function getJSON(url) {
        var resp ;
        var xmlHttp ;

        resp  = '' ;
        xmlHttp = new XMLHttpRequest();

        if(xmlHttp != null)
        {
            xmlHttp.open( "GET", url, false );
            xmlHttp.send( null );
            resp = xmlHttp.responseText;
        }

        return resp ;
}

var jsondata = getJSON('https://hackeropuit.nl/events.json');
var columns = ["Name", "Location", "StartDate", "EndDate", "URL", "Comment"]

// (B) PARSE JSON INTO OBJECT
var parsed = JSON.parse(jsondata);
console.table(parsed);

// (C) TABLE HEADER
var theWrap = document.getElementById("tableWrap");
var theCell = null;
for (let key in columns ) {
  theCell = document.createElement("div");
  theCell.innerHTML = columns[key];
  theCell.classList.add("cell");
  theCell.classList.add("head");
  theWrap.appendChild(theCell);
}

// (D) TABLE CELLS
var theEvent = null;
var altRow = false;
for (let key in parsed) {
  theEvent = parsed[key];
  for (let i in theEvent) {
    theCell = document.createElement("div");
    theCell.innerHTML = theEvent[i];
    theCell.classList.add("cell");
    if (altRow) { 
      theCell.classList.add("alt"); 
    }
    theWrap.appendChild(theCell);
  }
  altRow = !altRow;
}
