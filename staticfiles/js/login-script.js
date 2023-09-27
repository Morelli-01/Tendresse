const password_field = document.querySelector('#password')
const show_psw_checkbox_label = document.querySelector('#sh-checkbox-label')
const show_psw_checkbox = document.querySelector('#sh-checkbox')

show_psw_checkbox.addEventListener("click", (e) => {
    if (show_psw_checkbox.checked) {
        password_field.type = 'text';
        show_psw_checkbox_label.textContent = 'Nascondi Password'
    } else {
        password_field.type = 'password';
        show_psw_checkbox_label.textContent = 'Mostra Password'
    }
});

var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'), {
    keyboard: false
})
if (document.URL.toString().includes('registered')) {
    myModal.toggle()
}
