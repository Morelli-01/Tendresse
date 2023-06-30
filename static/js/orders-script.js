document.addEventListener('DOMContentLoaded', () => {
    for (const order_container of document.querySelectorAll('.order')) {
        let d = order_container.querySelector('div')
        let icon = d.querySelector('div>p>i')
        let cart_element = order_container.querySelectorAll('div>div>div')
        let address_child = (order_container.querySelector('div>div>.address').children  )
        d.addEventListener('click', () => {
            if (icon.classList.contains('fa-rotate-90')) {
                icon.classList.remove('fa-rotate-90')
                for (const c of cart_element) {
                    c.classList.remove('show')
                }
                for(const c of address_child){
                    c.classList.remove('show')
                }
            } else {
                icon.classList.add('fa-rotate-90')
                for (const c of cart_element) {
                    c.classList.add('show')
                }
                for (const c of address_child) {
                    c.classList.add('show')
                }
            }
        })
    }

})


// cart_element.remove()
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
        // let product = JSON.parse(feedback_btn[i].parentNode.parentNode.parentNode.parentNode.querySelector('span').textContent)
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


