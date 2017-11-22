/* initialize plugins */
require([
  'jquery',
  'superfish',
], function($){
    $(document).ready(function(){
        $('ul.sf-menu').superfish();
    });
});
