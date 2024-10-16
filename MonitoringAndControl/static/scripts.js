function updateData(){
    fetch('http://127.0.0.1:8000/getData')
    .then(response => response.json())
    .then(data =>{
        document.getElementById('noOfVehiclesWest').innerHTML = data.noOfVehiclesWest;
    });
}

setInterval(updateData,1000);