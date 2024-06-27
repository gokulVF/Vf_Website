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
















                            <div class="col-lg-3 col-md-3 col-sm-12">
                                    <div class="item-inner-image text-start">
                                        <img src="images/flights/flight_grid_5.png" alt="image">
                                        <h5 class="mb-0">Dragon Airlines</h5>
                                        <small>Operated by China</small>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner">
                                        <div class="content">
                                            <h5 class="mb-0">Sunday May 15, 2022</h5>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner">
                                        <div class="content">
                                            <p class="mb-0">12:30</p>
                                            <p class="mb-0 text-uppercase fs-14">DAC</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-2 col-md-2 col-sm-12">
                                    <div class="item-inner flight-time">
                                        <p class="mb-0">16H 45M <br>2 Stops</p>
                                    </div>
                                </div>
                                <div class="col-lg-3 col-md-3 col-sm-12">
                                    <div class="item-inner text-end">
                                        <p class="theme2 fs-4 fw-bold mb-1">$2,045</p>
                                        <button class="nir-btn-black rounded-pill mb-1">Book Now</button>
                                    </div>
                                </div>
                                <div class="col-lg-12">
                                    <div class="accordion accordion-flush border-t mt-1 pt-1" id="accordionflush">
                                        <div class="accordion-item overflow-hidden">
                                            <div class="justify-content-between">
                                                <button
                                                    class="accordion-button collapsed bg-white fw-bold border-0 theme"
                                                    style="font-size: 14px;" type="button" data-bs-toggle="collapse"
                                                    data-bs-target="#flush-collapseOne" aria-expanded="false"
                                                    aria-controls="flush-collapseOne">Flight Details <i
                                                        class="fa fa-caret-down theme" aria-hidden="true"></i></button>
                                                <button type="button"
                                                    class="bg-white float-end theme rounded-pill morefare-btn"
                                                    data-bs-toggle="modal" data-bs-target="#morefarePop"> + More
                                                    Fare</button>
                                            </div>
                                            <div class="modal fade" id="morefarePop" tabindex="-1" role="dialog"
                                                aria-labelledby="exampleModalLabel" aria-hidden="true">
                                                <div class="modal-dialog" role="document"
                                                    style="max-width: 1020px;top: 10%;">
                                                    <div class="modal-content fo-pop-head">
                                                        <div class="modal-header shadows px-4">
                                                            <h3 class="modal-title theme" id="exampleModalLabel">More
                                                                Fare Options Available</h3>
                                                            <button type="button" class="btn-close"
                                                                data-bs-dismiss="modal" aria-label="Close"></button>
                                                        </div>
                                                        <div class="modal-body fo-pop-div ">
                                                            <div class="text-center mb-2">
                                                                <span>
                                                                    <span class="fw-bold black">New Delhi →
                                                                        Bengaluru</span>
                                                                    <span class="ms-3 fs-14 black">Akasa Air · Fri, 6 Sep
                                                                        24 · Departure at 22:40 - Arrival at 01:25 (+1
                                                                        day)</span>
                                                                </span>
                                                            </div>
                                                            <div class="f-options row">
                                                                <div class="col-lg-4 fo-opt-div border-all bg-white shadows">
                                                                    <div class="py-1 b_bot">
                                                                        <span class="fw-bold black">₹ 6,670</span>
                                                                        <span class="fs-12">per adult</span>
                                                                        <p class="fs-12 mb-0">SAVER</p>
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
                                                                        <button type="button" class="bg-theme white py-1 px-5 rounded-pill">BOOK NOW</button>
                                                                    </div>
                                                                </div>
                                                                <div class="col-lg-4 fo-opt-div border-all bg-white shadows">
                                                                    <div class="py-1 b_bot">
                                                                        <span class="fw-bold black">₹ 6,670</span>
                                                                        <span class="fs-12">per adult</span>
                                                                        <p class="fs-12 mb-0">SAVER</p>
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
                                                                        <button type="button" class="bg-theme white py-1 px-5 rounded-pill">BOOK NOW</button>
                                                                    </div>
                                                                </div>
                                                                <div class="col-lg-4 fo-opt-div border-all bg-white shadows">
                                                                    <div class="py-1 b_bot">
                                                                        <span class="fw-bold black">₹ 6,670</span>
                                                                        <span class="fs-12">per adult</span>
                                                                        <p class="fs-12 mb-0">SAVER</p>
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
                                                                        <button type="button" class="bg-theme white py-1 px-5 rounded-pill">BOOK NOW</button>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div id="flush-collapseOne" class="accordion-collapse collapse mt-2"
                                                aria-labelledby="flush-headingOne"
                                                data-bs-parent="#accordionFlushExample">
                                                <div class="accordion-body p-0">
                                                    <ul class="nav nav-pills mb-3 bg-grey rounded-pill" id="pills-tab"
                                                        role="tablist">
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link active fo-btn rounded-pill"
                                                                id="pills-fd1-tab" data-bs-toggle="pill"
                                                                data-bs-target="#pills-fd1" type="button" role="tab"
                                                                aria-controls="pills-fd1" aria-selected="true">Flight
                                                                Detailes</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="pills-fd2-tab" data-bs-toggle="pill"
                                                                data-bs-target="#pills-fd2" type="button" role="tab"
                                                                aria-controls="pills-fd3" aria-selected="false">Fare
                                                                Summary</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="pills-fd3-tab" data-bs-toggle="pill"
                                                                data-bs-target="#pills-fd3" type="button" role="tab"
                                                                aria-controls="pills-fd3" aria-selected="false">Fare
                                                                Rules</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <button class="nav-link fo-btn rounded-pill"
                                                                id="pills-fd4-tab" data-bs-toggle="pill"
                                                                data-bs-target="#pills-fd4" type="button" role="tab"
                                                                aria-controls="pills-fd4" aria-selected="false">Baggage
                                                                Info</button>
                                                        </li>
                                                        <li class="nav-item" role="presentation">
                                                            <i class="fa fa-times closefo-btn" aria-hidden="true"></i>
                                                        </li>
                                                    </ul>
                                                    <div class="tab-content" id="pills-tabContent">
                                                        <div class="tab-pane fade show active" id="pills-fd1"
                                                            role="tabpanel" aria-labelledby="pills-fd1-tab"
                                                            tabindex="0">1</div>
                                                        <div class="tab-pane fade" id="pills-fd2" role="tabpanel"
                                                            aria-labelledby="pills-fd2-tab" tabindex="0">2</div>
                                                        <div class="tab-pane fade" id="pills-fd3" role="tabpanel"
                                                            aria-labelledby="pills-fd3-tab" tabindex="0">3</div>
                                                        <div class="tab-pane fade" id="pills-fd4" role="tabpanel"
                                                            aria-labelledby="pills-fd4-tab" tabindex="0">4</div>
                                                    </div>
                                                    <div class="row flight-detail-wrap align-items-center pt-1 mt-1">
                                                        <div class="col-lg-4">
                                                            <div class="flight-date">
                                                                <ul>
                                                                    <li>Economy</li>
                                                                    <li>Thursday, Jun 16 - 23:20</li>
                                                                    <li class="theme">22h 50m</li>
                                                                </ul>
                                                            </div>
                                                        </div>
                                                        <div class="col-lg-8">
                                                            <div class="flight-detail-right">
                                                                <h5><i class="fa fa-plane"></i> IST - Istanbul Airport,
                                                                    Turkish</h5>
                                                                <div
                                                                    class="flight-detail-info d-flex align-items-center p-2 py-3 bg-grey rounded mb-2">
                                                                    <img src="images/flights/flight_grid_3.png" alt="">
                                                                    <ul>
                                                                        <li>Tpm Line</li>
                                                                        <li>Operated by Airlines</li>
                                                                        <li>Economy | Flight EK585 | Aircraft BOEING
                                                                            777-300ER</li>
                                                                        <li>Adult(s): 25KG luggage free</li>
                                                                    </ul>
                                                                </div>
                                                                <h5 class="mb-0">DXB - Dubai, United Arab Emirates</h5>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>