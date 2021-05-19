function collect(){
    var BS=0,BPS=0,BPD=0,P=0,S=0;
    var BloodSugar =document.getElementById("BloodSugar").value;
    var BloodPressureSystolic = document.getElementById("BloodPressureSystolic").value;
    var BloodPressureDiastolic = document.getElementById("BloodPressureDiastolic").value;
    var Pulse = document.getElementById("Pulse").value;
    var SpO2 = document.getElementById("SpO2").value;
    var Fever = document.getElementById("Fever");
    var Cough =document.getElementById("Cough");
    var Headache = document.getElementById("Headache");
    var InaCrowdedPlace = document.getElementById("InaCrowdedPlace");
    if(BloodSugar>= 80 && BloodSugar<=180){
        BS=1;
    }
    if(BloodPressureSystolic>=110 && BloodPressureSystolic<=120){
        BPS=1;
    }
    if(BloodPressureDiastolic>=70 && BloodPressureDiastolic<=80){
        BPD=1;
    }
    if(Pulse>=60 && Pulse<=100){
        P=1;
    }
    if(SpO2>= 98 && SpO2<=100){
        S=1;
    }
    console.log(BS,BPS,BPD,P,S);
    if(Fever.checked== true || Cough.checked == true || Headache.checked == true || InaCrowdedPlace.checked == true){
        if(BS==0 || BPS==0 || BPD == 0 || P == 0 || S == 0){
            alert("You are at Risk!!! You need to consult a Doctor");
        }
        else{
            alert("You are safe!!! But You have mild symptoms.Get yourself checked by a Doctor!!!");
        }
    }
    else
    {
        if (BS==0 || BPS==0 || BPD == 0 || P == 0 || S == 0)
        {
            window.alert("You are safe!!! But You have other abnormalities .Get yourself checked by a Doctor!!!");
        }
        else
        {
            alert("You are safe!!! But follow the protocols and monitor your health continuosly");
        }
    }
}