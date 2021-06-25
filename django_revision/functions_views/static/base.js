function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

  function myFunction(){
    console.log("yes");
    var str = document.getElementsByClassName('code_syntex');
    for(i = 0; i<str.length ; i++){
        str[i].innerHTML = str[i].innerHTML.replaceAll('\\\\' , '\\');

    }

}