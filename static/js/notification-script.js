const color_info = '#007aff'
const color_success = '#198754'
const color_danger = '#dc3545'
const toast = document.getElementById('toast_notifier')
var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl)
})

if (window.location.href.includes('/bolle/dst/')) {


    if (document.URL.includes('dst_already_exists')) {
        toast.querySelector('#toast-body').textContent = 'Il nome del destinatario esiste già'
        toast.querySelector('#toast-icon').style.fill = color_danger

        toastList[0].show()
        setTimeout(() => {
            toastList[0].hide()

        }, 10000)
    } else if (document.URL.includes('successfully_added')) {
        toast.querySelector('#toast-body').textContent = 'Destinatario aggiunto correttamente'
        toast.querySelector('#toast-icon').style.fill = color_success

        toastList[0].show()
        setTimeout(() => {
            toastList[0].hide()

        }, 10000)
    } else if (document.URL.includes('successfully_edited')) {
        toast.querySelector('#toast-body').textContent = 'Destinatario modificato correttamente'
        toast.querySelector('#toast-icon').style.fill = color_success

        toastList[0].show()
        setTimeout(() => {
            toastList[0].hide()

        }, 10000)
    }
} else if (window.location.href.includes('/account/')) {
    if (document.URL.includes('edited')) {
        toast.querySelector('#toast-body').textContent = 'Info modificate correttamente'
        toast.querySelector('#toast-icon').style.fill = color_success

        toastList[0].show()
        setTimeout(() => {
            toastList[0].hide()

        }, 10000)
    }
} else if (window.location.href.includes('/bolle/dashboard/')) {
    if (document.URL.includes('_succesfully_removed')) {
        let nome_bolla = document.URL.split('#')[1].split('_')

        toast.querySelector('#toast-body').textContent = 'Bolla '+nome_bolla[0]+' rimossa correttamente'
        toast.querySelector('#toast-icon').style.fill = color_success

        toastList[0].show()
        setTimeout(() => {
            toastList[0].hide()

        }, 10000)
    } else if (document.URL.includes('_succesfully_edited')) {
        let nome_bolla = document.URL.split('#')[1].split('_')
        toast.querySelector('#toast-body').textContent = 'Bolla '+nome_bolla[0]+' modificata correttamente'
        toast.querySelector('#toast-icon').style.fill = color_success

        toastList[0].show()
        setTimeout(() => {
            toastList[0].hide()

        }, 10000)
    }
}else if (window.location.href.includes('/bolle/')) {
    if (document.URL.includes('successfully_created')) {
        toast.querySelector('#toast-title').textContent = 'Notifica'

        toast.querySelector('#toast-body').textContent = 'Bolla creata correttamente'
        toast.querySelector('#toast-icon').style.fill = color_success

        toastList[0].show()
        setTimeout(() => {
            toastList[0].hide()

        }, 10000)
    } else if (document.URL.includes('already_exist')) {
        toast.querySelector('#toast-title').textContent = 'Impossibile creare la bolla'

        toast.querySelector('#toast-body').textContent = 'Una bolla con tale numero/anno esiste già!!'
        toast.querySelector('#toast-icon').style.fill = color_danger

        toastList[0].show()
        setTimeout(() => {
            toastList[0].hide()

        }, 10000)
    }
}

