// Function that show a card if a certain checkbox is checked.
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



// function postData(url, payLoad) {
//     var jsonData = JSON.stringify(payLoad);
//     return $.ajax({
//         type: "POST",
//         crossDomain: true,
//         dataType: "json",
//         contentType: "application/json",
//         data: jsonData,
//         url: url
//     });
// }



// jQuery(window).on("load", function() {

//     document.getElementById("go").addEventListener("click", function() {

//         randomized = document.getElementById("randomized").checked
//         extra_populated = document.getElementById("extra-populated").checked
//         equal_material = document.getElementById("equal-material").checked

//         white_pawns = document.getElementById("white-pawns").options.value

//         payload = {
//             "randomized": randomized,
//             "extra_populated": extra_populated,
//             "equal_material": equal_material,
//             "select_pieces": {
//                 "white_pawns": white_pawns,
//             }
//         }

//     });

// });
