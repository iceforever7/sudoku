
function showContent(container) {
      // Hide all containers
      var containers = document.getElementsByClassName("content");
      for (var i = 0; i < containers.length; i++) {
        containers[i].style.display = "none";
      }
      // Show selected container
      document.getElementById(container).style.display = "block";
    }