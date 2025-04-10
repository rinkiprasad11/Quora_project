
function showModal() {
    var modal = document.getElementById("logoutModal");
    modal.style.display = "block";
}


function hideModal() {
    var modal = document.getElementById("logoutModal");
    modal.style.display = "none";
}


window.onclick = function(event) {
    var modal = document.getElementById("logoutModal");
    if (event.target === modal) {
        hideModal();
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', function(event) {
        const username = document.querySelector('input[name="username"]').value;
        const password = document.querySelector('input[name="password"]').value;
        
        if (!username || !password) {
            alert("Both fields are required!");
            event.preventDefault();  
        }
    });
});
