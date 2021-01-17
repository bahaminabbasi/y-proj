$(document).ready(function(){
  //###Navbar Menu###
  var timer = {};
  $('#myNavbar li').hover(function(){
    var menu1 = $(this);
    var dataAttr = menu1.attr('data-timer');
    clearTimeout(timer[dataAttr]);
    timer[dataAttr] = setTimeout(function(){
      menu1.addClass('activeMenu');
      $('>ul',menu1).fadeIn(0);
      $('>.menuLevel3',menu1).fadeIn(0);  
    },500)
    
  },function(){
    var menu1 = $(this);
    var dataAttr = menu1.attr('data-timer');
    clearTimeout(timer[dataAttr]);
    timer[dataAttr] = setTimeout(function(){
      menu1.removeClass('activeMenu');
      $('>ul',menu1).fadeOut(0);
      $('>.menuLevel3',menu1).fadeOut(0);
    },600)
    
  });

  //###Cart of Header###
  $(".cartList").hide();
  
  var timer;
  function debounce(){
      clearTimeout(timer);
      timer = setTimeout(function(){
          $(".cartList").fadeOut('fast');
      },450);
  }
  
  $(".cart1").hover(function() {
      // hover over
      $(".cartList").show();
      clearTimeout(timer);
    },function(){
      // hover out
      debounce();
    });
  $(".cartList").mouseenter(function(){
    clearTimeout(timer);
  });
  $(".cartList").mouseleave(function(){
    debounce();
  });
  

  $('.bottomCart1 button').click(function(){
    $(this).closest('.list-group-item').css('display','none');

  });

  //####scroll of navbar and sticky effect
  var offset = 100;
  $(window).scroll(function(){
    var y = $(this).scrollTop();
    if($('body').width() > 992){
      if(y >= offset){
        $('.navigation1').addClass('sticky');
      } else{
        $('.navigation1').removeClass('sticky');
      };
    } else{
      $('.navigation1').removeClass('sticky');
    };
    
    
  });

  //####toggle Search Bar ###
  $('.searchBtnSm').click(function(){
    $('div.searchBarSmall').slideToggle(300);
  });
  
  $(document).on('click', function(event){
    if(!$(event.target).closest('.searchBarSmall').length && !$(event.target).closest('.searchBtnSm').length){
      $('div.searchBarSmall').slideUp(300);
    }
  })

  
  
  //###Margin top Elements after Header ###
  //$('header').next().css('margin-top','185px');
  if($(window).width() > 768){
    $('header').next().css('margin-top','185px');
  }else{
    $('header').next().css('margin-top','85px');
  };

  //store js
  $('.bottumList1 button.close').click(function(){
    $(this).closest('div.PL2').css('display','none');
  });

});


//owl Carousel##########
$(document).ready(function(){
  $('.owl-carousel').owlCarousel({
    autoplay: true,
    autoplayHoverPause: true,
    margin: 10,
    nav: true,
    loop: true,
    navText: [
      "<i class='fa fa-caret-left'></i>",
      "<i class='fa fa-caret-right'></i>"
    ],
    responsive: {
      0: {
        items: 2
      },
      600: {
        items: 3
      },
      1000: {
        items: 5
      }
    }
  });

});

//######btn Low Up #### single product######//
$(document).ready(function(){
  $('.btnLow').click(function(){
    var T = $(this).next('.count1').html();
      if($(this).next('button').html()!=1)
      {
        $(this).next('button').html(--T);
      }else{
        $(this).next('button').html() = 1;
      } 
  });
  $('.btnUp').click(function(){

    var counterPro = $(this).prev('.count1').html()
    $(this).prev('button').html(++counterPro);
    $('.continueBuy').css('display', 'none');
    $('.updateBtn').css('display', 'block');
  });

  $('.updateBtn').click(function(){
    $(this).css('display', 'none')
    $(this).prev('.continueBuy').css('display', 'block')
  });
});

//###Product.html slider Price####
$(document).ready(function(){
  $('#price-range').slider({
      min: 0,
      max: 1000,
      range: true,
      values: [200,500]
  });
  
  $('#topSort button').click(function(){
    $('#topSort').find('button').removeClass('active1')
    $(this).addClass('active1')
  });



  /////###Timer for sign up###
  function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.text(minutes + ":" + seconds);

        if (--timer < 0) {
            timer = 0;
        }
    }, 1000);
};

$('.bTimer').click(function(){
  var fiveMinutes = 60 * 0.1,
      display = $('#time');
    startTimer(fiveMinutes, display);
    this.disabled = true;
    $('#payam').css('display','block');

    setTimout(function(){
      $(".bTimer").disabled = false; 
   }, 10000);


});

//####Button of dropdown in menu + vs - ###
$('button.dropButton').click(function(){
  $('div.accordion').find('button.dropButton').not($(this)).removeClass('open1')
  $(this).toggleClass('open1') 
});

});

<<<<<<< HEAD
// });
=======
<<<<<<< HEAD
});
})
=======
});
>>>>>>> 30a06fd5edbe28fe2630a6b062f82df6de97b904
>>>>>>> a8c8e893328d090c882b4271b199a14771c42f78
