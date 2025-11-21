import unittest
from television import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.television = Television()

    def tearDown(self):
        del self.television

    def test_init(self):
        self.assertEqual(self.television.__str__(), 'Power - False, Channel - 0, Volume - 0.')

    def test_power(self):
        self.television.power()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 0.')
        self.television.power()
        self.assertEqual(self.television.__str__(), 'Power - False, Channel - 0, Volume - 0.')

    def test_mute(self):
        self.television.power()
        self.television.volume_up()
        self.television.mute()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 0.')
        self.television.mute()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 1.')
        self.television.power()
        self.television.mute()
        self.assertEqual(self.television.__str__(), 'Power - False, Channel - 0, Volume - 1.')
        self.television.mute()
        self.assertEqual(self.television.__str__(), 'Power - False, Channel - 0, Volume - 1.')

    def test_channel_up(self):
        self.television.channel_up()
        self.assertEqual(self.television.__str__(), 'Power - False, Channel - 0, Volume - 0.')
        self.television.power()
        self.television.channel_up()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 1, Volume - 0.')
        self.television.channel_up()
        self.television.channel_up()
        self.television.channel_up()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 0.')

    def test_channel_down(self):
        self.television.channel_down()
        self.assertEqual(self.television.__str__(), 'Power - False, Channel - 0, Volume - 0.')
        self.television.power()
        self.television.channel_down()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 3, Volume - 0.')

    def test_volume_up(self):
        self.television.volume_up()
        self.assertEqual(self.television.__str__(), 'Power - False, Channel - 0, Volume - 0.')
        self.television.power()
        self.television.volume_up()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 1.')
        self.television.mute()
        self.television.volume_up()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 2.')
        self.television.volume_up()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 2.')

    def test_volume_down(self):
        self.television.volume_down()
        self.assertEqual(self.television.__str__(), 'Power - False, Channel - 0, Volume - 0.')
        self.television.power()
        self.television.volume_up()
        self.television.volume_up()
        self.television.volume_down()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 1.')
        self.television.volume_up()
        self.television.mute()
        self.television.volume_down()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 1.')
        self.television.volume_down()
        self.television.volume_down()
        self.assertEqual(self.television.__str__(), 'Power - True, Channel - 0, Volume - 0.')


if __name__ == '__main__':
    unittest.main()