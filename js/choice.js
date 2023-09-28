
function showContent(container) {
      // Hide all containers
      var containers = document.getElementsByClassName("content");
      for (var i = 0; i < containers.length; i++) {
        containers[i].style.display = "none";
      }
      // Show selected container
      document.getElementById(container).style.display = "block";
    }

    //尝试使用多线程，但不知为何无法创建new worker
    //self.postMessage("Game");