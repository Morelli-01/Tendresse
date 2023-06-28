var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'), {
    keyboard: false
})
if (document.URL.toString().includes('edited')) {
    myModal.toggle()
}