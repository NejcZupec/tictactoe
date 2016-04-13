function TicTacToeGame(boardObject) {
    this.board = boardObject;
    this.currentPlayer = "p1";

    this.registerEvents();
}

TicTacToeGame.prototype = {

    addCircleToField: function (field) {
        field.removeClass("field-empty");
        field.addClass("field-circle");
        field.append("<div class='circle'></div>");
    },

    addCrossToField: function (field) {
        field.removeClass("field-empty");
        field.addClass("field-cross");
    },

    togglePlayers: function () {
        if (this.currentPlayer === "p1") {
            this.currentPlayer = "p2";
        } else {
            this.currentPlayer = "p1";
        }

        // toggle players info divs
        $("#player-1-info").toggleClass("player-info-active");
        $("#player-2-info").toggleClass("player-info-active");
    },

    clickOnField: function (field) {
        var that = this;

        // check if move is valid and if it is, send it to the server
        if (field.hasClass("field-empty")) {
            this.sendMoveToServer(this.currentPlayer, field);

            if (this.currentPlayer === "p1") {
                that.addCrossToField(field);
            } else {
                that.addCircleToField(field);
            }
        }
    },

    lockFields: function () {
        $(".field").removeClass('field-empty');
    },

    sendMoveToServer: function (player, field) {
        var fieldId = field.attr("id");
        var x = fieldId.charAt(6);
        var y = fieldId.charAt(8);
        var that = this;

        $.ajax({
            type: "POST",
            url: newMoveUrl,
            data: {
                "player": player,
                "x": x,
                "y": y,
            },
            success: function (response) {
                if (response === 'None') {
                    that.togglePlayers();
                } else {
                    that.lockFields();
                    alert(response);
                }
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