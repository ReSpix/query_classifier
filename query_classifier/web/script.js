let resultData = 0

document.getElementById('submitButton').addEventListener('click', function () {
    const inputValue = document.getElementById('inputField').value;

    // URL for GET request, append the input value as a query parameter
    const url = `http://127.0.0.1:8000/classification/${encodeURIComponent(inputValue)}`;

    // Create a new XMLHttpRequest object
    const xhr = new XMLHttpRequest();

    // Configure it: GET-request for the URLs
    xhr.open('GET', url, true);

    // Set up a function to handle the response
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Parse the JSON response
            const response = JSON.parse(xhr.responseText);
            // Display the result
            //document.getElementById('result').innerText = JSON.stringify(response, null, 2);
            displayResult(response);
            resultData = response['result'];
        } else {
            // Display an error message if the request failed
            document.getElementById('result').innerText = `Error: ${xhr.status}`;
        }
    };

    // Send the request
    xhr.send();
});

document.getElementById('openButton').addEventListener('click', function () {
    openURL();
});

function displayResult(data) {
    const resultContainer = document.getElementById('result');
    resultContainer.innerHTML = ''; // Clear previous results

    // Create a table to display the result
    const table = document.createElement('table');

    // Add query row
    const queryRow = document.createElement('tr');
    //queryRow.innerHTML = `<th>Query</th><td colspan="2">${data.query}</td>`;
    table.appendChild(queryRow);

    // Add result rows
    const resultData = data.result;

    for (let key in resultData) {
        if (Array.isArray(resultData[key])) {
            resultData[key].forEach((item, index) => {
                const row = document.createElement('tr');
                if (index === 0) {
                    row.innerHTML = `<th>${key}</th><td>${item}</td>`;
                } else {
                    row.innerHTML = `<th></th><td>${item}</td>`;
                }
                table.appendChild(row);
            });
        } else {
            const row = document.createElement('tr');
            row.innerHTML = `<th>${key}</th><td>${resultData[key]}</td>`;
            table.appendChild(row);
        }
    }

    resultContainer.appendChild(table);
}

function openURL() {
    let url = `https://www.farpost.ru/rabota/vacansii/?`;

    if (resultData['по должности-лемме'] != "Нет") {
        url = url.slice(0, -1);
        url += `+/${resultData['по должности-лемме']}/?`;
    }

    let employment = {
        'вахта': 'watch',
        'вечерняя': 'evening',
        'временная': 'temporary',
        'дневная': 'day',
        'ночная': 'night',
        'подработка': 'free',
        'посменная': 'shift',
        'посуточная': '24hours',
        'удаленная': 'remote',
        'на дому': 'remote',
        'на неполный день': 'part',
        'по выходным': 'weekends',
    }
    if (resultData['занятость'][0] != 'Нет') {
        resultData['занятость'].forEach(item => {
            url += `employment%5B%5D=${employment[item]}&`
        }
        );
    }

    window.open(url, '_blank');
}