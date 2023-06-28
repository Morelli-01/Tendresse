const cart_container = document.getElementById('cart-container')
const cart_element = document.getElementById('cart-element')
const cart_products = JSON.parse(document.getElementById('cart').textContent.replaceAll("'", '"'))
const summary_container = document.getElementById('summary-container')
var total = 0;
draw_cart()

function draw_cart() {
    for (const i in cart_products) {
        p = cart_products[i]
        product = document.getElementById('cart' + p.pid)
        let card = cart_element.cloneNode(true)
        card.className = 'card mb-3'
        card.querySelector('div>div>div>img').src = '/static/images/' + product.querySelector('img1').textContent
        card.querySelector('div>div>div>div>h6').textContent = product.querySelector('title').textContent
        ps = card.querySelectorAll('div>div>div>div>p')
        ps[0].textContent = 'Taglia: ' + p.size
        ps[1].textContent = 'Prezzo: ' + product.querySelector('price').textContent + '€'
        ps[2].textContent = 'Quantità: ' + p.qty

        cart_container.appendChild(card)
        let tlt = document.createElement('p')
        tlt.textContent = product.querySelector('title').textContent
        summary_container.querySelectorAll('div')[1].appendChild(tlt)

        let prz = document.createElement('p')
        prz.textContent = (product.querySelector('price').textContent * p.qty).toString() + '€'
        summary_container.querySelectorAll('div')[2].appendChild(prz)
        total += product.querySelector('price').textContent * p.qty
        document.getElementById('total-container').textContent = total.toString() + '€'

        let rem_btn = card.querySelector('button')
        rem_btn.id = i
        rem_btn.addEventListener('click', remove_product)
    }
}

function remove_product() {
    let path = '/cart/remove/'
    csrftoken = getCookie('csrftoken');
    msg = {
        product_index: this.id
    }
    // console.log(JSON.stringify(msg))
    fetch(path, {
        "body": JSON.stringify(msg),
        "method": "POST",
        "headers": {'X-CSRFToken': csrftoken},
        "mode": 'same-origin' // Do not send CSRF token to another domain.
    }).then(data => {
        // console.log(data)
        location.reload()
    })
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

if (document.getElementById('user-logged').value === 'False') {
    var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'), {
        keyboard: false
    })
}

document.getElementById('checkout-btn').addEventListener('click', () => {
    if (document.getElementById('user-logged').value === 'False') {
        myModal.toggle()
    } else {
        window.location.href = "/checkout/1/"
    }

})