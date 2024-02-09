import keyboard
import time
import pyautogui

def load_positions(file_path):
    """Load positions from the file."""
    with open(file_path, 'r') as f:
        positions = [tuple(map(int, line.strip().split(', '))) for line in f]
    return positions

def replay_mouse_slow(positions, duration_per_move=0):
    print("Press 'space' to start replaying.")
    keyboard.wait('space')
    print("Starting replay...")
    time.sleep(3)  # Introduce a 3-second delay after pressing spacebar

    for pos in positions:
        x, y = pos
        pyautogui.moveTo(x, y, duration=duration_per_move)  # Move cursor to the position
        time.sleep(duration_per_move)  # Wait for the specified duration before moving to the next position

    print("Replay completed.")

def main():
    file_path = 'mouse_path.txt'
    positions = load_positions(file_path)
    replay_mouse_slow(positions)

if __name__ == "__main__":
    main()
