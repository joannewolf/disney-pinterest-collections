var sizeTheOverlays = function() {
    $('.overlay')
        .resize()
        .each(function() {
            var h = $(this)
                .parent()
                .outerHeight();
            var w = $(this)
                .parent()
                .outerWidth();
            $(this).css("height", h);
            $(this).css("width", w);
        });
};
  
sizeTheOverlays();

function arrayDataToJsonString(data) {
    let result = '[';
    for (let i = 0; i < data.length; i += 1) {
        if (i === data.length) {
            break;
        }
        result = `${result}"${data[i]}"`;
        if (i !== data.length - 1) {
            result = `${result},`;
        }
    }

    result = `${result}]`;
    return result;
};

const copyStringToClipboard = (str) => {
    // Create new element
    var el = document.createElement('textarea');
    // Set value (string to be copied)
    el.value = str;
    // Set non-editable to avoid focus and move outside of view
    el.setAttribute('readonly', '');
    el.style = {position: 'absolute', left: '-9999px'};
    document.body.appendChild(el);
    // Select text inside element
    el.select();
    // Copy text to clipboard
    document.execCommand('copy');
    // Remove temporary element
    document.body.removeChild(el);
};
