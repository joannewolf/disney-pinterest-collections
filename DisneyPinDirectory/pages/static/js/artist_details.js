$(document).ready(() => {
    $('.btn-create').click(function () {
        $('#create-board-name').val('');
        $('.tag-label').removeClass('checked');
        $('.tag-label input[type=checkbox]').prop('checked', false);
    });
    $('.btn-update').click(btnUpdateListener);

    fetchBoards()
});

$('.tag-label input[type=checkbox]').change(function() {
    $(this).parent().toggleClass('checked');
});

function btnUpdateListener() {
    const boardId = $(this).data('board-id');
    $('#update-board-id').val(boardId);
    const name = $(this).data('board-name');
    $('#update-board-name').val(name);

    $('.tag-label').removeClass('checked');
    $('.tag-label input[type=checkbox]').prop('checked', false);
    var tagsId = $(this).data('board-tags-id').toString();
    tagsId = tagsId.split(',');
    for (const id of tagsId) {
        $(`#update-tag-${id}`).addClass('checked');
        $(`#update-tag-${id} input[type=checkbox]`).prop('checked', true);
    }
}

const fetchBoards = () => {
    const tableName = '#board-table-content';
    $(tableName).empty();
    const htmlString = `
        <tr>
            <td> Searching... </td>
            ${'<td> - </td>'.repeat(1)}
        </tr>
    `;
    $(tableName).append(htmlString);

    const artistNumber = $('#artist-number').html();
    const url = `/artists/${artistNumber}/boards`;
    $.ajax({
        type: 'GET',
        url,
        traditional: true,
    }).then(function(data) {
        refreshBoardTable(data);
    }).fail(function(xhr) {
        alertFail(xhr, '讀取記錄');
    });
};

$('#create-button').click(function() {
    const name = $('#create-board-name').val();
    let tagsId = $('input[name="create-tag"]:checked').map(function(){
        return $(this).val();
    }).get();
    tagsId = tagsId.join(',');

    if (name === '' || tagsId === '') {
        alertSubmitFail('新增');
        return;
    }

    createBoard(name, tagsId);
});

const createBoard = (name, tagsId) => {
    const artistNumber = $('#artist-number').html();
    const url = `/artists/${artistNumber}/board/create`;
    const formData = new FormData();

    formData.append('name', name);
    formData.append('tag_ids', tagsId);
    console.log(name)
    console.log(tagsId)

    $.ajax({
        type: 'POST',
        url,
        data: formData,
        processData: false,
        contentType: false,
    }).then(function(data) {
        $('#create-board-modal').modal('hide');
        alertSuccess('新增');

        const newBoardHtml = boardDataToHtmlString(data['data']);
        $('#board-table-content tr:last').after(newBoardHtml);
        $('.btn-update').unbind('click');
        $('.btn-update').click(btnUpdateListener);
    }).fail(function(xhr) {
        alertFail(xhr, '新增');
    });
};

$('#update-button').click(function() {
    const boardId = $('#update-board-id').val();
    const name = $('#update-board-name').val();
    let tagsId = $('input[name="update-tag"]:checked').map(function(){
        return $(this).val();
    }).get();
    tagsId = tagsId.join(',');

    if (name === '' || tagsId === '') {
        alertSubmitFail('更新');
        return;
    }

    updateBoard(boardId, name, tagsId);
});

const updateBoard = (boardId, name, tagsId) => {
    const artistNumber = $('#artist-number').html();
    const url = `/artists/${artistNumber}/board/${boardId}/update`;
    const formData = new FormData();

    formData.append('name', name);
    formData.append('tag_ids', tagsId);
    console.log(name)
    console.log(tagsId)

    $.ajax({
        type: 'POST',
        url,
        data: formData,
        processData: false,
        contentType: false,
    }).then(function(data) {
        $('#update-board-modal').modal('hide');
        alertSuccess('更新');
        
        // update table row
        const htmlString = boardDataToHtmlString(data['data']);
        $(`#board-info-${boardId}`).html(htmlString);
        $('.btn-update').unbind('click');
        $('.btn-update').click(btnUpdateListener);
    }).fail(function(xhr) {
        alertFail(xhr, '更新');
    });
};

const boardDataToHtmlString = (data) => {
    const {
        id,
        name,
        tags,
    } = data;

    let tagsHtml = '';
    for (const tag of tags) {
        const tagHtml = `
            <a href=/tags/${tag.id}>
                <label class="tag-label" style="background-color:${tag.color};">
                    ${tag.name}
                </label>
            </a>`;
        tagsHtml = tagsHtml.concat(tagHtml);
    }
    const tagsId = tags.map(({ id }) => id).join(',');

    const buttonHtml = `
        <button class="btn btn-primary btn-update btn-custom"
            data-board-id=${id} data-board-name=${name}
            data-board-tags-id="${tagsId}"
            data-toggle="modal" data-target="#update-board-modal"
        >
            <i class="fa fa-pencil"></i>
        </button>`;

    const htmlString = `
        <td> ${name} </td>
        <td> ${buttonHtml} </td>
        <td> ${tagsHtml} </td>`;

    return htmlString;
}

const refreshBoardTable = (data) => {
    $('.btn-update').unbind('click');

    const tableName = '#board-table-content';
    $(tableName).empty();

    const {
        data: boards,
    } = data;

    for (let i = 0; i < boards.length; i++) {
        const htmlString = `
            <tr id="board-info-${boards[i]['id']}">
                ${boardDataToHtmlString(boards[i])}
            </tr>`;
        $(tableName).append(htmlString);
    }

    $('.btn-update').click(btnUpdateListener);
};