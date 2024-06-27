// FORM --------------------------------------------------------------------------------------------

function showForm() {
    var x = document.getElementById("form")
    if (x.style.display === "none") {
        x.style.display = "block" ;
    } else {
        x.style.display = "none" ;
    }
}

function hideForm() {
    var x = document.getElementById("form");
    if (x.style.display === "block") {
        x.style.display = "none";
        mod()
    } else {
        x.style.display = "none";
    }
}

function getAdultCount() {
    $rowno = $("#attribute_table tr").length-2
    totaladult=0
    totalchild=0
    roominfo=[]
    totalroominf0=[]

    for(i=1;i<=$rowno;i++) {
        totaladult=parseInt(totaladult) + parseInt($("#adult_"+i).val())
        totalchild=parseInt(totalchild) + parseInt($("#child_"+i).val())
        // var childAge = parseInt($("#child_"+i).val()) !== 0 ? [parseInt($("#childage_"+i).val())] : null;
        
        // Handle the first row separately
        // var childrenCountFirstRow = parseInt($("#child_1").val());
        // var childAgeFirstRow = [];

        // for (var k = 1; k <= childrenCountFirstRow; k++) {
        //     var ageFirstRow = parseInt($("#childage_" + k).val());
        //     if (!isNaN(ageFirstRow)) {
        //         childAgeFirstRow.push(ageFirstRow);
        //     }
        // }

        // roominfo[0] = {
        //     "NoOfAdults": parseInt($("#adult_1").val()),
        //     "NoOfChild": parseInt($("#child_1").val()),
        //     "ChildAge": childAgeFirstRow
        // };
        
        var childrenCount = parseInt($("#child_" + i).val());
        var childAge = [];

        for (var j = 1; j <= childrenCount; j++) {
        var age = parseInt($("#childage_" + i + "_" + j).val());
        if (!isNaN(age)) {
            childAge.push(age);
        }
        
    }
        roominfo[i-1]={"NoOfAdults":parseInt($("#adult_"+i).val()) ,"NoOfChild":parseInt($("#child_"+i).val()),"ChildAge":childAge }
        // roominfo[i-1]={"NoOfAdults":parseInt($("#adult_"+i).val()) ,"NoOfChild": parseInt($("#child_"+i).val()),"ChildAge": childAge }
    }

    var roomCount = $rowno + " " + "Room" +" " + "&" + " " + totaladult +" " + "Adults";
    document.getElementById('room').value = roomCount;
    
    showChildAgeSelectors()

    // console.log($rowno,totaladult,totalchild)
    totalroominf0={"TotalRooms":$rowno,"NoOfAdults":totaladult,"NoOfChild":totalchild}
    console.log(roominfo,totalroominf0)
    console.log(totalroominf0)

    document.getElementById('roomInfoInput').value = JSON.stringify(roominfo);
    document.getElementById('totalRoomInfoInput').value = JSON.stringify(totalroominf0);
    document.getElementById('totalNoOfRooms').value = $rowno;

    // document.getElementById('roomInfoInput').value = JSON.stringify(roominfo);
    // document.getElementById('totalRoomInfoInput').value = JSON.stringify({
    //     "TotalRooms": $rowno,
};

function showChildAgeSelectors() {
    // Hide all child age selectors first
    $("[id^=childage_]").hide();
    $("[id^=age_]").hide();

    // Get the number of children selected in the first row
    var childrenCountFirstRow = parseInt($("#child_1").val());

    // Show the corresponding child age selectors in the first row
    for (var i = 1; i <= childrenCountFirstRow; i++) {
        $("#childage_" + i).show();
        $("#age_" + i).show();
    }

    // Iterate through each dynamically added row
    $("#attribute_table tr").each(function(index, row) {
        var rowNumber = index + 1;
        var childrenCount = parseInt($("#child_" + rowNumber).val());

        // Show the corresponding child age selectors for each dynamically added row
        for (var i = 1; i <= childrenCount; i++) {
            $("#childage_" + rowNumber + "_" + i).show();
            document.getElementById("age_"+i).innerHTML = "Age "+ i;
            $("#age_" + i).show();
        }
    });
}

function add_attribute_row() {
    // Get the current number of rows
    var $rowno = $("#attribute_table tr").length - 1;

    // Check if the limit of 6 rows has been reached
    if ($rowno <= 6) {
        var prevRowIsValid = validatePreviousRow($rowno - 1);

        if (prevRowIsValid) {
        // Add a new row
        $("#attribute_table tr:last").after("<tr id='row" + $rowno + "'>" +
            "<td class='room_no'>Room" + $rowno + "</td>" +
            "<td><select name='attribute_name' onchange='getAdultCount()' id='adult_" + $rowno + "' class='selectbox_form  attribute_name'>" +
            "<option value='1' selected>1</option><option value='2'>2</option><option value='3'>3</option>" +
            "<option value='4'>4</option><option value='5'>5</option><option value='6'>6</option></select></td>" +
            "<td><select name='attribute_id' id='child_" + $rowno + "' onchange='getAdultCount()' class='selectbox_form  attribute_value'>" +
            "<option data-parent='0' value='0'>Select</option><option data-parent='Colour' value='1'>1</option><option data-parent='Colour' value='2'>2</option>" +
            "<option data-parent='Colour' value='3'>3</option><option data-parent='Colour' value='4'>4</option></select></td></tr>");

            for (var i = 1; i <=4 ; i++) {
            $("#row" + $rowno).append("<td><select id='childage_" + $rowno + "_" + i + "' onchange='getAdultCount()' class='selectbox_form  attribute_value'>" +
                "<option data-parent='Colour' value='1'>1</option><option data-parent='Colour' value='2'>2</option>" +
                "<option data-parent='Colour' value='3'>3</option><option data-parent='Colour' value='4'>4</option><option data-parent='Colour' value='5'>5</option>" +
                "<option data-parent='Colour' value='6'>6</option><option data-parent='Colour' value='7'>7</option><option data-parent='Colour' value='8'>8</option>" +
                "<option data-parent='Colour' value='9'>9</option><option data-parent='Colour' value='10'>10</option><option data-parent='Colour' value='11'>11</option>" +
                "<option data-parent='Colour' value='12'>12</option></select></td>");
        }

        // Call the getAdultCount function
        showChildAgeSelectors();
        getAdultCount();
    } else {
        // Alert the user or handle the case where the previous row's selects are not valid
        alert("Please select valid options for the Adults.");
    } 
    } else {
        // Alert the user or handle the case where the limit is reached
        alert("Only 6 rooms are allowed..");
    }
}

// Function to validate the selects of the previous row--------------------------------------------
function validatePreviousRow(prevRowNo) {
// Check if the previous row's selects have valid values
var adultValue = $("#adult_" + prevRowNo).val();
// var childValue = $("#child_" + prevRowNo).val();

// Return true if both selects have valid values, otherwise false
return adultValue !== "0" ;
}

function del_att_row() {
    rowno = $("#attribute_table tr").length-2 ;
    if(rowno > 1)
    $('#row' + rowno).remove();
    getAdultCount()
}

// FILTER HOTEL NAME --------------------------------------------------------------------------------------

function sortHotels(criteria) {
    var hotelList = document.getElementById('hotelList');
    var hotels = Array.from(hotelList.getElementsByClassName('hotel'));

    var sortOrder = hotelList.getAttribute('data-sort-order') || 'asc';

    hotels.sort(function(a, b) {
        var aValue = a.getAttribute('data-' + criteria);
        var bValue = b.getAttribute('data-' + criteria);

        // Handle numeric or string comparisons based on the criteria
        if (criteria === 'Price' || criteria === 'Rating') {
            return sortOrder === 'asc' ? aValue - bValue : bValue - aValue;
        } else if (criteria === 'Name') {
            return sortOrder === 'asc' ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
        }
    });

    // Clear the existing hotel list
    hotelList.innerHTML = '';

    // Append the sorted hotels to the list
    hotels.forEach(function(hotel) {
        hotelList.appendChild(hotel);
    });

    // Toggle sort order for the next click
    hotelList.setAttribute('data-sort-order', sortOrder === 'asc' ? 'desc' : 'asc');
}

// FILTER HOTEL PRICE ---------------------------------------------------------------------------

function filterHotelsByPrice(minPrice,maxPrice) {
    // priceInput = document.querySelectorAll(".price-input input")
   //  var minPrice = parseInt(priceInput[0].value);
   //  var maxPrice = parseInt($(".input-max").val());

     console.log("Filtering by Price:", minPrice, maxPrice);

     $(".hotel").each(function () {
         var hotelPrice = parseInt($(this).data("price"));

         console.log("Hotel Price:", hotelPrice);

         if (hotelPrice >= minPrice && hotelPrice <= maxPrice) {
             $(this).show();
         } else {
             $(this).hide();
         }
     });
}
 
//  FILTER HOTEL STARS  -----------------------------------------------------
function filterHotelsByRating() {
    var selectedRatings = [];
    // Iterate over checked star rating checkboxes
    $('input[name="checklist"]:checked').each(function () {
        selectedRatings.push($(this).val());
    });

    $(".hotel").each(function () {
        var hotelRating = parseInt($(this).data("rating"));

        // Show the hotel if it matches any of the selected ratings, or if no ratings are selected
        if (selectedRatings.length === 0 || selectedRatings.includes(hotelRating.toString())) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}

// Attach the filter function to the checkbox change event
$('input[name="checklist"]').on("change", function () {
    filterHotelsByRating();
});

// Submit Functions-----------------------------------------------------------
function mod() {
    if(validateForm()){
        document.getElementById("modify-sec").submit();
        document.getElementById('preloader').style.display = 'block';
        document.getElementById('status').style.display = 'block';
    }
}

// HOTEL ROOM FUNCTIONS -----------------------------------------------------------

function hiderooms(hotelCode) {
    document.getElementById(hotelCode).style.display = 'none';
    var showButton = document.getElementById(hotelCode+'2');
    var hideButton = document.getElementById(hotelCode+'1');
    showButton.style.display = 'block';
    hideButton.style.display = 'none';
    // document.getElementById(hotelCode).style.display = 'none';
}

function handleSelectRoom(hotelCode, traceId, resultIndex, tokenId) {
    // Your existing code for hiding rooms...
    document.getElementById(hotelCode).innerHTML = "<div class='w-50 mx-auto d-flex align-items-center'><div id='loading' class='w-50 text-end'></div><p class='mb-0 theme1'>Loading....</p></div>"
    // AJAX request to send data to views.py
    var showButton = document.getElementById(hotelCode+'2');
    var hideButton = document.getElementById(hotelCode+'1');
    showButton.style.display = 'none';
    hideButton.style.display = 'block';
    document.getElementById(hotelCode).style.display='block'
    var csrftoken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    $.ajax({
        url: "/get_room_details/",  // Replace with the actual URL of your views.py
        type: "POST",
        data: {
            'hotelCode': hotelCode,
            'traceId': traceId,
            'resultIndex': resultIndex,
            'tokenId': tokenId
        },
        headers: {
            'X-CSRFToken': csrftoken  // Include the CSRF token in the headers
        },
        success: function(response) {
            // var roomDetailsData = response.room_details;
            // updateRoomDetails(roomDetailsData, hotelCode);
            document.getElementById(hotelCode).innerHTML = response.room_details_html;
            // console.log(roomDetailsData);
        },
        error: function(error) {
            document.getElementById(hotelCode).innerHTML = "<div class='w-100 mx-auto text-center border-t align-items-center pt-2'><img src='/VFpages/static/image/booking/No-Hotel-Avail2.jpg' alt='' style='width: 60px;' class='me-3'><a class='black fw-bold'>Sorry, No Rooms Available! <span class='theme2 ms-2' style='font-size: 14px;'>Modify Search & Try Again</span></a></div>"
            console.error(error);
        }
    });
}

// STAR FUNCTIONS ----------------------------------------------------------------

function updateStars() {
    var starInput = document.getElementById('starInput');
    var starViews = document.querySelectorAll('.star-view');

    var starValue = parseInt(starInput.value);

    starViews.forEach(function(starView, index) {
        if (index + 3 === starValue) {
            starView.style.display = 'block';
            markStars(starView, index + 3);
        } else {
            starView.style.display = 'none';
        }
    });
}

function markStars(starView, count) {
    var stars = starView.querySelectorAll('.fa-star');
    for (var i = 0; i < count; i++) {
        stars[i].classList.add('checked');
    }
}

// Validate form Functions---------------------------------------------------------------------------
function validateForm() {
    var des = document.getElementsByClassName("des")[0].value.trim();
    var room = document.getElementById("room").value.trim();
    if (des === "") {
        document.getElementById("des_error").innerHTML="Please Enter Your Destination";
        return false; // Prevent form submission
    } 
        if (room === "") {
        alert("Please Enter Room Information");
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}

// Search Functions---------------------------------------------------------------------------
$(function () {
    $("#autocompleteInput").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/search_destinations",
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
            $("#cityIdInput").val(ui.item.cityID);
            $("#countryCodeInput").val(ui.item.countryCode);
        }
    });
});

// FORM ROOM VALUE FUNCTIONS -----------------------------------------------------------
$(document).ready(function() {
    var roomDetails = JSON.parse($("#roomDetails").val());
    var roomsCount = roomDetails.length;
    var html = "";

    for (var i = 1; i <= roomsCount; i++) { 
        html += "<tr id='row" + i + "' class='room-info'>";
        html += "<td class='room_no'>Room" + i + "</td>"; 
        html += "<td>";
        html += "<select name='attribute_name' class='selectbox_form attribute_name' id='adult_" + i + "' onchange='getAdultCount()'>";
        html += "<option value='1'>1</option>";
        html += "<option value='2'>2</option>";
        html += "<option value='3'>3</option>";
        html += "<option value='4'>4</option>";
        html += "<option value='5'>5</option>";
        html += "<option value='6'>6</option>";
        html += "</select>";
        html += "</td>";
        html += "<td>";
        html += "<select name='attribute_id' id='child_" + i + "' class='selectbox_form attribute_value' onchange='updateChildAges(" + i + ");getAdultCount()'>";
        html += "<option data-parent='0' value='0'>Select</option>";
        html += "<option value='1'>1</option>";
        html += "<option value='2'>2</option>";
        html += "<option value='3'>3</option>";
        html += "<option value='4'>4</option>";
        html += "</select>";
        html += "</td>";

        // Initially hide all child age select tags
        for (var j = 1; j <= 4; j++) {
            html += "<td>";
            html += "<select name='attribute_child' id='childage_" + i + "_" + j + "' class='selectbox_form attribute_value' style='display: none' onchange='getAdultCount()'>";
            // html += "<option data-parent='0'>Select</option>";
            for (var age = 1; age <= 12; age++) {
                html += "<option value='" + age + "'>" + age + "</option>";
            }
            html += "</select>";
            html += "</td>";
        }

        html += "</tr>";
    }

    $("#attribute_table").append(html);

    // Set values for adult and child selects
    $.each(roomDetails, function(i, item) {
        $("#adult_" + (i + 1)).val(item.NoOfAdults);
        $("#child_" + (i + 1)).val(item.NoOfChild);
        
        var childAges = item.ChildAge;
        for (var j = 0; j < childAges.length; j++) {
            $("#childage_" + (i + 1) + "_" + (j + 1)).val(childAges[j]);
        }

        // Show child age select tags up to the selected child count
        for (var k = 1; k <= item.NoOfChild; k++) {
            $("#childage_" + (i + 1) + "_" + k).show();
            document.getElementById("age_"+k).innerHTML = "Age "+ k;
        }
    });
});

// Update child age Functions------------------------------------------------------
function updateChildAges(roomIndex) {
    var childCount = $("#child_" + roomIndex).val();
    for (var i = 1; i <= 4; i++) {
        if (i <= childCount) {
            $("#childage_" + roomIndex + "_" + i).show();
        } else {
            $("#childage_" + roomIndex + "_" + i).hide();
        }
    }
}


// Room Booking Functions------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {
    var hiddenInput = document.getElementById('select-5');
    var selectElement = document.getElementById('nation');
    var selectedValue = hiddenInput.value;

    for (var i = 0; i < selectElement.options.length; i++) {
        if (selectElement.options[i].value === selectedValue) {
            selectElement.options[i].selected = true;
            break;
        }
    }
});

function bookRoom() {
var hiddenPhoneNumber = document.getElementById('hiddenPhoneNumber');
    
if (hiddenPhoneNumber && hiddenPhoneNumber.value) {
var form = document.createElement('form');
document.getElementById('preloader').style.display = 'block';
document.getElementById('status').style.display = 'block';
form.method = 'POST';
form.action = '/hotelreview/';
var roomJsonList = document.getElementById('hide-123').value;
var datalist = document.getElementById('data-123').value;
var unescapedValue = datalist.replace(/&quot;/g, '"');
var parsedJSON = JSON.parse(unescapedValue);
var unescapedValue1 = roomJsonList.replace(/&quot;/g, '"');
var parsedJSON1 = JSON.parse(unescapedValue1);
var hotelCode = parsedJSON.HotelCode; 
var hotelId = hotelCode + 'A';
var hotelNameInputElement = document.getElementById(hotelId);
if (hotelNameInputElement) {
    var hotelName = hotelNameInputElement.value;
    var csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    var csrfTokenField = document.createElement('input');
    csrfTokenField.type = 'hidden';
    csrfTokenField.name = 'csrfmiddlewaretoken';
    csrfTokenField.value = csrfToken;
    form.appendChild(csrfTokenField);
    var roomJsonElement = document.createElement('input');
    roomJsonElement.type = 'hidden';
    roomJsonElement.name = 'roomJsonElement';
    roomJsonElement.value = JSON.stringify(parsedJSON1);
    form.appendChild(roomJsonElement);
    var hotelNameField = document.createElement('input');
    hotelNameField.type = 'hidden';
    hotelNameField.name = 'hotelName';
    hotelNameField.value = hotelName;
    form.appendChild(hotelNameField);
    var hide123Value = document.createElement('input');
    hide123Value.type = 'hidden';
    hide123Value.name = 'hide123Value';
    hide123Value.value = JSON.stringify(parsedJSON);
    form.appendChild(hide123Value);
    var categoryid1 = document.getElementById('categoryid').value;
    var categoryidField = document.createElement('input');
    categoryidField.type = 'hidden';
    categoryidField.name = 'categoryid1';
    categoryidField.value = categoryid1;
    form.appendChild(categoryidField);
    document.body.appendChild(form);
    form.submit();
} else {
    console.error('Hotel name input element not found.');
}
} else {
    console.log("noo result")
    $("#log-btn-switch").click();
}
}

// SLIDER RANGE FUNCTION ---------------------------------------------------------
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

// Date Functions-----------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', function() {
    // Get the initial formatted dates from hidden inputs
    var formattedCheckin = document.getElementById('checkin').value;
    var formattedCheckout = document.getElementById('checkout').value;

    // Get references to the date input fields
    var startDateInput = document.getElementById('check-in');
    var endDateInput = document.getElementById('check-out');

    // Set the initial values from the hidden inputs
    startDateInput.value = formattedCheckin;
    endDateInput.value = formattedCheckout;

    // Set the minimum date for check-in to today
    var today = new Date();
    var year = today.getFullYear();
    var month = ('0' + (today.getMonth() + 1)).slice(-2);
    var day = ('0' + today.getDate()).slice(-2);
    var todayString = year + '-' + month + '-' + day;
    startDateInput.min = todayString;

    // Function to set the next day for check-out based on the selected check-in date
    function setNextDate() {
        var startDate = new Date(startDateInput.value);
        if (!isNaN(startDate.getTime())) {
            var nextDate = new Date(startDate);
            nextDate.setDate(startDate.getDate() + 1);

            var nextYear = nextDate.getFullYear();
            var nextMonth = ('0' + (nextDate.getMonth() + 1)).slice(-2);
            var nextDay = ('0' + nextDate.getDate()).slice(-2);
            var nextDateString = nextYear + '-' + nextMonth + '-' + nextDay;

            endDateInput.value = nextDateString;
            endDateInput.min = nextDateString;
        }
    }

    // Attach event listener to the check-in date input
    startDateInput.addEventListener('change', setNextDate);

    // Set the initial next date for check-out based on the initial check-in date
    setNextDate();
});

// View Details click functions----------------------------------------------------------------------------
document.getElementById('viewDetailsLink').addEventListener('click', function(event) {
    event.preventDefault();
        document.getElementById('preloader').style.display = 'block';
        document.getElementById('status').style.display = 'block';
        console.log('printed success 787')
    })

























// COMMENTS____________________________________

 // Attach the filter function to the input change event
 // $(".input-min, .input-max").on("input", function () {
 //     filterHotelsByPrice();
 // });

// function bookRoom(roomIndices) {
//     var roomJsonElement = roomIndices;
//     var hotelName = document.querySelector('.hotel-name p').innerText;
//     var queryParams = 'roomJsonElement=' + encodeURIComponent(JSON.stringify(roomJsonElement)) +
//                       '&hotelName=' + encodeURIComponent(hotelName);

//     var csrftoken = document.cookie.match(/csrftoken=([\w-]+)/)[1];

//     // Assuming you have jQuery available
//     $.ajax({
//         url: '/hotelreview/?' + queryParams,
//         type: 'GET',
//         headers: {
//             'X-CSRFToken': csrftoken  // Include the CSRF token in the headers
//         },
//         success: function (response) {
//             console.log(response);
//             var newWindow = window.open();
//             newWindow.document.write(response.html);
//             // Handle the response as needed
//         },
//         error: function (error) {
//             console.error(error);
//         }
//     });
// }


// function bookRoom(hotelcode, roomIndices) {
//     var roomJsonElement = roomIndices;
//     var hotelId = hotelcode + 'A';

//     // Use getElementById to get the input element by ID
//     var hotelNameInputElement = document.getElementById(hotelId);
//     var hide123Value = document.getElementById('hide-123').value;
//     // console.log(room123Value)
//     // Check if the input element exists
//     if (hotelNameInputElement) {
//         var hotelName = hotelNameInputElement.value;
//         console.log(hotelName);
//         var queryParams = 'roomJsonElement=' + encodeURIComponent(JSON.stringify(roomJsonElement)) +
//             '&hotelName=' + encodeURIComponent(hotelName) + '&hide123Value=' + encodeURIComponent(JSON.stringify(hide123Value));

//         var csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)[1];

//         // Construct the URL with the CSRF token
//         var url = '/hotelreview/?' + queryParams + '&csrfmiddlewaretoken=' + csrfToken;

//         // Open the URL in a new tab or window
//         var newWindow = window.open(url, '_blank');

//         // If the new window/tab was successfully opened, handle it as needed
//         if (!newWindow) {
//             console.error('Unable to open new window/tab.');
//         }
//     } else {
//         console.error('Hotel name input element not found.');
//     }
// }

// function bookRoom() {{
//     var roomJsonList =   document.getElementById('hide-123').value;
//     var datalist =   document.getElementById('data-123').value;
//     var unescapedValue = datalist.replace(/&quot;/g, '"');
//     // Parse the unescaped value as JSON
//     var parsedJSON = JSON.parse(unescapedValue);
//     var unescapedValue1 = roomJsonList.replace(/&quot;/g, '"');
//     // Parse the unescaped value as JSON
//     var parsedJSON1 = JSON.parse(unescapedValue1);
//     console.log(roomJsonList)
//     console.log(parsedJSON)
//     var hotelCode = parsedJSON.HotelCode; 
//     console.log(hotelCode)
//     hotelId = hotelCode + 'A';
//     var hotelNameInputElement = document.getElementById(hotelId);
//     if (hotelNameInputElement) {{
//         var hotelName = hotelNameInputElement.value;
//         var csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
//         var queryParams = 'roomJsonElement=' + encodeURIComponent(JSON.stringify(parsedJSON1)) +
//             '&hotelName=' + encodeURIComponent(hotelName) + '&hide123Value=' + encodeURIComponent(JSON.stringify(parsedJSON)) +
//             '&csrfmiddlewaretoken=' + encodeURIComponent(csrfToken);

//         var url = '/hotelreview/';
//         var xhr = new XMLHttpRequest();
//         xhr.open('POST', url, true);
//         xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
//         xhr.setRequestHeader('X-CSRFToken', csrfToken);
//         xhr.onreadystatechange = function() {{
//             if (xhr.readyState === 4 && xhr.status === 200) {{
//                 var newWindow = window.open("", "_blank");
//                 newWindow.document.write(xhr.responseText);
//             }}
//         }};
//         xhr.send(queryParams);
//     }} else {{
//         console.error('Hotel name input element not found.');
//     }}
// }}

// function bookRoom() {
//     var roomJsonList = document.getElementById('hide-123').value;
//     var datalist = document.getElementById('data-123').value;
//     var unescapedValue = datalist.replace(/&quot;/g, '"');
//     // Parse the unescaped value as JSON
//     var parsedJSON = JSON.parse(unescapedValue);
//     var unescapedValue1 = roomJsonList.replace(/&quot;/g, '"');
//     // Parse the unescaped value as JSON
//     var parsedJSON1 = JSON.parse(unescapedValue1);
//     console.log(roomJsonList);
//     console.log(parsedJSON);
//     var hotelCode = parsedJSON.HotelCode; 
//     console.log(hotelCode);
//     hotelId = hotelCode + 'A';
//     var hotelNameInputElement = document.getElementById(hotelId);
//     if (hotelNameInputElement) {
//         var hotelName = hotelNameInputElement.value;
//         var csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
//         var queryParams = 'roomJsonElement=' + encodeURIComponent(JSON.stringify(parsedJSON1)) +
//             '&hotelName=' + encodeURIComponent(hotelName) + '&hide123Value=' + encodeURIComponent(JSON.stringify(parsedJSON)) +
//             '&csrfmiddlewaretoken=' + encodeURIComponent(csrfToken);
            
//         var url = '/hotelreview/';
//         fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/x-www-form-urlencoded',
//                 'X-CSRFToken': csrfToken
//             },
//             body: queryParams
//         })
//         .then(response => response.text())
//         .then(data => {
//             var newWindow = window.open("", "_blank");
//             newWindow.document.write(data);
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     } else {
//         console.error('Hotel name input element not found.');
//     }
// }


// // Assuming you have jQuery included in your project
// $('.view-details-link').on('click', function(event) {
//     event.preventDefault();

//     var hotelCode = $(this).data('hotel-code');
//     var traceId = $(this).data('trace-id');
//     var resultIndex = $(this).data('result-index');
//     var tokenId = $(this).data('token-id');

//     // Your AJAX request to send data to views.py
//     var csrftoken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
//     $.ajax({
//         url: "/your_view/",  
//         type: "POST",
//         data: {
//             'hotelCode': hotelCode,
//             'traceId': traceId,
//             'resultIndex': resultIndex,
//             'tokenId': tokenId
//         },
//         headers: {
//             'X-CSRFToken': csrftoken  // Include the CSRF token in the headers
//         },
//         success: function(response) {
//             // Handle the response from the server
//             if (response.error) {
//                 console.log('hii')
//                 console.error(response.error);
//             } else {
//                 // document.body.innerHTML = response.html;
//                 var newWindow = window.open();
//                 newWindow.document.write(response.html);
//                 console.log(response.html)
//                 console.log('hello')
//                 // updateRoomDetails(response.room_details, hotelCode);
//             }
//         },
//         error: function(error) {
//             // Handle errors if any
//             console.error(error);
//         }
//     });
// });


  
