function showSelectPieces() {
    // Get the checkbox
    var checkbox = document.getElementById("randomized");
    // Get the card
    var card = document.getElementById("select-pieces-card");
  
    // If the checkbox is checked, display the output card
    if (checkbox.checked == true){
        card.style.display = "block";
    } else {
        card.style.display = "none";
    }
  }