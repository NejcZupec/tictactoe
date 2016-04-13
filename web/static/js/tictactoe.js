$(document).ready(function () {

    var currentPlayer = 'x';

    $('.field').on('click', function (field) {

        if ($(this).hasClass('empty')) {
            if (currentPlayer == 'x') {
                addCrossToField($(this));
                currentPlayer = 'o';
            } else {
                addCircleToField($(this));
                currentPlayer = 'x';
            }
        }
    })
});

function addCircleToField(field) {
    field.removeClass('empty');
    field.addClass('field-circle');
    field.append('<div class="circle"></div>')
}

function addCrossToField(field) {
    field.removeClass('empty');
    field.addClass('field-cross');
}