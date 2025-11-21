class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status__ = False
        self.__muted__ = False
        self.__volume__ = Television.MIN_VOLUME
        self.__channel__ = Television.MIN_CHANNEL

    def power(self):
        self.__status__ = not self.__status__

    def mute(self):
        if self.__status__:
            self.__muted__ = not self.__muted__

    def channel_up(self):
        if self.__status__:
            if self.__channel__ == Television.MAX_CHANNEL:
                self.__channel__ = Television.MIN_CHANNEL
            else:
                self.__channel__ += 1

    def channel_down(self):
        if self.__status__:
            if self.__channel__ == Television.MIN_CHANNEL:
                self.__channel__ = Television.MAX_CHANNEL
            else:
                self.__channel__ -= 1

    def volume_up(self):
        if self.__status__:
            if self.__muted__:
                Television.mute(self)
            if self.__volume__ < Television.MAX_VOLUME:
                self.__volume__ += 1

    def volume_down(self):
        if self.__status__:
            if self.__muted__:
                Television.mute(self)
            if self.__volume__ > Television.MIN_VOLUME:
                self.__volume__ -= 1

    def __str__(self):
        if self.__muted__:
            return f'Power - {self.__status__}, Channel - {self.__channel__}, Volume - {0}.'
        else:
            return f'Power - {self.__status__}, Channel - {self.__channel__}, Volume - {self.__volume__}.'