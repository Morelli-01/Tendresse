const order_increase_btn = document.getElementById('order-increase-btn')
const order_decrease_btn = document.getElementById('order-decrease-btn')
const select_element = document.querySelector('select')


select_element.addEventListener('change', ()=>{
    console.log(select_element.options[select_element.selectedIndex])
    if(select_element.options[select_element.selectedIndex] === order_increase_btn){
        // console.log('increase')
        window.location.href = '/product/ordered/price-increase'
    }
    if(select_element.options[select_element.selectedIndex] === order_decrease_btn){
        // console.log('increase')
        window.location.href = '/product/ordered/price-decrease'
    }
})

if(document.URL.toString().includes('/product/ordered/price-decrease')){
    select_element.selectedIndex = 2
}
if(document.URL.toString().includes('/product/ordered/price-increase')){
    select_element.selectedIndex = 1
}

const filter_cat_btn = document.getElementById('filter-cat-btn')

filter_cat_btn.addEventListener('click', ()=>{
    let icon = filter_cat_btn.querySelector('div>div>i')
    let cat_collapse =  document.querySelector('#category-collapse')
    if (icon.classList.contains('fa-plus')){
        icon.classList.remove('fa-plus')
        icon.classList.add('fa-minus')
        cat_collapse.classList.add('show')
    }else{
        icon.classList.add('fa-plus')
        icon.classList.remove('fa-minus')
        cat_collapse.classList.remove('show')

    }
})

const filter_color_btn = document.getElementById('filter-color-btn')

filter_color_btn.addEventListener('click', ()=>{
    let icon = filter_color_btn.querySelector('div>i')
    let cat_collapse =  document.querySelector('#color-collapse')
    if (icon.classList.contains('fa-plus')){
        icon.classList.remove('fa-plus')
        icon.classList.add('fa-minus')
        cat_collapse.classList.add('show')
    }else{
        icon.classList.add('fa-plus')
        icon.classList.remove('fa-minus')
        cat_collapse.classList.remove('show')

    }
})