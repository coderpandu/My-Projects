# ********** ALARM CLOCK PROJECT **********

import time
import datetime
import pygame   # Working with sounds


def set_alarm(alarm_time):
    print(f"\nAlarm set for {alarm_time}")

    sound_file = "Projects/Final Boss Battle - Rod Kim.mp3"
    is_running = True

    while is_running:
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        # Check if alarm time matches current time
        if current_time == alarm_time:
            print("WAKE UP! 😴")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Wait until sound finishes
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)