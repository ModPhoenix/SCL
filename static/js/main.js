$(document).ready(function($) {
    $('.reply-btn-js').click(function() {   
        $('.comment-form-reply').removeClass('show-reply-form');
        $(this).parents('.comment-footer').siblings('.comment-form-reply').addClass('show-reply-form');
    });

    $('.reply-cancel-js').click(function() {   
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
  }

$('.my-gallery').each( function() {
    var $pic     = $(this),
        getItems = function() {
            var items = [];
            $pic.find('a').each(function() {
                var $href   = $(this).attr('href');
                    // $size   = $(this).data('size').split('x');
                    // $width  = $size[0],
                    // $height = $size[1];
 
                var item = {
                    src : $href,
                    w   : 1000,
                    h   : 1000
                }
 
                items.push(item);
            });
            return items;
        }
 
    var items = getItems();

    var $pswp = $('.pswp')[0];
    $pic.on('click', 'a', function(event) {
        event.preventDefault();
         
        var $index = $(this).index();
        var options = {
            index: $index,
            bgOpacity: 0.7,
            showHideOpacity: true
        }
         
        // Initialize PhotoSwipe
        var lightBox = new PhotoSwipe($pswp, PhotoSwipeUI_Default, items, options);
        lightBox.init();
    });
});
