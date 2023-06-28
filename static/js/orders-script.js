class feedback {
    constructor(id, pid) {
        this.id = id
        this.pid = pid
    }
}

var feedbacks = []
for (const feed of document.querySelectorAll('#feedbacks>span')) {
    feedbacks.push(new feedback(feed.id, feed.textContent))
}

const cart_element = document.getElementById('cart-element')

const products = document.querySelectorAll('#container>div>span')

for (const order_div of document.querySelectorAll('#container>div>order')) {
    // console.log(order_div)
    let card_cont = order_div.querySelector('#card-container')
    // console.log(card_cont)
    let cart_products = JSON.parse(card_cont.querySelector('#to-draw').textContent)
    for (const i in cart_products) {
        let p = cart_products[i]
        let product = document.getElementById('product' + p.pid)
        let card = cart_element.cloneNode(true)
        card.className = 'card mb-3 collapse'
        card.querySelector('div>div>div>img').src = '/static/images/' + product.querySelector('img1').textContent
        card.querySelector('div>div>div>div>h6').textContent = product.querySelector('title').textContent
        ps = card.querySelectorAll('div>div>div>div>p')
        ps[0].textContent = 'Taglia: ' + p.size
        ps[1].textContent = 'Prezzo: ' + product.querySelector('price').textContent + '€'
        ps[2].textContent = 'Quantità: ' + p.qty
        card.querySelector('#feed-btn').value = p.pid


        for (const feed of feedbacks) {
            if (feed.pid === p.pid) {
                card.querySelector('#feed-btn').disabled = true
                card.querySelector('#feed-btn').textContent = 'Hai gia lasciato una recnsione per quetso oggetto'
            }
        }


        card_cont.appendChild(card)


        order_div.querySelector('div').addEventListener('click', () => {
            let icon = order_div.querySelector('div>p>i')
            if (card.className.includes('show')) {
                card.classList.remove('show')
                icon.classList.remove('fa-rotate-90')
                for (const c of order_div.querySelector('address').children) {
                    c.classList.remove('show')
                }
            } else {
                card.classList.add('show')
                icon.classList.add('fa-rotate-90')
                for (const c of order_div.querySelector('address').children) {
                    c.classList.add('show')
                }
            }
        })
    }
}


cart_element.remove()
const feed_modal = new bootstrap.Modal(document.getElementById('feedback-modal'), {
    keyboard: false
})
const feedback_btn = document.querySelectorAll('#feed-btn')
for (const i in feedback_btn) {
    if (isNaN(parseInt(i))) {
        continue
    }
    // console.log(feedback_btn[i].value)
    feedback_btn[i].addEventListener('click', () => {
        let product = JSON.parse(feedback_btn[i].parentNode.parentNode.parentNode.parentNode.querySelector('span').textContent)
        // console.log('write a feed for element with id ' + feedback_btn[i].value)
        feed_modal._element.querySelector('#pid-input').value = feedback_btn[i].value
        feed_modal.toggle()

    })
}

const stars = document.querySelectorAll('.star')
const star_input = document.getElementById('star-count')
for (let i = 0; i < 5; i++) {

    stars[i].addEventListener('click', () => {
        star_input.value = i + 1
        for (let j = 0; j < 5; j++) {
            if (j <= i) {
                stars[j].classList.remove('fa-regular')
                stars[j].classList.add('fa-solid')
            } else {
                stars[j].classList.remove('fa-solid')
                stars[j].classList.add('fa-regular')
            }
        }

    })
}


