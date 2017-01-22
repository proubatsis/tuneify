$(document).ready(function() {
    var is_loading = false;
    var btn = $("#createSpotifyPlaylistButton");
    var btnIco = $(btn).find("i");
    var btnPar = $(btn).find("p");
    var btnText = btnPar.text();

    var startLoading = function() {
        is_loading = true;
        btnPar.text("");
        btnIco.addClass("fa");
        btnIco.addClass("fa-refresh");
        btnIco.addClass("fa-spin");
    };

    var doneLoading = function() {
        is_loading = false;
        btnPar.text(btnText);
    };

    var removeSpinner = function() {
        btnIco.removeClass("fa-refresh");
        btnIco.removeClass("fa-refresh");
        btnIco.removeClass("fa-spin");
    };

    btn.click(function() {
        if(!is_loading) {
            startLoading();

            $.ajax({
                contentType: "application/json",
                data: JSON.stringify({
                    subreddit: $("#subredditInput").val(),
                    playlist_name: $("#playlistInput").val()
                }),
                error: function() {
                    removeSpinner();
                    btn.text("Error!");
                    setTimeout(doneLoading, 2500);
                },
                success: function() {
                    removeSpinner();
                    btn.text("Playlist Created!");
                    setTimeout(doneLoading, 2500);
                },
                type: "POST",
                url: "/api/spotify/playlist"
            });
        }
    });
});