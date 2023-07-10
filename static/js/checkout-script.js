const ship_1 = document.getElementById('ship-1')
const ship_2 = document.getElementById('ship-2')
const ship_1_cont = document.getElementById('ship-1-cont')
const ship_2_cont = document.getElementById('ship-2-cont')
var ship_radios = [ship_1, ship_2]
var ship_radios_cont = [ship_1_cont, ship_2_cont]
const add_addr_modal = new bootstrap.Modal(document.getElementById('add-address'), {
    keyboard: false
})
document.getElementById('new-addr-btn').addEventListener('click', () => {
    add_addr_modal.toggle()
})
const consegna_modal = new bootstrap.Modal(document.getElementById('consegna-modal'), {
    keyboard: false
})
const indirizzo_modal = new bootstrap.Modal(document.getElementById('indirizzo-modal'), {
    keyboard: false
})

for (const radio in ship_radios_cont) {
    ship_radios_cont[radio].addEventListener('click', () => {
        ship_radios[radio].checked = true
        for (const other_radio of ship_radios) {
            if (other_radio === ship_radios[radio]) {
                continue
            } else {
                other_radio.checked = false
            }
        }
    })
}

const address_list = document.querySelectorAll('#adderss-list>div>input')
const address_list_cont = document.querySelectorAll('#adderss-list>div')


for (const addr in address_list_cont) {
    if (addr === 'entries') {
        break
    }
    address_list_cont[addr].addEventListener('click', () => {
        address_list[addr].checked = true
        for (const other_addr of address_list) {
            if (address_list[addr] !== other_addr) {
                other_addr.checked = false
            }
        }
    })
}


const proceed_btn = document.getElementById('proceed-btn')
proceed_btn.addEventListener('click', () => {
    let ship, addr_id;
    if (ship_1.checked) {
        ship = 'standard'
    } else if (ship_2.checked) {
        ship = 'collect'
    } else {
        consegna_modal.toggle()
        return
    }


    for (const addr of address_list) {
        if (addr.checked === true) {
            let path = '/checkout/1/'
            addr_id = addr.id
            let csrftoken = getCookie('csrftoken');
            let msg = {
                ship_method: ship,
                addr_id: addr_id,
            }
            fetch(path, {
                "body": JSON.stringify(msg),
                "method": "POST",
                "headers": {'X-CSRFToken': csrftoken},
                "mode": 'same-origin' // Do not send CSRF token to another domain.
            }).then(data => {
                console.log(data)
                window.location.href = '/checkout/2/'
            })

        }
    }
    indirizzo_modal.toggle()
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

