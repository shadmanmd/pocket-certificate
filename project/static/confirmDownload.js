function confirmAadhaar(aadhaar_key, e) {
  var key = prompt("Enter the private key for your Aadhaar");
  if (key == aadhaar_key) {
    console.log("Hi");
  } else {
    alert("Wrong private key.");
    e.preventDefault();
  }
}

function confirmPan(pan_key, e) {
  var key = prompt("Enter the private key for your PAN");
  if (key == pan_key) {
    console.log("Hi");
  } else {
    alert("Wrong private key.");
    e.preventDefault();
  }
}

function confirmVoter(voter_key, e) {
  var key = prompt("Enter the private key for your Voter ID");
  if (key == voter_key) {
    console.log("Hi");
  } else {
    alert("Wrong private key.");
    e.preventDefault();
  }
}

function confirmDriving(driving_key, e) {
  var key = prompt("Enter the private key for your Driving Licence");
  if (key == driving_key) {
    console.log("Hi");
  } else {
    alert("Wrong private key.");
    e.preventDefault();
  }
}
