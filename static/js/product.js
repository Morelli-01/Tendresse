// const main_container = document.getElementById('main-container')
const myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'), {
    keyboard: false
})
const qty_selector = document.getElementById('qty-sel')
const path = '/cart/atc/'

const size_btns = document.querySelectorAll('#size-btn-group>button')
for (const btn of size_btns) {
    btn.addEventListener('click', () => {
        btn.className = 'btn btn-outline-dark m-1 active'
        for (const other_btn of size_btns) {
            if (other_btn !== btn) {
                other_btn.className = 'btn btn-outline-dark m-1'
            }
        }
    })
}


const atc_btn = document.getElementById('atc-btn')
atc_btn.addEventListener('click', () => {
    let size_btn = get_choosed_size()
    if (size_btn === '') {
        myModal.toggle()
        return
    }
    csrftoken = getCookie('csrftoken');
    msg = {
        pid: document.URL.split('/')[4],
        qty: qty_selector.selectedIndex + 1,
        size: size_btn.innerText
    }
    console.log(JSON.stringify(msg))
    fetch(path, {
        "body": JSON.stringify(msg),
        "method": "POST",
        "headers": {'X-CSRFToken': csrftoken},
        "mode": 'same-origin' // Do not send CSRF token to another domain.
    }).then(data => {
        console.log(data)
    })
    n_prod.textContent = parseInt(n_prod.textContent)+1
})

function get_choosed_size() {
    for (const btn of size_btns) {
        if (btn.className.includes('active')) {
            return btn
        }
    }
    return ''
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded',()=> {
    let size_btn_group = document.getElementById('size-btn-group')
    let size_availability_span = size_btn_group.querySelectorAll('span')
    for(const i in size_availability_span){
    if(size_availability_span[i].textContent==='0'){
        size_btns[i].disabled = true
    }
}

})

const feedbacks = document.querySelectorAll('#stars-container')

for(const feed of feedbacks){
    let n_star = feed.querySelector('span').textContent
    let stars = feed.querySelectorAll('i')
    for (const i in stars){
        if(i<n_star){
            stars[i].classList.remove('fa-regular')
            stars[i].classList.add('fa-solid')
        }
    }
}