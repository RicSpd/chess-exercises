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



function postData(url, payLoad) {
    var jsonData = JSON.stringify(payLoad);
    return $.ajax({
        type: "POST",
        crossDomain: true,
        dataType: "json",
        contentType: "application/json",
        data: jsonData,
        url: url
    });
}



jQuery(window).on("load", function() {

    document.getElementById("go").addEventListener("click", function() {

        randomized = document.getElementById("randomized").checked
        extra_populated = document.getElementById("extra-populated").checked
        equal_material = document.getElementById("equal-material").checked

        white_pawns = document.getElementById("white-pawns").options.value

        payload = {
            "randomized": randomized,
            "extra_populated": extra_populated,
            "equal_material": equal_material,
            "select_pieces": {
                "white_pawns": white_pawns,
            }
        }
        
        result = postData("/exercises", payload)

        // result.done(function(response) {

        //     // create a new div element containing the new chart
        //     placeholder = document.createElement('div');
        //     placeholder.innerHTML = response['div'];
        //     divsBokehPlot = placeholder.children;

        //     // get span element to remove: necessary to remove old plots
        //     document.getElementById("spanGraph").remove();

        //     // appending div element
        //     newSpan = document.createElement('span')
        //     newSpan.setAttribute('id', 'spanGraph')
        //     newSpan.append(divsBokehPlot[0])
        //     document.getElementById("graph").append(newSpan)
            
        //     // creating script DOM element
        //     placeholder2 = document.createElement('div');
        //     placeholder2.innerHTML = response['script'];
        //     script_bokeh = placeholder2.children;

        //     // executing Javascript script
        //     jQuery.globalEval(script_bokeh[0].text) 

        //     console.log("Get data done!")

        // }).fail(function() {
        //     console.log("POST Ajax call failed.")
        //     document.getElementById("graph_text").innerHTML = "--- Failed ---"
        // })

    });

});
