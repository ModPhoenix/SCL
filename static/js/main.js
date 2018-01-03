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

(function(){
    var a = document.querySelector('.post-detail .aside'), b = null, P = 67;  // если ноль заменить на число, то блок будет прилипать до того, как верхний край окна браузера дойдёт до верхнего края элемента. Может быть отрицательным числом
    window.addEventListener('scroll', Ascroll, false);
    document.body.addEventListener('scroll', Ascroll, false);
    function Ascroll() {
      if (b == null) {
        var Sa = getComputedStyle(a, ''), s = '';
        for (var i = 0; i < Sa.length; i++) {
          if (Sa[i].indexOf('overflow') == 0 || Sa[i].indexOf('padding') == 0 || Sa[i].indexOf('border') == 0 || Sa[i].indexOf('outline') == 0 || Sa[i].indexOf('box-shadow') == 0 || Sa[i].indexOf('background') == 0) {
            s += Sa[i] + ': ' +Sa.getPropertyValue(Sa[i]) + '; '
          }
        }
        b = document.createElement('div');
        b.style.cssText = s + ' box-sizing: border-box; width: ' + a.offsetWidth + 'px;';
        a.insertBefore(b, a.firstChild);
        var l = a.childNodes.length;
        for (var i = 1; i < l; i++) {
          b.appendChild(a.childNodes[1]);
        }
        a.style.height = b.getBoundingClientRect().height + 'px';
        a.style.padding = '0';
        a.style.border = '0';
      }
      var Ra = a.getBoundingClientRect(),
          R = Math.round(Ra.top + b.getBoundingClientRect().height - document.querySelector('.comments-wrap').getBoundingClientRect().top + 25);  // селектор блока, при достижении верхнего края которого нужно открепить прилипающий элемент;  Math.round() только для IE; если ноль заменить на число, то блок будет прилипать до того, как нижний край элемента дойдёт до футера
      if ((Ra.top - P) <= 0) {
        if ((Ra.top - P) <= R) {
          b.className = 'stop-aside-detail';
          b.style.top = - R +'px';
        } else {
          b.className = 'sticky-aside-detail';
          b.style.top = P + 'px';
        }
      } else {
        b.className = '';
        b.style.top = '';
      }
      window.addEventListener('resize', function() {
        a.children[0].style.width = getComputedStyle(a, '').width
      }, false);
    }
    })()