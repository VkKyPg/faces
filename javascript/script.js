$(document).ready(function() {

  $("#addCategory").click(function() {
    $("#categoryForm").slideToggle();
<<<<<<< HEAD
  });

  $("#addCategory").mouseenter(function() {
    $("#underline").css({backgroundColor: '#BEE2E7'});
  });

  $("#addCategory").mouseleave(function() {
    $("#underline").css({});
  });

  $(".exit").click(function() {
    $("#categoryForm").slideToggle();
=======
  });

  $("#addCategory").mouseenter(function() {
    $("#underline").css({backgroundColor: '#BEE2E7'});
>>>>>>> cec67c30caf4d761ad3bc44b123b0e4b95e23ce1
  });

  $("#addCategory").mouseleave(function() {
    $("#underline").css({});
  });

  $("#exit").click(function() {
    $("#categoryForm").slideToggle();
    $("#personForm").slideToggle();
  });

  $("#addPerson").click(function() {
    $("#personForm").slideToggle();
  })

});
