class feedback{
    constructor(stars, comment, pid) {
        this.stars = stars
        this.comment = comment
        this.pid = pid
    }
}
class product{
    constructor(pid, img1, title) {
        this.pid = pid
        this.img1 = img1
        this.title = title

    }

}

const feedbacks = document.querySelectorAll('#feedback')
const products = document.querySelectorAll('#product')
var feeds = []
var ps = []

for(const f of feedbacks){
    let feed = new feedback(
        f.querySelector('.stars').textContent,
        f.querySelector('.comment').textContent,
        f.querySelector('.pid').textContent,
    )
    feeds.push(feed)
}


for(const p of products){
    let prod = new product(
        p.querySelector('.pid').textContent,
        p.querySelector('.img1').textContent,
        p.querySelector('.title').textContent,
    )
    ps.push(prod)
}

document.querySelector('.carousel-item').classList.add('active')

const stars_container = document.querySelectorAll('#stars-container')

for(const feed of stars_container){
    let n_star = feed.querySelector('span').textContent
    let stars = feed.querySelectorAll('i')
    for (const i in stars){
        if(i<n_star){
            stars[i].classList.remove('fa-regular')
            stars[i].classList.add('fa-solid')
        }
    }
}