# Story

class Tracks:
    # User-facing properties:
    #   name: string

User Story

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


class TrackTracker():
    def add (self, list):
        # Parameters:
        #   Track : string representing music track that was listened to
        pass

    def track_list_listened(self):
        # Returns:
        #   A list of tracks the user has listened to
        pass


# EXAMPLE

"""
Initially there are no tracks listened to 
"""
tracker = TrackTracker()
tracker.track_list_listened() # => []

"""
When the user listens to a song
It is added to the list of songs that the user has listened to
"""
tracker = TrackTracker()
tracker.add("50 Cent - Many men")
tracker.track_list_listened() # => ["50 Cent - Many men"]

"""
When the user listens to multiple songs
They are added to the list of tracks
"""
tracker = TrackTracker()
tracker.add("50 Cent - Many men")
tracker.add("2Pac - Temptations")
tracker.add("Tears For Fears - Everybody wants to rule the world")
tracker.track_list_listened() # => [
    "50 Cent - Many men", "2Pac - Temptations", "Tears For Fears - Everybody wants to rule the world"]
