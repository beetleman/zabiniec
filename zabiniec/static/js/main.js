/*global jQuery */

(function($) {
    "use strict";
    $('.porn .play button').click(function() {
        var movie = $('.porn .movie');
        var height = $(window).height()*0.4;
        movie.height(height);
        movie.slideToggle();
    });
})(jQuery);
