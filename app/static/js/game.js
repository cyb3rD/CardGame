$(document).ready(function () {
    
    $(".btn_action").click(function () {
        event.preventDefault();
        $("input[name='command_event']").val($(this).attr("name"));
        $("input[name='command_param']").val($(this).val());
        $("#GameData").submit();
    });
});