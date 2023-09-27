
const search_div = document.querySelector('#search-div')
const search_bar = document.querySelector('#search-bar')
const search_opt_div = document.querySelector('#search-opt')
var actual_sel
const search_opt = search_div.querySelectorAll('p')
for (const p of search_opt) {
    p.addEventListener('mouseenter', () => {
        p.classList.add('bg-opacity-50')
        actual_sel = p.querySelector('a').textContent
    })
    p.addEventListener('mouseleave', () => {
        p.classList.remove('bg-opacity-50')
    })
    p.addEventListener('change', () => {
        console.log('selected')
    })
}
search_bar.addEventListener('focusin', () => {
    search_opt_div.classList.remove('visually-hidden')
    if (search_bar.value === '') {
        for (const p of search_opt) {
            if (!p.textContent.includes(search_bar.value)) {
                p.classList.remove('visually-hidden')
            }
        }
    }
})
search_bar.addEventListener('focusout', () => {
    // console.log(actual_sel)
    if (actual_sel !== undefined) {
        search_bar.value = actual_sel
        window.location.href = '/bolle/dst/'+actual_sel+'/'
    }
    search_opt_div.classList.add('visually-hidden')
})

search_bar.addEventListener('input', (e) => {
    // console.log(e)
    if (search_bar.value == '') {
        for (const p of search_opt) {
            p.classList.remove('visually-hidden')

        }
    } else {
        for (const p of search_opt) {
            if (!p.textContent.includes(search_bar.value) && !p.textContent.toString().toLowerCase().includes(search_bar.value.toString())) {
                p.classList.add('visually-hidden')
            }
        }
    }
})