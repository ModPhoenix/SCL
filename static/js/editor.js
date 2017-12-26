var Image = Quill.import('formats/image');
Image.className = 'img-fluid';
Quill.register(Image, true);

var toolbarOptions = [
    [{ 'header': [2, 3, 4, false] }],

    ['bold', 'italic', 'underline', 'strike'],

    [{ 'align': [] }],

    ['blockquote',],

    [{ 'list': 'ordered' }, { 'list': 'bullet' }],

    [{ 'color': [] }, { 'background': [] }],

    ['link', 'image', 'video'],

    ['clean']
];

const quill = new Quill('#editor-container', {
    modules: {
        toolbar: toolbarOptions
    },
    placeholder: 'Напишите что то...',
    theme: 'snow'
});

function selectLocalImage() {
    const input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.click();

    // Listen upload local image and save to server
    input.onchange = () => {
        const file = input.files[0];

        // file type is only image.
        if (/^image\//.test(file.type)) {
            saveToServer(file);
        } else {
            console.warn('You could only upload images.');
        }
    };
}

function saveToServer(file) {
    const fd = new FormData();
    fd.append('image', file);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/image-upload/', true);
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    xhr.onload = () => {
        if (xhr.status === 200) {
            // this is callback data: url
            const data = JSON.parse(xhr.responseText);
            insertToEditor(data);
        }
    };
    xhr.send(fd);
}

function insertToEditor(data) {
    // push image url to rich editor.
    const range = quill.getSelection();
    console.log(data.link_crop);
    if (data.link_crop == null) {
        quill.pasteHTML(range.index, `<a href="${data.link}" class="img"><img src="${data.link}" class="img-fluid" alt="${data.name}"></a>`);
    }
    else {
        quill.pasteHTML(range.index, `<a href="${data.link}" class="img"><img src="${data.link_crop}" class="img-fluid" alt="${data.name}"></a>`);
    }
}

// quill editor add image handler
quill.getModule('toolbar').addHandler('image', () => {
    selectLocalImage();
});



$(document).ready(function () {
    var content = document.getElementById('id_content');
    var qlEditor = document.getElementsByClassName('ql-editor');

    if (content.value === '') {
        // Ести поле textarea пустое, вставлет пробел 
        content.value = ' ';
    } else {
        // При редактировании поста вставляет html
        // с textarea в quill редактор
        $('.ql-editor').html(content.value);
    }

    $("#toolbar-container").stick_in_parent();

});
// Передает html разметку с редактора в textarea
// при отправке формы
var form = document.querySelector('form');
form.onsubmit = function () {
    var content = document.getElementById('id_content');
    content.value = quill.root.innerHTML;
};

/* sticky-editor */

(function () {  // анонимная функция (function(){ })(), чтобы переменные "a" и "b" не стали глобальными
    var a = document.querySelector('.ql-toolbar'), b = null;  // селектор блока, который нужно закрепить
    window.addEventListener('scroll', Ascroll, false);
    document.body.addEventListener('scroll', Ascroll, false);  // если у html и body высота равна 100%
    function Ascroll() {
        if (b == null) {  // добавить потомка-обёртку, чтобы убрать зависимость с соседями
            var Sa = getComputedStyle(a, ''), s = '';
            for (var i = 0; i < Sa.length; i++) {  // перечислить стили CSS, которые нужно скопировать с родителя
                if (Sa[i].indexOf('overflow') == 0 || Sa[i].indexOf('padding') == 0 || Sa[i].indexOf('border') == 0 || Sa[i].indexOf('outline') == 0 || Sa[i].indexOf('box-shadow') == 0 || Sa[i].indexOf('background') == 0) {
                    s += Sa[i] + ': ' + Sa.getPropertyValue(Sa[i]) + '; '
                }
            }
            b = document.createElement('div');  // создать потомка
            b.style.cssText = s + ' box-sizing: border-box; width: ' + a.offsetWidth + 'px;';
            a.insertBefore(b, a.firstChild);  // поместить потомка в цепляющийся блок первым
            var l = a.childNodes.length;
            for (var i = 1; i < l; i++) {  // переместить во вновь созданного потомка всех остальных потомков (итого: создан потомок-обёртка, внутри которого по прежнему работают скрипты)
                b.appendChild(a.childNodes[1]);
            }
            a.style.height = b.getBoundingClientRect().height + 'px';  // если под скользящим элементом есть другие блоки, можно своё значение
            a.style.padding = '0';
            a.style.border = '0';  // если элементу присвоен padding или border
        }
        if (a.getBoundingClientRect().top <= 57) { // elem.getBoundingClientRect() возвращает в px координаты элемента относительно верхнего левого угла области просмотра окна браузера
            b.className = 'sticky-editor';
        } else {
            b.className = '';
        }
        window.addEventListener('resize', function () {
            a.children[0].style.width = getComputedStyle(a, '').width
        }, false);  // если изменить размер окна браузера, измениться ширина элемента
    }
})()