function TicTacToeGame(boardObject, currentPlayer, newMoveUrl, aiNextMoveUrl, aiPlayer, onlineGame, opponentMoveUrl,
                       player, sequenceNo) {
    this.board = boardObject;
    this.currentPlayer = currentPlayer; // ['p1', 'p2']
    this.newMoveUrl = newMoveUrl;
    this.aiNextMoveUrl = aiNextMoveUrl;
    this.aiPlayer = aiPlayer;  // ['p1', 'p2', '']
    this.onlineGame = onlineGame;  // ['true', 'false']
    this.opponentMoveUrl = opponentMoveUrl;
    this.player = player;  // [p1, p2] in this browser only this user can play
    this.sequenceNo = parseInt(sequenceNo);

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
        $("#player-1-info .h4-your-turn").toggleClass("h4-your-turn-hidden");
        $("#player-2-info .h4-your-turn").toggleClass("h4-your-turn-hidden");

        // lock/unlock fields
        this.toggleLockUnlockFields();

        // increment sequence number
        this.sequenceNo++;
    },

    clickOnField: function (field) {
        // check if move is valid and if it is, send it to the server
        if (field.hasClass("field-empty") && !field.hasClass("field-locked")) {
            var fieldId = field.attr("id");
            var x = fieldId.charAt(6);
            var y = fieldId.charAt(8);
            this.sendMoveToServer(this.currentPlayer, x, y);
            this.addCrossOrCircle(x, y);
        }
    },

    lockFields: function () {
        $(".field").addClass("field-locked");
    },

    unlockFields: function () {
        $(".field").removeClass("field-locked");
    },

    toggleLockUnlockFields: function () {
        if (this.player !== '' &&  this.player !== this.currentPlayer) {
            this.lockFields();
        } else if (this.player !== '' && this.player == this.currentPlayer) {
            this.unlockFields();
        }
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
                    } else if (that.onlineGame === 'true') {
                        that.opponentMoveListener();
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

    opponentMoveListener: function () {
        var that = this;

        if (this.player !== this.currentPlayer) {
            $.ajax({
                type: "GET",
                url: this.opponentMoveUrl,
                data: {
                    "opponent_player": this.currentPlayer,
                    "sequence_no": this.sequenceNo
                },
                success: function (data) {
                    if (data !== null) {
                        that.addCrossOrCircle(data.x, data.y);

                        // game is in_progress
                        if (data.action == null) {
                            that.togglePlayers();

                        // game has ended
                        } else {
                            that.lockFields();
                            that.showResult(data.action);
                        }
                    } else {
                        setTimeout(function () {
                            that.opponentMoveListener();
                        ;}, 500);
                    }
                }
            });
        }
    },

    startGame: function () {
        this.toggleLockUnlockFields();

        if (this.aiPlayer === this.currentPlayer) {
            this.getAiNextMove();
        }

        if (this.onlineGame === 'true') {
            this.opponentMoveListener();
        }
    }
};