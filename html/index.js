document.addEventListener("DOMContentLoaded", function() {
  function showMessage() {
    let message = "Your message was sent";
    alert(message);
  }

  const button = document.getElementById("send-button");

  button.addEventListener("click", showMessage);
});
