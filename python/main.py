from pydub import AudioSegment
from pydub.playback import play
import os
import random
import time


SOUNDS_DIR = 'sounds'
DELAY_SECONDS = 5


def run():
    bird_sounds = load_sounds()

    while True:
        print('Playing a sound')
        play(random_sound(bird_sounds))
        time.sleep(DELAY_SECONDS)


def load_sounds():
    return [AudioSegment.from_wav(os.path.join(SOUNDS_DIR, f)) for f in os.listdir(SOUNDS_DIR)]


def random_sound(sounds):
    r = random.randint(0, len(sounds))
    print(r)
    return sounds[r]


if __name__ == '__main__':
    run()

