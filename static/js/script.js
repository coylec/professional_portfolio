$(document).ready(function() {


// Modal popup$(function () {
    $('.portfolio-item').magnificPopup({
        type: 'inline',
        preloader: false,
        focus: '#username',
        modal: true
    });
    $(document).on('click', '.portfolio-modal-dismiss', function (e) {
        e.preventDefault();
        $.magnificPopup.close();
    });


/* Back to top button */

    var offset = 5;

    var duration = 300;

    $(window).scroll(function () {

        if ($(this).scrollTop() > offset) {

            $(".back-to-top").fadeIn(duration);
        } else {
            $(".back-to-top").fadeOut(duration);
        }

    });

$(".back-to-top").click(function(event) {

	event.preventDefault();

	$("html, body").animate({scrollTop: 0}, duration);

	return false;

});

});