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
