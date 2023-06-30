const userAction = async () => { 
  const response = await fetch("http://localhost:5000/patients?count=20");
  const myJson = await response.json(); 

  myJson.forEach(element => {
    console.log(element.firstName);
    var root = document.getElementById("root");
    var html = root.innerHTML;
    root.innerHTML += '</div><div class="display"><div> ' + element.firstName + '</div><div> ' + element.email + ' </div><div> ' + element.nhsNumber + ' </div></div>';
  });
  }