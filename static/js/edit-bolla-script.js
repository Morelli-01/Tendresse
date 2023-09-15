var add_btn = document.querySelector('#add_prod')
var rm_btn = document.querySelector('#rm_prod')
var n = 1
const base_prod = document.querySelector('#base_prod')
const prod_container = document.querySelector('#prod_container')
const same_addr_btn = document.querySelector('#same_address')
const data_bolla = document.querySelector('#data_bolla')
const data_trasporto = document.querySelector('#data_trasporto')
const add_addr_submit = document.querySelector('#add-addr-submit')
const alt_dst_element = document.querySelector('#alt-dst')
const modal_close_btn = document.querySelector('#modal-close-btn')
const add_addr_modal = new bootstrap.Modal(document.getElementById('add-address'), {
    keyboard: false
})


add_rem_merce_logic()
set_date_from_bolla()
same_address_logic()
set_merce_from_bolla()
set_sameAddress_from_bolla()

function add_rem_merce_logic() {
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
}

function set_date_from_bolla() {
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
    if (parseInt(mm) < 10) {
        mm = '0' + mm
    }
    if (parseInt(dd) < 10) {
        dd = '0' + dd
    }
    data_trasporto.value = `${yyyy}-${mm}-${dd}`;
}

function same_address_logic() {
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

}

function set_merce_from_bolla() {
    let descrizioni = document.querySelector('.descrizioni')
    let qta = document.querySelector('.qta')
    let um = document.querySelector('.um')
    let note = document.querySelector('.note')


    let descr_obj = JSON.parse(descrizioni.textContent.replaceAll('\'', '"'))
    let qta_obj = JSON.parse(qta.textContent.replaceAll('\'', '"'))
    let um_obj = JSON.parse(um.textContent.replaceAll('\'', '"'))
    let note_obj = JSON.parse(note.textContent.replaceAll('\'', '"'))
    for (let i = 0; i < descr_obj.descrizioni.length; i++) {
        if (i !== 0) {
            add_btn.click()
        }
        document.querySelector('#descr' + i).value = descr_obj.descrizioni[i]
        document.querySelector('#qta' + i).value = qta_obj.qta[i]
        document.querySelector('#um' + i).value = um_obj.um[i]
        document.querySelector('#note' + i).value = note_obj.note[i]
    }

}

function set_sameAddress_from_bolla() {
    let same_address = document.querySelector('.sameAddress')
    if (same_address.textContent === 'True') {
        same_addr_btn.checked = true
    } else {
        same_addr_btn.checked = false
        let alt_dst = alt_dst_element.cloneNode(true)
        alt_dst.id = 'alt-dst-injected'
        alt_dst.classList.remove('visually-hidden')
        alt_dst.querySelector('#alt-dst-name').value = document.querySelector('.dst-2-name').textContent
        alt_dst.querySelector('#alt-dst-line1').value = document.querySelector('.dst-2-line1').textContent
        alt_dst.querySelector('#alt-dst-city').value =document.querySelector('.dst-2-city').textContent
        alt_dst.querySelector('#alt-dst-zip').value = document.querySelector('.dst-2-zip').textContent
        alt_dst.querySelector('#alt-dst-province').value = document.querySelector('.dst-2-province').textContent
        alt_dst.querySelector('#alt-dst-country').value = document.querySelector('.dst-2-country').textContent

        alt_dst.querySelector('#alt-dst-label1').textContent = document.querySelector('.dst-2-name').textContent
        alt_dst.querySelector('#alt-dst-label2').textContent = document.querySelector('.dst-2-line1').textContent

        document.querySelector('#same_address_label').after(alt_dst)

    }
}

