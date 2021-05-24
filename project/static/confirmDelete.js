function deleteAadhaar(citizen_id, citizen_name) {
  console.log("Hi");
  var res = confirm(
    "Are you sure you want to delete " + citizen_name + "'s Aadhaar card?"
  );
  if (res == true) {
    $.ajax({
      url: "http://localhost:5000/delete/aadhaar_id/" + citizen_id,
      success: function () {
        alert(citizen_name + "'s Aadhaar deleted.");
        window.location.replace("http://localhost:5000/admin/manage-doc");
      },
    });
  } else {
  }
}

function deletePan(citizen_id, citizen_name) {
  console.log("Hi");
  var res = confirm(
    "Are you sure you want to delete " + citizen_name + "'s PAN card?"
  );
  if (res == true) {
    $.ajax({
      url: "http://localhost:5000/delete/pan_id/" + citizen_id,
      success: function () {
        alert(citizen_name + "'s PAN card deleted.");
        window.location.replace("http://localhost:5000/admin/manage-doc");
      },
    });
  } else {
  }
}

function deleteVoter(citizen_id, citizen_name) {
  console.log("Hi");
  var res = confirm(
    "Are you sure you want to delete " + citizen_name + "'s Voter ID card?"
  );
  if (res == true) {
    $.ajax({
      url: "http://localhost:5000/delete/voter_id/" + citizen_id,
      success: function () {
        alert(citizen_name + "'s Voter ID card deleted.");
        window.location.replace("http://localhost:5000/admin/manage-doc");
      },
    });
  } else {
  }
}

function deleteDriving(citizen_id, citizen_name) {
  console.log("Hi");
  var res = confirm(
    "Are you sure you want to delete " + citizen_name + "'s Driving licence?"
  );
  if (res == true) {
    $.ajax({
      url: "http://localhost:5000/delete/driving_id/" + citizen_id,
      success: function () {
        alert(citizen_name + "'s Driving licence deleted.");
        window.location.replace("http://localhost:5000/admin/manage-doc");
      },
    });
  } else {
  }
}
