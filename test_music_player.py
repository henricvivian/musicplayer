# tests/test_music_player.py

import unittest
import os
from src.music_player import load_music

class TestMusicPlayer(unittest.TestCase):

    def test_load_music_file_exists(self):
        """
        Test loading a music file that exists.
        """
        self.assertTrue(load_music("src/assets/your_music_file.mp3"))

    def test_load_music_file_not_exists(self):
        """
        Test loading a music file that does not exist.
        """
        self.assertFalse(load_music("non_existent_file.mp3"))

if __name__ == '__main__':
    unittest.main()
