HTMLElement.prototype.queryA = function(a) {return this.querySelectorAll(a)}
HTMLElement.prototype.query = function(a) {return this.querySelector(a)}


String.prototype.format = function() {
	var r = this;
	for (var i=0;i<arguments.length;i++) {
		var rstring = "{"+i.toString()+"}";
		r = r.replace(rstring,arguments[i]);
	}
	return r;
}
function collectTableData(){
    var myTableArray = [];

$("table.standard-table tr").each(function() {
    var arrayOfThisRow = [];
    var tableData = $(this).find('td');
    if (tableData.length > 0) {
        tableData.each(function() { arrayOfThisRow.push($(this).text()); });
        myTableArray.push(arrayOfThisRow);
    }
});

return myTableArray;
}


function generateDownload() {
	var filename = "AllData.json";
	var text = JSON.stringify(collectTableData());
	var blob = new Blob([text],{type:"text/plain"});
    var url = URL.createObjectURL(blob);
    
	
	var link = document.createElement("a");
	link.download = filename;
	link.href = url;
	link.target = "_blank";
	document.body.appendChild(link);
	link.click();
    link.remove();
}

generateDownload();