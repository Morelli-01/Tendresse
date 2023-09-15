const form = document.querySelector('#edit-form')
const edit_btn = document.querySelector('#edit-btn')
const del_btn = document.querySelector('#del-btn')

del_btn.addEventListener('click', () => {
    let name = window.location.href
    name = name.split('/')
    form.setAttribute('action', '/bolle/dst/delete/' + name[5] + '/')
    form.submit()

})
edit_btn.addEventListener('click', () => {
    form.setAttribute('action', '')
    form.submit()
})

document.addEventListener('DOMContentLoaded', () => {
    let name = window.location.href
    name = name.split('/')
    search_bar.value = name[5].replaceAll('%20', ' ')
    console.log(name[5])
})
