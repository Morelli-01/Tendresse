
document.addEventListener('DOMContentLoaded', () => {
    for (const order_container of document.querySelectorAll('.order')) {
        let d = order_container.querySelector('div')
        let icon = d.querySelector('div>div>i')
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


