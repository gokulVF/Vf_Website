// DATE
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
// SHOW PAX FORM
function showOnePaxForm() {
    var flightForm = document.getElementById("pas_form_onetrip")
    if(flightForm.style.display === "none") {
        flightForm.style.display = "block";
    } else {
        flightForm.style.display = "none"
    }
}

// PAXFORM ONETRIP
// SHOW PAX FORM
function showRoundPaxForm() {
    var flightForm = document.getElementById("pas_form_roundtrip")
    if(flightForm.style.display === "none") {
        flightForm.style.display = "block";
    } else {
        flightForm.style.display = "none"
    }
}