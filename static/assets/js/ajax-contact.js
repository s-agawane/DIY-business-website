function getFormData($form) {
  var unindexed_array = $form.serializeArray();
  var indexed_array = {};

  $.map(unindexed_array, function (n, i) {
    indexed_array[n["name"]] = n["value"];
  });

  return indexed_array;
}

$(function () {
  // Get the form.
  var form = $("#contact-form");

  // Get the messages div.
  var formMessages = $(".form-message");

  // Set up an event listener for the contact form.
  $(form).submit(function (e) {
    // Stop the browser from submitting the form.
    e.preventDefault();

    var data = getFormData($(form));

    window.open(
      String("mailto:" + data.recipient).replace("^", "@") +
        "?subject=[" +
        data.email +
        "]&body=" +
        data.massage
    );

    $(formMessages).removeClass("error");
    $(formMessages).addClass("success");

    // Set the message text.
    $(formMessages).text("Please proceed with your email client.");

    // Clear the form.
    $("#contact-form input,#contact-form textarea").val("");
  });
});
