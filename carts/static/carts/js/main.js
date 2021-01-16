$('.btnUp').click(function(){

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

  var counterPro = $(this).prev('.count1').html()
  var product_id = $(this).attr('data-id')
  var btn_click = $(this)

  var url = '/carts/maxlimit/'
  var btn_class = 'btn btn-outline-primary btnUp d-none'
  // var btn_class_active = "btn btn-outline-primary btnUp" 
  
  $.ajax({
      url: url,
      method: 'POST',
      data: {
          'product_id': product_id,
          'counterPro': counterPro,
      },
      success: function(data){
        if(data['status'] == 'ok'){
          btn_click.attr({'class':btn_class})
        }

      }
  });

});


$('.btnLow').click(function(){

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

  var counterPro = $(this).next('.count1').html()
  var product_id = $(this).attr('data-id')
  var btn_click = $(this).next().next('.btnUp')

  var url = '/carts/maxlimit/'
  var btn_class = 'btn btn-outline-primary btnUp d-block'
  // var btn_class_active = "btn btn-outline-primary btnUp" 
  
  $.ajax({
      url: url,
      method: 'POST',
      data: {
          'product_id': product_id,
          'counterPro': counterPro,
      },
      success: function(data){
        if(data['status'] == 'ok'){
          btn_click.attr({'class':btn_class})
        }

      }
  });

});