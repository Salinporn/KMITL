document.writeln("<table border><tr><td colspan=7>August 2023</td></tr>")
document.writeln("<tr><td>Mon</td>")
document.writeln("<td>Tue</td>")
document.writeln("<td>Wed</td>")
document.writeln("<td>Thu</td>")
document.writeln("<td>Fri</td>")
document.writeln("<td>Sat</td>")
document.writeln("<td>Sun</td></tr>")

var day = 0;
for(var i = 0; i < 5; i++) {
    document.writeln("<tr>")
    for(var j = 0; j < 7; j++) {
        if(1 <= day && day <= 31) {
            document.writeln("<td>" + day + "</td>");
            
        } else {
            document.writeln("<td></td>");
        }
        day++;
    }
    document.writeln("</tr>");
}

document.writeln("</table>");