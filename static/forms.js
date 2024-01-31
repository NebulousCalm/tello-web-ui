// NOTE FOR ZACH: TOF SENSOR FOR SOME COOL RECOGNITION THINGS

const addInput = () =>{
    let input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('class', 'planInput')
    input.setAttribute('name', 'item')

    let select = document.createElement('select');
    select.setAttribute('name', 'select');
    select.setAttribute('class', 'selectClass')

    let forward = document.createElement("option");
    forward.text = "Forward";
    forward.value = "forward";

    let backward = document.createElement("option");
    backward.text = "Backward"
    backward.value = "backward"

    let left = document.createElement("option");
    left.text = "Left"
    left.value = "left"

    let right = document.createElement("option");
    right.text = "Right"
    right.value = "right"

    let up = document.createElement("option");
    up.text = "Up"
    up.value = "up"

    let down = document.createElement("option");
    down.text = "Down"
    down.value = "down"

    let anticlockwise = document.createElement("option");
    anticlockwise.text = "Anti-clockwise"
    anticlockwise.value = "anticlockwise"

    let clockwise = document.createElement("option");
    clockwise.text = "Clockwise";
    clockwise.value = "clockwise";

    let flipforward = document.createElement("option");
    flipforward.text = "Flip Forward";
    flipforward.value = "flipforward";

    let flipbackward = document.createElement("option");
    flipbackward.text = "Flip Backward"
    flipbackward.value = "flipbackward"

    let flipleft = document.createElement("option");
    flipleft.text = "Flip Left"
    flipleft.value = "flipleft"

    let flipright = document.createElement("option");
    flipright.text = "Flip Right"
    flipright.value = "flipright"

    let parentForm = document.getElementById('parentForm');
    parentForm.append(input, parentForm.lastChild);
    let appendSection = document.getElementsByClassName('planInput');
    parentForm.append(select, parentForm.lastChild);

    select.append(forward, backward, left, right, up, down, flipbackward, flipforward, flipright, flipleft, anticlockwise, clockwise);
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
