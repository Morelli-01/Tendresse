const main_div = document.getElementById('main-container')
var position = 0;
var widht = innerHeight - document.querySelector('nav').scrollHeight;
const imgs = document.querySelectorAll('body>div>div>img')
const footer = document.querySelector('footer')
for (let i = 0; i < imgs.length; i++) {
    imgs[i].style.height = (widht).toString() + 'px'
    window.addEventListener('resize', () => {
        imgs[i].style.height = (widht).toString() + 'px'
    })
}

async function handleWheel(event) {
    // console.log(event)

    const deltaY = event.deltaY;
    if (deltaY > 0) {
        document.body.style.overflowY = 'hidden'
        if (position < imgs.length) {
            position += 1;
        } else {
            return;
        }

        // description_container[position-1].className = 'position-absolute ms-5 description-container hidden'
        // description_container[position].className = 'position-absolute ms-5 description-container visible'


        if (position < imgs.length) {
            deactivateScroll()
            main_div.style.transitionDuration = '900ms';
            main_div.style.transform = 'translate3d(0px, ' + ((-widht) * position).toString() + 'px' + ', 0px)';
            setTimeout(activateScroll, 900);
        } else if (position == imgs.length) {
            deactivateScroll()
            main_div.style.transitionDuration = '100ms';
            main_div.style.transform = 'translate3d(0px, ' + ((-widht) * (imgs.length - 1) - document.querySelector('footer').scrollHeight).toString() + 'px' + ', 0px)';
            setTimeout(activateScroll, 100);
        }


        // Rotellina verso il basso
    } else if (deltaY < 0) {
        document.body.style.overflowY = 'hidden'
        if (position > 0) {
            position -= 1;
        } else {
            return;
        }

        // Rotellina verso l'alto
        if (position == imgs.length - 1) {
            deactivateScroll()
            main_div.style.transitionDuration = '300ms';
            main_div.style.transform = 'translate3d(0px, ' + ((-widht) * position).toString() + 'px' + ', 0px)';
            setTimeout(activateScroll, 300);

        } else if (position > 0) {
            deactivateScroll()
            main_div.style.transitionDuration = '900ms';
            main_div.style.transform = 'translate3d(0px, ' + ((-widht) * position).toString() + 'px' + ', 0px)';
            setTimeout(activateScroll, 900);

        } else {
            deactivateScroll()
            main_div.style.transitionDuration = '900ms';
            main_div.style.transform = 'translate3d(0px, ' + ((-widht) * position).toString() + 'px' + ', 0px)';
            setTimeout(activateScroll, 900);
        }

    }
    if (position >= 3) {
        footer.classList.remove('visually-hidden')
    } else {
        footer.classList.add('visually-hidden')
    }
}

function handleScroll(event) {
    event.preventDefault();
}

function activateScroll() {
    window.removeEventListener('wheel', handleScroll);
    // console.log('scroll activated')
    window.addEventListener("wheel", handleWheel)
    main_div.style.transitionDuration = '0s';
    document.body.style.overflowY = 'clip'
}

function deactivateScroll() {
    window.removeEventListener("wheel", handleWheel)
    window.addEventListener('wheel', handleScroll, {passive: false});
    // console.log('scroll deactivated')
}

function set_footer() {
    footer.classList.add('position-absolute')
    footer.style.top = (window.innerHeight - footer.clientHeight).toString() + 'px'
    footer.classList.add('visually-hidden')
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('window loaded')
    main_div.style.top = document.querySelector('nav').scrollHeight.toString() + 'px'
    deactivateScroll()
    main_div.style.transitionDuration = '1000ms';
    main_div.style.transform = 'translate3d(0px, 0px, 0px)';
    setTimeout(activateScroll, 1000);
    position = 0;
})

window.addEventListener('resize', () => {
    main_div.style.top = document.querySelector('nav').scrollHeight.toString() + 'px'
})

window.addEventListener("wheel", handleWheel)

// const n_prod = document.getElementById('n-prod')
// fetch('/cart/items/count').then(data=>{
//     data.text().then(b =>{
//         n_prod.textContent = b;
//     })
// })

set_footer()