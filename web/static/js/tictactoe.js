$(document).ready(function () {

    var currentPlayer = 'x';

    $('.field').on('click', function (field) {

        // check if the move is valid
        if ($(this).hasClass('empty')) {
            if (currentPlayer == 'x') {
                addCrossToField($(this));
                currentPlayer = 'o';
            } else {
                addCircleToField($(this));
                currentPlayer = 'x';
            }

            // toggle player
            $("#player-1-info").toggleClass('player-info-active');
            $("#player-2-info").toggleClass('player-info-active');
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