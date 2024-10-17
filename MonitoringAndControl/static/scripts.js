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
    });
}

setInterval(updateData,100);