$(document).ready(() => {
    $('.btn-create').click(btnCreateListener);
    $('.btn-update').click(btnUpdateListener);

    // default action
    $('#filter-form-btn').trigger('click');
});

function btnCreateListener() {
    $('#create-author-name').val('');
}

function btnUpdateListener() {
    const authorId = $(this).data('author-id');
    const name = $(this).data('author-name');

    $('#update-author-id').html(authorId);
    $('#update-author-name').val(name);
}


let formData = {};
let pageNumber = 1;

$('#filter-form-btn').click(function() {
    // Reset
    pageNumber = 1;

    const name = $('#search-name').val();
    const perPage = $('#search-per-page').val();

    formData.name = name;
    formData.per_page = perPage;

    fetchAuthors();
});

const fetchAuthors = () => {
    formData.page_number = pageNumber;
    const tableName = '#author-table-content';
    $(tableName).empty();
    const htmlString = `
        <tr>
            <td> 搜尋中... </td>
            ${'<td> - </td>'.repeat(3)}
        </tr>
    `;
    $(tableName).append(htmlString);

    const url = '/api/v1/admin/authors';
    $.ajax({
        type: 'GET',
        url,
        data: formData,
        traditional: true,
    }).then(function(data) {
        refreshAuthorTable(data);
    }).fail(function(xhr) {
        alertFail(xhr, '讀取記錄');
    });
};

$('#create-button').click(function() {
    const name = $('#create-author-name').val();

    if (name === '') {
        alertSubmitFail('新增');
        return;
    }

    createAuthor(name);
});

const createAuthor = (name) => {
    const url = `/api/v1/admin/author/create`;
    const formData = new FormData();

    formData.append('name', name);

    $.ajax({
        type: 'POST',
        url,
        data: formData,
        processData: false,
        contentType: false,
    }).then(function(data) {
        $('#create-author-modal').modal('hide');
        alertSuccess('新增');

        clearFilter();
        $('#filter-form-btn').trigger('click');
    }).fail(function(xhr) {
        alertFail(xhr, '新增');
    });
};

$('#update-button').click(function() {
    const authorId = $('#update-author-id').html();
    const name = $('#update-author-name').val();

    if (name === '') {
        alertSubmitFail('更新');
        return;
    }

    updateAuthor(authorId, name);
});

const updateAuthor = (authorId, name) => {
    const url = `/api/v1/admin/author/${authorId}/update`;
    const formData = new FormData();

    formData.append('name', name);

    $.ajax({
        type: 'POST',
        url,
        data: formData,
        processData: false,
        contentType: false,
    }).then(function(data) {
        $('#update-author-modal').modal('hide');
        alertSuccess('更新');

        // update table
        $('.btn-update').unbind('click');
        const {
            id,
            name,
        } = data['data'];
        $(`#author-info-${id}`).find('td').eq(1).html(name);
        $(`#update-author-button-${id}`).data('author-name', name);
        $('.btn-update').click(btnUpdateListener);

    }).fail(function(xhr) {
        alertFail(xhr, '更新');
    });
};

const clearFilter = () => {
    $('#search-name').val('');
    $('#search-per-page').val('10').change();
    pageNumber = 1;
}

const authorDataToHtmlString = (data) => {
    const {
        id,
        name,
        book_count: bookCount,
    } = data;

    
    const buttonHtml = `
        <button class="btn btn-primary btn-update btn-custom"
            id="update-author-button-${id}"
            data-author-id="${id}" data-author-name="${name}"
            data-toggle="modal" data-target="#update-author-modal"
        >
            編輯
        </button>`;

    const htmlString = `
        <td> ${id} </td>
        <td> ${name} </td>
        <td> ${bookCount} </td>
        <td> ${buttonHtml} </td>`;

    return htmlString;
}

const refreshAuthorTable = (data) => {
    $('.btn-update').unbind('click');

    const tableName = '#author-table-content';
    $(tableName).empty();

    const {
        data: authors,
        total_count: totalCount,
        num_pages: numPages
    } = data;

    if (authors.length > 0) {
        for (let i = 0; i < authors.length; i++) {
            const htmlString = `
                <tr id="author-info-${authors[i]['id']}">
                    ${authorDataToHtmlString(authors[i])}
                </tr>`;
            $(tableName).append(htmlString);
        }
    }
    else {
        const htmlString = `
            <tr>
                <td> 當前條件查無資料 </td>
                ${'<td> - </td>'.repeat(3)}
            </tr>
        `;
        $(tableName).append(htmlString);
    }

    $('#author-pagination').html(generatePaginationHtmlString(numPages, 'fetchAuthors'));
    $('#total-amount').html(totalCount);
    $('#current-page-amount').html(authors.length);

    $('.btn-update').click(btnUpdateListener);
};
