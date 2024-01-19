const elements = document.getElementsByClassName("hidden");
for (let i = 0, len = elements.length; i < len; i++) {
    document.getElementsByClassName('hidden')[i].addEventListener('click', function(){
        window.location.href = 'http://localhost:5000/run?plan=' + document.getElementsByClassName('hidden')[i].innerHTML;
    })
}