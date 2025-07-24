document.addEventListener('DOMContentLoaded', function () {
  const nameInput = document.querySelector('input[name="name"]');
  const messageInput = document.querySelector('input[name="message"]');
  const form = document.getElementById('myForm');

  // Function for handling name input validation on Tab key
  function handleNameTab() {
    const inputValue = nameInput.value.trim().toLowerCase();

    if (inputValue === 'p10') {
      alert('Input entered: ' + inputValue);
      console.log("You entered: p10");
    } else if (inputValue.startsWith('p')) {
      alert('Input entered: ' + inputValue);
      console.log("You entered something starting with p");
    } else {
      console.log("You entered something else:", inputValue);
    }
  }

  // Handle Tab in the "name" input
  nameInput.addEventListener('keydown', function (event) {
    if (event.key === 'Tab') {
      handleNameTab(); // Call the function when Tab is pressed
    }
  });

  // Handle Tab in the "message" input
  messageInput.addEventListener('keydown', function (event) {
    if (event.key === 'Tab') {
        handleNameTab(); // Call the function when Tab is pressed
    }
  });

  // Form submit handler
  form.addEventListener('submit', function (event) {
    event.preventDefault();

    const name = nameInput.value;
    const message = messageInput.value;

    console.log('Name:', name);
    console.log('Message:', message);
    alert(`Submitted!\nName: ${name}\nMessage: ${message}`);
  });
});
