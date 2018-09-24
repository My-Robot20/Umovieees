$(document).ready(function(){

      $mastHeadBrand = $("#welcome");
      $name = $("#name");
      $info = $("#info");
      

      $mastHeadBrand.show(1600);
      $name.show(1600);
      $info.show(1600);


      
    $('#getAction').click(function(evt){
         if (this.id === 'getAction')
             evt.preventDefault();	
             $.get('/getMethod', function(getData) {
                 $('#getData').val(getData);
                 });
     });

     $('#postAction').click(function(evt2){
         if (this.id === 'postAction')
             evt2.preventDefault();	
             $.post('/postMethod', function(postData) {
                 $('#getData').val(postData);
                 });
     });
     $('#putAction').click(function(evt3){
     	if(this.id === 'putAction')
          evt3.preventDefault();
      	  $.ajax({
               url: '/putMethod',
               type: 'PUT',
               success: function(response) {
               	   $('#getData').val(response);
                      
               }
           });
     });
     $('#deleteAction').click(function(evt4){
     	if(this.id === 'deleteAction')
          evt4.preventDefault();
      	  $.ajax({
               url: '/deleteMethod',
               type: 'DELETE',
               success: function(deleteData) {
               	   $('#getData').val(deleteData);
                      
               }
           });
     });


     /*function insert(data){
       $.ajax({
               url: "/postMethod",
               data: $('form').serialize(),
               type: "POST",
               success: function(resp){
                console.log(resp);
              }
                
           });   
     }

     $("#postAction").click(function(evt5) {
        var input = $("#inputData").val();
        evt5.preventDefault();
        insert(input);
    });  */

     /*$('#id').click(function(){
      	});*/
});

