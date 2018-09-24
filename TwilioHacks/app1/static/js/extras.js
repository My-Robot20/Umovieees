$(document).ready(function(){
    
    $mastHeadBrand = $("#welcome");
    $name = $("#name");
    $info = $("#info");
    $speak = $("#speak");
    $getWizardy = $("#getWizardy");
    $write = $("#write");



    $mastHeadBrand.show(1600);
    $name.show(1600);
    $info.show(1600);


      clippy.load('Links',function(agent){
          
          agent.show();
          $speak.click(function(){
               agent.speak('My name is Links. I am Links the cat');
               
             });

          $getWizardy.click(function(){
               agent.play('GetWizardy');
               
             });

          $write.click(function(){
               agent.play('Writing');
               
             });


       });


 });