var add_btn = document.querySelector('#add_prod')
var rm_btn = document.querySelector('#rm_prod')
var n = 1
const base_prod = document.querySelector('#base_prod')
const prod_container = document.querySelector('#prod_container')
const same_addr_btn = document.querySelector('#same_address')
const set_n_bolla_btn = document.querySelector('#set-n-bolla-btn')
add_btn.addEventListener('click', () => {
    let new_prod = base_prod.cloneNode(true)
    new_prod.id = 'prod' + n.toString()
    new_prod.querySelector('#prod_n').textContent = n + 1
    new_prod.classList.remove('visually-hidden')
    new_prod.querySelector('#descr').name = 'descr' + n.toString()
    new_prod.querySelector('#descr').setAttribute('required', true)
    new_prod.querySelector('#descr').id = 'descr' + n.toString()

    new_prod.querySelector('#qta').name = 'qta' + n.toString()
    new_prod.querySelector('#qta').id = 'qta' + n.toString()

    new_prod.querySelector('#um').name = 'um' + n.toString()
    new_prod.querySelector('#um').id = 'um' + n.toString()

    new_prod.querySelector('#note').name = 'note' + n.toString()
    new_prod.querySelector('#note').id = 'note' + n.toString()

    prod_container.appendChild(new_prod)
    n += 1

})
rm_btn.addEventListener('click', () => {
    if (n > 1) {
        document.querySelector('#prod' + (n - 1).toString()).remove()
        n -= 1;
    }
})
const data_bolla = document.querySelector('#data_bolla')
const data_trasporto = document.querySelector('#data_trasporto')
if (window.location.href.includes('edit')) {

    let data = data_bolla.placeholder.split('-')
    let yyyy = data[0]
    let mm = data[1]
    let dd = data[2]
    if (parseInt(mm) < 10) {
        mm = '0' + mm
    }
    if (parseInt(dd) < 10) {
        dd = '0' + dd
    }
    data_bolla.value = `${yyyy}-${mm}-${dd}`;
    data = data_trasporto.placeholder.split('-')
    yyyy = data[0]
    mm = data[1]
    dd = data[2]
    if(parseInt(mm) < 10)
    {
        mm = '0' + mm
    }
    if (parseInt(dd) < 10) {
        dd = '0' + dd
    }
    data_trasporto.value = `${yyyy}-${mm}-${dd}`;

} else {
    document.addEventListener('DOMContentLoaded', () => {

        const today = new Date();
        const yyyy = today.getFullYear();
        let mm = today.getMonth() + 1;
        let dd = today.getDate();
        if (mm < 10) {
            mm = '0' + mm;
        }
        if (dd < 10) {
            dd = '0' + dd;
        }
        data_bolla.value = `${yyyy}-${mm}-${dd}`;
        data_trasporto.value = `${yyyy}-${mm}-${dd}`;
        same_addr_btn.checked = true
    })
}


const add_addr_submit = document.querySelector('#add-addr-submit')
const add_addr_modal = new bootstrap.Modal(document.getElementById('add-address'), {
    keyboard: false
})
const alt_dst_element = document.querySelector('#alt-dst')
const modal_close_btn = document.querySelector('#modal-close-btn')
same_addr_btn.addEventListener('change', (e) => {
    if (!same_addr_btn.checked) {
        add_addr_modal.toggle()
    } else if (same_addr_btn.checked) {
        document.querySelector('#alt-dst-injected').remove()
    }
})
add_addr_submit.addEventListener('click', (e) => {
    e.preventDefault()
    let alt_dst = alt_dst_element.cloneNode(true)
    alt_dst.id = 'alt-dst-injected'
    alt_dst.classList.remove('visually-hidden')
    let dst_in = document.getElementById('add-address')
    console.log(dst_in.querySelector('#name').value)
    alt_dst.querySelector('#alt-dst-name').value = dst_in.querySelector('#name').value
    alt_dst.querySelector('#alt-dst-line1').value = dst_in.querySelector('#line1').value
    // alt_dst.querySelector('#alt-dst-line2').value = dst_in.querySelector('#line2').value
    alt_dst.querySelector('#alt-dst-city').value = dst_in.querySelector('#city').value
    alt_dst.querySelector('#alt-dst-zip').value = dst_in.querySelector('#zip').value
    alt_dst.querySelector('#alt-dst-province').value = dst_in.querySelector('#province').value
    alt_dst.querySelector('#alt-dst-country').value = dst_in.querySelector('#country').value
    alt_dst.querySelector('#alt-dst-label1').textContent = dst_in.querySelector('#name').value
    alt_dst.querySelector('#alt-dst-label2').textContent = dst_in.querySelector('#line1').value
    console.log(alt_dst)
    document.querySelector('#same_address_label').after(alt_dst)
    add_addr_modal.toggle()
})
modal_close_btn.addEventListener('click', () => {
    same_addr_btn.checked = true
})

set_n_bolla_btn.addEventListener('click', () => {
    let number = document.querySelector('#number')
    let year = document.querySelector('#year')
    if (number.readOnly) {
        number.removeAttribute('readonly')
        year.removeAttribute('readonly')
        set_n_bolla_btn.textContent = 'Annulla modifica numero-anno bolla'
        set_n_bolla_btn.classList.remove('btn-outline-info')
        set_n_bolla_btn.classList.add('btn-outline-danger')

    } else {
        number.setAttribute('readonly', true)
        year.setAttribute('readonly', true)
        set_n_bolla_btn.textContent = 'Modifica numero-anno bolla'
        set_n_bolla_btn.classList.add('btn-outline-info')
        set_n_bolla_btn.classList.remove('btn-outline-danger')
        number.value = 0
        const today = new Date();
        const yyyy = today.getFullYear();
        year.value = yyyy
    }

})