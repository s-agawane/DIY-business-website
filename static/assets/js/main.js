$(function () {
  "use strict";

  //===== Section Menu Active

  var scrollLink = $(".page-scroll");
  // Active link switching
  $(window).scroll(function () {
    var scrollbarLocation = $(this).scrollTop();

    scrollLink.each(function () {
      var sectionOffset = $(this.hash).offset().top - 73;

      if (sectionOffset <= scrollbarLocation) {
        $(this).parent().addClass("active");
        $(this).parent().siblings().removeClass("active");
      }
    });
  });

  //===== close navbar-collapse when a  clicked

  $(".navbar-nav a").on("click", function () {
    $(".navbar-collapse").removeClass("show");
  });

  $(".navbar-toggler").on("click", function () {
    $(this).toggleClass("active");
  });

  $(".navbar-nav a").on("click", function () {
    $(".navbar-toggler").removeClass("active");
  });

  //===== Sidebar

  $('[href="#side-menu-left"], .overlay-left').on("click", function (event) {
    $(".sidebar-left, .overlay-left").addClass("open");
  });

  $('[href="#close"], .overlay-left').on("click", function (event) {
    $(".sidebar-left, .overlay-left").removeClass("open");
  });

  //===== Slick

  $(".slider-items-active").slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    speed: 800,
    arrows: true,
    prevArrow: '<span class="prev"><i class="lni lni-arrow-left"></i></span>',
    nextArrow: '<span class="next"><i class="lni lni-arrow-right"></i></span>',
    dots: true,
    autoplay: true,
    autoplaySpeed: 5000,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 3,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
          arrows: false,
        },
      },
    ],
  });

  var $el, $p, $ps, $up, totalHeight;

  $(".sidebar-box .button").click(function () {
    totalHeight = 0;

    $el = $(this);
    $p = $el.parent();
    $up = $p.parent();
    $ps = $up.find("p:not('.read-more')");

    // measure how tall inside should be by adding together heights of all inside paragraphs (except read-more paragraph)
    $ps.each(function () {
      totalHeight += $(this).outerHeight();
    });

    $up
      .css({
        // Set height to prevent instant jumpdown when max height is removed
        height: $up.height(),
        "max-height": 9999,
      })
      .animate({
        height: totalHeight,
      });

    // fade out read-more
    $p.fadeOut();

    // prevent jump-down
    return false;
  });

  //===== Isotope Project 4

  $(".container").imagesLoaded(function () {
    var $grid = $(".grid").isotope({
      // options
      transitionDuration: "1s",
      filter: $(".portfolio-menu > ul > li.active").attr("data-filter"),
    });

    // filter items on button click
    $(".portfolio-menu ul").on("click", "li", function () {
      var filterValue = $(this).attr("data-filter");
      $grid.isotope({
        filter: filterValue,
      });
    });

    //for menu active class
    $(".portfolio-menu ul li").on("click", function (event) {
      $(this).siblings(".active").removeClass("active");
      $(this).addClass("active");
      event.preventDefault();
    });
  });

  //===== slick Testimonial Four

  //===== testimonial active

  $(".testimonial-active").slick({
    dots: true,
    speed: 800,
    arrows: false,
    autoplay: true,
    autoplaySpeed: 1000,
    centerMode: true,
    centerPadding: "0",
    slidesToShow: 3,
    slidesToScroll: 4,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 3,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
          centerMode: false,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });

  //====== Magnific Popup

  $(".video-popup").magnificPopup({
    type: "iframe",
    // other options
  });

  //===== Magnific Popup

  $(".image-popup").magnificPopup({
    type: "image",
    gallery: {
      enabled: true,
    },
  });

  //===== Back to top

  // Show or hide the sticky footer button
  $(window).on("scroll", function (event) {
    if ($(this).scrollTop() > 600) {
      $(".back-to-top").fadeIn(200);
    } else {
      $(".back-to-top").fadeOut(200);
    }
  });

  //Animate the scroll to yop
  $(".back-to-top").on("click", function (event) {
    event.preventDefault();

    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1500
    );
  });

  //=====

  //=====  WOW active

  new WOW().init();
});

//===== Prealoder

$(window).on("load", function (event) {
  $(".preloader").delay(500).fadeOut(500);
});
