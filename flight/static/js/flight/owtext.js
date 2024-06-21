    <div class="flight-container flight" ticket-price="${flight.OffredFare}" flight-name="${flight.AirlineName}" 
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
                <button type="button" class="btn btn-primary book-btn book-button1" data-trace-id="${flight.TraceId}" data-result-index="${flight.ResultIndex}" 
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
    </div>

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