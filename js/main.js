jQuery(document).ready(function() {

    Handlebars.registerHelper( 'sectid', function(path) {
        return "section-" + path;
    });

    Handlebars.registerHelper('commalist', function(items, options) {
      var out = '';

      for(var i=0, l=items.length; i<l; i++) {
        out = out + options.fn(items[i]) + (i!==(l-1) ? ",":"");
      }
      return out;
    });

    Handlebars.registerHelper('toUpperCase', function(str) {
      return str.toUpperCase();
    });

    function renderKnow(know) {
        var source    = jQuery('#know-template').html();
        var template  = Handlebars.compile(source);
        var container = jQuery('.featured-datasets');

        // cycle over array of know and render each cat
        know.map(function(cat) {
            var html = template(cat);
            container.append(html)
        });
    };

    function renderNav(know) {
        var source    = jQuery('#know-nav').html();
        var template  = Handlebars.compile(source);
        var container = jQuery('.featured-nav');

        // cycle over array of know and render each cat
        know.map(function(cat) {
            var html = template(cat);
            container.append(html)
        });
    };

    function onDataSuccess(knowResult) {
        var know       = knowResult.data;        // loaded from JSON
        var knowMap     = {}

        // cycle over know to build map
        know.map(function(cat) {
            knowMap[cat.uid] = cat;
        });

        // fill it
        renderNav(know);
        renderKnow(know);
    };

    $.getJSON('python/know.json', function(data){ onDataSuccess(data); });

});

(function($){

$(document).ready(function(){
var $window = $(window),
        $body = $(document.body),
        $doc = $('.doc-container'),
        $nav = $doc.find ('.doc-nav');

    // make the document navigation affix when scroll
    $('#featured-nav').affix({
      offset: {
        top: function () {
          return 156; // replace with your top position to start affix
        }
      }
    });

    // change navigation active according to scroll
    $body.scrollspy({
      target: '.doc-sidebar'
    });

});

})(jQuery);