
document.getElementById('Warn').style.display="none";
document.getElementById('Warn2').style.display="none";


function ONSub(){
    var mail = document.getElementById("mail");
    var password = document.getElementById("password");
    var Cpassword = document.getElementById("Cpassword");
    var number = document.getElementById("number");
    if(!(mail.value == "" || password.value == "" || Cpassword.value == "" || number.value == "")){
        
        var user = mail.value;
        var pass = password.value;
        var tele = number.value;

       

        alert("Account creates succesfully");
        // location.href='/';
    }
    if(mail.value == "" || password.value == "" || Cpassword.value == "" || number.value == ""){
        if(document.getElementById('Warn').style.display == "none"){
            document.getElementById('Warn').style.display = "block";
        }
        console.log("Please enter value")
    }
    else{
        if(document.getElementById('Warn').style.display == "block"){
            document.getElementById('Warn').style.display = "none";
        }
    }
    if(!(password.value == Cpassword.value)){
        alert("Passwords must match");
    }


}

