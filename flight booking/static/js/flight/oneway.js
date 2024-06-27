//TIME FILTER ACTIVE
// Ensure JavaScript runs after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get all buttons with the class 'ftime_btn'
    const buttons = document.querySelectorAll('.ftime_btn');

    // Add event listener to each button
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Toggle the 'active' class on the clicked button
            this.classList.toggle('active');
        });
    });

    // adult child count 

    // Get the hidden input value
    var hiddenadult = document.getElementById("hiddenAdultValue").value;
    var hiddenchild = document.getElementById("hiddenChildValue").value;
    var hiddeninfant = document.getElementById("hiddeninfantValue").value;
    var hiddenclass = document.getElementById("hiddenclassValue").value;
    // Get the select element
    var selectadult = document.getElementById("Adult_inp");
    var selectchild = document.getElementById("Child_inp");
    var selectinfant = document.getElementById("Infant_inp");
    var selectclass = document.getElementById("class_inp");
    
    // Set the select element value
    selectadult.value = hiddenadult;
    selectchild.value = hiddenchild;
    selectinfant.value = hiddeninfant;
    selectclass.value = hiddenclass;
});

//  CHECK FARES FUNCTION
document.addEventListener('DOMContentLoaded', function() {
    // Function to update the hidden input
    function updateHiddenInput() {
        const selectedFare = document.querySelector('input[name="fav_language"]:checked').value;
        document.getElementById('selectedFare').value = selectedFare;
    }

    // Get all radio buttons
    const radioButtons = document.querySelectorAll('input[name="fav_language"]');

    // Add event listener to each radio button
    radioButtons.forEach(function(radio) {
        radio.addEventListener('change', updateHiddenInput);
    });

    // Initialize hidden input with the default checked value
    updateHiddenInput();
});


// DIRECT FLIGHTS FUNCTION - ONE TRIP
var checkbox = document.getElementById("flexSwitchCheckDefault");
var resultInput = document.getElementById("resultValue");

// Initialize checkbox based on the hidden input value
checkbox.checked = (resultInput.value === "True");

function updateResult() {
    var formattedValue = checkbox.checked ? "True" : "False";
    resultInput.value = formattedValue;
    console.log("DirectFlight is now: " + formattedValue);
}

// Add an event listener to detect changes
checkbox.addEventListener("change", updateResult);

// Initialize the result input based on the current state of the checkbox
updateResult();

// PAXFORM ONETRIP
// SHOW PAX FORM - ONE TRIP
function showOnePaxForm() {
    var flightForm = document.getElementById("pas_form_onetrip")
    if(flightForm.style.display === "none") {
        flightForm.style.display = "block";
    } else {
        flightForm.style.display = "none"
    }
}

// HIDE PAX FORM - ONE TRIP
function hideOneTripForm() {
    var x = document.getElementById("pas_form_onetrip");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "none";
    }
}

// PAXFORM - ROUND TRIP
// SHOW PAX FORM - ROUND TRIP
function showRoundPaxForm() {
    var flightForm = document.getElementById("pas_form_roundtrip")
    if(flightForm.style.display === "none") {
        flightForm.style.display = "block";
    } else {
        flightForm.style.display = "none"
    }
}

// HIDE PAX FORM - ROUND TRIP
function hideRoundTripForm() {
    var x = document.getElementById("pas_form_roundtrip");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "none";
    }
}

// PAX COUNT SHOW - ONE TRIP
document.addEventListener('DOMContentLoaded', function () {
    // Get select elements
    const adultSelect = document.getElementById('Adult_inp');
    const childSelect = document.getElementById('Child_inp');
    const infantSelect = document.getElementById('Infant_inp');

    // Get input element
    const pasInput = document.getElementById('pasInput');

    // Update input value function
    function updateInputValue() {
        const adults = adultSelect.value;
        const children = childSelect.value;
        const infants = infantSelect.value;
        pasInput.value = `${adults} Adults, ${children} Child, ${infants} Infant`;
    }

    // Listen for changes in select elements
    adultSelect.addEventListener('change', updateInputValue);
    childSelect.addEventListener('change', updateInputValue);
    infantSelect.addEventListener('change', updateInputValue);

    // Initial update
    updateInputValue();
});

// PAX COUNT SHOW - ROUND TRIP
document.addEventListener('DOMContentLoaded', function () {
    // Get select elements
    const adultSelect = document.getElementById('Adult_inp_rt');
    const childSelect = document.getElementById('Child_inp_rt');
    const infantSelect = document.getElementById('Infant_inp_rt');

    // Get input element
    const pasInput = document.getElementById('pasInput_rt');

    // Update input value function
    function updateInputValue() {
        const adults = adultSelect.value;
        const children = childSelect.value;
        const infants = infantSelect.value;
        pasInput.value = `${adults} Adults, ${children} Child, ${infants} Infant`;
    }

    // Listen for changes in select elements
    adultSelect.addEventListener('change', updateInputValue);
    childSelect.addEventListener('change', updateInputValue);
    infantSelect.addEventListener('change', updateInputValue);

    // Initial update
    updateInputValue();
});

// FLIGHT CITY SEARCH - ONE TRIP
$(function () {
    $("#round-to").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/search_destinations_flight/",
                dataType: "json",
                data: {
                    query: request.term
                },
                success: function (data) {
                    response(data.data);
                }
            });
        },
        minLength: 2,
        select: function (event, ui) {
            // Update the hidden input fields with selected values
            $("#tcitycodeInput").val(ui.item.cityCode);
            $("#tairportCodeInput").val(ui.item.AirportCode);
            $("#tcitynmae").val(ui.item.CityName);
        }
    });
});

$(function () {
    $("#round-from").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/search_destinations_flight/",
                dataType: "json",
                data: {
                    query: request.term
                },
                success: function (data) {
                    response(data.data);
                }
            });
        },
        minLength: 2,
        select: function (event, ui) {
            // Update the hidden input fields with selected values
            $("#FcitycodeInput").val(ui.item.cityCode);
            $("#FairportCodeInput").val(ui.item.AirportCode);
            $("#Fcityname").val(ui.item.CityName);
        }
    });
});

// FLIGHT CITY SEARCH - ROUND TRIP
$(function () {
    var fromCityCode = '';
    $("#onetripfrom").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/search_destinations_flight/",
                dataType: "json",
                data: {
                    query: request.term
                },
                success: function (data) {
                    response(data.data);
                }
            });
        },
        minLength: 2,
        select: function (event, ui) {
            fromCityCode = ui.item.cityCode;
            $("#citycodeInput").val(ui.item.cityCode);
            $("#airportCodeInput").val(ui.item.AirportCode);
            $("#aircityname").val(ui.item.CityName);
            
            // Clear TO input when FROM input changes
            $("#onetripto").val('');
            $("#tocitycodeInput").val('');
            $("#toairportCodeInput").val('');
            $("#toaircityname").val('');
        }
    });

    $("#onetripto").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/search_destinations_flight/",
                dataType: "json",
                data: {
                    query: request.term
                },
                success: function (data) {
                    // Filter out the city that is selected in the "FROM" input
                    var filteredData = data.data.filter(function(item) {
                        return item.cityCode !== fromCityCode;
                    });
                    response(filteredData);
                }
            });
        },
        minLength: 2,
        select: function (event, ui) {
            if (ui.item.cityCode === fromCityCode) {
                alert("The destination city cannot be the same as the departure city.");
                event.preventDefault();
                $(this).val('');
                return false;
            }
            $("#tocitycodeInput").val(ui.item.cityCode);
            $("#toairportCodeInput").val(ui.item.AirportCode);
            $("#toaircityname").val(ui.item.CityName);
        }
    });
});


// FILTER FUNCTIONS TOP - ONE TRIP
function sortFlight(criteria) {
    var flightLists = document.querySelectorAll('#flightlist');

    flightLists.forEach(function(flightList) {
        var flights = Array.from(flightList.querySelectorAll('.flight-container'));

        var sortOrder = flightList.getAttribute('data-sort-order') || 'asc';

        flights.sort(function(a, b) {
            var aValue, bValue;

            if (criteria === 'Price') {
                console.log("Price")
                aValue = parseFloat(a.getAttribute('ticket-price'));
                bValue = parseFloat(b.getAttribute('ticket-price'));
            } else if (criteria === 'Duration') {
                var aDuration = a.getAttribute('ticket-duration-time');
                var bDuration = b.getAttribute('ticket-duration-time');
                return sortOrder === 'asc' ? aDuration.localeCompare(bDuration) : bDuration.localeCompare(aDuration);
            } else if (criteria === 'Departure') {
                var aDeparture = a.getAttribute('flight-departure-time');
                var bDeparture = b.getAttribute('flight-departure-time');
                return sortOrder === 'asc' ? aDeparture.localeCompare(bDeparture) : bDeparture.localeCompare(aDeparture);
            } else if (criteria === 'Arrival') {
                var aArrival = a.getAttribute('flight-arrival-time');
                var bArrival = b.getAttribute('flight-arrival-time');
                return sortOrder === 'asc' ? aArrival.localeCompare(bArrival) : bArrival.localeCompare(aArrival);
            } else if (criteria === 'Name') {
                var aName = a.getAttribute('flight-name');
                var bName = b.getAttribute('flight-name');
                return sortOrder === 'asc' ? aName.localeCompare(bName) : bName.localeCompare(aName);
            }

            return sortOrder === 'asc' ? aValue - bValue : bValue - aValue;
        });

        flightList.innerHTML = '';

        flights.forEach(function(flight) {
            flightList.appendChild(flight);
        });

        flightList.setAttribute('data-sort-order', sortOrder === 'asc' ? 'desc' : 'asc');
    });
}


//   flight time based filter
$(document).ready(function () {
    $(".ftime_btn").click(function () {
        var selectedTime = $(this).text().trim();
        var timeType = $(this).attr("for").split("-")[0]; // "departure" or "arrival"

        // Hide all flights
        $(".flight-container").hide();

        // Show flights based on selected time
        $(".flight-container").each(function () {
            var timeAttr;
            if (timeType === "departure") {
                timeAttr = $(this).attr("flight-departure-time");
            } else if (timeType === "arrival") {
                timeAttr = $(this).attr("flight-arrival-time");
            }

            if (timeAttr && isTimeInRange(timeAttr, selectedTime)) {
                $(this).show();
            }
        });
    });

    // Function to check if a given time is in the selected range
    function isTimeInRange(flightTime, selectedTime) {
        var selectedHour = parseInt(selectedTime.split(":")[0], 10);
        var flightHour = parseInt(flightTime.split(":")[0], 10);

        return (selectedTime.includes("Before 6AM") && flightHour < 6) ||
            (selectedTime.includes("6AM-12PM") && flightHour >= 6 && flightHour < 12) ||
            (selectedTime.includes("12PM-6PM") && flightHour >= 12 && flightHour < 18) ||
            (selectedTime.includes("After 6PM") && flightHour >= 18);
    }
});

// FLIGHT LISTS - ONE TRIP_________________________________________


const rangeInput = document.querySelectorAll(".range-input input"),
priceInput = document.querySelectorAll(".price-input input"),
range = document.querySelector(".slider .progress");
let priceGap = 1000;

priceInput.forEach(input =>{
    input.addEventListener("input", e =>{
        let minPrice = parseInt(priceInput[0].value),
        maxPrice = parseInt(priceInput[1].value);
        
        if((maxPrice - minPrice >= priceGap) && maxPrice <= rangeInput[1].max){
            if(e.target.className === "input-min"){
                rangeInput[0].value = minPrice;
                range.style.left = ((minPrice - rangeInput[0].min) / (rangeInput[0].max - rangeInput[0].min)) * 100 + "%";
            }else{
                rangeInput[1].value = maxPrice;
                range.style.right = ((rangeInput[1].max - maxPrice) / (rangeInput[1].max - rangeInput[1].min)) * 100 + "%";
            }
        }
    });
});

rangeInput.forEach(input =>{
    input.addEventListener("input", e =>{
        RangeSlider()
        
    });
});

$( document ).ready(function() {
    RangeSlider()
});

function RangeSlider() {
    let minVal = parseInt(rangeInput[0].value),
    maxVal = parseInt(rangeInput[1].value);
    filterHotelsByPrice(minVal,maxVal)
    console.log(minVal,maxVal)
    if((maxVal - minVal) < priceGap){
        if(e.target.className === "range-min"){
            rangeInput[0].value = Math.min(maxVal - priceGap, rangeInput[0].max);
        }else{
            rangeInput[1].value = Math.max(minVal + priceGap, rangeInput[1].min);
        }
    }else{
        priceInput[0].value = minVal;
        priceInput[1].value = maxVal;
        range.style.left = ((minVal - rangeInput[0].min) / (rangeInput[0].max - rangeInput[0].min)) * 100 + "%";
        range.style.right = ((rangeInput[1].max - maxVal) / (rangeInput[1].max - rangeInput[1].min)) * 100 + "%";
    }
}

function filterHotelsByPrice(minPrice,maxPrice) {
    // priceInput = document.querySelectorAll(".price-input input")
    // var minPrice = parseInt(priceInput[0].value);
    // var maxPrice = parseInt($(".input-max").val());

     console.log("Filtering by Price:", minPrice, maxPrice);

     $(".flight").each(function () {
         var hotelPrice = parseInt($(this).data("price"));

         console.log("Hotel Price:", hotelPrice);

         if (hotelPrice >= minPrice && hotelPrice <= maxPrice) {
             $(this).show();
         } else {
             $(this).hide();
         }
     });
}
// AIRLINE NAME FILTER FUNCTIONS
document.querySelectorAll('.name_check').forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
        updateFlightList();
    });
});

function updateFlightList() {
    var selectedAirlines = Array.from(document.querySelectorAll('.name_check:checked'))
        .map(function (checkbox) {
            return checkbox.getAttribute('data-airline').toLowerCase(); // Convert to lowercase
        });

    document.querySelectorAll('.flight-container').forEach(function (flight) {
        var airlineName = flight.getAttribute('flight-name');
        if (airlineName) {
            airlineName = airlineName.toLowerCase(); // Convert to lowercase
            if (selectedAirlines.length === 0 || selectedAirlines.includes(airlineName)) {
                flight.style.display = 'block';
            } else {
                flight.style.display = 'none';
            }
        } else {
            flight.style.display = 'none'; // Handle case where flight-name attribute is missing
        }
    });
}

// REfund filter
document.querySelectorAll('.refund_check').forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
        refundFlightList();
    });
});

function refundFlightList() {
    var selectedAirlines = Array.from(document.querySelectorAll('.refund_check:checked'))
        .map(function (checkbox) {
            return checkbox.getAttribute('data-refund').toLowerCase(); // Convert to lowercase
        });

    document.querySelectorAll('.flight-container').forEach(function (flight) {
        var airlineName = flight.getAttribute('flight-refund');
        if (airlineName) {
            airlineName = airlineName.toLowerCase(); // Convert to lowercase
            if (selectedAirlines.length === 0 || selectedAirlines.includes(airlineName)) {
                flight.style.display = 'block';
            } else {
                flight.style.display = 'none';
            }
        } else {
            flight.style.display = 'none'; // Handle case where flight-name attribute is missing
        }
    });
}

// FLIGHT STOP FILTER FUNCTIONS
document.querySelectorAll('.form-check-inputs').forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
        updateFlightLists();
    });
});

function updateFlightLists() {
    var selectedAirlinesClass = Array.from(document.querySelectorAll('.form-check-inputs:checked'))
        .map(function (checkbox) {
            return checkbox.getAttribute('data-stops').toLowerCase(); // Convert to lowercase
        });

    document.querySelectorAll('.flight-container').forEach(function (flight) {
        var airlineClass = flight.getAttribute('flight-stop'); // Corrected attribute names
        if (airlineClass) {
            airlineClass = airlineClass.toLowerCase(); // Convert to lowercase
            if (selectedAirlinesClass.length === 0 || selectedAirlinesClass.includes(airlineClass)) {
                flight.style.display = 'block';
            } else {
                flight.style.display = 'none';
            }
        } else {
            flight.style.display = 'none'; // Handle case where flight-stop or flight-stops attribute is missing
        }
    });
}

// SUBMIT FORM
function submitOneTripForm() {
    if(validateOneTripForm()){
        document.getElementById("one-trip").submit();
       console.log("submitted ot")
    }
}

// VALIDATE FORM - ONE TRIP
function validateOneTripForm() {
    var from = document.getElementById("onetripfrom").value;
    var to = document.getElementById("onetripto").value;
    if (from === "") {
        alert("Please Enter From");
        return false; // Prevent form submission
    } 
        if (to === "") {
        alert("Please Enter To");
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}

// flight list

const FLightL = document.getElementById('flight_details').textContent;
// Parse the JSON string
const flights = JSON.parse(FLightL);
let jsonData = flights
console.log("flight details",jsonData)
const combinedFlightMap = {};

jsonData.forEach(flight => {
    const combinedKey = flight.AirlineNumber + '-' + flight.SAirlineNumber;
    if (!combinedFlightMap[combinedKey]) {
        combinedFlightMap[combinedKey] = [];
    }
    combinedFlightMap[combinedKey].push(flight);
});

const groupedFlights = Object.values(combinedFlightMap);

console.log(groupedFlights);

// Example usage:
let flightDataArray = groupedFlights;
// console.log("Flight Data Array:", flightDataArray);
var jsonString = JSON.stringify(flightDataArray);
document.querySelector('[name="Sort_F_details"]').value = jsonString;



document.addEventListener("DOMContentLoaded", function() {
    let flightsByNumberJSON = document.getElementById('Sort_F_details').value;
    var flightsByNumber = JSON.parse(flightsByNumberJSON);
    // console.log(flightsByNumber);

    const flightsContainer = document.getElementById("flightlist");
    const staticUrl = document.getElementById("static-url").dataset.staticUrl;
    const token_id_value = document.getElementById("token_id_fare").value;

    // Loop through each array and create a details container for each
    flightsByNumber.forEach((array, index) => {
    // const arrayDiv = document.createElement('div');
    // arrayDiv.classList.add('details-container');

    // Create HTML for details of the first object in the array
    const flight = array[0];
    const priceContainerHTML = array.map(flight => {
        return `<div class="col-lg-4 mb-2 fo-opt-div border-all bg-white shadows">
                    <div class="py-1 b_bot">
                        <span class="fw-bold black">₹ ${flight.OffredFare}</span>
                        <span class="fs-12">per adult</span>
                        <p class="fs-12 mb-0">${flight.AirlineType} / ${flight.FlightClass}</p>
                    </div>
                    <div class="py-1">
                        <p class="fs-13 mb-0">
                            <b>Baggage</b></p>
                        <ul class="mb-2">
                            <li>
                                <span class="fs-12">7 Kgs Cabin
                                    Baggage</span>
                            </li>
                            <li>
                                <span class="fs-12">15 Kgs
                                    Check-in Baggage</span>
                            </li>
                        </ul>
                        <p class="fs-13 mb-0">
                            <b>Flexibility</b></p>
                        <ul class="mb-2">
                            <li>
                                <span class="fs-12">Cancellation
                                    fee starts at ₹ 3,100 (up to 4 days before
                                    departure)</span>
                            </li>
                            <li>
                                <span class="fs-12">Date Change
                                    fee starts at ₹ 2,850 (up to 4 days before
                                    departure)</span>
                            </li>
                        </ul>
                        <p class="fs-13 mb-0"><b>Seats,
                                Meals &amp; More</b></p>
                        <ul class="mb-2">
                            <li>
                                <span class="fs-12">Chargeable
                                    Seats</span>
                            </li>
                            <li>
                                <span
                                    class="fs-12">Chargeable
                                    Meals</span>
                            </li>
                        </ul>
                    </div>
                    <div class="mb-2">
                        <button type="button" class="bg-theme white py-1 px-5 rounded-pill select-btn price-class" data-flight="${flight.ResultIndex}" onclick="handleSelectFlight('${token_id_value}','${encodeURIComponent(JSON.stringify(flight))}')">SELECT</button>
                    </div>
                </div>
               `;
    }).join('');

    let flightHTML;
    if(flight.Stopconformation === 'Non-stop') {
        flightHTML = ` <div  class="flight-container flight flight-full" data-price="${flight.OffredFare}" ticket-price="${flight.OffredFare}" flight-name="${flight.AirlineName}" flight-refund="${flight.nonrefund}"
                ticket-duration-time="${flight.total_hour}:${flight.totalminute}"   flight-departure-time="${flight.departurehoure}:${flight.departureminute}" flight-arrival-time="${flight.arrivalhoure}:${flight.arrivalminute}" Flight-stop="${flight.Stopconformation}">
                        <div class="item mb-2 border-all shadows p-2 px-2 rounded">
                            <div class="row d-flex align-items-center justify-content-between">
                                <div class="col-lg-3 col-md-3 col-sm-12">
                                    <div class="item-inner-image text-start">
                                        <img src="${staticUrl}${flight.AirlineCode}.gif" alt="Flight-logo" style="width: 65px;height: 60px;border-radius: 4px;">
                                        <p class="mb-0 fw-bold theme2 fs-19">${flight.AirlineName} | ${flight.AirlineCode}-${flight.AirlineNumber}</p>
                                        <small>${flight.AirlineType} / ${flight.FlightClass}</small>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner">
                                        <div class="content">
                                        <h5 class="mb-0">${flight.OrginAirportCode}</h5>
                                            <p class="mb-0">${flight.departure_H_M}</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner">
                                        <div class="content">
                                            <p class="mb-0 fw-bold theme2"><i class="fa fa-clock-o" aria-hidden="true"></i> ${flight.total_H_M}</p>
                                            <p class="mb-0 fs-14 text-uppercase">${flight.Stopconformation}</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner flight-time">
                                        <h5 class="mb-0">${flight.DestinationAirportCode}</h5>
                                        <p class="mb-0">${flight.arrival_H_M}</p>
                                    </div>
                                </div>
                                <div class="col-lg-3 col-md-3 col-sm-12">
                                    <div class="item-inner text-end">
                                        <p class="theme2 fs-4 fw-bold mb-1">₹ ${flight.OffredFare}</p>
                                        <button type="button" class="nir-btn py-1 rounded-pill mb-1 book-btn book-button1"  data-trace-id="${flight.TraceId}" data-result-index="${flight.ResultIndex}" onclick="handleSelectFlight('${ flight.TraceId }', '${ flight.ResultIndex }','${token_id_value}','${flight.Stopconformation}','${flight.FlightClass}','${flight.start_date}','${flight.total_H_M}','${flight.OrginAirportCode}','${flight.DestinationAirportCode}','${flight.AirlineCode}')">Book Now</button>
                                    </div>
                                </div>
                                <div class="col-lg-12">
                                    <div class="accordion accordion-flush border-t mt-1 pt-1" id="accordionflush">
                                        <div class="accordion-item overflow-hidden">    
                                            <div class="justify-content-between">
                                                <button
                                                    class="accordion-button collapsed bg-white fw-bold border-0 theme flight-btn"
                                                    style="font-size: 14px;" type="button" data-bs-toggle="collapse"
                                                    data-bs-target="#${flight.ResultIndex}flush-collapseOne" aria-expanded="false"
                                                    aria-controls="flush-collapseOne" id="${flight.ResultIndex}01" >Flight Details <i
                                                        class="fa fa-caret-down theme" aria-hidden="true"></i></button>
                                                <button type="button"
                                                    class="bg-white float-end theme rounded-pill morefare-btn more-btn"
                                                    data-bs-toggle="modal" data-bs-target="#${flight.ResultIndex}morefarePop" id="${flight.ResultIndex}2"> + More Fare</button>
                                            </div>
                                            <div class="modal fade" id="${flight.ResultIndex}morefarePop" tabindex="-1" role="dialog"
                                                aria-labelledby="exampleModalLabel" aria-hidden="true">
                                                <div class="modal-dialog" role="document"
                                                    style="max-width: 1020px;top: 10%;">
                                                    <div class="modal-content fo-pop-head">
                                                        <div class="modal-header shadows px-4">
                                                            <h4 class="modal-title theme" id="exampleModalLabel">More
                                                                Fare Options Available</h4>
                                                            <button type="button" class="btn-close"
                                                                data-bs-dismiss="modal" aria-label="Close"></button>
                                                        </div>
                                                        <div class="modal-body fo-pop-div" id="${flight.ResultIndex}3">
                                                            <div class="text-center mb-2">
                                                                <span>
                                                                    <span class="fw-bold black">${flight.OrginAirportCityName}, ${flight.OrginAirportCoutryName} → ${flight.DestinationCityName}, ${flight.DestinationCountryName}</span>
                                                                    <span class="ms-3 fs-14 black">${flight.AirlineName} · Departure at ${flight.departure_H_M} - Arrival at ${flight.arrival_H_M}</span>
                                                                </span>
                                                            </div>
                                                            <div class="f-options row">
                                                                ${priceContainerHTML}
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            
                                            <div id="${flight.ResultIndex}flush-collapseOne" class="accordion-collapse collapse mt-2"
                                                aria-labelledby="flush-headingOne"
                                                data-bs-parent="#accordionFlushExample">
                                                <div class="accordion-body p-0"  id="${flight.ResultIndex}4">
                                                    <ul class="nav nav-pills mb-3 bg-grey rounded-pill" id="pills-tab"
                                                        role="tablist">
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link active fo-btn rounded-pill"
                                                                id="${flight.ResultIndex}pills-fd1-tab" data-bs-toggle="pill"
                                                                data-bs-target="#${flight.ResultIndex}pills-fd1" type="button" role="tab"
                                                                aria-controls="${flight.ResultIndex}pills-fd1" aria-selected="true">Flight
                                                                Detailes</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="${flight.ResultIndex}pills-fd2-tab" data-bs-toggle="pill"
                                                                data-bs-target="#${flight.ResultIndex}pills-fd2" type="button" role="tab"
                                                                aria-controls="${flight.ResultIndex}pills-fd2" aria-selected="false" onclick="addPassengerDetails('${flight.ResultIndex}', '${encodeURIComponent(JSON.stringify(flight.passenger_details))}')">Fare
                                                                Summary</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="${flight.ResultIndex}pills-fd3-tab" data-bs-toggle="pill"
                                                                data-bs-target="#${flight.ResultIndex}pills-fd3" type="button" role="tab"
                                                                aria-controls="${flight.ResultIndex}pills-fd3" aria-selected="false">Fare
                                                                Rules</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="${flight.ResultIndex}pills-fd4-tab" data-bs-toggle="pill"
                                                                data-bs-target="#${flight.ResultIndex}pills-fd4" type="button" role="tab"
                                                                aria-controls="${flight.ResultIndex}pills-fd4" aria-selected="false">Baggage
                                                                Info</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <i class="fa fa-times closefo-btn" aria-hidden="true"></i>
                                                        </li>
                                                    </ul>
                                                    <div class="tab-content" id="pills-tabContent">
                                                        <div class="tab-pane fade show active" id="${flight.ResultIndex}pills-fd1"
                                                            role="tabpanel" aria-labelledby="pills-fd1-tab"
                                                            tabindex="0">
                                                            <div class="row">
                                                                <div class="col-lg-3 align-items-center">
                                                                    <img src="${staticUrl}${flight.AirlineCode}.gif" alt="Flight-logo" style="width: 50px; height: 50px; border-radius:2px;">
                                                                    <p class="mb-0 fw-bold theme2">${flight.AirlineName} | ${flight.AirlineCode}-${flight.AirlineNumber}</p>
                                                                    <small class="mb-0 fs-13"> ${flight.AirlineType} / ${flight.FlightClass}</small>
                                                                </div> 
                                                                <div class="col-lg-7">
                                                                    <div class="d-flex align-items-center justify-content-between">
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold black">(${flight.OrginAirportCode}) ${flight.OrginAirportName}</p>
                                                                            <p class="mb-0 fs-12">${flight.OrginAirportCityName}, ${flight.OrginAirportCoutryName}</p>
                                                                            <p class="mb-0 fs-12">Terminal: ${flight.OrginAirportTerminal}</p>
                                                                            <p class="mb-0 fs-14 fw-bold">${flight.departure_H_M}</p>
                                                                        </div>
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold rounded-pill px-3 shadows theme dur-time">${flight.total_H_M}</p>
                                                                        </div>
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold black">(${flight.DestinationAirportCode}) ${flight.DestinationAirportName}</p>
                                                                            <p class="mb-0 fs-12">${flight.DestinationCityName}, ${flight.DestinationCountryName}</p>
                                                                            <p class="mb-0 fs-12">Terminal: ${flight.DestinationTerminal}</p>
                                                                            <p class="mb-0 fs-14 fw-bold">${flight.arrival_H_M}</p>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="col-lg-2 my-auto text-center">
                                                                    <p class="mb-0 fs-14 theme2 fw-bold">${flight.nonrefund}</p>
                                                                    <p class="mb-0 fs-13">Seat Left: ${flight.setsAvailable}</p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="tab-pane fade" id="${flight.ResultIndex}pills-fd2" role="tabpanel"
                                                            aria-labelledby="pills-fd2-tab" tabindex="0"> 
                                                            <table class="table text-start fs-12" id="${flight.ResultIndex}passengerTable">
                                                                <thead>
                                                                    <tr>
                                                                        <th>TYPE</th>
                                                                        <th>BASE FARE</th>
                                                                        <th>TAXES &amp; FEES</th>
                                                                        <th>TOTAL</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    
                                                                <tr>
                                                                    <td></td>
                                                                    <td></td>
                                                                    <td>Total</td>
                                                                    <td><span>${flight.PublishedFare}</span>
                                                                    <span>-${flight.discount1 + flight.discount2}</span>
                                                                    <span>${flight.discount1 + flight.discount2 - flight.PublishedFare }</span>
                                                                    </td>

                                                                    </tr>
                                                                </tbody>
                                                                
                                                            </table>
                                                        </div>
                                                        <div class="tab-pane fade" id="${flight.ResultIndex}pills-fd3" role="tabpanel"
                                                            aria-labelledby="pills-fd3-tab" tabindex="0">
                                                            <div class="text-end">
                                                                
                                                                <button type="button"
                                                    class="book-btn book-btn1 bg-white theme rounded-pill v-fare-btn mb-1"
                                                    data-bs-toggle="modal" data-bs-target="#${ flight.ResultIndex}010morefarePop" id="${flight.ResultIndex}2" result-index="${flight.ResultIndex}" onclick="show_fare_details('${token_id_value}','${ flight.TraceId }','${flight.ResultIndex}' )" >View Fare Rule</button>
                                                            </div>
                                                            <table class="table text-start fs-12">
                                                                <thead>
                                                                    <tr>
                                                                        <th>SECTOR</th>
                                                                        <th>TIME FRAME</th>
                                                                        <th>CHARGES & DISCRIPTION</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="f-code">${flight.OrginAirportCode} - ${flight.DestinationAirportCode}</td>
                                                                        <td>From & Above Before Dept</td>
                                                                        <td>INR 4000* + 0</td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                            <div class="modal fade" id="${ flight.ResultIndex}010morefarePop" tabindex="-1" role="dialog"
                                                                aria-labelledby="exampleModalLabel" aria-hidden="true">
                                                                <div class="modal-dialog" role="document"
                                                                    style="max-width: 1020px;top: 10%;">
                                                                    <div class="modal-content fo-pop-head">
                                                                        <div class="modal-header shadows px-4">
                                                                            <h4 class="modal-title theme" id="exampleModalLabel">Fare Rule Details</h4>
                                                                            <button type="button" class="btn-close"
                                                                                data-bs-dismiss="modal" aria-label="Close"></button>
                                                                        </div>
                                                                        <div class="modal-body fo-pop-div" id="${flight.ResultIndex}3">
                                                                            <div class="modal-body">
                                                                            <div id="${ flight.ResultIndex}00">

                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            </div>
                                                        </div>
                                                        <div class="tab-pane fade" id="${flight.ResultIndex}pills-fd4" role="tabpanel"
                                                            aria-labelledby="pills-fd4-tab" tabindex="0">
                                                            <table class="table text-start fs-12">
                                                                <thead>
                                                                    <tr>
                                                                        <th>SECTOR</th>
                                                                        <th>CHECK IN</th>
                                                                        <th>CABIN</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="f-code">${flight.OrginAirportCode} - ${flight.DestinationAirportCode}</td>
                                                                        <td>${flight.checkinbag} / Person</td>
                                                                        <td>${flight.combainbag} / Person</td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>  `;
            
    } else if (flight.Stopconformation === '1-stop(s)'){
        flightHTML =`<div  class="flight-container flight flight-full" data-price="${flight.OffredFare}" ticket-price="${flight.OffredFare}" flight-name="${flight.FirstAirlineName}" flight-refund="${flight.onerefund}"
                ticket-duration-time="${flight.final_total_hours}:${flight.final_total_minutes}"   flight-departure-time="${flight.Firstdeparturehoure}:${flight.Firstdepartureminute}" flight-arrival-time="${flight.Firstarrivalhoure}:${flight.Firstarrivalminute}" Flight-stop="${flight.Stopconformation}">
                        <div class="item mb-2 border-all shadows p-2 px-2 rounded">
                            <div class="row d-flex align-items-center justify-content-between">
                                <div class="col-lg-3 col-md-3 col-sm-12">
                                    <div class="item-inner-image text-start">
                                        <img src="${staticUrl}${ flight.FirstAirlineCode }.gif" alt="Flight-logo" style="width: 65px;height: 60px;border-radius: 4px;">
                                        <p class="mb-0 fw-bold theme2 fs-19">${flight.FirstAirlineName} | ${flight.FirstAirlineCode}-${flight.AirlineNumber}</p>
                                        <small>${flight.AirlineType} / ${flight.FlightClass}</small>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner">
                                        <div class="content">
                                        <h5 class="mb-0">${flight.FristOrginAirportCode}</h5>
                                            <p class="mb-0">${flight.Firstdepartur_H_M}</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner">
                                        <div class="content">
                                            <p class="mb-0 fw-bold theme2"><i class="fa fa-clock-o" aria-hidden="true"></i> ${flight.FinalTotal_H_M}</p>
                                            <p class="mb-0 fs-14 text-uppercase">${flight.Stopconformation}</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner flight-time">
                                        <h5 class="mb-0">${flight.SecondDestinationAirportCode}</h5>
                                        <p class="mb-0">${flight.Scondarrival_H_M}</p>
                                    </div>
                                </div>
                                <div class="col-lg-3 col-md-3 col-sm-12">
                                    <div class="item-inner text-end">
                                        <p class="theme2 fs-4 fw-bold mb-1">₹ ${flight.OffredFare}</p>
                                        <button type="button" class="nir-btn py-1 rounded-pill mb-1 book-btn book-button1"  data-trace-id="${flight.TraceId}" data-result-index="${flight.ResultIndex}" onclick="handleSelectFlight('${token_id_value}','${encodeURIComponent(JSON.stringify(flight))}')">Book Now</button>
                                    </div>
                                </div>
                                <div class="col-lg-12">
                                    <div class="accordion accordion-flush border-t mt-1 pt-1" id="accordionflush">
                                        <div class="accordion-item overflow-hidden">
                                            <div class="justify-content-between">
                                                <button
                                                    class="accordion-button collapsed bg-white fw-bold border-0 theme flight-btn"
                                                    style="font-size: 14px;" type="button" data-bs-toggle="collapse"
                                                    data-bs-target="#${flight.ResultIndex}flush-collapseOne" aria-expanded="false"
                                                    aria-controls="${flight.ResultIndex}flush-collapseOne" id="${flight.ResultIndex}01" >Flight Details <i
                                                        class="fa fa-caret-down theme" aria-hidden="true"></i></button>
                                                <button type="button"
                                                    class="bg-white float-end theme rounded-pill morefare-btn more-btn"
                                                    data-bs-toggle="modal" data-bs-target="#${flight.ResultIndex}morefarePop" id="${flight.ResultIndex}02"> + More Fare</button>
                                            </div>
                                            <div class="modal fade" id="${flight.ResultIndex}morefarePop" tabindex="-1" role="dialog"
                                                aria-labelledby="exampleModalLabel" aria-hidden="true">
                                                <div class="modal-dialog" role="document"
                                                    style="max-width: 1020px;top: 10%;">
                                                    <div class="modal-content fo-pop-head">
                                                        <div class="modal-header shadows px-4">
                                                            <h4 class="modal-title theme" id="exampleModalLabel">More
                                                                Fare Options Available</h4>
                                                            <button type="button" class="btn-close"
                                                                data-bs-dismiss="modal" aria-label="Close"></button>
                                                        </div>
                                                        <div class="modal-body fo-pop-div" id="${flight.ResultIndex}02">
                                                            <div class="text-center mb-2">
                                                                <span>
                                                                    <span class="fw-bold black">${flight.FristOrginAirportCityName}, ${flight.FristOrginAirportCoutryName} → ${flight.FristDestinationCityName}, ${flight.FristDestinationCountryName}</span>
                                                                    <span class="ms-3 fs-14 black">${flight.FirstAirlineName} · Departure at ${flight.Firstdepartur_H_M} - Arrival at ${flight.Firstarrival_H_M}</span>
                                                                </span>
                                                                
                                                            </div>
                                                            <div class="text-center mb-2">
                                                            <span>
                                                                    <span class="fw-bold black">${flight.SecondOrginAirportCityName}, ${flight.SecondOrginAirportCoutryName} → ${flight.SecondDestinationCityName}, ${flight.SecondDestinationCountryName}</span>
                                                                    <span class="ms-3 fs-14 black">${flight.SecondAirlineName} · Departure at ${flight.Sconddeparture_H_M} - Arrival at ${flight.Scondarrival_H_M} </span>
                                                                </span>
                                                            </div>
                                                            <div class="f-options row">
                                                                ${priceContainerHTML}
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            
                                            <div id="${flight.ResultIndex}flush-collapseOne" class="accordion-collapse collapse mt-2"
                                                aria-labelledby="flush-headingOne"
                                                data-bs-parent="#accordionFlushExample">
                                                <div class="accordion-body p-0"  id="${flight.ResultIndex}01">
                                                    <ul class="nav nav-pills mb-3 bg-grey rounded-pill" id="pills-tab"
                                                        role="tablist">
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link active fo-btn rounded-pill"
                                                                id="${flight.ResultIndex}pills-fd1-tab" data-bs-toggle="pill"
                                                                data-bs-target="#${flight.ResultIndex}pills-fd1" type="button" role="tab"
                                                                aria-controls="${flight.ResultIndex}pills-fd1" aria-selected="true">Flight
                                                                Detailes</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="${flight.ResultIndex}pills-fd2-tab" data-bs-toggle="pill"
                                                                data-bs-target="#${flight.ResultIndex}pills-fd2" type="button" role="tab"
                                                                aria-controls="${flight.ResultIndex}pills-fd2" aria-selected="false" onclick="addPassengerDetails('${flight.ResultIndex}', '${encodeURIComponent(JSON.stringify(flight.passenger_details))}')">Fare Summary</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="${flight.ResultIndex}pills-fd3-tab" data-bs-toggle="pill"
                                                                data-bs-target="#${flight.ResultIndex}pills-fd3" type="button" role="tab"
                                                                aria-controls="${flight.ResultIndex}pills-fd3" aria-selected="false">Fare
                                                                Rules</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="${flight.ResultIndex}pills-fd4-tab" data-bs-toggle="pill"
                                                                data-bs-target="#${flight.ResultIndex}pills-fd4" type="button" role="tab"
                                                                aria-controls="${flight.ResultIndex}pills-fd4" aria-selected="false">Baggage
                                                                Info</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <i class="fa fa-times closefo-btn" aria-hidden="true"></i>
                                                        </li>
                                                    </ul>
                                                    <div class="tab-content" id="pills-tabContent">
                                                        <div class="tab-pane fade show active" id="${flight.ResultIndex}pills-fd1"
                                                            role="tabpanel" aria-labelledby="${flight.ResultIndex}pills-fd1-tab"
                                                            tabindex="0">
                                                            <div class="row">
                                                                <div class="col-lg-3 align-items-center">
                                                                    <img src="${staticUrl}${ flight.FirstAirlineCode }.gif" alt="Flight-logo" style="width: 50px; height: 50px; border-radius:2px;">
                                                                    
                                                                    <p class="mb-0 fw-bold theme2">${flight.FirstAirlineName} | ${flight.FirstAirlineCode}-${flight.AirlineNumber}</p>
                                                                    <small class="mb-0 fs-13"> ${flight.AirlineType} / ${flight.FlightClass}</small>
                                                                </div> 
                                                                <div class="col-lg-7">
                                                                    <div class="d-flex align-items-center justify-content-between">
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold black">(${flight.FristOrginAirportCode}) ${flight.FristOrginAirportName}</p>
                                                                            <p class="mb-0 fs-12">${flight.FristOrginAirportCityName}, ${flight.FristOrginAirportCoutryName}</p>
                                                                            <p class="mb-0 fs-12">Terminal: ${flight.FristOrginAirportTerminal}</p>
                                                                            <p class="mb-0 fs-14 fw-bold">${flight.Firstdepartur_H_M}</p>
                                                                        </div>
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold rounded-pill px-3 shadows theme dur-time">${flight.Firsttotal_H_M}</p>
                                                                        </div>
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold black">(${flight.FristDestinationAirportCode}) ${flight.FristDestinationAirportName}</p>
                                                                            <p class="mb-0 fs-12">${flight.FristDestinationCityName}, ${flight.FristDestinationCountryName}</p>
                                                                            <p class="mb-0 fs-12">Terminal: ${flight.FristDestinationTerminal}</p>
                                                                            <p class="mb-0 fs-14 fw-bold">${flight.Firstarrival_H_M}</p>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="col-lg-2 my-auto text-center">
                                                                    <p class="mb-0 fs-14 theme2 fw-bold">${flight.onerefund}</p>
                                                                    <p class="mb-0 fs-13">Seat Left: ${flight.FristsetsAvailable}</p>
                                                                </div>
                                                            </div>
                                                            <div class="row">
                                                                <div class="col-lg-3 align-items-center">
                                                                    <img src="${staticUrl}${ flight.SecondAirlineCode }.gif" alt="Flight-logo" style="width: 50px; height: 50px; border-radius:2px;">
                                                                    <p class="mb-0 fw-bold theme2">${flight.SecondAirlineName} | ${flight.SecondAirlineCode}-${flight.SAirlineNumber}</p>
                                                                    <small class="mb-0 fs-13"> ${flight.AirlineType} / ${flight.SecondFlightClass}</small>
                                                                </div> 
                                                                <div class="col-lg-7">
                                                                    <div class="d-flex align-items-center justify-content-between">
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold black">(${flight.SecondOrginAirportCode}) ${flight.SecondOrginAirportName}</p>
                                                                            <p class="mb-0 fs-12">${flight.SecondOrginAirportCityName}, ${flight.SecondOrginAirportCoutryName}</p>
                                                                            <p class="mb-0 fs-12">Terminal: ${flight.SecondOrginAirportTerminal}</p>
                                                                            <p class="mb-0 fs-14 fw-bold">${flight.Sconddeparture_H_M}</p>
                                                                        </div>
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold rounded-pill px-3 shadows theme dur-time">${flight.Scondtotal_H_M}</p>
                                                                        </div>
                                                                        <div>
                                                                            <p class="mb-0 fs-14 fw-bold black">(${flight.SecondDestinationAirportCode}) ${flight.SecondDestinationAirportName}</p>
                                                                            <p class="mb-0 fs-12">${flight.SecondDestinationCityName}, ${flight.SecondDestinationCountryName}</p>
                                                                            <p class="mb-0 fs-12">Terminal: ${flight.SecondDestinationTerminal}</p>
                                                                            <p class="mb-0 fs-14 fw-bold">${flight.Scondarrival_H_M}</p>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class="col-lg-2 my-auto text-center">
                                                                    <p class="mb-0 fs-14 theme2 fw-bold">${flight.onerefund}</p>
                                                                    <p class="mb-0 fs-13">Seat Left: ${flight.SecondsetsAvailable}</p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="tab-pane fade" id="${flight.ResultIndex}pills-fd2" role="tabpanel"
                                                            aria-labelledby="${flight.ResultIndex}pills-fd2-tab" tabindex="0"> 
                                                            <table class="table text-start fs-12" id="${flight.ResultIndex}passengerTable">
                                                                <thead>
                                                                    <tr>
                                                                        <th>TYPE</th>
                                                                        <th>BASE FARE</th>
                                                                        <th>TAXES & FEES</th>
                                                                        <th>TOTAL</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    <tr>
                                                                    <td></td>
                                                                    <td></td>
                                                                    <td>Total</td>
                                                                    <td><span>${flight.PublishedFare}</span>
                                                                    <span>-${flight.discount1 + flight.discount2}</span>
                                                                    <span>${flight.discount1 + flight.discount2 - flight.PublishedFare }</span>
                                                                    </td>

                                                                    </tr>
                                                                </tbody>
                                                                
                                                                
                                                            </table>
                                                        </div>
                                                        <div class="tab-pane fade" id="${flight.ResultIndex}pills-fd3" role="tabpanel"
                                                            aria-labelledby="${flight.ResultIndex}pills-fd3-tab" tabindex="0">
                                                            <div class="text-end">
                                                                <button type="button"
                                                    class="book-btn book-btn1 bg-white theme rounded-pill v-fare-btn mb-1"
                                                    data-bs-toggle="modal" data-bs-target="#${ flight.ResultIndex}010morefarePop" id="${flight.ResultIndex}2" result-index="${flight.ResultIndex}" onclick="show_fare_details('${token_id_value}','${ flight.TraceId }','${flight.ResultIndex}' )" >View Fare Rule</button>
                                                            </div>
                                                            <table class="table text-start fs-12">
                                                                <thead>
                                                                    <tr>
                                                                        <th>SECTOR</th>
                                                                        <th>TIME FRAME</th>
                                                                        <th>CHARGES & DISCRIPTION</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="f-code">${flight.OrginAirportCode} - ${flight.DestinationAirportCode}</td>
                                                                        <td>From & Above Before Dept</td>
                                                                        <td>INR 4000* + 0</td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                             <div class="modal fade" id="${flight.ResultIndex}010morefarePop" tabindex="-1" role="dialog"
                                                                aria-labelledby="exampleModalLabel" aria-hidden="true">
                                                                <div class="modal-dialog" role="document"
                                                                    style="max-width: 1020px;top: 10%;">
                                                                    <div class="modal-content fo-pop-head">
                                                                        <div class="modal-header shadows px-4">
                                                                            <h4 class="modal-title theme" id="exampleModalLabel">Fare Rule Details</h4>
                                                                            <button type="button" class="btn-close"
                                                                                data-bs-dismiss="modal" aria-label="Close"></button>
                                                                        </div>
                                                                        <div class="modal-body fo-pop-div" id="${flight.ResultIndex}3">
                                                                            <div class="modal-body">
                                                                            <div id="${ flight.ResultIndex}00">

                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            </div>
                                                        </div>
                                                        <div class="tab-pane fade" id="${flight.ResultIndex}pills-fd4" role="tabpanel"
                                                            aria-labelledby="${flight.ResultIndex}pills-fd4-tab" tabindex="0">
                                                            <table class="table text-start fs-12">
                                                                <thead>
                                                                    <tr>
                                                                        <th>SECTOR</th>
                                                                        <th>CHECK IN</th>
                                                                        <th>CABIN</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    <tr>
                                                                        <td class="f-code">${flight.FristOrginAirportCode} - ${flight.FristDestinationAirportCode}</td>
                                                                        <td>${flight.Fristcheckinbag} / Person</td>
                                                                        <td>${flight.Fristcombainbag} / Person</td>
                                                                    </tr>
                                                                    <tr>
                                                                    <td class="f-code">${flight.SecondOrginAirportCode} - ${flight.SecondDestinationAirportCode}</td>
                                                                        <td>${flight.Secondcheckinbag} / Person</td>
                                                                        <td>${flight.Secondcombainbag} / Person</td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>`
                }
    flightsContainer.innerHTML += flightHTML;

// Add event listener to each price element
    let priceElements = flightsContainer.querySelectorAll('.price-class');
    let selectedButton = null;
    priceElements.forEach(priceElement => {
    priceElement.addEventListener('click', function(event) {
        const selectedresultindex =  event.currentTarget.dataset.flight;
        console.log("selectedPrice",selectedresultindex);

        const flight_fare_details = flightsContainer.querySelector('.book-btn1');
        const flightfaredetails = flightsContainer.querySelector('.book-btn2');
        const book_non_flight = flightsContainer.querySelector('.book-button1');
        const book_one_flight = flightsContainer.querySelector('.book-button2');
        const flight_faredetails = flightsContainer.querySelector('.flight-fare');
        console.log(flight_faredetails);
        const changeprice = flightsContainer.querySelector('.change-price');
        const flightclass = flightsContainer.querySelector('.change-F-class');
        const flightclass2 = flightsContainer.querySelector('.change-F-class2');
        const flightclass3 = flightsContainer.querySelector('.change-F-class3');
        // const selectBtn = arrayDiv.querySelector('.price-class')
        
        // let selectedFlight = array.find(flight => flight.ResultIndex === selectedresultindex);
        // console.log("flight price",selectedFlight);
        // if (flight_fare_details) {
        //     flight_fare_details.setAttribute("onclick", `show_fare_details('${token_id_value}','${selectedFlight.TraceId}','${selectedFlight.ResultIndex}' )`);
        // } 
        // if (flightfaredetails) {
        //     flightfaredetails.setAttribute("onclick", `show_fare_details('${token_id_value}','${selectedFlight.TraceId}','${selectedFlight.ResultIndex}' )`);
        // }
        // if(book_non_flight){
        //     book_non_flight.setAttribute("onclick", `handleSelectFlight('${ selectedFlight.TraceId }', '${ selectedFlight.ResultIndex }','${token_id_value}','${selectedFlight.Stopconformation}','${selectedFlight.FlightClass}','${selectedFlight.start_date}','${selectedFlight.total_H_M}','${selectedFlight.OrginAirportCode}','${selectedFlight.DestinationAirportCode}','${selectedFlight.AirlineCode}')`)
        // }
        // if(book_one_flight){
        //     book_one_flight.setAttribute("onclick",`handleSelectFlight('${ selectedFlight.TraceId }', '${ selectedFlight.ResultIndex }','${token_id_value}','${selectedFlight.Stopconformation}','${selectedFlight.FlightClass}','${selectedFlight.Firstdstart_date}','${selectedFlight.Firsttotal_H_M}','${selectedFlight.FirstOrginAirportCode}','${selectedFlight.SecondDestinationAirportCode}','${selectedFlight.FirstAirlineCode}')`)
        // }
        // if (flight_faredetails) {
        // flight_faredetails.setAttribute("value",`[{"passengerCount": "${selectedFlight.APassengerCount}","passengerType": "${selectedFlight.APassengerType}","baseFare": "${selectedFlight.ABaseFare}","tax": "${selectedFlight.ATax}","discount1":"${selectedFlight.discount1}","discount2":"${selectedFlight.discount2}","AdditionalTxnFeePub":"${selectedFlight.AdditionalTxnFeePub}","OtherCharges":"${selectedFlight.OtherCharges}","ServiceFee":"${selectedFlight.ServiceFee}","AirlineTransFee":"${selectedFlight.AirlineTransFee}","IncentiveEarned":"${selectedFlight.IncentiveEarned}"},{"passengerCount": "${selectedFlight.BPassengerCount}","passengerType": "${selectedFlight.BPassengerType}","baseFare": "${selectedFlight.BBaseFare}","tax": "${selectedFlight.BTax}"},{"passengerCount": "${selectedFlight.CPassengerCount}","passengerType": "${selectedFlight.CPassengerType}","baseFare": "${selectedFlight.CBaseFare}","tax": "${selectedFlight.CTax}"}]`)
        // }if(changeprice){
        // changeprice.textContent = ` ₹ ${selectedFlight.OffredFare}`;
        // }if(flightclass){
        // flightclass.textContent = `${selectedFlight.AirlineType} / ${selectedFlight.FlightClass}`;
        // }if(flightclass2){
        // flightclass2.textContent = `${selectedFlight.AirlineType} / ${selectedFlight.FlightClass}`;
        // }if(flightclass3){
        // flightclass3.textContent = `${selectedFlight.AirlineType} / ${selectedFlight.SecondFlightClass}`;
        // }

         // Variable to store the currently selected button

        // Deselect the previously selected button, if any
        if (selectedButton) {
            selectedButton.innerHTML = "SELECT";
        }
        
        // Select the clicked button
        const selectBtn = event.currentTarget;
        selectBtn.innerHTML = "SELECTED";
        selectedButton = selectBtn; // Update the selectedButton reference

        // Your existing code for handling button click event goes here
        // ...

    });
});


});



// Passenger data
    
//     var fareSummaryInput = document.getElementById('fare-summary1');

// if (fareSummaryInput) {
//     var guestDataString = fareSummaryInput.value; // Get the value of the input
//     var passengers = JSON.parse(guestDataString);
    
//     console.log(passengers);
// } else {
//     console.log("No input element found with the id 'fare-summary1'");
// }
// var passengers = [
//         {"PassengerCount": 2, "PassengerType": 1, "BaseFare": 4752, "Tax": 729, "discount1": 30, "discount2": 60}, 
//         {"PassengerCount": 2, "PassengerType": 2, "BaseFare": 4752, "Tax": 0}, 
//         {"PassengerCount": 2, "PassengerType": 3, "BaseFare": 0, "Tax": 729}
//     ];

//     // Function to generate table rows
//     function generateTableRows(passenger) {
//         if (passenger.PassengerType === undefined) {
//             return ''; // Return empty string if passenger type is undefined
//         }

//         var type;
//         if (passenger.PassengerType === 1) {
//             type = "Adult";
//         } else if (passenger.PassengerType === 2) {
//             type = "Child";
//         } else if (passenger.PassengerType === 3) {
//             type = "Infant";
//         }
        
//         var baseFare = "INR " + (passenger.BaseFare || 0).toFixed(2);
//         var tax = "INR " + ((passenger.Tax || 0)+(passenger.OtherCharges || 0)+(passenger.ServiceFee || 0)+(passenger.AdditionalTxnFeepub || 0)+(passenger.AirlineTransFee || 0)).toFixed(2);
//         var total = "INR " + ((passenger.BaseFare || 0) + (passenger.Tax || 0)).toFixed(2);

//         return "<tr><td>" + type + " X " + passenger.PassengerCount + "</td><td>" + baseFare + "</td><td>" + tax + "</td><td>" + total + "</td></tr>";
//     }

//     // Generate table rows
//     var tableBody = document.querySelector("#passengerTable tbody");
//     passengers.forEach(function(passenger) {
//         tableBody.innerHTML += generateTableRows(passenger);
//     });

//     // Calculate total
//     var totalBaseFare = passengers.reduce(function(sum, passenger) {
//         return sum + (passenger.BaseFare || 0); // Ensure adding only if BaseFare is defined
//     }, 0);

//     var totalTax = passengers.reduce(function(sum, passenger) {
//         return sum + (passenger.Tax || 0); // Ensure adding only if Tax is defined
//     }, 0);

//     var offeredfare = passengers.reduce(function(sum, passenger) {
//         return sum + (passenger.discount1 || 0) + (passenger.discount2 || 0)+(passenger.IncentiveEarned || 0)+(passenger.AdditionalTxnFeePub || 0);
//     }, 0);

//     var totalRow = "<tr><td>Total</td><td>INR " + totalBaseFare.toFixed(2) + "</td><td>INR " + totalTax.toFixed(2) + "</td><td>INR " + (totalBaseFare + totalTax).toFixed(2) + "</td></tr>";
//     tableBody.innerHTML += totalRow;
//     var finalfare = "<tr><td><strong>Final total fare</strong></td><td>INR " + offeredfare.toFixed(2) + "</td><td>INR " + (totalBaseFare + totalTax).toFixed(2) + "</td><td><strong>INR " + ((totalBaseFare + totalTax) - offeredfare).toFixed(2) + "</strong></td></tr>";
//     tableBody.innerHTML += finalfare;
});


function show_fare_details( tokenId,traceId,resultIndex) {
    
    var csrftoken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    $.ajax({
        url: "/Fare_rule_details/",  // Replace with the actual URL of your views.py
        type: "POST",
        data:{
            // "EndUserIp": "192.168.11.120",
            "tokenId": tokenId,
            "traceId": traceId,
            "resultIndex": resultIndex,
        },
        
        headers: {
            'X-CSRFToken': csrftoken  // Include the CSRF token in the headers
        },
        success: function(response) {
            // var roomDetailsData = response.room_details;
            // updateRoomDetails(roomDetailsData, hotelCode);
            document.getElementById(resultIndex +'00').innerHTML = response.fare_details_html;
            // console.log(roomDetailsData);
        },
        error: function(error) {
            document.getElementById(resultIndex +'00').innerHTML = "<a>N0 fare rule details Available</a>"
            console.error(error);
        }
    });
}

function addPassengerDetails(ResultIndex, passengerDetailsString) {
    // Alert for debugging purposes
    // alert(ResultIndex);

    // Select the table body using the ResultIndex
    const tbody = document.querySelector(`#${ResultIndex}passengerTable tbody`);

    // Check if the table body exists
    if (!tbody) {
        console.error(`Table body not found for ResultIndex: ${ResultIndex}`);
        return;
    }

    // Clear existing rows in the table body
    tbody.innerHTML = '';

    try {
        // Parse the passenger details from the JSON string
        const passengerDetails = JSON.parse(decodeURIComponent(passengerDetailsString));
        console.log(passengerDetails);

        // Loop through each detail and create a new row in the table
        passengerDetails.forEach(detail => {
            const row = document.createElement('tr');

            const passengerCountCell = document.createElement('td');
            passengerCountCell.textContent = detail.PassengerCount;
            row.appendChild(passengerCountCell);

            const baseFareCell = document.createElement('td');
            baseFareCell.textContent = detail.BaseFare;
            row.appendChild(baseFareCell);

            const taxCell = document.createElement('td');
            taxCell.textContent = detail.Tax;
            row.appendChild(taxCell);

            const totalCell = document.createElement('td');
            totalCell.textContent = detail.Total;
            row.appendChild(totalCell);

            tbody.appendChild(row);
        });
    } catch (error) {
        // Log any errors that occur during JSON parsing
        console.error('Error parsing JSON:', error);
    }
}


function handleSelectFlight(tokenId, Flightdetails) {
    var form = document.createElement('form');
    form.method = 'POST';
    form.action = '/flightreview/'; // Update with the appropriate URL
    var csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    // Create hidden input fields for necessary data
    var csrfTokenField = document.createElement('input');
    csrfTokenField.type = 'hidden';
    csrfTokenField.name = 'csrfmiddlewaretoken';
    csrfTokenField.value = csrfToken;
    form.appendChild(csrfTokenField);
// Add other necessary hidden input fields
   
    
    var tokenIdField = document.createElement('input');
    tokenIdField.type = 'hidden';
    tokenIdField.name = 'tokenId';
    tokenIdField.value = tokenId;
    form.appendChild(tokenIdField);
    var AirlinedetailsField = document.createElement('input');
    AirlinedetailsField.type = 'hidden';
    AirlinedetailsField.name = 'flightDetails';
    AirlinedetailsField.value =Flightdetails;
    form.appendChild(AirlinedetailsField)
  
    document.body.appendChild(form);
    form.submit();
}   


// document.addEventListener("DOMContentLoaded", function() {
//     // Get the hidden input value
//     var hiddenadult = document.getElementById("hiddenAdultValue").value;
//     var hiddenchild = document.getElementById("hiddenChildValue").value;
//     var hiddeninfant = document.getElementById("hiddeninfantValue").value;
//     var hiddenclass = document.getElementById("hiddenclassValue").value;
//     // Get the select element
//     var selectadult = document.getElementById("Adult_inp");
//     var selectchild = document.getElementById("Child_inp");
//     var selectinfant = document.getElementById("Infant_inp");
//     var selectclass = document.getElementById("class_inp");
    
//     // Set the select element value
//     selectadult.value = hiddenadult;
//     selectchild.value = hiddenchild;
//     selectinfant.value = hiddeninfant;
//     selectclass.value = hiddenclass;
// });









// // DATE - ONE TRIP
// document.addEventListener('DOMContentLoaded', function() {
//     var today = new Date();
//     var year = today.getFullYear();
//     var month = ('0' + (today.getMonth() + 1)).slice(-2); // Months are zero-based
//     var day = ('0' + today.getDate()).slice(-2);

//     var todayString = year + '-' + month + '-' + day;

//     // Set the default value and minimum date to today for the start date input
//     var startDateInput = document.getElementById('check-in');
//     startDateInput.value = todayString;
//     startDateInput.min = todayString;

//     // Set the next date input based on the start date
//     function setNextDate() {
//         var startDate = new Date(startDateInput.value);
//         if (!isNaN(startDate.getTime())) {
//             var nextDate = new Date(startDate);
//             nextDate.setDate(startDate.getDate() + 1); // Increment by one day

//             var year = nextDate.getFullYear();
//             var month = ('0' + (nextDate.getMonth() + 1)).slice(-2); // Months are zero-based
//             var day = ('0' + nextDate.getDate()).slice(-2);

//             var nextDateString = year + '-' + month + '-' + day;
//             document.getElementById('check-out').value = nextDateString;
//             document.getElementById('check-out').min = nextDateString;
//         }
//     }

//     startDateInput.addEventListener('change', setNextDate);

//     // Set the initial next date
//     setNextDate(); 
// });

// // DATE - ROUND TRIP
// document.addEventListener('DOMContentLoaded', function() {
//     var today = new Date();
//     var year = today.getFullYear();
//     var month = ('0' + (today.getMonth() + 1)).slice(-2); // Months are zero-based
//     var day = ('0' + today.getDate()).slice(-2);

//     var todayString = year + '-' + month + '-' + day;

//     // Set the default value and minimum date to today for the start date input
//     var startDateInput = document.getElementById('rcheck-in');
//     startDateInput.value = todayString;
//     startDateInput.min = todayString;

//     // Set the next date input based on the start date
//     function setNextDate() {
//         var startDate = new Date(startDateInput.value);
//         if (!isNaN(startDate.getTime())) {
//             var nextDate = new Date(startDate);
//             nextDate.setDate(startDate.getDate() + 1); // Increment by one day

//             var year = nextDate.getFullYear();
//             var month = ('0' + (nextDate.getMonth() + 1)).slice(-2); // Months are zero-based
//             var day = ('0' + nextDate.getDate()).slice(-2);

//             var nextDateString = year + '-' + month + '-' + day;
//             document.getElementById('rcheck-out').value = nextDateString;
//             document.getElementById('rcheck-out').min = nextDateString;
//         }
//     }

//     startDateInput.addEventListener('change', setNextDate);

//     // Set the initial next date
//     setNextDate(); 
// });



// MULTI TRIP_______________________________________________________________________________________
// function addFlight() {
//     var container = document.getElementById("multitrip-container");

//     // Create a new flight container
//     var newFlight = document.createElement("div");
//     newFlight.className = "multitrip-container-item";
//     newFlight.style.display = "none";

//     // Your existing code for the flight input fields (copy and paste from the original code)
//     newFlight.innerHTML = `<div class="d-flex col-md-12">
//                                         <fieldset class="scheduler-border col-md-3">
//                                             <legend class="scheduler-border">From</legend>
//                                             <div class="control-group">
//                                                 <div class="controls bootstrap-timepicker">
//                                                     <input type="text"  id="from" placeholder="Enter The City" style="font-size: 14px;">
//                                                     <i class="icon-time"></i>
//                                                 </div>
//                                             </div>
//                                         </fieldset>
//                                         <fieldset class="scheduler-border col-md-2">
//                                             <legend class="scheduler-border">To</legend>
//                                             <div class="control-group">
//                                                 <div class="controls bootstrap-timepicker">
//                                                     <input type="text" id="to" placeholder="Enter The City" style="font-size: 14px;">
//                                                     <i class="icon-time"></i>
//                                                 </div>
//                                             </div>
//                                         </fieldset>
//                                         <fieldset class="scheduler-border col-md-2">
//                                             <legend class="scheduler-border">Departure</legend>
//                                             <div class="control-group">
//                                                 <div class="controls bootstrap-timepicker">
//                                                     <input type="date" id="checkOutDate"  class="check" data-date="" data-date-format="DD MMMM YYYY" value="2023-12-23" style="font-size: 14px;">
//                                                     <i class="icon-time"></i>
//                                                 </div>
//                                             </div>
//                                         </fieldset>
//                                         <fieldset class="scheduler-border col-md-1 mb-3">
//                                             <legend class="scheduler-border">Class</legend>
//                                             <div class="control-group">
//                                                 <div class="controls bootstrap-timepicker">
//                                                     <select style="border: none;padding: 2px 3px;" name= "classes">
//                                                         <option value="All">All</option>
//                                                         <option selected value="Econamy">Econamy</option>
//                                                         <option value="Business">Business</option>
//                                                         <option value="First">First</option>
//                                                     </select>
//                                                     <i class="icon-time"></i>
//                                                 </div>
//                                             </div>
//                                         </fieldset>
//                                         <fieldset class="scheduler-border col-md-3 mb-3">
//                                             <legend class="scheduler-border">Travellers & Class</legend>
//                                             <div class="control-group">
//                                                 <div class="controls bootstrap-timepicker">
//                                                     <input type="text" placeholder="1 Room & 0 Adults" id="room" style="font-size: 14px;" onclick="showForm2()">
//                                                     <input type="hidden" id="roomInfoInput" name="roomInfo">
//                                                     <input type="hidden" id="totalRoomInfoInput" name="totalRoomInfo">
//                                                     <i class="icon-time"></i>
//                                                 </div>
//                                             </div>
//                                         </fieldset>
//                                         <div id="flight_inp_form4" >
//                                             <div class="inp-form" >
//                                                 <div class="d-flex">
//                                                     <div class="col_1">
//                                                         <label for="Adults">Adults</label>
//                                                         <select name="Adults" id="Adult_inp">
//                                                             <option value="0">Select</option>
//                                                             <option value="1">1</option>
//                                                             <option value="2">2</option>
//                                                             <option value="3">3</option>
//                                                             <option value="4">4</option>
//                                                             <option value="5">5</option>
//                                                             <option value="6">6</option>
//                                                         </select>
//                                                     </div>
//                                                     <div class="col_1"> 
//                                                         <label for="Child">Child</label>
//                                                         <select name="Childs" id="Child_inp">
//                                                             <option value="0">Select</option>
//                                                             <option value="1">1</option>
//                                                             <option value="2">2</option>
//                                                             <option value="3">3</option>
//                                                             <option value="4">4</option>
//                                                             <option value="5">5</option>
//                                                             <option value="6">6</option>
//                                                         </select>
//                                                     </div>
//                                                     <div class="col_1">
//                                                         <label for="Infant">Infant</label>
//                                                         <select name="Infants" id="Adult_inp">
//                                                             <option value="0">Select</option>
//                                                             <option value="1">1</option>
//                                                             <option value="2">2</option>
//                                                             <option value="3">3</option>
//                                                             <option value="4">4</option>
//                                                             <option value="5">5</option>
//                                                             <option value="6">6</option>
//                                                         </select>
//                                                     </div>
//                                                 </div>
//                                             </div>
//                                         </div>
//                                     </div>
//     `;

//     // Append the new flight container to the main container
//     container.appendChild(newFlight);

//     // Toggle the display of the new flight container
//     if (newFlight.style.display === "none") {
//         newFlight.style.display = "block";
//     } else {
//         newFlight.style.display = "none";
//     }
// }

// function showFlightForm2() {
//     var flightForm = document.getElementById("flight_inp_form2")
//     if(flightForm.style.display === "none") {
//         flightForm.style.display = "block";
//     } else {
//         flightForm.style.display = "none"
//     }
// }

// function showForm() {
//     var flightForm = document.getElementById("flight_inp_form3")
//     if(flightForm.style.display === "none") {
//         flightForm.style.display = "block";
//     } else {
//         flightForm.style.display = "none"
//     }
// }
// function showForm2() {
//     var flightForm = document.getElementById("flight_inp_form4")
//     if(flightForm.style.display === "none") {
//         flightForm.style.display = "block";
//     } else {
//         flightForm.style.display = "none"
//     }

//     var header = document.getElementById("myTab");
//     var btns = header.getElementsByClassName("trip-btn");
//     for (var i = 0; i < btns.length; i++) {
//     btns[i].addEventListener("click", function() {
//     var current = document.getElementsByClassName("active");
//     current[0].className = current[0].className.replace(" active", "");
//     this.className += " active";
//     });
// }}