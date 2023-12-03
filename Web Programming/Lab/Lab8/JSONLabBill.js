function toJSON(){
    var table = document.getElementById('originalTable');
    var textarea = document.getElementById('displayTextarea');

    var tableData = [];
  
    for (var i = 1; i < table.rows.length - 1; i++) {
      var row = table.rows[i];
      var rowData = {};
  
      for (var j = 0; j < row.cells.length; j++) {
  
        var headerCell = table.rows[0].cells[j];
        rowData[headerCell.textContent] = row.cells[j].textContent;
      }

      tableData.push(rowData);
    }
  
    var jsonData = JSON.stringify(tableData, null, 2);
  
    textarea.value = jsonData;

}

function convert() {
    var textarea = document.getElementById('displayTextarea');
    var table = document.getElementById('newTable');
    var jsonData = textarea.value;
    var tableData = JSON.parse(jsonData);

    table.innerHTML = "";
    
    //header
    var header = Object.keys(tableData[0]);
    var headerRow = table.insertRow(0);
    for (var i = 0; i < header.length; i++) {
        var headerCell = headerRow.insertCell(i);
        headerCell.innerHTML = header[i];
    }

    //body
    for (var i = 0; i < tableData.length; i++) {
        var row = table.insertRow(i + 1);
        for (var j = 0; j < header.length; j++) {
            var cell = row.insertCell(j);
            cell.innerHTML = tableData[i][header[j]];
        }
    }

    //footer
    var footerRow = table.insertRow(table.rows.length);
    var footerCell = footerRow.insertCell(0);
    footerCell.colSpan = 4;
    footerCell.innerHTML = "Total";
    var total = 0;
    for (var i = 0; i < tableData.length; i++) {
        total += parseInt(tableData[i]["Amount"]);
    }
    var footerCell = footerRow.insertCell(1);
    footerCell.innerHTML = total;
}

window.onload = toJSON;
