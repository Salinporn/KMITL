const output = document.getElementById("result");
const table = document.getElementById("myTable");
const cells = table.getElementsByTagName("td");

let result = 0;
let operator = "";
let operand = "";
let operand2 = "";
let flag = 0;
let memory = 0;
let isMemorySet = false;

// Function to handle mouse events
function mouseEvent(event) {
    for (let i = 0; i < cells.length; i++) {
        cells[i].addEventListener("click", (event) => {
            if (cells[i].id == "c") {
                result = 0;
                operator = "";
                operand = "";
                operand2 = "";
                flag = 0;
                output.innerHTML = result;
            }
            else if (cells[i].id == "Backspace") {
                operand = output.innerHTML;
                if (operand.length == 1) {
                    output.innerHTML = "0";
                    operand = "";
                }
                else {
                    if (flag == 0) {
                        operand = operand.substring(0, operand.length - 1);
                        output.innerHTML = operand;
                    }
                    else {
                        operand2 = operand2.substring(0, operand2.length - 1);
                        output.innerHTML = operand2;
                    }
                }
            }
            else if (cells[i].id == "Enter") {
                if (operator == "+") {
                    result = parseInt(operand) + parseInt(operand2);
                    output.innerHTML = result;
                }
                else if (operator == "-") {
                    result = parseInt(operand) - parseInt(operand2);
                    output.innerHTML = result;
                }
                else if (operator == "*") {
                    result = parseInt(operand) * parseInt(operand2);
                    output.innerHTML = result;
                }
                else if (operator == "/") {
                    result = parseInt(operand) / parseInt(operand2);
                    output.innerHTML = result;
                }
                operand = result;
                operand2 = "";
                flag = 0;
            }
            else if (cells[i].id == "+" || cells[i].id == "-" || cells[i].id == "*" || cells[i].id == "/") {
                operator = cells[i].id;
                flag = 1;
            }
            else if (cells[i].id == "sin") {
                result = Math.sin(parseInt(operand));
                output.innerHTML = result;
                operand = result;
            }
            else if (cells[i].id == "cos") {
                result = Math.cos(parseInt(operand));
                output.innerHTML = result;
                operand = result;
            }
            else if (cells[i].id == "tan") {
                result = Math.tan(parseInt(operand));
                output.innerHTML = result;
                operand = result;
            }
            else if (cells[i].id == "pi") {
                operand = operand.substring(0, operand.length - 1);
                result = Math.PI * parseInt(operand);
                output.innerHTML = result;
            }
            else if (cells[i].id == "sqrt") {
                result = Math.sqrt(parseInt(operand));
                output.innerHTML = result;
                operand = result;
            }
            else if (cells[i].id == "square") {
                result = parseInt(operand) * parseInt(operand);
                output.innerHTML = result;
                operand = result;
            }
            else if (cells[i].id == "1/x") {
                result = 1 / parseInt(operand);
                output.innerHTML = result;
                operand = result;
            }
            else if (cells[i].id == "factorial") {
                result = 1;
                for (let j = 1; j <= parseInt(operand); j++) {
                    result *= j;
                }
                output.innerHTML = result;
                operand = result;
            }
            else if (cells[i].id == "mc") {
                memory = 0;
                isMemorySet = false;
            }
            else if (cells[i].id == "m+") {
                memory += parseFloat(output.innerHTML);
                isMemorySet = true;
            }
            else if (cells[i].id == "m-") {
                memory -= parseFloat(output.innerHTML);
                isMemorySet = true;
            }
            else if (cells[i].id == "mr") {
                if (isMemorySet) {
                    output.innerHTML = memory.toString();
                    operand = memory.toString();
                }
            }
            else {
                if (flag == 0) {
                    operand += cells[i].id;
                    output.innerHTML = operand;
                }
                else {
                    operand2 += cells[i].id;
                    output.innerHTML = operand2;
                }
            }
        });
    }
}

mouseEvent();

// Function to handle keyboard events
function keyBoardEvent(event) {
    const key = event.key;
    const id = key == "*" ? "*" : key == "/" ? "/" : key;

    if (id === "c") {
        result = 0;
        operator = "";
        operand = "";
        operand2 = "";
        flag = 0;
        output.innerHTML = result;
    } else if (id == "Backspace") {
        operand = output.innerHTML;
        if (operand.length == 1) {
            output.innerHTML = "0";
            operand = "";
        } else {
            if (flag == 0) {
                operand = operand.substring(0, operand.length - 1);
                output.innerHTML = operand;
            } else {
                operand2 = operand2.substring(0, operand2.length - 1);
                output.innerHTML = operand2;
            }
        }
    } else if (id == "Enter") {
        if (operator == "+") {
            result = parseInt(operand) + parseInt(operand2);
        } else if (operator == "-") {
            result = parseInt(operand) - parseInt(operand2);
        } else if (operator == "*") {
            result = parseInt(operand) * parseInt(operand2);
        } else if (operator == "/") {
            result = parseInt(operand) / parseInt(operand2);
        }
        operand = result;
        operand2 = "";
        flag = 0;
        if (flag == 0) {
            output.innerHTML = operand;
        } else {
            output.innerHTML = operand2;
        }
    } else if (id == "+" || id == "-" || id == "*" || id == "/") {
        operator = id;
        flag = 1;
    } else if (!isNaN(id)) {
        if (flag == 0) {
            operand += id;
            output.innerHTML = operand;
        } else {
            operand2 += id;
            output.innerHTML = operand2;
        }
    }
}

document.addEventListener("keydown", keyBoardEvent);
