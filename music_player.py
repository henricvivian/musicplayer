# src/music_player.py

import pygame
import os
import sys

# Initialize Pygame mixer
pygame.mixer.init()

# Initialize Pygame display
pygame.display.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Enhanced Music Player')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)

# Load and play a music file
def load_music(file_path):
    """
    Loads and plays the specified music file.
    """
    if os.path.exists(file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(-1)  # Loop the music
            return True
        except pygame.error as e:
            print(f"Unable to load {file_path}: {e}")
            return False
    else:
        print(f"File not found: {file_path}")
        return False

# Draw text on the screen
def draw_text(text, position, size=24, color=WHITE):
    """
    Draws the specified text on the screen at the given position.
    """
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# Draw button
def draw_button(text, rect, color, hover_color, action=None):
    """
    Draws a button with the specified properties and action.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if rect[0] < mouse[0] < rect[0] + rect[2] and rect[1] < mouse[1] < rect[1] + rect[3]:
        pygame.draw.rect(screen, hover_color, rect)
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(screen, color, rect)
    
    draw_text(text, (rect[0] + 10, rect[1] + 10), size=20)

def pause_music():
    """
    Pauses the currently playing music.
    """
    pygame.mixer.music.pause()
    print("Music paused")

def resume_music():
    """
    Resumes the paused music.
    """
    pygame.mixer.music.unpause()
    print("Music resumed")

def stop_music():
    """
    Stops the currently playing music.
    """
    pygame.mixer.music.stop()
    print("Music stopped")

def quit_program():
    """
    Quits the program.
    """
    pygame.quit()
    sys.exit()

def main():
    """
    Main function to run the music player.
    """
    running = True
    music_file = "src/assets/your_music_file.mp3"  # Replace with your own music file path
    if not load_music(music_file):
        return

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background
        screen.fill(DARK_GRAY)

        # Draw title
        draw_text("Enhanced Music Player", (150, 50), size=36)

        # Draw buttons
        draw_button("Pause", (150, 150, 100, 50), BLUE, LIGHT_GRAY, pause_music)
        draw_button("Resume", (350, 150, 100, 50), BLUE, LIGHT_GRAY, resume_music)
        draw_button("Stop", (150, 250, 100, 50), BLUE, LIGHT_GRAY, stop_music)
        draw_button("Quit", (350, 250, 100, 50), BLUE, LIGHT_GRAY, quit_program)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
