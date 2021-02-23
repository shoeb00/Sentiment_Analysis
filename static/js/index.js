function validator(){
    console.log(document.getElementById("inputText").value.length, document.getElementById("inputFile").value)
    if(document.getElementById("inputText").value.length == 0 && document.getElementById("inputFile").value.length == 0){
        alert('Please provide an input')
        return false;
    }
    if(document.getElementById("inputText").value && document.getElementById("inputFile").value.length){
        alert('Please select a single input')
        return false;
    }
    return true;
}
function fileValidation() { 
    var fileInput = document.getElementById('inputFile'); 
    var filePath = fileInput.value; 
    var allowedExtensions = /(\.txt|\.csv)$/i; 
      
    if (!allowedExtensions.exec(filePath)) { 
        alert('Invalid file type, please select a .txt or .csv file'); 
        fileInput.value = ''; 
        return false; 
    }  
}
function wrap(){
    document.querySelector('.wrap').style.cssText = 'background-color : black; display : inline;' 
    alert('wrapper triggered')
    $(".loadingAnimation").fadeOut("slow");
}