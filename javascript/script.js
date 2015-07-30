$(document).ready(function() {

  $("#addCategory").click(function() {
    $("#categoryForm").fadeIn(200);
    $('.restofpage').css({"opacity": '0.2'});
  });

  $("#exit").click(function() {
    $("#categoryForm").fadeOut(200);
    $("#personForm").fadeOut(200);
    $('.restofpage').css({"opacity": '1'});
  });

  $("#addPerson").click(function() {
    $("#personForm").fadeIn(200);
    $('.restofpage').css({"opacity": '0.2'});
  })

  $("#createbutton").mouseenter(function() {
    $("#buttonbutton").css({"background-color": "#00C5CD"});
  })

  $("#createbutton").mouseleave(function() {
    $("#buttonbutton").css({"background-color": "#333333"});
  })

});
