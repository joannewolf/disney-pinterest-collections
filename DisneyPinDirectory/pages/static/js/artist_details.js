// import tinycolor from "https://esm.sh/tinycolor2";

$(document).ready(() => {
    // var color = tinycolor("#f0f0f6");
    // console.log(color.isLight())

    // $(".tag-label").each(function(i, obj) {
    //     const labelBackgroundColor = tinycolor($(this).css('backgroundColor'));
    //     if (labelBackgroundColor.isLight()) {
    //         $(this).css("color", "blue");
    //     }
    //     else {
    //         $(this).css("color", "green");
    //     }
    // });
    console.log('update color')
    updageTagLabelColor();

    $('.btn-create').click(function () {
        $(".tag-label").removeClass("checked");
        $(".tag-label input[type=checkbox]").prop("checked", false);
    });
});

$(".tag-label input[type=checkbox]").change(function() {
    $(this).parent().toggleClass("checked");
});

