

$(document).ready(function()
{
    $('img.toTop').click(function(){
        //$('html').scrollTop(0);
        $('html, body').animate({scrollTop: '0px'}, 300);
        event.preventDefault();
    })

});
