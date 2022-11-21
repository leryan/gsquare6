class TrackTracker():
    def __init__(self):
        self._tracks = []
    def add (self, list):
        self._tracks.append(list)
        # Parameters:
        #   Track : string representing music track that was listened to

    def track_list_listened(self):
        return self._tracks
        # Returns:
        #   A list of tracks the user has listened to