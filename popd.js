document.addEventListener("DOMContentLoaded", function() {
    const inputs=document.getElementsByClassName("pgen");
    const input1 = document.getElementsByClassName("pana");
    const generateButton = document.getElementById("generate");
    const passwordDiv = document.getElementById("password");
    const analyseButton=document.getElementById("analyse");
    analyseButton.addEventListener("click",function(){
        alert(input1[0].value);
    });
    generateButton.addEventListener("click", function() {
        for(let i=0;i<inputs.length;i++){
            alert(inputs[i].value);
        } 
    });
  });
  function generatePassword(length) {
    let password = length;
    return password;
  }