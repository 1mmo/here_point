// .img height = width script
var cw = $('.img').width();
$('.img').css({'height':cw+'px'});

// Скрипт сворачивает окно фильтров на малых экранах
$(document).ready(function() {
    if ($(window).width() < '768') {
        $('#buttonCollapse').click();
    }
})
