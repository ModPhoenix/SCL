$(document).ready(function ($) {
    $('.reply-btn-js').click(function () {
        $('.comment-form-reply').removeClass('show-reply-form');
        $(this).parents('.comment-footer').siblings('.comment-form-reply').addClass('show-reply-form');
    });

    $('.reply-cancel-js').click(function () {
        $('.comment-form-reply').removeClass('show-reply-form');
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

var csrfToken = getCookie("csrftoken");

/* 
* Comments
*/

// Плавный скролинг
$(".comments-item-date").click(function () {
    console.log(csrfToken);
    var elementClick = $(this).attr("href");
    var destination = $(elementClick).offset().top - 100;
    jQuery("html:not(:animated),body:not(:animated)").animate({ scrollTop: destination }, 500);
    return false;
});

var commentForm = $(".comments-form-reply").clone();

$(".comments-item-button-reply").click(function () {
    var commentId = $(this).closest(".comments-item").attr("id");
    var commentIdValue = Number(commentId.split('-').slice(1));
    $(".form-reply-js").remove();
    $("#" + commentId).append(commentForm);
    $("#" + commentId + " .comments-form-reply").addClass("form-reply-js");
    $("#" + commentId + " .comments-form-reply form").append('<input class="form-reply-js" type="hidden" name="parent_id" id="id_parent_id" value="' + commentIdValue + '">');
});

$("#comments").on("click", ".btn-comment-reply-cancel", function () {
    $(".form-reply-js").remove();
});

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