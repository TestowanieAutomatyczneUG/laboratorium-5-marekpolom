import unittest
import src.song

song = src.song.song

class HammingTest(unittest.TestCase):
    def test_song_first_day(self):
        self.assertEqual(song(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")