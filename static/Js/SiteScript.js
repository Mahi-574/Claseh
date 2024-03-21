var myModal = document.getElementById('Modal-rezaro')
var myInput = document.getElementById('Modal-rezaro')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})

function mySearch() {
    var myId = document.getElementById("search").value;
    window.open("/Home/Search/" + myId);
}

