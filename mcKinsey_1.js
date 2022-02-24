
// Financial Services Lab - McKinsey – Front-End 
let itemCount = 0;
const input = document.getElementById("input");
const list = document.getElementById("list");
const button = document.getElementById("button");
button.addEventListener("click", () => {
    const inputValue = input.value;
    if (/^[\s]*$/.test(inputValue)) {
        document.getElementById("alert").style = "display:block"
        return;
    }
    else {
        document.getElementById("alert").style = "display:None"
    }

    const newItem = document.createElement("li");
    newItem.append(inputValue);

    ++itemCount;
    if (itemCount % 3 === 0) {
        newItem.style = "color:red;";
    } else {
        newItem.style = "color:black;";
    }

    list.append(newItem);
    input.value = "";
});

