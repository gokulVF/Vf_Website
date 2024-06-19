// DATE - ONE TRIP
document.addEventListener('DOMContentLoaded', function() {
    var today = new Date();
    var year = today.getFullYear();
    var month = ('0' + (today.getMonth() + 1)).slice(-2); // Months are zero-based
    var day = ('0' + today.getDate()).slice(-2);

    var todayString = year + '-' + month + '-' + day;

    // Set the default value and minimum date to today for the start date input
    var startDateInput = document.getElementById('check-in');
    startDateInput.value = todayString;
    startDateInput.min = todayString;

    // Set the next date input based on the start date
    function setNextDate() {
        var startDate = new Date(startDateInput.value);
        if (!isNaN(startDate.getTime())) {
            var nextDate = new Date(startDate);
            nextDate.setDate(startDate.getDate() + 1); // Increment by one day

            var year = nextDate.getFullYear();
            var month = ('0' + (nextDate.getMonth() + 1)).slice(-2); // Months are zero-based
            var day = ('0' + nextDate.getDate()).slice(-2);

            var nextDateString = year + '-' + month + '-' + day;
            document.getElementById('check-out').value = nextDateString;
            document.getElementById('check-out').min = nextDateString;
        }
    }

    startDateInput.addEventListener('change', setNextDate);

    // Set the initial next date
    setNextDate(); 
});

// DATE - ROUND TRIP
document.addEventListener('DOMContentLoaded', function() {
    var today = new Date();
    var year = today.getFullYear();
    var month = ('0' + (today.getMonth() + 1)).slice(-2); // Months are zero-based
    var day = ('0' + today.getDate()).slice(-2);

    var todayString = year + '-' + month + '-' + day;

    // Set the default value and minimum date to today for the start date input
    var startDateInput = document.getElementById('rcheck-in');
    startDateInput.value = todayString;
    startDateInput.min = todayString;

    // Set the next date input based on the start date
    function setNextDate() {
        var startDate = new Date(startDateInput.value);
        if (!isNaN(startDate.getTime())) {
            var nextDate = new Date(startDate);
            nextDate.setDate(startDate.getDate() + 1); // Increment by one day

            var year = nextDate.getFullYear();
            var month = ('0' + (nextDate.getMonth() + 1)).slice(-2); // Months are zero-based
            var day = ('0' + nextDate.getDate()).slice(-2);

            var nextDateString = year + '-' + month + '-' + day;
            document.getElementById('rcheck-out').value = nextDateString;
            document.getElementById('rcheck-out').min = nextDateString;
        }
    }

    startDateInput.addEventListener('change', setNextDate);

    // Set the initial next date
    setNextDate(); 
});

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


// PAXFORM ONETRIP
// SHOW PAX FORM - ROUND TRIP
function showRoundPaxForm() {
    var flightForm = document.getElementById("pas_form_roundtrip")
    if(flightForm.style.display === "none") {
        flightForm.style.display = "block";
    } else {
        flightForm.style.display = "none"
    }
}

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

// FILTER FUNCTIONS TOP - ONE TRIP
function sortFlight(criteria) {
    var flightLists = document.querySelectorAll('#flightlist');

    flightLists.forEach(function(flightList) {
        var flights = Array.from(flightList.querySelectorAll('.flight-container, .flight-container1'));

        var sortOrder = flightList.getAttribute('data-sort-order') || 'asc';

        flights.sort(function(a, b) {
            var aValue, bValue;

            if (criteria === 'Price') {
                console.log("Price")
                aValue = parseFloat(a.getAttribute('ticket-price')) || parseFloat(a.getAttribute('ticket-prices'));
                bValue = parseFloat(b.getAttribute('ticket-price')) || parseFloat(b.getAttribute('ticket-prices'));
            } else if (criteria === 'Duration') {
                aValue = parseInt(a.getAttribute('ticket-duration-hours') || 0) * 60 + parseInt(a.getAttribute('ticket-duration-minutes') || 0);
                bValue = parseInt(b.getAttribute('ticket-duration-hours') || 0) * 60 + parseInt(b.getAttribute('ticket-duration-minutes') || 0);
            } else if (criteria === 'Departure') {
                var aDeparture = a.getAttribute('flight-departure-time') || a.getAttribute('flight-departure-times');
                var bDeparture = b.getAttribute('flight-departure-time') || b.getAttribute('flight-departure-times');
                return sortOrder === 'asc' ? aDeparture.localeCompare(bDeparture) : bDeparture.localeCompare(aDeparture);
            } else if (criteria === 'Arrival') {
                var aArrival = a.getAttribute('flight-arrival-time') || a.getAttribute('flight-arrival-times');
                var bArrival = b.getAttribute('flight-arrival-time') || b.getAttribute('flight-arrival-times');
                return sortOrder === 'asc' ? aArrival.localeCompare(bArrival) : bArrival.localeCompare(aArrival);
            } else if (criteria === 'Name') {
                var aName = a.getAttribute('flight-name') || a.getAttribute('flight-names');
                var bName = b.getAttribute('flight-name') || b.getAttribute('flight-names');
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

// FLIGHT LISTS - ONE TRIP_________________________________________
document.addEventListener("DOMContentLoaded", function() {
let flightsByNumberJSON = document.getElementById('Sort_F_details').value;
var flightsByNumber = JSON.parse(flightsByNumberJSON);
// console.log(flightsByNumber);

const flightsContainer = document.getElementById("flightlist");

// Loop through each array and create a details container for each
flightsByNumber.forEach((array, index) => {
    const arrayDiv = document.createElement('div');
    arrayDiv.classList.add('details-container');

    // Create HTML for details of the first object in the array
    const flight = array[0];
    const priceContainerHTML = array.map(flight => {
        return `<div class="row">
                            <div class="col-md-12 mt-3">
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="d-flex col-md-6" style="gap:60px; width:40%">
                                        <div>
                                            <p class="f-fil">SAVER</p>
                                        </div>
                                        <div>
                                            <h4 class="f-price1">₹ ${flight.OffredFare}</h4>
                                        </div>
                                    </div>
                                    <div style="width:40%;text-align:start;">
                                        <p class="f-class">${flight.AirlineType} / ${flight.FlightClass}</p>
                                    </div>
                                    <div class="f-sel-btn mb-3"  style="width:20%">
                                        <button type="button" data-flight="${flight.ResultIndex}"  class="btn btn-primary select-btn price-class">Select</button>
                                    </div>
                                </div>
                            </div>
                        </div>`;
    }).join('');

    if(flight.Stopconformation === 'Non-stop') {
        arrayDiv.innerHTML = ` <div class="flight-container" class="flight" ticket-price="${flight.OffredFare}" flight-name="${flight.AirlineName}" 
                ticket-duration-hours="${flight.totalhour}" ticket-duration-minutes="${flight.totalminute}"  flight-departure-time="${flight.departurehoure}:${flight.departureminute}" flight-arrival-time="${flight.arrivalhoure}:${flight.arrivalminute}" Flight-stop="${flight.Stopconformation}">
                    <div class="row">
                        <div class="col-md-1 mt-3">
                            <img src="{% static 'image/AirlineLogo/' %}${ flight.AirlineCode }.gif" alt="Flight-logo" >
                        </div>
                        <div class="col-md-3 align-items-center mt-3">
                            <h4 class="f-name">${flight.AirlineName} | ${flight.AirlineCode}-${flight.AirlineNumber}</h4>
                            <p class="f-class change-F-class">${flight.AirlineType} / ${flight.FlightClass}</p>
                        </div>
                        <div class="col-md-1 d-flex justify-content-between p-2">
                            <img src="{% static 'image/flight/refuntable ico.svg.'%}"alt="R-icon" class="r-icon">
                            <img src="{% static 'image/flight/luggage.svg.'%}" alt="lug-icon" class="icon">
                        </div>
                        <div class="col-md-4">
                            <div class="flight-timings">
                                <div class=" d-flex" style="border-bottom: 1px solid blue;">
                                    <p class="f-time-in">${flight.departure_H_M}</p>
                                    <p class="f_to_time">${flight.total_H_M}</p>
                                    <p class="f-time-in">${flight.arrival_H_M}</p>
                                </div>
                                <div class="d-flex mt-2">
                                    <p class="f-code">${flight.OrginAirportCode}</p>
                                    <p class="f_to_time">${flight.Stopconformation}</p>
                                    <p class="f-code">${flight.DestinationAirportCode}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 flight-price">
                            <h4 class="f-price change-price" >₹ ${flight.OffredFare}</h4>  
                            <button type="button"   class="btn btn-primary book-btn book-button1" data-trace-id="${flight.TraceId}" data-result-index="${flight.ResultIndex}" 
                            onclick="handleSelectFlight('${ flight.TraceId }', '${ flight.ResultIndex }','{{ token_id }}','${flight.Stopconformation}','${flight.FlightClass}','${flight.start_date}','${flight.total_H_M}','${flight.OrginAirportCode}','${flight.DestinationAirportCode}','${flight.AirlineCode}')">Book Now</button>
                        </div>
                        <div id="flight-details"></div>
                    </div>
                    <div class="container">
                        <div class="flight-features d-flex">
                            <div class="mr-2">
                                <button type="button" class="btn btn-primary more-btn" id="${flight.ResultIndex}2" onclick="showFare('${flight.ResultIndex}','${flight.ResultIndex}','${flight.ResultIndex}')">More Fare</button>
                            </div>
                            <div>
                                <button type="button" id="${flight.ResultIndex}01" class="btn flight-btn" onclick="showFlightDetail('${flight.ResultIndex}','${flight.ResultIndex}','${flight.ResultIndex}')">Flight Details</button>
                            </div>
                        </div>
                    </div>
                    <div class="container mt-3" style="display: none;background: #D9D9D945; border-radius: 8px; align-items: center; justify-content: center;text-align: center;"  id="${flight.ResultIndex}3">
                        ${priceContainerHTML}
                    </div>

                    <input type="hidden"  class="flight-fare fare-summary1" value='[{"passengerCount": "${flight.APassengerCount}","passengerType": "${flight.APassengerType}","baseFare": "${flight.ABaseFare}","tax": "${flight.ATax}","discount1":"${flight.discount1}","discount2":"${flight.discount2}","AdditionalTxnFeePub":"${flight.AdditionalTxnFeePub}","OtherCharges":"${flight.OtherCharges}","ServiceFee":"${flight.ServiceFee}","AirlineTransFee":"${flight.AirlineTransFee}","IncentiveEarned":"${flight.IncentiveEarned}"},{"passengerCount": "${flight.BPassengerCount}","passengerType": "${flight.BPassengerType}","baseFare": "${flight.BBaseFare}","tax": "${flight.BTax}"},{"passengerCount": "${flight.CPassengerCount}","passengerType": "${flight.CPassengerType}","baseFare": "${flight.CBaseFare}","tax": "${flight.CTax}"}]'>

                    <div id="${flight.ResultIndex}4" class="container mt-3" style="display: none;">
                        <div>
                            <div>
                                <ul class="nav nav-tabs " id="myTab" role="tablist">
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link active btn" id="${flight.ResultIndex}home-tab"  data-bs-toggle="tab" data-bs-target="#${flight.ResultIndex}home-tab-pane" type="button" role="tab" aria-controls="${flight.ResultIndex}home-tab-pane" aria-selected="true" autofocus>Flight Detailes</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link btn" id="${flight.ResultIndex}profile-tab"  data-bs-toggle="tab" data-bs-target="#${flight.ResultIndex}profile-tab-pane" type="button" role="tab" aria-controls="${flight.ResultIndex}profile-tab-pane" aria-selected="false" >Fare Summary</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link btn" class="fare_details_1" id="${flight.ResultIndex}contact-tab"   data-bs-toggle="tab" data-bs-target="#${flight.ResultIndex}contact-tab-pane" type="button" role="tab" aria-controls="${flight.ResultIndex}contact-tab-pane" aria-selected="false" >Fare Rules</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link btn" id="${flight.ResultIndex}bag-tab"  data-bs-toggle="tab" data-bs-target="#${flight.ResultIndex}bag-tab-pane" type="button" role="tab" aria-controls="${flight.ResultIndex}contact-tab-pane" aria-selected="false">Baggage Info</button>
                                    </li>
                                </ul>
                                <div class="tab-content mt-2" id="myTabContent">
                                    <div class="tab-pane fade show active col-md-12" id="${flight.ResultIndex}home-tab-pane"  role="tabpanel" aria-labelledby="${flight.ResultIndex}home-tab" tabindex="0">
                                        <div class="container">
                                            <div class="row">
                                                <div class="col-md-3">
                                                    <img src="{% static 'image/AirlineLogo/' %}${ flight.AirlineCode }.gif" alt="Flight-logo" style="width: 43%; height: 75px; padding-bottom: 10px;">
                                                    <h4 class="f-name">${flight.AirlineName} | ${flight.AirlineCode}-${flight.AirlineNumber}</h4>
                                                    <p class="f-class change-F-class2"> ${flight.AirlineType} / ${flight.FlightClass}</p>
                                                </div> 
                                                <div class="col-md-6">
                                                    <div class="flight-timings">
                                                        <div class="d-flex" style="border-bottom: 1px solid blue;">
                                                            <p class="f-time-in">${flight.departure_H_M}</p>
                                                            <p class="f_to_time">${flight.total_H_M}</p>
                                                            <p class="f-time-in">${flight.arrival_H_M}</p>
                                                        </div>
                                                        <div class="d-flex mt-2">
                                                            <div>
                                                                <p class="f-code">${flight.OrginAirportCode} ${flight.OrginAirportName}</p>
                                                                <p class="f-code2">${flight.OrginAirportCityName}, ${flight.OrginAirportCoutryName}</p>
                                                                <p class="f-term">Terminal: ${flight.OrginAirportTerminal}</p>
                                                            </div>
                                                            <div>
                                                                <p class="f-code">${flight.DestinationAirportCode} ${flight.DestinationAirportName}</p>
                                                                <p class="f-code2">${flight.DestinationCityName}, ${flight.DestinationCountryName}</p>
                                                                <p class="f-term">Terminal: ${flight.DestinationTerminal}</p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-3 ms-12" style="text-align: center;">
                                                    <p class="f-refund">${flight.nonrefund}</p>
                                                    <p class="f-code2">Seat Left: ${flight.setsAvailable}</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade show" role="tabpanel" id="${flight.ResultIndex}profile-tab-pane" aria-labelledby="${flight.ResultIndex}home-tab" tabindex="0">
                                        <div class="container">
                                            <div>
                                                <table class="table" id="passengerTable">
                                                    <thead>
                                                        <tr>
                                                            <th>TYPE</th>
                                                            <th>BASE FARE</th>
                                                            <th>TAXES & FEES</th>
                                                            <th>TOTAL</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade show" id="${flight.ResultIndex}contact-tab-pane"  role="tabpanel" aria-labelledby="${flight.ResultIndex}home-tab" tabindex="0">
                                        <div class="container">
                                            <div>
                                                <table class="table">
                                                    <thead>
                                                        <tr>
                                                            <th>SECTOR</th>
                                                            <th>TIME FRAME</th>
                                                            <th>CHARGES & DISCRIPTION</th>
                                                            <th>FARE DETAILS</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <td class="f-code">${flight.OrginAirportCode} - ${flight.DestinationAirportCode}</td>
                                                            <td>From & Above Before Dept</td>
                                                            <td>INR 4000* + 0</td>
                                                            <td>
                                                                <button type="button" class="btn btn-primary book-btn book-btn1" data-toggle="modal" data-target="#${ flight.ResultIndex}exampleModal" result-index="${flight.ResultIndex}" onclick="show_fare_details('{{ token_id }}','${ flight.TraceId }','${flight.ResultIndex}' )" >View Fare Rule</button>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <div class="modal fade" id="${ flight.ResultIndex}exampleModal" tabindex="-1" role="${ flight.ResultIndex}dialog" aria-labelledby="${ flight.ResultIndex}exampleModalLabel" aria-hidden="true">
                                                    <div class="modal-dialog" role="document">
                                                    <div class="modal-content">
                                                        <div class="modal-header">
                                                        <h5 class="modal-title" id="exampleModalLabel">Fare Rules</h5>
                                                        <button type="button" class="close-btn" data-dismiss="modal" aria-label="Close">
                                                            <span aria-hidden="true">&times;</span>
                                                        </button>
                                                        </div>
                                                        <div class="modal-body">
                                                            <div id="${ flight.ResultIndex}00"></div>
                                                        </div>
                                                        <div class="modal-footer">
                                                            <button type="button" class="book-btn" data-dismiss="modal" aria-label="Close" style="color: white;border: none;width: 100px;">
                                                                Ok
                                                            </button>
                                                        </div>
                                                    </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade show" id="${flight.ResultIndex}bag-tab-pane"  role="tabpanel" aria-labelledby="${flight.ResultIndex}home-tab" tabindex="0">
                                        <div class="container">
                                            <div>
                                                <table class="table">
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
                </div> `;
            
    } else if (flight.Stopconformation === '1-stop(s)'){
        arrayDiv.innerHTML =`<div class="flight-container1" class="flight" ticket-prices="${flight.OffredFare}" flight-names="${flight.FirstAirlineName}" 
                ticket-duration-hours="${flight.Firsttotalhour}" ticket-duration-minutes="${flight.Firsttotalhour}" ticket-duration-minutes="${flight.Firsttotalminute}"  flight-departure-times="${flight.Firstdeparturehoure}:${flight.Firstdepartureminute}" flight-arrival-times="${flight.Firstarrivalhoure}:${flight.Firstarrivalminute} " Flight-stops="${flight.Stopconformation}">
                    <div class="row">
                        <div class="col-md-1 mt-3">
                            <img src="{% static 'image/AirlineLogo/' %}${ flight.FirstAirlineCode }.gif" alt="Flight-logo">
                        </div>
                        <div class="col-md-3 align-items-center mt-3">
                            <h4 class="f-name">${flight.FirstAirlineName} | ${flight.FirstAirlineCode}-${flight.AirlineNumber}</h4>
                            <p class="f-class change-F-class">${flight.AirlineType} / ${flight.FlightClass}</p>
                        </div>
                        <div class="col-md-1 d-flex justify-content-between p-2">
                            <img src="{% static 'image/flight/refuntable ico.svg.'%}"alt="R-icon" class="r-icon">
                            <img src="{% static 'image/flight/luggage.svg.'%}" alt="lug-icon" class="icon">
                        </div>
                        <div class="col-md-4">
                            <div class="flight-timings">
                                <div class=" d-flex" style="border-bottom: 1px solid blue;">
                                    <p class="f-time-in">${flight.Firstdepartur_H_M}</p>
                                    <p class="f_to_time">${flight.FinalTotal_H_M}</p>
                                    <p class="f-time-in">${flight.Scondarrival_H_M}</p>
                                </div>
                                <div class="d-flex mt-2">
                                    <p class="f-code">${flight.FristOrginAirportCode}</p>
                                    <p class="f_to_time">${flight.Stopconformation}</p>
                                    <p class="f-code">${flight.SecondDestinationAirportCode}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-3 flight-price">
                            <h4 class="f-price change-price" >₹ ${flight.OffredFare}</h4>  
                            <button type="button" class="btn btn-primary book-btn book-button2" data-trace-id="${flight.TraceId}" data-result-index="${flight.ResultIndex}" 
                            onclick="handleSelectFlight('${ flight.TraceId }', '${ flight.ResultIndex }','{{ token_id }}','${flight.Stopconformation}','${flight.FlightClass}','${flight.Firstdstart_date}','${flight.FinalTotal_H_M}','${flight.FristOrginAirportCode}','${flight.SecondDestinationAirportCode}','${flight.FirstAirlineCode}')">Book Now</button>
                        </div>
                    </div>
                    <div class="container">
                        <div class="flight-features d-flex">
                            <div class="mr-2">
                                <button type="button" class="btn btn-primary more-btn" id="${flight.ResultIndex}2" onclick="showFare('${flight.ResultIndex}','${flight.ResultIndex}','${flight.ResultIndex}')">More Fare</button>
                            </div>
                            <div>
                                <button type="button" id="${flight.ResultIndex}01" class="btn flight-btn" onclick="showFlightDetail('${flight.ResultIndex}','${flight.ResultIndex}','${flight.ResultIndex}')">Flight Details</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="container mt-3" style="display: none;background: #D9D9D945; border-radius: 8px; align-items: center; justify-content: center;text-align: center;"  id="${flight.ResultIndex}3">
                        ${priceContainerHTML}
                    </div>

                    <input type="hidden" id="fare-summary2" class="flight-fare" value='[{"passengerCount": "${flight.APassengerCount}","passengerType": "${flight.APassengerType}","baseFare": "${flight.ABaseFare}","tax": "${flight.ATax}","discount1":"${flight.discount1}","discount2":"${flight.discount2}","AdditionalTxnFeePub":"${flight.AdditionalTxnFeePub}","OtherCharges":"${flight.OtherCharges}","ServiceFee":"${flight.ServiceFee}","AirlineTransFee":"${flight.AirlineTransFee}","IncentiveEarned":"${flight.IncentiveEarned}"},{"passengerCount": "${flight.BPassengerCount}","passengerType": "${flight.BPassengerType}","baseFare": "${flight.BBaseFare}","tax": "${flight.BTax}"},{"passengerCount": "${flight.CPassengerCount}","passengerType": "${flight.CPassengerType}","baseFare": "${flight.CBaseFare}","tax": "${flight.CTax}"}]'>

                    <div id="${flight.ResultIndex}4" class="container mt-3" style="display: none;">
                        <div>
                            <div>
                                <ul class="nav nav-tabs " id="myTab" role="tablist">
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link active btn" id="${flight.ResultIndex}home-tab"  data-bs-toggle="tab" data-bs-target="#${flight.ResultIndex}home-tab-pane" type="button" role="tab" aria-controls="${flight.ResultIndex}home-tab-pane" aria-selected="true" autofocus>Flight Detailes</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link btn" id="${flight.ResultIndex}profile-tab"  data-bs-toggle="tab" data-bs-target="#${flight.ResultIndex}profile-tab-pane" type="button" role="tab" aria-controls="${flight.ResultIndex}profile-tab-pane" aria-selected="false">Fare Summary</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link btn" id="${flight.ResultIndex}contact-tab"   data-bs-toggle="tab" data-bs-target="#${flight.ResultIndex}contact-tab-pane" type="button" role="tab" aria-controls="${flight.ResultIndex}contact-tab-pane" aria-selected="false"  >Fare Rules</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button class="nav-link btn" id="${flight.ResultIndex}bag-tab"  data-bs-toggle="tab" data-bs-target="#${flight.ResultIndex}bag-tab-pane" type="button" role="tab" aria-controls="${flight.ResultIndex}contact-tab-pane" aria-selected="false">Baggage Info</button>
                                    </li>
                                </ul>
                                <div class="tab-content mt-2" id="myTabContent">
                                    <div class="tab-pane fade show active col-md-12" id="${flight.ResultIndex}home-tab-pane"  role="tabpanel" aria-labelledby="${flight.ResultIndex}home-tab" tabindex="0">
                                        <div class="container">
                                            
                                            <div class="row">
                                                <div class="col-md-3">
                                                    <img src="{% static 'image/AirlineLogo/' %}${ flight.FirstAirlineCode }.gif" alt="Flight-logo" style="width: 43%; height: 75px; padding-bottom: 10px;">
                                                    <h4 class="f-name">${flight.FirstAirlineName} | ${flight.FirstAirlineCode}-${flight.AirlineNumber}</h4>
                                                    <p class="f-class change-F-class2">${flight.AirlineType} / ${flight.FlightClass}</p>
                                                </div> 
                                                <div class="col-md-6">
                                                    <div class="flight-timings">
                                                        <div class="d-flex" style="border-bottom: 1px solid blue;">
                                                            <p class="f-time-in">${flight.Firstdepartur_H_M}</p>
                                                            <p class="f_to_time">${flight.Firsttotal_H_M}</p>
                                                            <p class="f-time-in">${flight.Firstarrival_H_M}</p>
                                                        </div>
                                                        <div class="d-flex mt-2">
                                                            <div>
                                                                <p class="f-code">${flight.FristOrginAirportCode} ${flight.FristOrginAirportName}</p>
                                                                <p class="f-code2">${flight.FristOrginAirportCityName}, ${flight.FristOrginAirportCoutryName}</p>
                                                                <p class="f-term">Terminal: ${flight.FristOrginAirportTerminal}</p>
                                                            </div>
                                                            <div>
                                                                <p class="f-code">${flight.FristDestinationAirportCode} ${flight.FristDestinationAirportName}</p>
                                                                <p class="f-code2">${flight.FristDestinationCityName}, ${flight.FristDestinationCountryName}</p>
                                                                <p class="f-term">Terminal: ${flight.FristDestinationTerminal}</p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-3 ms-12" style="text-align: center;">
                                                    <p class="f-refund">${flight.onerefund}</p>
                                                    <p class="f-code2">Seat Left: ${flight.FristsetsAvailable}</p>
                                                </div>
                                            </div>
                                            
                                            <div class="row">
                                                <div class="col-md-3">
                                                    <img src="{% static 'image/AirlineLogo/' %}${ flight.SecondAirlineCode }.gif" alt="Flight-logo" style="width: 43%; height: 75px; padding-bottom: 10px;">
                                                    <h4 class="f-name">${flight.SecondAirlineName} | ${flight.SecondAirlineCode}-${flight.SAirlineNumber}</h4>
                                                    <p class="f-class change-F-class3">${flight.AirlineType} / ${flight.SecondFlightClass}</p>
                                                </div> 
                                                <div class="col-md-6">
                                                    <div class="flight-timings">
                                                        <div class="d-flex" style="border-bottom: 1px solid blue;">
                                                            <p class="f-time-in">${flight.Sconddeparture_H_M}</p>
                                                            <p class="f_to_time">${flight.Scondtotal_H_M}</p>
                                                            <p class="f-time-in">${flight.Scondarrival_H_M}</p>
                                                        </div>
                                                        <div class="d-flex mt-2">
                                                            <div>
                                                                <p class="f-code">${flight.SecondOrginAirportCode} ${flight.SecondOrginAirportName}</p>
                                                                <p class="f-code2">${flight.SecondOrginAirportCityName}, ${flight.SecondOrginAirportCoutryName}</p>
                                                                <p class="f-term">Terminal: ${flight.SecondOrginAirportTerminal}</p>
                                                            </div>
                                                            <div>
                                                                <p class="f-code">${flight.SecondDestinationAirportCode} ${flight.SecondDestinationAirportName}</p>
                                                                <p class="f-code2">${flight.SecondDestinationCityName}, ${flight.SecondDestinationCountryName}</p>
                                                                <p class="f-term">Terminal: ${flight.SecondDestinationTerminal}</p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-3 ms-12" style="text-align: center;">
                                                    <p class="f-refund">${flight.onerefund}</p>
                                                    <p class="f-code2">Seat Left: ${flight.SecondsetsAvailable}</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade show" role="tabpanel" id="${flight.ResultIndex}profile-tab-pane" aria-labelledby="${flight.ResultIndex}home-tab" tabindex="0">
                                        <div class="container">
                                            <div>
                                                <table class="table">
                                                    <thead>
                                                        <tr>
                                                            <th>TYPE</th>
                                                            <th>BASE FARE</th>
                                                            <th>TAXES & FEES</th>
                                                            <th>TOTAL</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade show" id="${flight.ResultIndex}contact-tab-pane"  role="tabpanel" aria-labelledby="${flight.ResultIndex}home-tab" tabindex="0">
                                        <div class="container">
                                            <div>
                                                <table class="table">
                                                    <thead>
                                                        <tr>
                                                            <th>SECTOR</th>
                                                            <th>TIME FRAME</th>
                                                            <th>CHARGES & DISCRIPTION</th>
                                                            <th>FARE DETAILS</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr>
                                                            <td class="f-code">${flight.FristOrginAirportCode} - ${flight.FristDestinationAirportCode} - ${flight.SecondDestinationAirportCode}</td>
                                                            <td>From & Above Before Dept</td>
                                                            <td>INR 4000* + 0</td>
                                                            <td>
                                                                <button type="button" class="btn btn-primary book-btn book-btn1" data-toggle="modal" data-target="#${ flight.ResultIndex}exampleModal" result-index="${flight.ResultIndex}" onclick="show_fare_details('{{ token_id }}','${ flight.TraceId }','${flight.ResultIndex}' )" >View Fare Rule</button>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <div class="modal fade" id="${ flight.ResultIndex}exampleModal" tabindex="-1" role="${ flight.ResultIndex}dialog" aria-labelledby="${ flight.ResultIndex}exampleModalLabel" aria-hidden="true">
                                                    <div class="modal-dialog" role="document">
                                                    <div class="modal-content">
                                                        <div class="modal-header">
                                                        <h5 class="modal-title" id="exampleModalLabel">Fare Rules</h5>
                                                        <button type="button" class="close-btn" data-dismiss="modal" aria-label="Close">
                                                            <span aria-hidden="true">&times;</span>
                                                        </button>
                                                        </div>
                                                        <div class="modal-body">
                                                            <div id="${ flight.ResultIndex}00"></div>
                                                        </div>
                                                    </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="tab-pane fade show" id="${flight.ResultIndex}bag-tab-pane"  role="tabpanel" aria-labelledby="${flight.ResultIndex}home-tab" tabindex="0">
                                        <div class="container">
                                            <div>
                                                <table class="table">
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
                </div>`
            
    }

    flightsContainer.appendChild(arrayDiv);

// Add event listener to each price element
    let priceElements = arrayDiv.querySelectorAll('.price-class');
    priceElements.forEach(priceElement => {
    priceElement.addEventListener('click', function(event) {
        const selectedresultindex =  event.currentTarget.dataset.flight;
        console.log("selectedPrice",selectedresultindex);

        const flight_fare_details = arrayDiv.querySelector('.book-btn1');
        const flightfaredetails = arrayDiv.querySelector('.book-btn2');
        const book_non_flight = arrayDiv.querySelector('.book-button1');
        const book_one_flight = arrayDiv.querySelector('.book-button2');
        const flight_faredetails = arrayDiv.querySelector('.flight-fare');
        console.log(flight_faredetails);
        const changeprice = arrayDiv.querySelector('.change-price');
        const flightclass = arrayDiv.querySelector('.change-F-class');
        const flightclass2 = arrayDiv.querySelector('.change-F-class2');
        const flightclass3 = arrayDiv.querySelector('.change-F-class3');
        const selectBtn = arrayDiv.querySelector('.price-class')
        
        let selectedFlight = array.find(flight => flight.ResultIndex === selectedresultindex);
        console.log("flight price",selectedFlight);
        if (flight_fare_details) {
            flight_fare_details.setAttribute("onclick", `show_fare_details('{{ token_id }}','${selectedFlight.TraceId}','${selectedFlight.ResultIndex}' )`);
        } 
        if (flightfaredetails) {
            flightfaredetails.setAttribute("onclick", `show_fare_details('{{ token_id }}','${selectedFlight.TraceId}','${selectedFlight.ResultIndex}' )`);
        }
        if(book_non_flight){
            book_non_flight.setAttribute("onclick", `handleSelectFlight('${ selectedFlight.TraceId }', '${ selectedFlight.ResultIndex }','{{ token_id }}','${selectedFlight.Stopconformation}','${selectedFlight.FlightClass}','${selectedFlight.start_date}','${selectedFlight.total_H_M}','${selectedFlight.OrginAirportCode}','${selectedFlight.DestinationAirportCode}','${selectedFlight.AirlineCode}')`)
        }
        if(book_one_flight){
            book_one_flight.setAttribute("onclick",`handleSelectFlight('${ selectedFlight.TraceId }', '${ selectedFlight.ResultIndex }','{{ token_id }}','${selectedFlight.Stopconformation}','${selectedFlight.FlightClass}','${selectedFlight.Firstdstart_date}','${selectedFlight.Firsttotal_H_M}','${selectedFlight.FirstOrginAirportCode}','${selectedFlight.SecondDestinationAirportCode}','${selectedFlight.FirstAirlineCode}')`)
        }
        if (flight_faredetails) {
        flight_faredetails.setAttribute("value",`[{"passengerCount": "${selectedFlight.APassengerCount}","passengerType": "${selectedFlight.APassengerType}","baseFare": "${selectedFlight.ABaseFare}","tax": "${selectedFlight.ATax}","discount1":"${selectedFlight.discount1}","discount2":"${selectedFlight.discount2}","AdditionalTxnFeePub":"${selectedFlight.AdditionalTxnFeePub}","OtherCharges":"${selectedFlight.OtherCharges}","ServiceFee":"${selectedFlight.ServiceFee}","AirlineTransFee":"${selectedFlight.AirlineTransFee}","IncentiveEarned":"${selectedFlight.IncentiveEarned}"},{"passengerCount": "${selectedFlight.BPassengerCount}","passengerType": "${selectedFlight.BPassengerType}","baseFare": "${selectedFlight.BBaseFare}","tax": "${selectedFlight.BTax}"},{"passengerCount": "${selectedFlight.CPassengerCount}","passengerType": "${selectedFlight.CPassengerType}","baseFare": "${selectedFlight.CBaseFare}","tax": "${selectedFlight.CTax}"}]`)
        }if(changeprice){
        changeprice.textContent = ` ₹ ${selectedFlight.OffredFare}`;
        }if(flightclass){
        flightclass.textContent = `${selectedFlight.AirlineType} / ${selectedFlight.FlightClass}`;
        }if(flightclass2){
        flightclass2.textContent = `${selectedFlight.AirlineType} / ${selectedFlight.FlightClass}`;
        }if(flightclass3){
        flightclass3.textContent = `${selectedFlight.AirlineType} / ${selectedFlight.SecondFlightClass}`;
        }

        let selectedButton = null; // Variable to store the currently selected button

        priceElements.forEach(priceElement => {
            priceElement.addEventListener('click', function(event) {
                // Deselect the previously selected button, if any
                if (selectedButton) {
                    selectedButton.innerHTML = "Select";
                }
                
                // Select the clicked button
                const selectBtn = event.currentTarget;
                selectBtn.innerHTML = "Selected";
                selectedButton = selectBtn; // Update the selectedButton reference

                // Your existing code for handling button click event goes here
                // ...

            });
        });
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
var passengers = [
        {"PassengerCount": 2, "PassengerType": 1, "BaseFare": 4752, "Tax": 729, "discount1": 30, "discount2": 60}, 
        {"PassengerCount": 2, "PassengerType": 2, "BaseFare": 4752, "Tax": 0}, 
        {"PassengerCount": 2, "PassengerType": 3, "BaseFare": 0, "Tax": 729}
    ];

    // Function to generate table rows
    function generateTableRows(passenger) {
        if (passenger.PassengerType === undefined) {
            return ''; // Return empty string if passenger type is undefined
        }

        var type;
        if (passenger.PassengerType === 1) {
            type = "Adult";
        } else if (passenger.PassengerType === 2) {
            type = "Child";
        } else if (passenger.PassengerType === 3) {
            type = "Infant";
        }
        
        var baseFare = "INR " + (passenger.BaseFare || 0).toFixed(2);
        var tax = "INR " + ((passenger.Tax || 0)+(passenger.OtherCharges || 0)+(passenger.ServiceFee || 0)+(passenger.AdditionalTxnFeepub || 0)+(passenger.AirlineTransFee || 0)).toFixed(2);
        var total = "INR " + ((passenger.BaseFare || 0) + (passenger.Tax || 0)).toFixed(2);

        return "<tr><td>" + type + " X " + passenger.PassengerCount + "</td><td>" + baseFare + "</td><td>" + tax + "</td><td>" + total + "</td></tr>";
    }

    // Generate table rows
    var tableBody = document.querySelector("#passengerTable tbody");
    passengers.forEach(function(passenger) {
        tableBody.innerHTML += generateTableRows(passenger);
    });

    // Calculate total
    var totalBaseFare = passengers.reduce(function(sum, passenger) {
        return sum + (passenger.BaseFare || 0); // Ensure adding only if BaseFare is defined
    }, 0);

    var totalTax = passengers.reduce(function(sum, passenger) {
        return sum + (passenger.Tax || 0); // Ensure adding only if Tax is defined
    }, 0);

    var offeredfare = passengers.reduce(function(sum, passenger) {
        return sum + (passenger.discount1 || 0) + (passenger.discount2 || 0)+(passenger.IncentiveEarned || 0)+(passenger.AdditionalTxnFeePub || 0);
    }, 0);

    var totalRow = "<tr><td>Total</td><td>INR " + totalBaseFare.toFixed(2) + "</td><td>INR " + totalTax.toFixed(2) + "</td><td>INR " + (totalBaseFare + totalTax).toFixed(2) + "</td></tr>";
    tableBody.innerHTML += totalRow;
    var finalfare = "<tr><td><strong>Final total fare</strong></td><td>INR " + offeredfare.toFixed(2) + "</td><td>INR " + (totalBaseFare + totalTax).toFixed(2) + "</td><td><strong>INR " + ((totalBaseFare + totalTax) - offeredfare).toFixed(2) + "</strong></td></tr>";
    tableBody.innerHTML += finalfare;
});

//RANGE INPUT PRICE FILTER - ONE TRIP
$(document).ready(function () {
    const rangeInput = $(".range-input input"),
        priceInput = $(".price-input input"),
        range = $(".slider .progress"),
        priceGap = 1000;

    priceInput.on("input", function () {
        let minPrice = parseInt(priceInput.eq(0).val()),
            maxPrice = parseInt(priceInput.eq(1).val());

        if (maxPrice - minPrice < priceGap) {
            if ($(this).hasClass("input-min")) {
                rangeInput.eq(0).val(maxPrice - priceGap);
            } else {
                rangeInput.eq(1).val(minPrice + priceGap);
            }
        } else {
            updateSlider(minPrice, maxPrice);
        }
    });

    rangeInput.on("input", function () {
        RangeSlider();
    });

    RangeSlider();

    function RangeSlider() {
        let minVal = parseInt(rangeInput.eq(0).val()),
            maxVal = parseInt(rangeInput.eq(1).val());

        if (maxVal - minVal < priceGap) {
            rangeInput.eq(0).val(maxVal - priceGap);
            minVal = parseInt(rangeInput.eq(0).val());
        }

        updateSlider(minVal, maxVal);
    }

    function updateSlider(minVal, maxVal) {
        priceInput.eq(0).val(minVal);
        priceInput.eq(1).val(maxVal);
        range.css({
            left: (minVal / rangeInput.eq(0).attr("max")) * 100 + "%",
            right: (100 - (maxVal / rangeInput.eq(1).attr("max")) * 100) + "%"
        });

        filterFlightsByPrice(minVal, maxVal);
        console.log(minVal, maxVal);
    }

    function filterFlightsByPrice(minPrice, maxPrice) {
        console.log("Filtering by Price:", minPrice, maxPrice);

        $(".flight-container,.flight-container1").each(function () {
            var flightPrice = parseInt($(this).attr("ticket-price")) || parseInt($(this).attr("ticket-prices"));

            console.log("Flight Price:", flightPrice);

            if (flightPrice >= minPrice && flightPrice <= maxPrice + 1000) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    }
});


// AIRLINE NAME FILTER FUNCTIONS
document.querySelectorAll('.form-check-input').forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
        updateFlightList();
    });
});

function updateFlightList() {
    var selectedAirlines = Array.from(document.querySelectorAll('.form-check-input:checked'))
        .map(function (checkbox) {
            return checkbox.getAttribute('data-airline').toLowerCase(); // Convert to lowercase
        });

    document.querySelectorAll('.flight-container, .flight-container1').forEach(function (flight) {
        var airlineName = flight.getAttribute('flight-name') || flight.getAttribute('flight-names');
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

    document.querySelectorAll('.flight-container, .flight-container1').forEach(function (flight) {
        var airlineClass = flight.getAttribute('flight-stop') || flight.getAttribute('flight-stops'); // Corrected attribute names
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

