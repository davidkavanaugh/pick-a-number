$(document).ready(() => {
  $.ajax({
    url: "/api",
    success: function (result) {
      $("#result-container").append(result.response);
    },
  });
});
