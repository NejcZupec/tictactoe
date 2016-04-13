$(document).ready(function () {

    // start a new TicTacToe game
    var game = new TicTacToeGame($("#board"));
});

function TicTacToeGame(boardObject) {
    this.board = boardObject;
    this.currentPlayer = 'p1';

    this.registerEvents();
}

TicTacToeGame.prototype = {

    addCircleToField: function (field) {
        field.removeClass('empty');
        field.addClass('field-circle');
        field.append('<div class="circle"></div>');
    },

    addCrossToField: function (field) {
        field.removeClass('empty');
        field.addClass('field-cross');
    },

    clickOnField: function (field) {

        // check if the move is valid
        if (field.hasClass('empty')) {
            if (this.currentPlayer == 'p1') {
                this.addCrossToField(field);
                this.currentPlayer = 'p2';
            } else {
                this.addCircleToField(field);
                this.currentPlayer = 'p1';
            }

            // toggle player
            $("#player-1-info").toggleClass('player-info-active');
            $("#player-2-info").toggleClass('player-info-active');
        }
    },

    registerEvents: function () {
        var that = this;

        $('.field').on('click', function () {
            that.clickOnField($(this));
        });
    }
};