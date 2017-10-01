$(function () {
    /* 1. OPEN THE FILE EXPLORER WINDOW */
    $(".js-upload-photos").click(function () {
      $("#fileupload").click();
    });
  
    /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
    $("#fileupload").fileupload({
      dataType: 'json',
      done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
        if (data.result.is_valid) {
          $("#gallery tbody").prepend(
            "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
          )
        }
      }
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