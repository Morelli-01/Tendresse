const cc_detail = document.getElementById('cc-detail')
const pp_detail = document.getElementById('pp-detail')
const collect_detail = document.getElementById('collect-detail')

const cc_detail_in = document.getElementById('cc-detail-in')
const pp_detail_in = document.getElementById('pp-detail-in')
const collect_detail_in = document.getElementById('collect-detail-in')

const cc_detail_div = document.getElementById('cc-detail-div')
const pp_detail_div = document.getElementById('pp-detail-div')
const collect_detail_div = document.getElementById('collect-detail-div')

cc_detail_div.addEventListener('click', () => {
    cc_detail.className = "collapse show"
    pp_detail.className = "collapse"
    collect_detail.className = "collapse"

    pp_detail_in.checked = false
    collect_detail_in.checked = false
    cc_detail_in.checked = true

})
pp_detail_div.addEventListener('click', () => {
    pp_detail.className = "collapse show"
    cc_detail.className = "collapse"
    collect_detail.className = "collapse"
    cc_detail_in.checked = false
    collect_detail_in.checked = false
    pp_detail_in.checked = true

})
collect_detail_div.addEventListener('click', () => {
    collect_detail.className = "collapse show"
    pp_detail.className = "collapse"
    cc_detail.className = "collapse"
    pp_detail_in.checked = false
    cc_detail_in.checked = false
    collect_detail_in.checked = true


})

const checkout_btn = document.getElementById('complete-order-btn')
const cc_modal = new bootstrap.Modal(document.getElementById('cc-modal'), {
    keyboard: false
})
const collect_modal = new bootstrap.Modal(document.getElementById('collect-modal'), {
    keyboard: false
})
const qty_unavailable_modal = new bootstrap.Modal(document.getElementById('qty-unavailable-modal'), {
    keyboard: false
})
checkout_btn.addEventListener('click', () => {
    let payment_method;
    let msg;
    if (cc_detail_in.checked) {
        payment_method = 'cc'
        let cc_name = document.getElementById('cc-name')
        let cc_number = document.getElementById('cc-number')
        let cc_exp = document.getElementById('cc-exp')
        let cc_cvv = document.getElementById('cc-cvv')
        if (cc_name.value === '' || cc_number.value === '' || cc_exp.value === '' || cc_cvv.value === '') {
            cc_modal.toggle()
        }
        msg = {
            payment_method: payment_method,
            cc: {
                name: cc_name,
                num: cc_number,
                exp: cc_exp,
                cvv: cc_cvv,
            }
        }
    } else if (pp_detail_in.checked) {
        payment_method = 'pp'
        msg = {
            payment_method: payment_method,
        }
    } else if (collect_detail_in.checked) {
        payment_method = 'collect'
        msg = {
            payment_method: payment_method,
        }
    }
    let csrftoken = getCookie('csrftoken');
    let path = '/checkout/2/'
    fetch(path, {
        body: JSON.stringify(msg),
        method: "POST",
        redirect: "follow",
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin' // Do not send CSRF token to another domain.
    }).then(response => {
        console.log(response)
        if (response.ok) {
            // La richiesta è stata redirezionata
            window.location.href = '/account/orders/'
        }else if (response.status === 409){
            collect_modal.toggle()
        }else if(response.status===406){
            qty_unavailable_modal.toggle()
        }
    })
})

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