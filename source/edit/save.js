// Cek status login saat halaman dimuat
window.onload = function() {
  var isLoggedIn = localStorage.getItem('isLoggedIn');
  var akun = document.getElementsByClassName("account");

  if (isLoggedIn === 'true') {
    akun[0].innerHTML = "Logout";
  } else {
    akun[0].innerHTML = "Login";
  }
}

function login() {
  localStorage.setItem('isLoggedIn', 'true');
  window.location.href = 'homepage.html';
  var akun = document.getElementsByClassName('account')[0];
  akun.innerHTML = 'Logout';
}

function logout() {
  localStorage.setItem('isLoggedIn', 'false');
  var akun = document.getElementsByClassName("account");
  akun[0].innerHTML = "Login";
  localStorage.removeItem('isLoggedIn');
  window.location.href = 'login.html';
}

function validateform(){  
  var user=document.getElementById("username").value;  
  var password=document.getElementById("password").value;
  if (user=="admin" && password=="123"){ 
    login()
    return true;  
  }else{  
    alert("Invalid Username of Password !!!");
    return false;  
    }
} 

function loadMenu(menuName) {
  window.location.href = "source/" + menuName + ".html";
}
function homepage(home){
  window.location.href = home + ".html";
}


