$(document).ready(() => {
    console.log('in base.js')
});


const updageTagLabelColor = () => {
    console.log('inside update color')
    $(".tag-label").each(function(i, obj) {
        const labelBackgroundColor = $(this).css('backgroundColor');
        console.log(labelBackgroundColor)
        // if (labelBackgroundColor.isLight()) {
        //     $(this).css("color", "blue");
        // }
        // else {
        //     $(this).css("color", "green");
        // }
    });
}
