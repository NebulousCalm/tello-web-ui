// NOTE FOR ZACH: TOF SENSOR FOR SOME COOL RECOGNITION THINGS

const addInput = () =>{
    let input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('class', 'planInput')
    input.setAttribute('name', 'item')

    let select = document.createElement('select');
    select.setAttribute('name', 'select');
    select.setAttribute('class', 'selectClass')

    let option = document.createElement("option");
    option.text = "Forward";
    option.value = "Forward";

    let option2 = document.createElement("option");
    option2.text = "Backward"
    option2.value = "Backward"

    let parentForm = document.getElementById('parentForm');
    parentForm.append(input, parentForm.lastChild);
    let appendSection = document.getElementsByClassName('planInput');
    parentForm.append(select, parentForm.lastChild);

    select.append(option, option2);
}

document.getElementById('add-input').addEventListener('click', addInput)

const inputCheck = (i) =>{
    let getInput = document.getElementsByClassName('planInput')[i];
    getInput.addEventListener('focusout', function(){
       if(getInput.value < 20){
           this.style.backgroundColor = "#ff0000";
       } else if (getInput.value > 500){
           this.style.backgroundColor = "#ff0000";
       }
    });
}

const elements = document.getElementsByClassName("planInput");
for (let i = 0, len = elements.length; i < len; i++) {
    inputCheck(i)
}