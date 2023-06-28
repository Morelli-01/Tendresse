const image_uploaded = document.getElementById('uploaded-image')
const icon_image_uploaded = document.getElementById('icon-upload-image')

function showImage(input) {
    var files = input.files;
    var images = image_uploaded.querySelectorAll('img');
    console.log(images)
    for (var i = 0; i < files.length; i++) {
        let reader = new FileReader();
        let img = image_uploaded.querySelectorAll('img')[i]
        reader.onload = function (e) {
            img.src = e.target.result;
        }

        reader.readAsDataURL(files[i]);

    }
}

// Aggiungi un event listener per chiamare la funzione showImage() quando l'input file cambia
var fileInput = document.querySelector('input[name="image"]');
fileInput.addEventListener('change', function () {
    showImage(this);
    image_uploaded.classList.remove('visually-hidden')
    icon_image_uploaded.classList.add('visually-hidden')
});


const  category_tags_container = document.getElementById('container-category-tags')
const  color_tags_container = document.getElementById('container-color-tags')

var add_tag_btn = category_tags_container.querySelector('#add-tag-btn')
var rm_tag_btn = category_tags_container.querySelector('#rm-tag-btn')

add_tag_btn.addEventListener('click', () => {
    let tag = category_tags_container.querySelector('#tag')
    category_tags_container.querySelector('#contaner-first-btn').insertAdjacentElement('afterend', tag.cloneNode(true))
})
rm_tag_btn.addEventListener('click', () => {
    const tags = category_tags_container.querySelectorAll('#tag')
    if (tags.length > 1) {
        tags[tags.length - 1].remove()
    }
})

add_tag_btn = color_tags_container.querySelector('#add-tag-btn')
rm_tag_btn = color_tags_container.querySelector('#rm-tag-btn')

add_tag_btn.addEventListener('click', () => {
    let tag = color_tags_container.querySelector('#tag')
    color_tags_container.querySelector('#contaner-first-btn').insertAdjacentElement('afterend', tag.cloneNode(true))
})
rm_tag_btn.addEventListener('click', () => {
    const tags = color_tags_container.querySelectorAll('#tag')
    if (tags.length > 1) {
        tags[tags.length - 1].remove()
    }
})