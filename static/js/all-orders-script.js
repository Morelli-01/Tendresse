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
        card.className = 'card mb-3 collapse mt-3'
        card.querySelector('div>div>div>img').src = '/static/images/' + product.querySelector('img1').textContent
        card.querySelector('div>div>div>div>h6').textContent = product.querySelector('title').textContent
        ps = card.querySelectorAll('div>div>div>div>p')
        ps[0].textContent = 'Taglia: ' + p.size
        ps[1].textContent = 'Prezzo: ' + product.querySelector('price').textContent + '€'
        ps[2].textContent = 'Quantità: ' + p.qty


        card_cont.appendChild(card)

        order_div.querySelector('div').addEventListener('click', () => {
            // console.log('clicked')
            let icon = order_div.querySelector('div>div>i')
            if (card.className.includes('show')) {
                card.classList.remove('show')
                icon.classList.remove('fa-rotate-90')
                for (const c of order_div.querySelectorAll('div>div>.address')) {
                    c.classList.remove('show')
                }
            } else {
                card.classList.add('show')
                icon.classList.add('fa-rotate-90')
                for (const c of order_div.querySelectorAll('div>div>.address')) {
                    c.classList.add('show')
                }
            }

        })
    }
}


cart_element.remove()





