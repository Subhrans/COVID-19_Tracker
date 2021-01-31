$(".counterUp").counterUp({delay:10,time:1000});

var typed = new Typed(".search",{
    strings:['Type City name',''],
    typeSpeed:30,
    backDelay: 900,
    backSpeed: 30,
    // show cursor
	showCursor: true,
    cursorChar: "|",
});
$(document).ready( function () {
    let data = $('#table_id').DataTable({
    "lengthMenu": [[3, 10, 25, 50, -1], [3, 10, 25, 50, "All"]],
    });
    $(".search").keyup(function(){
    data.search($(this).val()).draw();
    });
    $("#table_id_filter").addClass("d-none");
} );
