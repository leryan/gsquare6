from lib.tracklist import TrackTracker

"""
Initially there are no tracks listened to 
"""
def test_no_tracks_listened_to_returns_empty_list():
    tracker = TrackTracker()
    assert tracker.track_list_listened() == []

"""
When the user listens to a song
It is added to the list of songs that the user has listened to
"""
def test_user_listens_to_song_adds_to_list():
    tracker = TrackTracker()
    tracker.add("50 Cent - Many men")
    assert tracker.track_list_listened() == ["50 Cent - Many men"]

"""
When the user listens to multiple songs
They are added to the list of tracks
"""
def test_multiple_songs_added():
    tracker = TrackTracker()
    tracker.add("50 Cent - Many men")
    tracker.add("2Pac - Temptations")
    tracker.add("Tears For Fears - Everybody wants to rule the world")
    assert tracker.track_list_listened() == ["50 Cent - Many men", "2Pac - Temptations", "Tears For Fears - Everybody wants to rule the world"]
