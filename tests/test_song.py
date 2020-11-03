import unittest
import src.song

song = src.song.song

class HammingTest(unittest.TestCase):
    def test_song_first_day(self):
        self.assertEqual(song(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_song_second_day(self):
        self.assertEqual(song(2), "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_song_third_day(self):
        self.assertEqual(song(3), "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")
    
    def test_song_fourth_day(self):
        self.assertEqual(song(4), "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")
    
    def test_song_fifth_day(self):
        self.assertEqual(song(5), "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")
    
    def test_song_sixth_day(self):
        self.assertEqual(song(6), "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")
    
    def test_song_seventh_day(self):
        self.assertEqual(song(7), "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    