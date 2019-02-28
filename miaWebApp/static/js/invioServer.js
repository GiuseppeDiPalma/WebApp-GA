$(document).ready(function() {
    $("#submit").on('click', function(){
        // send ajax
        $.ajax({

            url: 'http://127.0.0.1:8081/', // url where to submit the request
            type : "POST", // type of action POST || GET
            dataType : 'json', // data type
            data : $("#form").serialize(), // post data || get data
            success : function(result) {
                // you can see the result from the console
                // tab of the developer tools
                console.log(result);
            },
            error: function(xhr, resp, text) {
                console.log(xhr, resp, text);
                }
            })
        });
});