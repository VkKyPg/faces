$(document).ready(function() {

  $("#addCategory").click(function() {
    $("#categoryForm").slideToggle();
  });

  $("#addCategory").mouseenter(function() {
    $("#underline").css({backgroundColor: '#BEE2E7'});
  });

  $("#addCategory").mouseleave(function() {
    $("#underline").css({});
  });

  $(".exit").click(function() {
    $("#categoryForm").slideToggle();
  });

});
