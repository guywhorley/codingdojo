
$(document).ready(function(){
  console.log('JQuery has loaded.');


  $('form').submit(function(){
    console.log('form submit handler> listener is working.');
    // there are three arguments that we are passing into $.post function
    //     1. the url we want to go to: '/quotes/create'
    //     2. what we want to send to this url: $(this).serialize()
    //            $(this) is the form and by calling .serialize() function on the form it will
    //            send post data to the url with the names in the inputs as keys
    //     3. the function we want to run when we get a response:
    //            function(res) { $('#quotes').html(res) }
    $.post('/posts/create', $(this).serialize(), function(resp) {
      console.log(resp);

      $('#post-content').html(resp);
    });
    // we have to return false for it to be a single page application because without it jQuery's
    // submit function will cause a refresh of the page which would defeat the point of AJAX
    return false;
  });
});

// $(document).ready(function() {
    // setup event handler for button click
    // $('#get_all_button').click(function(){
        // make ajax call to get html partial data
        // $.get('/quotes/index_html', function(resp) {
        //     $('#quotes').html(resp); // using html partial
        // });
        // JSON DATA
        // $.get('/quotes/index_html', function(resp) {
        //     --build page data here--
        // }, 'json');
    // }); //end click
// }); //end doc-ready
