Dropzone.options.fileDropzone = {
  url: "/",
  thumbnailWidth: 105,
  thumbnailHeight: 200,
  thumbnailMethod: "contain",
  uploadMultiple: false,
  acceptedFiles: ".jpeg, .jpg, .png",
  clickable: true,
  addRemoveLinks: true, 
  success: function(file, responseText) {
    console.log(responseText)
    document.getElementById("max-result").innerHTML = "This font most likely belongs to: " + responseText.max_result;
    document.getElementById("top-three-header").innerHTML = "You might also like:"
    var topThreeDiv = document.getElementById("top-three-result")
    for (var i=0; i<(responseText.top_three).length; i++){
      topThreeDiv.innerHTML += `
      <div>${ responseText.top_three[i] }</div>
   `}
  }
};