function TicTacToeGame(boardObject) {
    this.board = boardObject;
    this.currentPlayer = "p1";

    this.registerEvents();
}

TicTacToeGame.prototype = {

    addCircleToField: function (field) {
        field.removeClass("empty");
        field.addClass("field-circle");
        field.append("<div class='circle'></div>");
    },

    addCrossToField: function (field) {
        field.removeClass("empty");
        field.addClass("field-cross");
    },

    clickOnField: function (field) {

        // check if the move is valid
        if (field.hasClass("empty")) {
            if (this.currentPlayer === "p1") {
                this.addCrossToField(field);
                this.sendMoveToServer("p1", field);
                this.currentPlayer = "p2";
            } else {
                this.addCircleToField(field);
                this.sendMoveToServer("p2", field);
                this.currentPlayer = "p1";
            }

            // toggle player
            $("#player-1-info").toggleClass("player-info-active");
            $("#player-2-info").toggleClass("player-info-active");
        }
    },

    sendMoveToServer: function (player, field) {
        var field_id = field.attr("id");
        var x = field_id.charAt(6);
        var y = field_id.charAt(8);

        $.ajax({
            type: "POST",
            url: new_move_url,
            data: {
                'player': player,
                'x': x,
                'y': y,
            },
            success: function (response) {

            }
        });
    },

    registerEvents: function () {
        var that = this;

        $(".field").on("click", function () {
            that.clickOnField($(this));
        });
    }
};