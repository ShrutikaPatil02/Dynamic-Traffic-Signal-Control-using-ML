function updateData(){
    fetch('http://127.0.0.1:8000/getData')
    .then(response => response.json())
    .then(data =>{
        document.getElementById('noOfVehiclesNorth').innerHTML = data.noOfVehiclesNorth;
        document.getElementById('timerNorth').innerHTML = data.timerNorth;
        document.getElementById('noOfVehiclesEast').innerHTML = data.noOfVehiclesEast;
        document.getElementById('timerEast').innerHTML = data.timerEast;
        document.getElementById('noOfVehiclesWest').innerHTML = data.noOfVehiclesWest;
        document.getElementById('timerWest').innerHTML = data.timerWest;
        document.getElementById('noOfVehiclesSouth').innerHTML = data.noOfVehiclesSouth;
        document.getElementById('timerSouth').innerHTML = data.timerSouth;

        if(document.getElementById('timerNorth').innerHTML != '0'){
            document.getElementById('northRed').setAttribute.backgroundColor = "black";
            document.getElementById('northGreen').setAttribute.backgroundColor = "#5adf02";

            /*document.getElementById('northRed').setAttribute("background-color","#FF033E");
            document.getElementById('northGreen').setAttribute("background-color","black");*/
        }
        else{
            document.getElementById('northRed').setAttribute("background-color","#FF033E");
            document.getElementById('northGreen').setAttribute("background-color","black");
        }

        /*if(data.timerNorth != 0){
            document.getElementById('northRed').setAttribute("background-color","#FF033E");
            document.getElementById('northGreen').setAttribute("background-color","black");
        }
        else{
            document.getElementById('northRed').setAttribute("background-color","black");
            document.getElementById('northGreen').setAttribute("background-color","#5adf02");
        }

        /*if(data.timerSouth > 0){
            document.getElementById('southRed').setAttribute("background-color","#FF033E");
            document.getElementById('southGreen').setAttribute("background-color","#41a002");
        }
        else{
            document.getElementById('southRed').setAttribute("background-color","#920224");
            document.getElementById('southGreen').setAttribute("background-color","#5adf02");
        }

        if(data.timerEast > 0){
            document.getElementById('eastRed').setAttribute("background-color","#FF033E");
            document.getElementById('eastGreen').setAttribute("background-color","#41a002");
        }
        else{
            document.getElementById('eastRed').setAttribute("background-color","#920224");
            document.getElementById('eastGreen').setAttribute("background-color","#5adf02");
        }*/


    });
}

setInterval(updateData,100);