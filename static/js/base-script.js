const main_container = document.getElementById('main-container')

document.addEventListener('DOMContentLoaded', () => {
    console.log('doc loaded')
    main_container.style.top = document.querySelector('body>nav').offsetHeight.toString() + 'px'
})
window.addEventListener('load', () => {
    console.log('doc loaded')
    main_container.style.top = document.querySelector('body>nav').offsetHeight.toString() + 'px'
})

document.addEventListener('resize', () => {
    main_container.style.top = document.querySelector('body>nav').offsetHeight.toString() + 'px'
})

const footer = document.querySelector('footer')
footer.classList.add('position-absolute')
footer.classList.remove('fixed-bottom')
document.addEventListener('DOMContentLoaded', set_footer)

document.addEventListener('resize', () => {
    let h = document.querySelector('body>nav').offsetHeight + main_container.offsetHeight
    if (window.innerHeight - footer.offsetHeight > h) {
        footer.classList.add('fixed-bottom')
        footer.classList.remove('position-absolute')
    } else {
        footer.style.top = (document.querySelector('body>nav').offsetHeight + main_container.offsetHeight).toString() + 'px'
    }
})

const n_prod = document.getElementById('n-prod')
fetch('/cart/items/count').then(data => {
    data.text().then(b => {
        n_prod.textContent = b;
    })
})

function set_footer() {
    let h = document.querySelector('body>nav').offsetHeight + main_container.offsetHeight

    if (window.innerHeight - footer.offsetHeight > h) {
        footer.classList.add('fixed-bottom')
        footer.classList.remove('position-absolute')
    } else {
        if (document.URL.includes('product/')) {
            footer.style.top = (1.5 * document.querySelector('body>nav').offsetHeight + main_container.offsetHeight).toString() + 'px'
        } else {
            footer.style.top = (document.querySelector('body>nav').offsetHeight + main_container.offsetHeight).toString() + 'px'
        }

    }

}


let previousHeight = main_container.offsetHeight;
setInterval(function () {
    const currentHeight = main_container.offsetHeight;

    if (currentHeight !== previousHeight) {
        set_footer()
        previousHeight = currentHeight;
    }
}, 100);