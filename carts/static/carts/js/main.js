$('.btnUp').click(function(){


  var counterPro = $(this).prev('.count1').html()
  var product_id = $(this).attr('data-id')
  var btn_click = $(this)

  var url = '/carts/maxlimit/'
  
  $.ajax({
      url: url,
      method: 'POST',
      data: {
          'product_id': product_id,
          'counterPro': counterPro,
      },
      success: function(data){
        if(data['status'] == 'ok'){
          btn_click.attr({'disabled':true})
        }

      }
  });

});


$('.btnLow').click(function(){
  var counterPro = $(this).next('.count1').html()
  var product_id = $(this).attr('data-id')
  var btn_click = $(this).next().next('.btnUp')

  var url = '/carts/maxlimit/'
  
  $.ajax({
      url: url,
      method: 'POST',
      data: {
          'product_id': product_id,
          'counterPro': counterPro,
      },
      success: function(data){
        if(data['status'] == 'ok'){
          btn_click.attr({'disabled':false})
        }

      }
  });

});