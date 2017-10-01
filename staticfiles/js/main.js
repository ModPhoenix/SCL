$(document).ready(function($) {
    $('.reply-btn-js').click(function() {   
        $('.comment-form-reply').removeClass('show-reply-form');
        $(this).parents('.comment-footer').siblings('.comment-form-reply').addClass('show-reply-form');
    });

    $('.reply-cancel-js').click(function() {   
        $('.comment-form-reply').removeClass('show-reply-form');
    });
});
    