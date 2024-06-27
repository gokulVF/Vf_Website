
function showForm() {
  var x = document.getElementById("form")
  if (x.style.display === "none") {
      x.style.display = "block" ;
  } else {
      x.style.display = "none" ;
  }
}

function test() {
    if(validateForm()){
        document.getElementById("input-sec234").submit();
        document.getElementById('preloader').style.display = 'block';
        document.getElementById('status').style.display = 'block';
    }
}

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



// ==================function loder
document.addEventListener("DOMContentLoaded", function() {
// Show the loader when the window starts loading
var loader = document.getElementById("loader");
var content = document.getElementById("content");

// Hide the loader and show the content when the window has finished loading
window.addEventListener("load", function() {
    loader.style.display = "none";
    content.style.display = "block";
});
});



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

function verifyPAN() {
    const pan = document.getElementById('pan').value;
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
        const resultDiv = document.getElementById('result');
        if (data.success) {
            resultDiv.innerHTML = `<p>${data.message}</p>`;
        } else {
            resultDiv.innerHTML = `<p>Error: ${data.message}</p>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}




    //   DEFAULT ADULT FUNCTIONS
    $(document).ready(function() {
        $("#adult_1").val("2");
        getAdultCount();
        });


    function getAdultCount() {
        $rowno = $("#attribute_table tr").length-2
        totaladult=0
        totalchild=0
        roominfo=[]
        totalroominf0=[]

        for(i=1;i<=$rowno;i++) {
            totaladult=parseInt(totaladult) + parseInt($("#adult_"+i).val())
            totalchild=parseInt(totalchild) + parseInt($("#child_"+i).val())
            var childAge = parseInt($("#child_"+i).val()) !== 0 ? [parseInt($("#childage_"+i).val())] : null;
            
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
                $("#age_" + i).show();
            }
        });

        
    }


    function hideForm() {
    var x = document.getElementById("form");
    if (x.style.display === "block") {
        // If the form is being hidden, validate the previous row before hiding
        var prevRowNo = $("#attribute_table tr").length - 2; // Get the previous row number
        if (!validatePreviousRow(prevRowNo)) {
            alert("Please select valid options for the Adults.");
            return; // Do not hide the form if validation fails
        }
        x.style.display = "none";
    } else {
        x.style.display = "none";
    }
}


    function add_attribute_row() {
// Get the current number of rows
var $rowno = $("#attribute_table tr").length - 1;

// Check if the limit of 6 rows has been reached
if ($rowno <= 6) {
    // Check if the previous row's selects have valid values
    var prevRowIsValid = validatePreviousRow($rowno - 1);

    if (prevRowIsValid) {
        // Add a new row
        $("#attribute_table tr:last").after("<tr  id='row" + $rowno + "'>" +
            "<td class='room_no'>Room" + $rowno + "</td>" +
            "<td><select name='attribute_name' onchange='getAdultCount()' id='adult_" + $rowno + "' class='selectbox_form  attribute_name'>" +
            "<option value='1' selected>1</option><option value='2'>2</option><option value='3'>3</option>" +
            "<option value='4'>4</option><option value='5'>5</option><option value='6'>6</option></select></td>" +
            "<td><select name='attribute_id' id='child_" + $rowno + "' onchange='getAdultCount()' class='selectbox_form  attribute_value'>" +
            "<option data-parent='0' value='0'>Select</option><option data-parent='Colour' value='1'>1</option><option data-parent='Colour' value='2'>2</option>" +
            "<option data-parent='Colour' value='3'>3</option><option data-parent='Colour' value='4'>4</option></select></td></tr>");

        for (var i = 1; i <= 4; i++) {
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
    alert("Only 6 rooms are allowed.");
    }
}

// Function to validate the selects of the previous row
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
    showChildAgeSelectors();
    getAdultCount()
}




window.addEventListener('pageshow', function(event) {
    var historyTraversal = event.persisted || (typeof window.performance != 'undefined' && window.performance.navigation.type === 2);
    if (historyTraversal) {
        // Reload the page if navigating back
        window.location.reload();
    }
});
