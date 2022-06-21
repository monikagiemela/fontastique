Dropzone.options.fileDropzone = {
  url: "/",
  thumbnailWidth: 200,
  thumbnailHeight: 200,
  thumbnailMethod: "contain",
  uploadMultiple: false,
  acceptedFiles: ".jpeg, .jpg, .png",
  clickable: true,
  success: function(file, responseText) {
    console.log(responseText.url0);
    //document.getElementById("max-result").innerHTML = "This font most likely belongs to: " + responseText.max_result;
    document.getElementById("top-three-header").innerHTML = "You might like these fonts:";
    var topFourResultsDiv = document.getElementById("top-results");
    for (var i=0; i<(responseText.top_six).length; i++){
      var col = document.createElement("div");
      col.setAttribute("class", "col");
      topFourResultsDiv.appendChild(col);
      var card= document.createElement("div");
      card.setAttribute("class", "card");
      col.appendChild(card);
      var img= document.createElement("img");
      img.setAttribute("class", "card-img-top");
      img.setAttribute("alt", responseText.top_six[i]);
      img.setAttribute("id", i);
      card.appendChild(img);
      var cardBody = document.createElement("div");
      cardBody.setAttribute("class", "card-body");
      card.appendChild(cardBody);
      var cardText = document.createElement("p");
      cardText.setAttribute("class", "card-text");
      cardText.innerHTML = responseText.top_six[i];
      cardBody.appendChild(cardText);
    }
    var img0 = document.getElementById("0");
    var img1 = document.getElementById("1");
    var img2 = document.getElementById("2");
    var img3 = document.getElementById("3");
    var img4 = document.getElementById("4");
    var img5 = document.getElementById("5");
    img0.setAttribute("src", responseText.url0);
    img1.setAttribute("src", responseText.url1);
    img2.setAttribute("src", responseText.url2);
    img3.setAttribute("src", responseText.url3);
    img4.setAttribute("src", responseText.url4);
    img5.setAttribute("src", responseText.url5);
    
    // Create TryAnother prediction button
    var tryAnotherDiv = document.querySelector("#try-another");
    var buttonTryAnother = document.createElement("button");
    buttonTryAnother.setAttribute("id", "try-another-button");
    buttonTryAnother.textContent = "Check another text";
    tryAnotherDiv.appendChild(buttonTryAnother);
    buttonTryAnother.addEventListener("click", function() { 
      window.location.reload();
    })
  },
  transformFile: function(file, done) {
      // Create Dropzone reference for use in confirm button click handler
      var myDropZone = this;
      
      // Create the image editor overlay
      var editor = document.createElement("div");
      editor.setAttribute("id", "editor");
      document.body.appendChild(editor);
      
      // Create confirm button at the top left of the viewport
      var buttonConfirm = document.createElement("button");
      buttonConfirm.setAttribute("id", "button-confirm")
      buttonConfirm.textContent ="Confirm";
      editor.appendChild(buttonConfirm);
      buttonConfirm.addEventListener("click", function() { 
        // Get the output file data from Croppie
        croppie.result({
          type:"blob",
          
          size: "original"
          //{
          //  width: 105,
          //  height: 105
          //}

        }).then(function(blob) {
        
          // Create a new Dropzone file thumbnail
          myDropZone.createThumbnail(
            blob,
            myDropZone.options.thumbnailWidth,
            myDropZone.options.thumbnailHeight,
            myDropZone.options.thumbnailMethod,
            false, 
            function(dataURL) {
              
              // Update the Dropzone file thumbnail
              myDropZone.emit("thumbnail", file, dataURL);
              // Tell Dropzone of the new file
              done(blob);
            });
        });
 
        // Remove the editor from view
        editor.parentNode.removeChild(editor);
      });
      
      // Create the Croppie editor
      var croppie = new Croppie(editor, {
        enableResize: true
      });
      // Tell Croppie to load the file
      croppie.bind({
        url: URL.createObjectURL(file)
      });
  }
};