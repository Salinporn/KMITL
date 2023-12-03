document.writeln("<style>");
document.writeln("table {");
document.writeln("    border: 1px solid black;");
document.writeln("    border-collapse: collapse;");
document.writeln("}");
document.writeln("td {");
document.writeln("    padding: 5px 15px 5px 15px;");
document.writeln("    max-width: 20px;");
document.writeln("    text-align: center;");
document.writeln("}");
document.writeln("button {");
document.writeln("    width: 30px;");
document.writeln("}");
document.writeln("</style>");

document.writeln("<table id='calendarTable' border></table>");

// Initialize the current month and year
var currentMonth = 1; // January
var total_days_of_year = 365;

// Function to display the calendar for a given month
function showMonthOf2023(month, total_days_of_year) {
    // Check if the year is a leap year
    if (total_days_of_year == 366) {
        var daysOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    } else if (total_days_of_year == 365) {
        var daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    }

    // Calculate the first day of the month
    var firstDay = new Date(2023, month - 1, 1).getDay();

    // Adjust the starting day to ensure January starts with Monday (1)
    firstDay = (firstDay === 0) ? 7 : firstDay;
    
    var totalDays = daysOfMonth[month - 1];
    
    var table = document.getElementById("calendarTable");
    
    // Clear the existing table rows + update month
    table.innerHTML = '<tr><td><button onclick="previousMonth()">&lt;</button></td><td colspan="5">' + month + '/2023</td><td><button onclick="nextMonth()">&gt;</button></td></tr>'
    table.innerHTML += '<tr><td>Mon</td><td>Tue</td><td>Wed</td><td>Thu</td><td>Fri</td><td>Sat</td><td>Sun</td></tr>'
    
    // Fill in the calendar table
    var date = 1;
    for (var i = 0; i < 6; i++) {
        var row = document.createElement("tr");
        for (var j = 1; j <= 7; j++) { // Start from Monday (1) to Sunday (7)
            if ((i === 0 && j < firstDay)) {
                // Empty cells before the 1st day
                var cell = document.createElement("td");
                cell.textContent = "";
                row.appendChild(cell);
            } else if ( date > totalDays ) {
                if (j === 1) {
                    // Empty cells after the last day
                    break;
                }
                var cell = document.createElement("td");
                cell.textContent = "";
                row.appendChild(cell);
            } else {
                // Fill in the days of the month
                var cell = document.createElement("td");
                cell.textContent = date;
                row.appendChild(cell);
                date++;
            }
        }
        table.appendChild(row);
    }
}

// Function to go to the previous month
function previousMonth() {
    if (currentMonth > 1) {
        currentMonth--;
    }
    showMonthOf2023(currentMonth, total_days_of_year);
}

// Function to go to the next month
function nextMonth() {
    if (currentMonth < 12) {
        currentMonth++;
    }
    showMonthOf2023(currentMonth, total_days_of_year);
}

// Display the calendar for January
showMonthOf2023(currentMonth, total_days_of_year);
