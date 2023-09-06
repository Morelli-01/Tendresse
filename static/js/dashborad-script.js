var is_old_bolle_active = false
const bolle = document.querySelectorAll('.bolla')
const new_bolle = document.querySelectorAll('.bolla-nuova')
const old_bolle = document.querySelectorAll('.bolla-vecchia')
for (const bolla of bolle) {
    bolla.addEventListener('mouseenter', () => {
        bolla.classList.add('bg-dark')
        bolla.classList.add('bg-opacity-25')
    })
    bolla.addEventListener('mouseleave', () => {
        bolla.classList.remove('bg-dark')
        bolla.classList.remove('bg-opacity-25')
    })
}

const del_btns = document.querySelectorAll('.del-btn')
const confirm_modal = new bootstrap.Modal(document.getElementById('confirm-modal'), {
    keyboard: false
})
const close_modal_btn = document.querySelector('#close-modal')
for (const btn of del_btns) {
    btn.addEventListener('click', (event) => {
        event.preventDefault()
        // alert('sei sicuro di voler cancellare la bolla del **/****')
        confirm_modal._element.querySelector('h5').textContent = 'Sei sicuro di voler eliminare la bolla ' + btn.id + '?'
        confirm_modal._element.querySelector('form').action = '/bolle/delete/' + btn.id + '/'
        confirm_modal.toggle()
    })
}
close_modal_btn.addEventListener('click', () => {
    confirm_modal.toggle()
})

const dst_filter_div = document.querySelector('#dst-filter-div')
const dst_filter = document.querySelector('#dst-select')
const bolle_container = document.querySelector('#bolle-container')
const search_btn = document.querySelector('#search-btn')
const search_input_number = document.querySelector('#search-bolla-number')
const search_input_year = document.querySelector('#search-bolla-year')
search_btn.addEventListener('click', () => {
    if (isInteger(parseInt(search_input_number.value)) && isInteger(parseInt(search_input_year.value))) {
        let number = parseInt(search_input_number.value)
        let year = parseInt(search_input_year.value)
        console.log('valid input')
        try {
            var bolla_div = document.querySelector('#bolla_' + number.toString() + '-' + year.toString())
            if (parseInt(bolla_div.getBoundingClientRect().top) > 283) {
                bolle_container.scrollTop += parseInt(bolla_div.getBoundingClientRect().top) - 283
            } else {
                bolle_container.scrollTop -= 283 - parseInt(bolla_div.getBoundingClientRect().top)
            }
            bolla_div.style.backgroundColor = 'rgba(0,157,255,0.39)'
            setTimeout(function () {
                bolla_div.style.backgroundColor = '#ffffff'

            }, 500);
        } catch (err) {
            console.error('bolla non trovata')
            notify_with_toast()
        }


    }
})

function isInteger(str) {
    return /^\d+$/.test(str);
}

function notify_with_toast() {
    toast.querySelector('#toast-body').textContent = 'La bolla cercata non esiste'
    toast.querySelector('#toast-icon').style.fill = color_danger

    toastList[0].show()
    setTimeout(() => {
        toastList[0].hide()

    }, 3000)
}

const toogle_btn = document.querySelector('#toogle-btn')
const nuove_bolle_div = document.querySelector('#nuove-bolle')
const vecchie_bolle_div = document.querySelector('#vecchie-bolle')
set_toogle_btn()

function set_toogle_btn() {
    toogle_btn.addEventListener('click', () => {
        if (toogle_btn.textContent === 'Vecchie') {
            toogle_btn.textContent = 'Nuove'
            toogle_btn.classList.remove('btn-outline-danger')
            toogle_btn.classList.add('btn-outline-success')
            nuove_bolle_div.classList.add('visually-hidden')
            dst_filter_div.classList.add('visually-hidden')
            vecchie_bolle_div.classList.remove('visually-hidden')
            is_old_bolle_active = true

        } else {
            toogle_btn.textContent = 'Vecchie'
            toogle_btn.classList.add('btn-outline-danger')
            toogle_btn.classList.remove('btn-outline-success')
            nuove_bolle_div.classList.remove('visually-hidden')
            dst_filter_div.classList.remove('visually-hidden')
            vecchie_bolle_div.classList.add('visually-hidden')
            is_old_bolle_active = false

        }
    })
}

const download_btns = document.querySelectorAll('#download-btn')
set_download_btns()

function set_download_btns() {
    for (const btn of download_btns) {
        // console.log(btn)
        btn.addEventListener('click', () => {
            bolla_number = btn.querySelector('div').id
            console.log(bolla_number)

            fetch('/oldbolle/get_file/' + bolla_number).then(response => {
                // console.log(response)
                response.text().then(data => {
                    // console.log(data)
                    if (data !== 'not_found') {
                        let a = document.createElement("a");
                        a.href = '/static/OldBolle/' + data;
                        a.download = data;
                        a.click();

                        // Pulire l'ancora temporanea
                        window.URL.revokeObjectURL('/static/OldBolle/' + data);
                    } else {
                        fetch('/oldbolle/del_file/' + bolla_number).then(res => {
                            console.log(res.status)
                        })
                    }
                })
            })

        })
    }
}

const visualize_btns = document.querySelectorAll('#visualize-btn')
set_visualize_btns()

function set_visualize_btns() {
    for (const btn of visualize_btns) {
        // console.log(btn)
        btn.addEventListener('click', () => {
            bolla_number = btn.querySelector('i').id
            console.log(bolla_number)

            fetch('/oldbolle/get_file/' + bolla_number).then(response => {
                // console.log(response)
                response.text().then(data => {
                    // console.log(data)
                    if (data !== 'not_found') {
                        let a = document.createElement("a");
                        a.href = '/static/OldBolle/' + data;
                        a.target = '_blank'
                        a.click();

                        // Pulire l'ancora temporanea
                        window.URL.revokeObjectURL('/static/OldBolle/' + data);
                    } else {
                        fetch('/oldbolle/del_file/' + bolla_number).then(res => {
                            console.log(res.status)
                        })
                    }
                })
            })

        })
    }
}

const del_btns_old = document.querySelectorAll('.del-btn-old')

for (const btn of del_btns_old) {
    btn.addEventListener('click', (event) => {
        event.preventDefault()
        // alert('sei sicuro di voler cancellare la bolla del **/****')
        confirm_modal._element.querySelector('h5').textContent = 'Sei sicuro di voler eliminare la bolla ' + btn.id + '?'
        confirm_modal._element.querySelector('form').action = '/oldbolle/del_file/' + btn.id + '/'
        confirm_modal.toggle()
    })
}

const up_btn = document.querySelector('#up-btn')
const down_btn = document.querySelector('#down-btn')

up_btn.addEventListener('click', () => {
    bolle_container.scrollTop = 0
})
down_btn.addEventListener('click', () => {
    bolle_container.scrollTop = bolle_container.scrollHeight
})

dst_filter.addEventListener('change', (e) => {

    console.log(e)
    console.log()
    for (const bolla of new_bolle) {
        if (e.target.selectedOptions[0].value === 'all') {
            bolla.classList.remove('visually-hidden')
        } else {
            let dst_name = bolla.querySelector('dst').id
            if (e.target.selectedOptions[0].value !== dst_name){
                bolla.classList.add('visually-hidden')
            }else{
                bolla.classList.remove('visually-hidden')
            }

            // if (bolla.id.replace('bolla_', ''))
        }
    }
})