function addCar() {
    let manufacturer = document.querySelector('input[name="manufacturer"]').value;
    let model = document.querySelector('input[name="model"]').value;
    let instock = document.querySelector('select[name="instock"]').value;
    let price = document.querySelector('input[name="price"]').value;

    let carData = {
        manufacturer: manufacturer,
        model: model,
        instock: instock,
        price: price
    };

    fetch('http://127.0.0.1:5000/insert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(carData),
    })
        .then(response => {
            if (response.ok) {

                fetchTableData();
                $('#myModal').modal('hide');
            } else {
                console.error('Failed to add car');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}


function fetchTableData() {
    fetch('http://localhost:5000/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('table-body');
            tableBody.innerHTML = '';
            data.forEach(item => {
                const tr = document.createElement('tr');

                let stringifyItem = JSON.stringify(item)
                tr.innerHTML = `
                  <td>${item.id}</td>
                  <td>${item.manufacturer}</td>
                  <td>${item.model}</td>
                  <td>${item.instock}</td>
                  <td>${item.price}</td>
                  <td>
                      <button class="btn btn-outline-success" data-bs-toggle="modal" data-bs-target="#myModal" onclick="updateCarModal('${encodeURI(stringifyItem)}')">Edit</button>
                      <button type="button" class="btn btn-outline-danger" onclick="deleteCar(${item.id})">Delete</button>
                  </td>
              `;
                tableBody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));


    console.log(modalButton)
}


function deleteCar(id) {
    fetch('http://127.0.0.1:5000/delete/' + id, {
            method: "DELETE",
        }
    )
        .then(response => {
            if (response.ok) {
                fetchTableData()
            }
        })
}


function updateCarModal(car) {

    let modalButton = document.querySelector('.update-btn')


    car = JSON.parse(decodeURI(car))
    console.log("update", car)

    let manufacturer = document.querySelector('input[name="manufacturer"]').value = car.manufacturer;
    let model = document.querySelector('input[name="model"]').value = car.model;
    let instock = document.querySelector('select[name="instock"]').value = car.instock;
    let price = document.querySelector('input[name="price"]').value = car.price;


    let carData = {
        id: car.id,
        manufacturer: manufacturer,
        model: model,
        instock: instock,
        price: price
    };

    modalButton.innerHTML = `<button type="button" class="btn btn-success" data-bs-dismiss="modal" onclick=updateCar('${JSON.stringify(carData)}')>Update</button>`


}

function updateCar(carData) {

    let manufacturer = document.querySelector('input[name="manufacturer"]').value;
    let model = document.querySelector('input[name="model"]').value;
    let instock = document.querySelector('select[name="instock"]').value;
    let price = document.querySelector('input[name="price"]').value;

    carData = JSON.parse(carData);
    console.log("dataaa", carData)

    fetch('http://127.0.0.1:5000/update/' + carData.id, {
        method: "PUT",
        body: JSON.stringify({
            manufacturer: manufacturer,
            model: model,
            instock: instock,
            price: price
        }),
        headers: {"content-type": "application/json"}
    })
        .then(response => {
            if (response.ok) {

                fetchTableData()
                $('#myModal').modal('hide');
            } else {
                console.error("Fail To Update Car")
            }
        })
}

function resetButton() {

    let modalButton = document.querySelector('.update-btn')


    modalButton.innerHTML = `<button type="button" class="btn btn-success" data-bs-dismiss="modal" onclick="addCar()">Add</button>`
}


function resetForm() {

    document.querySelector('input[name="manufacturer"]').value = '';
    document.querySelector('input[name="model"]').value = '';
    document.querySelector('select[name="instock"]').value = '';
    document.querySelector('input[name="price"]').value = '';

}

fetchTableData();
