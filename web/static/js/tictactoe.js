function TicTacToeGame(boardObject, currentPlayer, newMoveUrl, aiNextMoveUrl, aiPlayer) {
    this.board = boardObject;
    this.currentPlayer = currentPlayer;
    this.newMoveUrl = newMoveUrl;
    this.aiNextMoveUrl = aiNextMoveUrl;
    this.aiPlayer = aiPlayer;

    this.registerEvents();
    this.startGame();
}

TicTacToeGame.prototype = {

    addCircle: function (x, y) {
        var field = $("#field-" + x + "-" + y);
        field.removeClass("field-empty");
        field.addClass("field-circle");
        field.append("<div class='circle'></div>");
    },

    addCross: function (x, y) {
        var field = $("#field-" + x + "-" + y);
        field.removeClass("field-empty");
        field.addClass("field-cross");
    },

    addCrossOrCircle: function (x, y) {
        if (this.currentPlayer === "p1") {
            this.addCross(x, y);
        } else {
            this.addCircle(x, y);
        }
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

        // check if move is valid and if it is, send it to the server
        if (field.hasClass("field-empty")) {
            var fieldId = field.attr("id");
            var x = fieldId.charAt(6);
            var y = fieldId.charAt(8);
            this.sendMoveToServer(this.currentPlayer, x, y);
            this.addCrossOrCircle(x, y);
        }
    },

    lockFields: function () {
        $(".field").removeClass("field-empty");
    },

    showResult: function (response) {
        var txt;

        if (response === "x") {
            txt = "Player 1 wins!";
            $(".player-1-result").addClass("text-success");
            $(".player-2-result").removeClass("text-success");
        } else if (response === "o") {
            txt = "Player 2 wins!";
            $(".player-1-result").removeClass("text-success");
            $(".player-2-result").addClass("text-success");
        } else {
            txt = "Draw";
            $(".player-1-result").removeClass("text-success");
            $(".player-2-result").removeClass("text-success");
        }

        $("#game-ended-modal h2").html(txt);
        $("#game-ended-modal").modal();
    },

    sendMoveToServer: function (player, x, y) {
        var that = this;

        $.ajax({
            type: "POST",
            url: that.newMoveUrl,
            data: {
                "player": player,
                "x": x,
                "y": y,
            },
            success: function (response) {

                // game is in_progress
                if (response === "None") {
                    that.togglePlayers();

                    if (that.aiPlayer === that.currentPlayer) {
                        that.getAiNextMove();
                    }

                // game has ended
                } else {
                    that.lockFields();
                    that.showResult(response);
                }
            }
        });
    },

    registerEvents: function () {
        var that = this;

        $(".field").on("click", function () {
            that.clickOnField($(this));
        });
    },

    getAiNextMove: function () {
        var that = this;

        $.ajax({
            type: "GET",
            url: this.aiNextMoveUrl,
            success: function (data) {

                that.addCrossOrCircle(data.x, data.y);
                that.sendMoveToServer(that.currentPlayer, data.x, data.y);
            }
        });
    },

    startGame: function () {
        if (this.aiPlayer === this.currentPlayer) {
            this.getAiNextMove();
        }
    }
};