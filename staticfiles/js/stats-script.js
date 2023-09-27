document.querySelector('.carousel-item').classList.add('active')


const stars_container = document.querySelectorAll('#stars-container')

for(const feed of stars_container){
    let n_star = feed.querySelector('p').textContent
    let stars = feed.querySelectorAll('i')
    for (const i in stars){
        if(i<n_star-0.5){
            stars[i].classList.remove('fa-regular')
            stars[i].classList.add('fa-solid')
        }
    }
}