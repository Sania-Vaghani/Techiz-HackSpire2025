(function($) {
    'use strict';

    // Mean Menu
	$('.mean-menu').meanmenu({
		meanScreenWidth: "991"
	});

    // Header Sticky
	$(window).on('scroll',function() {
		if ($(this).scrollTop() > 120){  
			$('.navbar-area').addClass("is-sticky");
		}
		else{
			$('.navbar-area').removeClass("is-sticky");
		}
	});

    // Language-switcher
    $(".language-option").each(function() {
        var each = $(this)
        each.find(".lang-name").html(each.find(".language-dropdown-menu a:nth-child(1)").text());
        var allOptions = $(".language-dropdown-menu").children('a');
        each.find(".language-dropdown-menu").on("click", "a", function() {
             allOptions.removeClass('selected');
             $(this).addClass('selected');
             $(this).closest(".language-option").find(".lang-name").html($(this).text());
        });
    })

    // Others Option For Responsive JS
	$(".side-nav-responsive .dot-menu").on("click", function(){
		$(".side-nav-responsive .container .container").toggleClass("active");
    });

    // hero Slider
    $('.hero-slider').owlCarousel({
        loop: true,
        margin: 30,
        autoHeight: true,
        nav: true,
        dots: false,
        items: 1,
        autoplay: true,
        autoplayHoverPause: true,
        navText: [
            "<i class='flaticon-left-arrow'></i>",
            "<i class='flaticon-chevron'></i>"
        ],
    })

    // Odometer JS
    $('.odometer').appear(function(e) {
        var odo = $(".odometer");
        odo.each(function() {
            var countNumber = $(this).attr("data-count");
            $(this).html(countNumber);
        });
    });

    // Brand Slider
    $('.brand-slider').owlCarousel({
        loop: true,
        margin: 30,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 2
            },
            520:{
                items: 3
            },
            668:{
                items: 5
            },
            1000:{
                items: 6
            },
        }
    })

    // Testimonials Slider
    $('.testimonials-slider').owlCarousel({
        loop: true,
        margin: 30,
        autoHeight: true,
        nav: false,
        dots: true,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            768:{
                items: 2,
            },
            1000:{
                items: 3,
            }
        }
    })

    // Testimonials Slider Two
    $('.testimonials-slider-two').owlCarousel({
        loop: true,
        margin: 10,
        autoHeight: true,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            768:{
                items: 2,
            },
            1000:{
                items: 3,
            }
        },
        navText: [
            "<i class='flaticon-left-arrow'></i>",
            "<i class='flaticon-chevron'></i>"
        ],
    })

    // Event Slider
    $('.event-slider').owlCarousel({
        loop: true,
        margin: 30,
        autoHeight: true,
        nav: false,
        dots: true,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            1000:{
                items: 2,
            }
        }
    })

    // Categories Slider
    $('.categories-slider').owlCarousel({
        loop: true,
        margin: 30,
        autoHeight: true,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            768:{
                items: 2,
            },
            1200:{
                items: 4,
            }
        },
        navText: [
            "<i class='flaticon-left-arrow'></i>",
            "<i class='flaticon-chevron'></i>"
        ],
    })

    // Course Slider
    $('.course-slider').owlCarousel({
        loop: true,
        margin: 30,
        autoHeight: true,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            768:{
                items: 2,
            },
            1200:{
                items: 3,
            }
        },
        navText: [
            "<i class='flaticon-left-arrow'></i>",
            "<i class='flaticon-chevron'></i>"
        ],
    })

    // Course Slider
    $('.course-slider-two').owlCarousel({
        loop: true,
        margin: 30,
        autoHeight: true,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            768:{
                items: 2,
            },
            1200:{
                items: 3,
            }
        },
        navText: [
            "<i class='flaticon-left-arrow'></i>",
            "<i class='flaticon-chevron'></i>"
        ],
    })

    // Instructors Slider
    $('.instructors-slider').owlCarousel({
        loop: true,
        margin: 30,
        autoHeight: true,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items: 1,
            },
            768:{
                items: 2,
            },
            1200:{
                items: 4,
            }
        },
        navText: [
            "<i class='flaticon-left-arrow'></i>",
            "<i class='flaticon-chevron'></i>"
        ],
    })

      // Blog Preview Slider
	$('.blog-preview-slider').owlCarousel({
		loop:true,
		margin: 30,
		nav: true,
		mouseDrag: true,
		dots: false,
        items: 1,
		autoHeight: true,
		autoplay: false,
		smartSpeed:1500,
        autoplayHoverPause: true,
        navText: [
            "<i class='flaticon-left-arrow'></i>",
            "<i class='flaticon-chevron'></i>"
        ],
    });

    // Tabs Single Page
    $('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
    $('.tab ul.tabs li').on('click', function (g) {
        var tab = $(this).closest('.tab'), 
        index = $(this).closest('li').index();
        tab.find('ul.tabs > li').removeClass('current');
        $(this).closest('li').addClass('current');
        tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
        tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
        g.preventDefault();
    });

    // FAQ Accordion JS
	$('.accordion').find('.accordion-title').on('click', function(){
		// Adds Active Class
		$(this).toggleClass('active');
		// Expand or Collapse This Panel
		$(this).next().slideToggle('fast');
		// Hide The Other Panels
		$('.accordion-content').not($(this).next()).slideUp('fast');
		// Removes Active Class From Other Titles
		$('.accordion-title').not($(this)).removeClass('active');		
    });

    // Popup Video 
    $('.play-btn').magnificPopup({
        disableOn: 0,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });

    // Count Time JS
	function makeTimer() {
		var endTime = new Date("October 30, 2029 17:00:00 PDT");			
		var endTime = (Date.parse(endTime)) / 1000;
		var now = new Date();
		var now = (Date.parse(now) / 1000);
		var timeLeft = endTime - now;
		var days = Math.floor(timeLeft / 86400); 
		var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
		var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
		var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
		if (hours < "10") { hours = "0" + hours; }
		if (minutes < "10") { minutes = "0" + minutes; }
		if (seconds < "10") { seconds = "0" + seconds; }
		$("#days").html(days + "<span>Days</span>");
		$("#hours").html(hours + "<span>Hours</span>");
		$("#minutes").html(minutes + "<span>Minutes</span>");
		$("#seconds").html(seconds + "<span>Seconds</span>");
	}
    setInterval(function() { makeTimer(); }, 300);

    // Subscribe form
    $(".newsletter-form").validator().on("submit", function (event) {
        if (event.isDefaultPrevented()) {
            // Handle The Invalid Form...
            formErrorSub();
            submitMSGSub(false, "Please enter your email correctly");
        } else {
            // Everything Looks Good!
            event.preventDefault();
        }
    });
    function callbackFunction (resp) {
        if (resp.result === "success") {
            formSuccessSub();
        }
        else {
            formErrorSub();
        }
    }
    function formSuccessSub(){
        $(".newsletter-form")[0].reset();
        submitMSGSub(true, "Thank you for subscribing!");
        setTimeout(function() {
            $("#validator-newsletter").addClass('hide');
        }, 4000)
    }
    function formErrorSub(){
        $(".newsletter-form").addClass("animated shake");
        setTimeout(function() {
            $(".newsletter-form").removeClass("animated shake");
        }, 1000)
    }
    function submitMSGSub(valid, msg){
        if(valid){
            var msgClasses = "validation-success";
        } else {
            var msgClasses = "validation-danger";
        }
        $("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
    }
        
    // AJAX MailChimp
    $(".newsletter-form").ajaxChimp({
        url: "https://envyTheme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
        callback: callbackFunction
    });

    // Back To Top
    $('body').append("<div class='go-top'><i class='ri-arrow-up-s-line'></i></div>");
    $(window).on('scroll', function() {
        var scrolled = $(window).scrollTop();
        if (scrolled > 600) $('.go-top').addClass('active');
        if (scrolled < 600) $('.go-top').removeClass('active');
    });
    $('.go-top').on('click', function() {
        $('html, body').animate({
            scrollTop: '0',
        }, 500 );
    });

    // Preloader
    $(window).on("load", function() {
        var preLoder = $(".loader-wrapper");
        preLoder.delay(700).fadeOut(500);
        $("body").addClass("loaded");
    });

    // AOS JS
	AOS.init();

    // TweenMax JS
	$('.banner-area').mousemove(function(e){
		var wx = $(window).width();
		var wy = $(window).height();
		var x = e.pageX - this.offsetLeft;
		var y = e.pageY - this.offsetTop;
		var newx = x - wx/2;
		var newy = y - wy/2;
		$('.banner-img').each(function(){
			var speed = $(this).attr('data-speed');
			if($(this).attr('data-revert')) speed *= -.4;
			TweenMax.to($(this), 1, {x: (1 - newx*speed), y: (1 - newy*speed)});
		});
	});

    // TweenMax JS
	$('.enrolled-area').mousemove(function(e){
		var wx = $(window).width();
		var wy = $(window).height();
		var x = e.pageX - this.offsetLeft;
		var y = e.pageY - this.offsetTop;
		var newx = x - wx/2;
		var newy = y - wy/2;
		$('.enrolled-img, .enrolled-img-two').each(function(){
			var speed = $(this).attr('data-speed');
			if($(this).attr('data-revert')) speed *= -.4;
			TweenMax.to($(this), 1, {x: (1 - newx*speed), y: (1 - newy*speed)});
		});
	});

    // Switch Btn
    $('body').append("<div class='switch-box'><label id='switch' class='switch'><input type='checkbox' onchange='toggleTheme()' id='slider'><span class='slider round'></span></label></div>");
})($);

// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('ledu_theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('ledu_theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('ledu_theme') === 'theme-dark') {
        setTheme('theme-dark');
        document.getElementById('slider').checked = false;
    } else {
        setTheme('theme-light');
      document.getElementById('slider').checked = true;
    }
})();