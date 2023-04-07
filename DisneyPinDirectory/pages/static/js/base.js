$(window).scroll(function(e){ 
    var $fixElement = $('.fixed'); 
    var isPositionFixed = ($fixElement.css('position') == 'fixed');
    if ($(this).scrollTop() > 200 && !isPositionFixed){ 
        $fixElement.css({'position': 'fixed', 'top': '0px', 'width': '230px'});
    }
    if ($(this).scrollTop() < 200 && isPositionFixed){
        $fixElement.css({'position': 'static', 'top': '0px'});
    } 
});
