document.addEventListener('DOMContentLoaded', function() {
    var launchButton = document.getElementById('launchButton');
  
    launchButton.addEventListener('click', function() {
      var paramInput = document.getElementById('paramInput');
      var parameter = paramInput.value;
  
      // Send the parameter to the Python script using a GET request
      var scriptUrl = 'http://localhost:5000/launch?param=' + encodeURIComponent(parameter);
      var xhr = new XMLHttpRequest();
      xhr.open('GET', scriptUrl, true);
      xhr.send();
    });
  });
