$(document).ready(function () {
  function App() {

  }

  App.prototype = {
    init: function () {
      this.initFancyBox();
      this.initNavigation();
      this.initPopups();
      this.initWOW();
      this.initMaps();
      this.initForm();
      this.initCallback();
      this.initReviewForm();
      this.initScroll();
    },
    initFancyBox: function () {
      $('.certificate__item').fancybox();
    },
    initPopups: function () {
      $(".js-btn-contact").click(function () {
        $(".js-popup-contact").fadeToggle("300", function () {

        });
      });
    },

    initNavigation: function () {
      var $navItems = $('.js-nav-item');

      $navItems.on('mouseenter', function (e) {
        var $navItem = $(this);
        var $navMenu = $navItem.find('.js-sub-menu');
        if ($navMenu.hasClass('js-sub-menu-footer')) {
          $navMenu.stop(true, false);
          $navMenu.fadeIn(200);
          return;
        }
        $navMenu.stop(true, false);
        $navMenu.slideDown(200);
      });

      $navItems.on('mouseleave', function (e) {
        var $navItem = $(this);
        var $navMenu = $navItem.find('.js-sub-menu');
        if ($navMenu.hasClass('js-sub-menu-footer')) {
          $navMenu.stop(true, false);
          $navMenu.fadeOut(200);
          return;
        }
        $navMenu.stop(true, false);
        $navMenu.slideUp(200);
      });
    },
    initWOW: function () {
      wow = new WOW({
        boxClass: 'wow',
        animateClass: 'animated',
        offset: 0,
        mobile: true,
        live: true
      })
      wow.init();
    },

    initMaps: function () {

      if (!window.ymaps) {
        return;
      }

      ymaps.ready(init);
      var myMap,
        myPlacemark;

      function init() {
        var center = window.mapCenter;
        myMap = new ymaps.Map("map", {
          center: center,
          zoom: 15
        });

        myPlacemark = new ymaps.Placemark(center, {
          hintContent: 'Ленинградский проспект, 32/2',
        });

        myMap.geoObjects.add(myPlacemark);
        myMap.behaviors.disable('scrollZoom');
      }
    },
    initCallback: function () {
      var $callbackForm = $('#callbackForm'),
        prsly = $callbackForm.parsley(),
        $submitBtn = $callbackForm.find('.js-callback-send-btn');
      $submitBtn.on('click', submit.bind(this));

      function submit(e) {
        e.preventDefault();
        e.stopPropagation();

        prsly.validate();
        if (prsly.isValid()) {
          $.post('/wp-admin/admin-ajax.php?action=send-callback', $callbackForm.serialize())
            .done(function (result) {
              if (result) {
                $callbackForm.slideUp(400, function () {
                  $('.js-enquiry-message').fadeIn(400);
                });
              }
            });
        }
      }

    },
    initReviewForm: function () {
      var $form = $('#reviewForm'),
        prsly = $form.parsley(),
        $submitBtn = $form.find('.js-review-send-btn');
      $submitBtn.on('click', submit.bind(this));

      function submit(e) {
        e.preventDefault();
        e.stopPropagation();

        prsly.validate();
        if (prsly.isValid()) {
          $.post('/wp-admin/admin-ajax.php?action=send-review', $form.serialize())
            .done(function (result) {
              if (result) {
                $form.fadeOut(400, function () {
                  $('.js-enquiry-message').fadeIn(400);
                });
              }
            });
        }
      }

    },
    initScroll: function () {
      $('a.js-scroll').smoothScroll({
        offset: -120,
        direction: 'top',
        speed: 'auto',
        autoCoefficient: 2,
      })
    },
    initForm: function () {
      var $enquiryForm = $('.js-enquiry-form'),
        $submitBtn = $enquiryForm.find('.js-send-enquiry-btn');

      prsly = $enquiryForm.parsley();
      $submitBtn.on('click', submit.bind(this));

      function submit(e) {
        e.preventDefault();
        e.stopPropagation();

        prsly.validate();
        if (prsly.isValid()) {
          $.post('/wp-admin/admin-ajax.php?action=send-enquiry', $enquiryForm.serialize())
            .done(function (result) {
              if (result) {
                $enquiryForm.slideUp(400, function () {
                  $('.js-enquiry-message').fadeIn(400);
                });

              }
            });
        }
      }
    }

  }

  var app = new App();
  app.init();

})
