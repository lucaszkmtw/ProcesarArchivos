$(document).ready(function () {

$(".button").click(function (e) { 
    e.preventDefault();

    $.ajax({
        url: "/procesado/",
        dataType: "json",
        success: function (response) {
        var task = response.id;
        console.log(task);
        $(function () {
            var progressUrl = "/celery-progress/"+ task;
            CeleryProgressBar.initProgressBar(progressUrl)
          });
        }
    });
});


});