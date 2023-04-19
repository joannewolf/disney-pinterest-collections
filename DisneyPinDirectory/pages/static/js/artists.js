$(document).ready(() => {
    $('.btn-create').click(function () {
        const maxArtistNumber = $('#max-artist-number').html();
        $('#create-artist-serial-number').val(parseInt(maxArtistNumber) + 1);
        $('#create-artist-name').val('');
        $('#create-artist-pinterest-page-url').val('');
        $('#create-artist-artstation-url').val('');
        $('#create-artist-behance-url').val('');
        $('#create-artist-deviantart-url').val('');
        $('#create-artist-facebook-url').val('');
        $('#create-artist-instagram-url').val('');
        $('#create-artist-pinterest-url').val('');
        $('#create-artist-pixiv-url').val('');
        $('#create-artist-tumblr-url').val('');
        $('#create-artist-twitter-url').val('');
        $('#create-artist-weibo-url').val('');
        $('#create-artist-other-url').val('');
    });
    // $('.btn-update').click(btnUpdateListener);

    fetchArtists();
});

function btnUpdateListener() {
//     const boardId = $(this).data('board-id');
//     $('#update-board-id').val(boardId);
//     const name = $(this).data('board-name');
//     $('#update-board-name').val(name);

//     $('.tag-label').removeClass('checked');
//     $('.tag-label input[type=checkbox]').prop('checked', false);
//     var tagsId = $(this).data('board-tags-id').toString();
//     tagsId = tagsId.split(',');
//     for (const id of tagsId) {
//         $(`#update-tag-${id}`).addClass('checked');
//         $(`#update-tag-${id} input[type=checkbox]`).prop('checked', true);
//     }
}

const fetchArtists = () => {
    const tableName = '#artist-table-content';
    $(tableName).empty();
    const htmlString = `
        <tr>
            <td> Searching... </td>
            ${'<td> - </td>'.repeat(2)}
        </tr>
    `;
    $(tableName).append(htmlString);

    const url = `/api/artists`;
    $.ajax({
        type: 'GET',
        url,
        traditional: true,
    }).then(function(data) {
        refreshArtistTable(data);
    }).fail(function(xhr) {
        alertFail(xhr, '讀取記錄');
    });
};

$('#create-button').click(function() {
    const serialNumber = $('#create-artist-serial-number').val();
    const name = $('#create-artist-name').val();
    const pinterestPageUrl = $('#create-artist-pinterest-page-url').val();
    const artstationUrl = $('#create-artist-artstation-url').val();
    const behanceUrl = $('#create-artist-behance-url').val();
    const deviantartUrl = $('#create-artist-deviantart-url').val();
    const facebookUrl = $('#create-artist-facebook-url').val();
    const instagramUrl = $('#create-artist-instagram-url').val();
    const pinterestUrl = $('#create-artist-pinterest-url').val();
    const pixivUrl = $('#create-artist-pixiv-url').val();
    const tumblrUrl = $('#create-artist-tumblr-url').val();
    const twitterUrl = $('#create-artist-twitter-url').val();
    const weiboUrl = $('#create-artist-weibo-url').val();
    const otherUrl = $('#create-artist-other-url').val();

    if (name === '' || serialNumber === '') {
        alertSubmitFail('新增');
        return;
    }

    createArtist(name, serialNumber, pinterestPageUrl,
        artstationUrl, behanceUrl, deviantartUrl, facebookUrl, instagramUrl,
        pinterestUrl, pixivUrl, tumblrUrl, twitterUrl, weiboUrl, otherUrl);
});

const createArtist = (name, serialNumber, pinterestPageUrl,
    artstationUrl, behanceUrl, deviantartUrl, facebookUrl, instagramUrl,
    pinterestUrl, pixivUrl, tumblrUrl, twitterUrl, weiboUrl, otherUrl) => {
    const url = `/api/artists/create`;
    const formData = new FormData();

    formData.append('name', name);
    formData.append('serial_number', serialNumber);
    formData.append('pinterest_page_url', pinterestPageUrl);
    formData.append('artstation_url', artstationUrl);
    formData.append('behance_url', behanceUrl);
    formData.append('deviantart_url', deviantartUrl);
    formData.append('facebook_url', facebookUrl);
    formData.append('instagram_url', instagramUrl);
    formData.append('pinterest_url', pinterestUrl);
    formData.append('pixiv_url', pixivUrl);
    formData.append('tumblr_url', tumblrUrl);
    formData.append('twitter_url', twitterUrl);
    formData.append('weibo_url', weiboUrl);
    formData.append('other_url', otherUrl);

    $.ajax({
        type: 'POST',
        url,
        data: formData,
        processData: false,
        contentType: false,
    }).then(function(data) {
        $('#create-artist-modal').modal('hide');
        alertSuccess('新增');

        const newArtistHtml = `
            <tr id="artist-info-${data['data']['id']}">
                ${artistDataToHtmlString(data['data'])}
            </tr>`;
        $('#artist-table-content').prepend(newArtistHtml);
        // $('.btn-update').unbind('click');
        // $('.btn-update').click(btnUpdcvateListener);

        const maxArtistNumber = $('#max-artist-number').html();
        $('#max-artist-number').html(parseInt(maxArtistNumber) + 1);
    }).fail(function(xhr) {
        alertFail(xhr, '新增');
    });
};

// $('#update-button').click(function() {
//     const boardId = $('#update-board-id').val();
//     const name = $('#update-board-name').val();
//     let tagsId = $('input[name="update-tag"]:checked').map(function(){
//         return $(this).val();
//     }).get();
//     tagsId = tagsId.join(',');

//     if (name === '' || tagsId === '') {
//         alertSubmitFail('更新');
//         return;
//     }

//     updateBoard(boardId, name, tagsId);
// });

// const updateBoard = (boardId, name, tagsId) => {
//     const artistNumber = $('#artist-number').html();
//     const url = `/api/artists/${artistNumber}/board/${boardId}/update`;
//     const formData = new FormData();

//     formData.append('name', name);
//     formData.append('tag_ids', tagsId);
//     console.log(name)
//     console.log(tagsId)

//     $.ajax({
//         type: 'POST',
//         url,
//         data: formData,
//         processData: false,
//         contentType: false,
//     }).then(function(data) {
//         $('#update-board-modal').modal('hide');
//         alertSuccess('更新');
        
//         // update table row
//         const htmlString = boardDataToHtmlString(data['data']);
//         $(`#board-info-${boardId}`).html(htmlString);
//         $('.btn-update').unbind('click');
//         $('.btn-update').click(btnUpdateListener);
//     }).fail(function(xhr) {
//         alertFail(xhr, '更新');
//     });
// };

const artistDataToHtmlString = (data) => {
    const {
        name,
        serial_number: serialNumber,
        pinterest_page_url: pinterestPageUrl,
    } = data;

    let artistName = '-';
    if (name) {
        artistName = name;
    }

    const htmlString = `
        <td> ${serialNumber} </td>
        <td>
            <a href=${pinterestPageUrl} target="_blank">
                <img class="icon-img" src="../media/pinterest.png"/>
            </a>
            &emsp;
            <a href="/artists/${serialNumber}" target="_blank">
                ${artistName}
            </a>
        </td>`;

    return htmlString;
}

const refreshArtistTable = (data) => {
    $('.btn-update').unbind('click');

    const tableName = '#artist-table-content';
    $(tableName).empty();

    const {
        data: artists,
    } = data;

    for (let i = 0; i < artists.length; i++) {
        const htmlString = `
            <tr id="artist-info-${artists[i]['id']}">
                ${artistDataToHtmlString(artists[i])}
            </tr>`;
        $(tableName).append(htmlString);
    }

    $('.btn-update').click(btnUpdateListener);
};
