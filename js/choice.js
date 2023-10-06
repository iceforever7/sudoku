
function showContent(container) {
      // Hide all containers
      var containers = document.getElementsByClassName("content");
      for (var i = 0; i < containers.length; i++) {
        containers[i].style.display = "none";
      }
      // Show selected container
      document.getElementById(container).style.display = "block";
}
var solve_container;
function showsolve_content(solve)
{
	solve_container=solve;
}

function changestyle()
{
	console.log(solve_container);
	var solve_containers = document.getElementsByClassName("solve_content");
    for (var i = 0; i < solve_containers.length; i++) {
      solve_containers[i].style.display = "none";
    }
	document.getElementById(solve_container).style.display = "block";
}