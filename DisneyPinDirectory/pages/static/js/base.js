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


const alertSuccess = (action='操作') => {
    new PNotify({
        title: `${action}成功`,
        text: `${action}成功`,
        delay: 3000,
        type: 'success',
        styling: 'bootstrap3',
    });
}

const alertSubmitFail = (action='操作', errorMsg='') => {
    if (!errorMsg) {
        errorMsg = '請確認所有必要欄位皆有填值。';
    }
    new PNotify({
        title: `${action}失敗`,
        text: errorMsg,
        delay: 3000,
        type: 'error',
        styling: 'bootstrap3',
    });
}

const alertFail = (xhr, action='操作') => {
    let errMsg = `${action}失敗，可能是此用戶無權限，請稍候再試。\n如為其他問題請洽技術人員。`;
    try {
        const error = JSON.parse(xhr.responseText).errors[0];
        if (error.code === 'form_error') {
            errMsg = `${action}失敗，${error.field}錯誤：${error.message}。`;
        }
        else {
            errMsg = `${action}失敗，${error.message}。`;
        }
    }
    catch {
        // do nothing
    }
    new PNotify({
        title: `${action}失敗`,
        text: errMsg,
        delay: 3000,
        type: 'error',
        styling: 'bootstrap3',
    });
}
