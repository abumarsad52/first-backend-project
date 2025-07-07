import time
import datetime
import pygame
def validate_time_format(t):
    try:
        datetime.datetime.strptime(t,"%H:%M:%S")
    except ValueError:
        return False
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"⏰ Current Time: {current_time}", end="\r")
        if current_time == alarm_time:
            print("\n🚨 Wake Up! 🚨")
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                print("▶️ Playing alarm... Press Enter to stop.")
                input()
                pygame.mixer.music.stop()
            except Exception as e:
                print(f"Error playing sound: {e}")
            is_running = False
        time.sleep(1)   
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
