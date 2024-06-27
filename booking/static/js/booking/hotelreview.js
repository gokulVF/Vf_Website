// Sample data similar to details.CancellationPolicies
var cancellationPoliciesString = document.getElementById("CancellationPolicies").value;
var cancellationPolicies = JSON.parse(cancellationPoliciesString);
console.log(cancellationPolicies)

// Function to generate <tr> elements dynamically
function generateCancellationPolicyRows() {
    var tableBody = document.getElementById("cancellationPoliciesTableBody");
    var tableRows = "";

    // Loop over cancellation policies and generate <tr> elements
    cancellationPolicies.forEach(function(policy) {
        // Format FromDate and ToDate
        var fromDate = new Date(policy.FromDate).toLocaleString('en-US', {day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit'});
        var toDate = new Date(policy.ToDate).toLocaleString('en-US', {day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit'});

        var row = `
            <tr>
                <td>${fromDate}</td>
                <td>${toDate}</td>
                <td>${policy.Charge}% of booking amount</td>
            </tr>
        `;
        tableRows += row;
    });

    // Update the table body with generated rows
    tableBody.innerHTML = tableRows;
}

// Call the function to generate rows
generateCancellationPolicyRows();

function validateForm() {
var valid = true;

// Reset all error messages and border styles
document.getElementById('nameError').innerText = '';
document.getElementById('phoneError').innerText = '';
document.getElementById('emailError').innerText = '';

var nameInput = document.querySelector('.username');
var phoneInput = document.querySelector('.phone_number');
var emailInput = document.querySelector('.email');

var name = nameInput.value;
var phone = phoneInput.value;
var email = emailInput.value;

// Validate name
if (name.trim() === '') {
    document.getElementById('nameError').innerText = 'Name is required';
    nameInput.style.border = '1px solid red';
    valid = false;
} else {
    nameInput.style.border = ''; // Reset border style if valid
}

// Validate phone
var phonePattern = /^\d{10}$/;
if (phone.trim() === '') {
    document.getElementById('phoneError').innerText = 'Phone number is required';
    phoneInput.style.border = '1px solid red';
    valid = false;
} else if (!phonePattern.test(phone)) {
    document.getElementById('phoneError').innerText = 'Invalid phone number';
    phoneInput.style.border = '1px solid red';
    valid = false;
} else {
    phoneInput.style.border = ''; // Reset border style if valid
}

// Validate email
var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (email.trim() === '') {
    document.getElementById('emailError').innerText = 'Email is required';
    emailInput.style.border = '1px solid red';
    valid = false;
} else if (!emailPattern.test(email)) {
    document.getElementById('emailError').innerText = 'Invalid email address';
    emailInput.style.border = '1px solid red';
    valid = false;
} else {
    emailInput.style.border = ''; // Reset border style if valid
}

// Retrieve validation data
var validation_data = document.getElementById('validationidforbooking').value;
var parsedNewData = JSON.parse(validation_data);
var pancard = parsedNewData.is_pan_mandatory_voucher;
var passportv = parsedNewData.is_passport_mandatory_voucher;
var pancard_book = parsedNewData.is_pan_mandatory_confirm;
var passport_book = parsedNewData.is_passport_mandatory_confirm;

guestData.forEach(function (room, roomIndex) {
    // Validate adults
    for (var i = 0; i < room.NoOfAdults; i++) {
        var adultFirstName = document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_first_name"]`);
        var adultLastName = document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_last_name"]`);
        var adultPannumber = document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_pancard"]`);
        var adultPassportnumber = document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_passport"]`);

        // Validate adult first name
        if (adultFirstName.value.trim() === '') {
            document.getElementById(`firstNameError_${roomIndex + 1}_adult_${i + 1}`).innerText = 'Please Enter the first name';
            adultFirstName.style.border = '1px solid red';
            valid = false;
        } else {
            adultFirstName.style.border = '';
            document.getElementById(`firstNameError_${roomIndex + 1}_adult_${i + 1}`).innerText = ''; // Reset error message if valid
        }

        // Validate adult last name
        if (adultLastName.value.trim() === '') {
            document.getElementById(`lastNameError_${roomIndex + 1}_adult_${i + 1}`).innerText = 'Please Enter the last name';
            adultLastName.style.border = '1px solid red';
            valid = false;
        } else {
            adultLastName.style.border = ''; // Reset border style if valid
            document.getElementById(`lastNameError_${roomIndex + 1}_adult_${i + 1}`).innerText = '';
        }

        // Validate PAN number for adults
        if (pancard || pancard_book) {
            if (adultPannumber.value.trim() === '') {
                document.getElementById(`pancardError_${roomIndex + 1}_adult_${i + 1}`).innerText = 'Please Enter the PAN number';
                adultPannumber.style.border = '1px solid red';
                valid = false;
            } else {
                adultPannumber.style.border = ''; // Reset border style if valid
                document.getElementById(`pancardError_${roomIndex + 1}_adult_${i + 1}`).innerText = '';
            }
        }

        // Validate passport number for adults
        if (passport_book || passportv) {
            if (adultPassportnumber.value.trim() === '') {
                document.getElementById(`passportError_${roomIndex + 1}_adult_${i + 1}`).innerText = 'Please Enter the passport number';
                adultPassportnumber.style.border = '1px solid red';
                valid = false;
            } else {
                adultPassportnumber.style.border = ''; // Reset border style if valid
                document.getElementById(`passportError_${roomIndex + 1}_adult_${i + 1}`).innerText = '';
            }
        }
    }

    // Validate children
    for (var j = 0; j < room.NoOfChild; j++) {
        var childFirstName = document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_first_name"]`);
        var childLastName = document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_last_name"]`);
        var childPannumber = document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_pancard"]`);
        var childPassportnumber = document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_passport"]`);

        // Validate child first name
        if (childFirstName.value.trim() === '') {
            document.getElementById(`cfirstNameError_${roomIndex + 1}_child_${j + 1}`).innerText = 'Please Enter the first name';
            childFirstName.style.border = '1px solid red';
            valid = false;
        } else {
            childFirstName.style.border = ''; // Reset border style if valid
            document.getElementById(`cfirstNameError_${roomIndex + 1}_child_${j + 1}`).innerText = ''; // Reset error message if valid
        }

        // Validate child last name
        if (childLastName.value.trim() === '') {
            document.getElementById(`clastNameError_${roomIndex + 1}_child_${j + 1}`).innerText = 'Please Enter the last name';
            childLastName.style.border = '1px solid red';
            valid = false;
        } else {
            childLastName.style.border = ''; // Reset border style if valid
            document.getElementById(`clastNameError_${roomIndex + 1}_child_${j + 1}`).innerText = '';
        }

        // Validate PAN number for children
        if (pancard || pancard_book) {
            if (childPannumber.value.trim() === '') {
                document.getElementById(`pancardError_${roomIndex + 1}_child_${j + 1}`).innerText = 'Please Enter the PAN number';
                childPannumber.style.border = '1px solid red';
                valid = false;
            } else {
                childPannumber.style.border = ''; // Reset border style if valid
                document.getElementById(`pancardError_${roomIndex + 1}_child_${j + 1}`).innerText = '';
            }
        }

        // Validate passport number for children
        if (passport_book || passportv) {
            if (childPassportnumber.value.trim() === '') {
                document.getElementById(`passportError_${roomIndex + 1}_child_${j + 1}`).innerText = 'Please Enter the passport number';
                childPassportnumber.style.border = '1px solid red';
                valid = false;
            } else {
                childPassportnumber.style.border = ''; // Reset border style if valid
                document.getElementById(`passportError_${roomIndex + 1}_child_${j + 1}`).innerText = '';
            }
        }
    }
});

var specialRequest = document.getElementById('req').value;

return valid;
}

var personsdetails = document.getElementById('hiddenGuestData').textContent;
var guestData = JSON.parse(personsdetails || "[]");

console.log(guestData);
var validation_data = document.getElementById('validationidforbooking').value;
var parsedNewData = JSON.parse(validation_data)
console.log(parsedNewData)

function generateRoomDetails() {
    var container = document.getElementById('guestDetailsContainer');
    container.innerHTML = ''; // Clear existing content

    var leadPassengerAssigned = false; // Flag to track lead passenger assignment
    var pancard = parsedNewData.is_pan_mandatory_voucher;
    var passportv = parsedNewData.is_passport_mandatory_voucher;
    var pancard_book = parsedNewData.is_pan_mandatory_confirm;
    var passport_book = parsedNewData.is_passport_mandatory_confirm;
    

    guestData.forEach(function (room, roomIndex) {
        var roomElement = document.createElement('div');
        roomElement.className = 'mt-2';
        roomElement.innerHTML = `<h3 class="theme">Room <span class="num">${roomIndex + 1}</span></h3>`;

        for (var i = 0; i < room.NoOfAdults; i++) {
            var adultElement = document.createElement('div');
            adultElement.className = 'my-2';

            // Assign lead passenger only if it hasn't been assigned yet
            // var leadCustomerText = (!leadPassengerAssigned && i === 0 && roomIndex === 0) ? ' - Lead Passenger' : '';
            // var leadpassenger = (!leadPassengerAssigned && i === 0 && roomIndex === 0) ? 0 : 1;
            var leadCustomerText = (i === 0) ? ' - Lead Passenger' : '';
            var leadpassenger = (i === 0) ? 0 : 1;

            // if (!leadPassengerAssigned && i === 0 && roomIndex === 0) {
            //     leadPassengerAssigned = true;
            // }

            const panFieldId = `pan_${roomIndex + 1}_adult_${i + 1}`;
            const resultDivId = `pancardError_${roomIndex + 1}_adult_${i + 1}`;
            const firstnameId = `firstName_${roomIndex + 1}_adult_${i + 1}`;
            const lastnameId = `lastName_${roomIndex + 1}_adult_${i + 1}`;
            const checkboxId = `checkboxId_${roomIndex + 1}_adult_${i + 1}`;
            const passport = `passport_${roomIndex + 1}_adult_${i + 1}`
            const passportDivId = `passportError_${roomIndex + 1}_adult_${i + 1}`;

            adultElement.innerHTML = `
                ${pancard || passportv || pancard_book || passport_book ? `
                <div class="">
                    <h4 class="name_no theme2">Adult <span class="num">${i + 1}</span><span class="theme">${leadCustomerText}</span></h4>
                </div>
                ${pancard || pancard_book ? `
                <form class="row pb-2">
                    <div class="col-lg-4 mb-0">
                        <input type="text" id="${panFieldId}" class="f-inp upercase" placeholder="Enter your PAN number" name="room_${roomIndex + 1}_adult_${i + 1}_pancard" required>
                        <span class="error" id="${resultDivId}"></span>
                    </div>
                    <div class="col-lg-3">
                        <button type="button" onclick="verifyPAN('${panFieldId}', '${resultDivId}','${firstnameId}','${lastnameId}','${checkboxId}')" class="nir-btn" style="border-radius: 4px;">Verify PAN</button>
                    </div>
                    ${leadCustomerText ? `
                    <div class="col-lg-3 mt-2 theme2 fw-bold" style="font-size:15px;" id="${checkboxId}">
                    <input type="checkbox" id="applyPanToAll" onclick="togglePanFields('pan_${roomIndex + 1}_${i + 1}', this)" > Apply to all Pax
                </div>` : ''}
                </form>
                ` :''}
                
                
                <div class="row">
                    <div class="col-lg-2 mb-1">
                        <select class="f-inp" style="height:50px;" name="room_${roomIndex + 1}_adult_${i + 1}_gender">
                            <option value="Mr">Mr</option>
                            <option value="Mrs">Mrs</option>
                            <option value="Miss">Miss</option>
                            <option value="Ms">Ms</option>
                        </select>
                    </div>
                    <div class="col-lg-5 mb-1">
                        <input type="text" class="f-inp" id="${firstnameId}" placeholder="Enter first name as per PAN" name="room_${roomIndex + 1}_adult_${i + 1}_first_name" required>
                        <span class="error" id="firstNameError_${roomIndex + 1}_adult_${i + 1}"></span>
                    </div>
                    <div class="col-lg-5 mb-1">
                        <input type="text" class="f-inp" id="${lastnameId}" placeholder="Enter last name as per PAN" name="room_${roomIndex + 1}_adult_${i + 1}_last_name" required>
                        <span class="error" id="lastNameError_${roomIndex + 1}_adult_${i + 1}"></span>
                    </div>
                </div>
                ${passportv || passport_book ? `
                <div class="row">
                    <div class="col-lg-5 mb-1">
                    <input type="text" class="f-inp" id="${passport}" name="room_${roomIndex + 1}_adult_${i + 1}_passport" placeholder="Enter passport Number" required>
                    <span id="${passportDivId}" class="error"></span>
                    </div>
                </div>
                ` : ''}` : `
                <div class="">
                    <h4 class="name_no theme2">Adult <span class="num">${i + 1}</span><span class="theme">${leadCustomerText}</span></h4>
                </div>
                <div class="row">
                    <div class="col-lg-2 mb-1">
                        <select class="f-inp" style="height:50px;" name="room_${roomIndex + 1}_adult_${i + 1}_gender">
                            <option value="Mr">Mr</option>
                            <option value="Mrs">Mrs</option>
                            <option value="Miss">Miss</option>
                            <option value="Ms">Ms</option>
                        </select>
                    </div>
                    <div class="col-lg-5 mb-1">
                        <input type="text" class="f-inp" placeholder="Enter your first name" name="room_${roomIndex + 1}_adult_${i + 1}_first_name" required>
                        <span class="error" id="firstNameError_${roomIndex + 1}_adult_${i + 1}"></span>
                    </div>
                    <div class="col-lg-5 mb-1">
                        <input type="text" class="f-inp" placeholder="Enter your last Name" name="room_${roomIndex + 1}_adult_${i + 1}_last_name" required>
                        <span class="error" id="lastNameError_${roomIndex + 1}_adult_${i + 1}"></span>
                    </div>
                </div>`}
                <input type="hidden" name="room_${roomIndex + 1}_adult_${i + 1}_age" value="0">
                <input type="hidden" name="leadpassenger_${roomIndex + 1}_adult_${i + 1}" value="${leadpassenger}">
            `;

            roomElement.appendChild(adultElement);
        }

        for (var j = 0; j < room.NoOfChild; j++) {
            var childElement = document.createElement('div');
            childElement.className = 'mt-2';

            const panFieldId = `pan_${roomIndex + 1}_child_${j + 1}`;
            const resultDivId = `pancardError_${roomIndex + 1}_child_${j + 1}`;
            const passport = `passport_${roomIndex + 1}_child_${j + 1}`
            const passportDivId = `passportError_${roomIndex + 1}_child_${j + 1}`;

            childElement.innerHTML = `
                ${pancard || passportv || pancard_book || passport_book ? `
                <div class="row">
                    <h4 class="name_no theme2">Child <span class="num">${j + 1}</span></h4>
                </div>
                ${pancard || pancard_book ? `
                <form class="row pb-2">
                    <div class="col-lg-4 mb-1">
                        <input type="text" id="${panFieldId}" class="f-inp upercase pan_first_input" placeholder="Enter Your PAN Card Number" name="room_${roomIndex + 1}_child_${j + 1}_pancard" required>
                        <span class="error" id="${resultDivId}"></span>
                    </div>
                    <div class="col-lg-4">
                        <button type="button" onclick="verifyPAN('${panFieldId}', '${resultDivId}')" class="nir-btn" style="border-radius: 4px;">Verify PAN</button>
                    </div>
                </form>
                ` : ''}
                
                <div class="row">
                    <div class="col-lg-2 mb-1">
                        <select class="f-inp" style="height:50px;" name="room_${roomIndex + 1}_child_${j + 1}_gender">
                            <option value="Mr">Mr</option>
                            <option value="Mrs">Mrs</option>
                            <option value="Miss">Miss</option>
                            <option value="Ms">Ms</option>
                        </select>
                    </div>
                    <div class="col-lg-5 mb-1">
                        <input class="f-inp" type="text" placeholder="Enter First Name as per PAN" name="room_${roomIndex + 1}_child_${j + 1}_first_name" required>
                        <span class="error" id="cfirstNameError_${roomIndex + 1}_child_${j + 1}"></span>
                    </div>
                    <div class="col-lg-5 mb-1">
                        <input class="f-inp" type="text" placeholder="Enter Last Name as per PAN" name="room_${roomIndex + 1}_child_${j + 1}_last_name" required>
                        <span class="error" id="clastNameError_${roomIndex + 1}_child_${j + 1}"></span>
                    </div>
                </div>
                ${passportv || passport_book ? `
                  <div class="row">
                    <div class="col-lg-5 mb-1">
                    <input type="text" class="f-inp" id="${passport}" name="room_${roomIndex + 1}_child_${j + 1}_passport" placeholder="Enter Passport Number" required>
                    <span id="${passportDivId}" class="error"></span>
                </div>
                </div>
                ` : ''}` : `
                <div class="row">
                    <h4 class="name_no theme2">Child <span class="num">${j + 1}</span></h4>
                </div>
                <div class="row">
                    <div class="col-lg-2 mb-1">
                        <select class="f-inp" style="height:50px;" name="room_${roomIndex + 1}_child_${j + 1}_gender">
                            <option value="Mr">Mr</option>
                            <option value="Mrs">Mrs</option>
                            <option value="Miss">Miss</option>
                            <option value="Ms">Ms</option>
                        </select>
                    </div>
                    <div class="col-lg-5 mb-1">
                        <input class="f-inp" type="text" placeholder="Enter Your First Name" name="room_${roomIndex + 1}_child_${j + 1}_first_name" required>
                        <span class="error" id="cfirstNameError_${roomIndex + 1}_child_${j + 1}"></span>
                    </div>
                    <div class="col-lg-5 mb-1">
                        <input class="f-inp" type="text" placeholder="Enter Your Last Name" name="room_${roomIndex + 1}_child_${j + 1}_last_name" required>
                        <span class="error" id="clastNameError_${roomIndex + 1}_child_${j + 1}"></span>
                    </div>
                </div>`}
                <div class="col-md-0" style="display:none">
                    <input class="f-inp" type="hidden" name="room_${roomIndex + 1}_child_${j + 1}_ChildAge" value="${room.ChildAge[j]}">
                    <input type="hidden" name="leadpassenger_${roomIndex + 1}_child_${j + 1}" value="1">
                </div>
            `;

            roomElement.appendChild(childElement);
        }

        container.appendChild(roomElement);
    });
}

function togglePanFields(panFieldId, checkbox) {
    var panValue = document.getElementById(panFieldId).value;
    var panFields = document.querySelectorAll('input[name*="pancard"]');

    panFields.forEach(function (field) {
        if (checkbox.checked) {
            field.value = panValue;
        } else {
            // Only clear non-lead passenger fields
            if (field.id !== panFieldId) {
                field.value = '';
            }
        }
    });
}

function verifyPAN(panFieldId, resultDivId, firstnameId, lastnameId, checkboxId,) {
    const pan = document.getElementById(panFieldId).value;

    if (!validationpan(pan, resultDivId)) {
        return; // Stop if the PAN format is invalid
    }

    const csrftoken = getCookie('csrftoken');

    fetch('/verify_pan/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ pan: pan })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById(resultDivId);
        const firstname = document.getElementById(firstnameId);
        const lastname = document.getElementById(lastnameId);
        const checkbox = document.getElementById(checkboxId);

        if (data.data['status'] === 'VALID') {
            // resultDiv.innerHTML = `<p>${data.data['status']}</p>`;
            checkbox.style.display = 'block';
            firstname.value = `${data.data['firstname']}`;
            lastname.value = `${data.data['secondname']}`;
            firstname.setAttribute('readonly', 'readonly');
            lastname.setAttribute('readonly', 'readonly');
        } else {
            resultDiv.innerHTML = `<p>Error: ${data.message}</p>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function validationpan(pan, resultDivId) {
    const panRegex = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;
    const resultDiv = document.getElementById(resultDivId);

    // Trim the PAN input to remove any leading/trailing spaces
    const trimmedPan = pan.trim();

    console.log(`PAN being validated: '${trimmedPan}'`);

    if (!panRegex.test(trimmedPan)) {
        resultDiv.innerHTML = '<p>Invalid PAN format. Please enter a valid PAN number.</p>';
        return false;
    } else {
        resultDiv.innerHTML = '';
        return true;
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

generateRoomDetails();

document.getElementById('myButton').addEventListener('click', function () {
    if (validateForm()) {
    // Collect adult and child details from the form

    var adultChildDetails = [];
    guestData.forEach(function (room, roomIndex) {
        var roomDetails = {
            adults: [],
            children: []
        };

        for (var i = 0; i < room.NoOfAdults; i++) {
        var adultDetails = {
            gender: document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_gender"]`)?.value || '',
            firstName: document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_first_name"]`)?.value || '',
            lastName: document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_last_name"]`)?.value || '',
            age: document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_age"]`)?.value || '',
            leadpassenger: document.querySelector(`[name="leadpassenger_${roomIndex + 1}_adult_${i + 1}"]`)?.value || '',
            pancardnumber: document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_pancard"]`)?.value || 'none',
            passportnumber: document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_passport"]`)?.value || 'none'
        };
        roomDetails.adults.push(adultDetails);
    }

    for (var j = 0; j < room.NoOfChild; j++) {
        var childDetails = {
            gender: document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_gender"]`)?.value || '',
            firstName: document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_first_name"]`)?.value || '',
            lastName: document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_last_name"]`)?.value || '',
            age: document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_ChildAge"]`)?.value || '',
            leadpassenger: document.querySelector(`[name="leadpassenger_${roomIndex + 1}_child_${j + 1}"]`)?.value || '',
            pancardnumber: document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_pancard"]`)?.value || 'none',
            passportnumber: document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_passport"]`)?.value || 'none'
        };
        roomDetails.children.push(childDetails);
    }

        // Add room details to the array
        adultChildDetails.push({
            ['room' + (roomIndex + 1)]: roomDetails
        });
    });


    var jsonString = JSON.stringify(adultChildDetails);
    // Submit the form
    document.querySelector('[name="user_information"]').value = jsonString;
    document.querySelector('form').submit();
} else {
    return false;
}
});

const timeoutDuration = 10 * 60 * 1000; // 10 minutes
let timeoutTimer;

function updateTimerDisplay(timeRemaining) {
    const minutes = Math.floor(timeRemaining / 60000);
    const seconds = Math.floor((timeRemaining % 60000) / 1000);
    const formattedTime = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    document.getElementById("timer").innerText = `Time remaining: ${formattedTime}`;
}

function resetTimer() {
    clearTimeout(timeoutTimer);
    let timeRemaining = timeoutDuration;

    function update() {
        updateTimerDisplay(timeRemaining);
        timeRemaining -= 1000;

        if (timeRemaining < 0) {
            $("#timeOutBtn").click();
            updateTimerDisplay(0); 
            setTimeout(function() {
                window.location.href = "{% url 'hotel' %}"; // Replace with the desired URL
            }, 2000);
        } else {
            timeoutTimer = setTimeout(update, 1000);
        }
    }

    update();
}
    
resetTimer();

function sendit() {
    if (validateForm()) {
        var currentTime = new Date();
        var currentTimeWithSec = currentTime.toString().slice(4, 24);

        var contime = currentTimeWithSec;

        document.getElementById('curTime').value = contime;

        var form = document.createElement('form');
        form.method = 'POST';
        form.action = '/hotelbooked/';

        // Get values of hidden inputs
        var blockBook = document.querySelector('.block_book').value;
        var hide123Val = document.querySelector('.hide_123_val').value;
        var categoryId = document.querySelector('.category_id').value;

        // Append hidden input fields to the form
        var blockBookField = document.createElement('input');
        blockBookField.type = 'hidden';
        blockBookField.name = 'block_book';
        blockBookField.value = blockBook;
        form.appendChild(blockBookField);

        var hide123ValField = document.createElement('input');
        hide123ValField.type = 'hidden';
        hide123ValField.name = 'hide_123_val';
        hide123ValField.value = hide123Val;
        form.appendChild(hide123ValField);

        var categoryIdField = document.createElement('input');
        categoryIdField.type = 'hidden';
        categoryIdField.name = 'category_id';
        categoryIdField.value = categoryId;
        form.appendChild(categoryIdField);

        // // Retrieve CSRF token from original form
        // var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        // // Add CSRF token to the new form
        // var csrfField = document.createElement('input');
        // csrfField.type = 'hidden';
        // csrfField.name = 'csrfmiddlewaretoken';
        // csrfField.value = csrfToken;
        // form.appendChild(csrfField);

        // Rest of your existing code
        document.body.appendChild(form);
        form.submit();
        document.getElementById('preloader').style.display = 'block';
        document.getElementById('status').style.display = 'block';
    } else {
        console.log("validation failed");
    }
}








// Commands

//     function validateForm() {
//     var valid = true;

//     document.getElementById('nameError').innerText = '';
//     document.getElementById('phoneError').innerText = '';
//     document.getElementById('emailError').innerText = '';

//     var nameInput = document.querySelector('.username');
//     var phoneInput = document.querySelector('.phone_number');
//     var emailInput = document.querySelector('.email');

//     var name = nameInput.value;
//     var phone = phoneInput.value;
//     var email = emailInput.value;

//     if (name.trim() === '') {
//         document.getElementById('nameError').innerText = 'Name is required';
//         nameInput.style.border = '1px solid red';
//         valid = false;
//     } else {
//         nameInput.style.border = ''; // Reset border style if valid
//     }

//     var phonePattern = /^\d{10}$/;
//     if (phone.trim() === '') {
//         document.getElementById('phoneError').innerText = 'Phone number is required';
//         phoneInput.style.border = '1px solid red';
//         valid = false;
//     } else if (!phonePattern.test(phone)) {
//         document.getElementById('phoneError').innerText = 'Invalid phone number';
//         phoneInput.style.border = '1px solid red';
//         valid = false;
//     } else {
//         phoneInput.style.border = ''; // Reset border style if valid
//     }

//     var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//     if (email.trim() === '') {
//         document.getElementById('emailError').innerText = 'Email is required';
//         emailInput.style.border = '1px solid red';
//         valid = false;
//     } else if (!emailPattern.test(email)) {
//         document.getElementById('emailError').innerText = 'Invalid email address';
//         emailInput.style.border = '1px solid red';
//         valid = false;
//     } else {
//         emailInput.style.border = ''; // Reset border style if valid
//     }

//     var validation_data = document.getElementById('validationidforbooking').value;
//     var parsedNewData = JSON.parse(validation_data)
//     var pancard = parsedNewData.is_pan_mandatory_voucher;
//     var passportv = parsedNewData.is_passport_mandatory_voucher;
//     var pancard_book = parsedNewData.is_pan_mandatory_confirm;
//     var passport_book = parsedNewData.is_passport_mandatory_confirm;

//     guestData.forEach(function (room, roomIndex) {
//     for (var i = 0; i < room.NoOfAdults; i++) {
//         var adultFirstName = document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_first_name"]`);
//         var adultLastName = document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_last_name"]`);
//         var pannumber = document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_pancard"]`);
//         var passportnumber = document.querySelector(`[name="room_${roomIndex + 1}_adult_${i + 1}_passport"]`);

//         if (adultFirstName.value.trim() === '') {
//             document.getElementById(`firstNameError_${roomIndex + 1}_adult_${i + 1}`).innerText = 'Please Enter the first name';
//             adultFirstName.style.border = '1px solid red';
//             valid = false;
//         } else {
//             adultFirstName.style.border = '';
//             document.getElementById(`firstNameError_${roomIndex + 1}_adult_${i + 1}`).innerText = ' '; // Reset border style if valid
//         }

//         if (adultLastName.value.trim() === '') {
//             document.getElementById(`lastNameError_${roomIndex + 1}_adult_${i + 1}`).innerText = 'Please Enter the last name';
//             adultLastName.style.border = '1px solid red';
//             valid = false;
//         } else {
//             adultLastName.style.border = ''; // Reset border style if valid
//             document.getElementById(`lastNameError_${roomIndex + 1}_adult_${i + 1}`).innerText = ' ';
//         }

//        if(pancard || pancard_book ){
//         if (pannumber.value.trim() === '') {
//             document.getElementById(`pancardError_${roomIndex + 1}_adult_${i + 1}`).innerText = 'Please Enter the PAN number';
//              phoneInput.style.border = '1px solid red';
//              valid = false;
//          }else {
//              phoneInput.style.border = ''; // Reset border style if valid
//              document.getElementById(`pancardError_${roomIndex + 1}_adult_${i + 1}`).innerText = '';
//          }
//         }
      
//         if(passport_book || passportv ){
//         if (passportnumber.value.trim() === '') {
//             document.getElementById(`passportError_${roomIndex + 1}_adult_${i + 1}`).innerText = 'Please Enter the passport number';
//              passport.style.border = '1px solid red';
//              console.log("pp error")
//              valid = false;
//          }else {
//             passport.style.border = ''; // Reset border style if valid
//             document.getElementById(`passportError_${roomIndex + 1}_adult_${i + 1}`).innerText = '';
//          }
//         }
//     }

//     for (var j = 0; j < room.NoOfChild; j++) {
//         var childFirstName = document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_first_name"]`);
//         var childLastName = document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_last_name"]`);
//         var pannumber = document.querySelector(`[name="room_${roomIndex + 1}_child_${j + 1}_pancard"]`);
//         var passportnumber = document.querySelector(`[name="room_${roomIndex + 1}_child_${i + 1}_passport"]`);

//         if (childFirstName.value.trim() === '') {
//             document.getElementById(`cfirstNameError_${roomIndex + 1}_child_${j + 1}`).innerText = 'Please Enter the first name';
//             childFirstName.style.border = '1px solid red';
//             valid = false;
//         } else {
//             childFirstName.style.border = ''; // Reset border style if valid
//             document.getElementById(`cfirstNameError_${roomIndex + 1}_child_${j + 1}`).innerText = ' ';
//         }

//         if (childLastName.value.trim() === '') {
//             document.getElementById(`clastNameError_${roomIndex + 1}_child_${j + 1}`).innerText = 'Please Enter the last name';
//             childLastName.style.border = '1px solid red';
//             valid = false;
//         } else {
//             childLastName.style.border = ''; // Reset border style if valid
//             document.getElementById(`clastNameError_${roomIndex + 1}_child_${j + 1}`).innerText = ' ';
//         }

//         if(pancard || pancard_book ){
//         if (pannumber.value.trim() === '') {
//             document.getElementById(`pancardError_${roomIndex + 1}_child_${j + 1}`).innerText = 'Please Enter the PAN number';
//             phoneInput.style.border = '1px solid red';
//             valid = false;
//         } 
//         else {
//             phoneInput.style.border = ''; // Reset border style if valid
//         }
//     }
//     if(passport_book || passportv ){
//         if (passportnumber.value.trim() === '') {
//             document.getElementById(`passportError_${roomIndex + 1}_child_${i + 1}`).innerText = 'Please Enter the passport number';
//              passport.style.border = '1px solid red';
//              console.log("pp error")
//              valid = false;
//          }else {
//             passport.style.border = ''; // Reset border style if valid
//          }
//         }
//     }
// });


//     var specialRequest = document.getElementById('req').value;

//     return valid;
// }


