// FLIGHT CITY SEARCH
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

// FORM - ADULT COUNT - ONE TRIP
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

// FORM - ADULT COUNT - ROUND TRIP
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

// SUBMIT FORM
function submitOneTripForm() {
    if(validateOneTripForm()){
        document.getElementById("one-trip").submit();
       console.log("submitted ot")
    }
}

// VALIDATE FORM  - ROUND TRIP
function validateRoundTripForm() {
    var from = document.getElementById("roundtripfrom").value;
    var to = document.getElementById("roundtripto").value;
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

// DIRECT FLIGHTS FUNCTION - ONE TRIP
 var checkbox = document.getElementById("flexSwitchCheckDefault");
 var resultInput = document.getElementById("resultValue");

 function updateResult() {
     var formattedValue = checkbox.checked ? "True" : "False";
     resultInput.value = formattedValue;
     console.log("DirectFlight is now: " + formattedValue);
 }

 // Add an event listener to detect changes
 checkbox.addEventListener("change", updateResult);

 updateResult();


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



window.addEventListener('pageshow', function(event) {
    var historyTraversal = event.persisted || (typeof window.performance != 'undefined' && window.performance.navigation.type === 2);
    if (historyTraversal) {
        // Reload the page if navigating back
        window.location.reload();
    }
});