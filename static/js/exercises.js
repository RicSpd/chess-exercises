// Function that show a card if a certain checkbox is checked.
function showSelectPieces() {
    // Get the elements
    var checkbox = document.getElementById("randomized");
    var card = document.getElementById("select-pieces-card");
  
    // If the checkbox is checked, display the output card
    if (checkbox.checked == true){
        card.style.display = "block";
    } else {
        card.style.display = "none";
    }
}



$('.copyButton').tooltip({
    trigger: 'click',
    placement: 'bottom'
  });
  
  function setTooltip(btn, message) {
    btn.tooltip('hide')
      .attr('data-original-title', message)
      .tooltip('show');
  }
  
  function hideTooltip(btn) {
    setTimeout(function() {
      btn.tooltip('hide');
    }, 1000);
  }
  
  var clipboard = new Clipboard('.copyButton');
  
  clipboard.on('success', function(e) {
      var btn = $(e.trigger);
    setTooltip(btn, 'Copied!');
    hideTooltip(btn);
  });



function copyToClipboard() {
    // Get the element
    var copyText = document.getElementById("fen-string");

    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);

    // Alert the copied text
    alert("Copied the text: " + copyText.value);
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
