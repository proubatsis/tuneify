$(document).ready(function() {
    var is_loading = false;
    var btn = $("#createSpotifyPlaylistButton");
    var btnText = btn.text();

    var startLoading = function() {
        is_loading = true;
        btn.text("");
        btn.addClass("fa-refresh");
        btn.addClass("fa-spin");
    };

    var doneLoading = function() {
        is_loading = false;
        btn.text(btnText);
    };

    var removeSpinner = function() {
        btn.removeClass("fa-refresh");
        btn.removeClass("fa-spin");
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