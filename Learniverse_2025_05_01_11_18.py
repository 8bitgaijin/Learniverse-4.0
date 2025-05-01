# -*- coding: utf-8 -*-
"""
Learniverse OS Demo - Cross-platform Pygame Test
Functional/Procedural Style - No OOP
"""

import pygame
# import platform
import random

from modules.os_utils import detect_os_name, get_local_path
# from pathlib import Path



# def get_local_path(os_name):
#     """Dispatch to OS-specific function to resolve script directory."""
#     try:
#         if os_name == "Windows":
#             return get_windows_path()
#         elif os_name == "macOS":
#             return get_mac_path()
#         elif os_name == "Linux":
#             return get_linux_path()
#         else:
#             raise ValueError(f"Unsupported OS: {os_name}")
#     except Exception as error:
#         print(f"[WARN] Path resolution failed: {error}")
#         return Path.cwd()


# def get_windows_path():
#     """Return the local path on Windows."""
#     return Path(__file__).resolve().parent


# def get_mac_path():
#     """Return the local path on macOS."""
#     return Path(__file__).resolve().parent


# def get_linux_path():
#     """Return the local path on Linux / Raspberry Pi."""
#     return Path(__file__).resolve().parent


# def detect_os_name():
#     """Return the current operating system name."""
#     system = platform.system()
#     if system == "Windows":
#         return "Windows"
#     elif system == "Darwin":
#         return "macOS"
#     elif system == "Linux":
#         return "Linux"
#     return "Unknown OS"


def create_text_surfaces(font, os_name, local_path):
    """Render OS name and wrapped path lines for display."""
    text_os = font.render(f"Detected OS: {os_name}", True, (255, 255, 255))
    rect_os = text_os.get_rect(center=(450, 400))

    wrapped_path_lines = render_wrapped_text(
        f"Local Path: {local_path}",
        font,
        (255, 255, 255),
        max_width=800,
        start_y=500
    )

    return (text_os, rect_os), wrapped_path_lines


def init_pygame():
    """Initialize pygame and return the window surface."""
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Learniverse")
    return screen


def load_font():
    """Return a default font object."""
    return pygame.font.SysFont(None, 48)


def render_wrapped_text(text, font, color, max_width, start_y, line_spacing=10):
    """Wrap long text and return list of (surface, rect) for each line."""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        test_surface = font.render(test_line, True, color)
        if test_surface.get_width() > max_width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = test_line

    lines.append(current_line)  # Add last line

    rendered = []
    for i, line in enumerate(lines):
        surface = font.render(line, True, color)
        rect = surface.get_rect(center=(450, start_y + i * (font.get_height() + line_spacing)))
        rendered.append((surface, rect))

    return rendered


def load_random_image(local_path):
    """Load a random JPG from GFX/main_menu relative to local_path."""
    gfx_path = local_path / "GFX" / "main_menu"
    jpg_files = list(gfx_path.glob("*.jpg"))

    if not jpg_files:
        print("[WARN] No JPGs found in GFX/main_menu")
        return None  # No image to load

    selected_file = random.choice(jpg_files)
    try:
        image = pygame.image.load(str(selected_file))
        return pygame.transform.scale(image, (900, 900))
    except Exception as e:
        print(f"[ERROR] Failed to load image: {e}")
        return None
    

def run_main_loop(screen, text_os, rect_os, wrapped_path_lines, background_img):
    """Main loop displaying OS info, path, and background image."""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))

        # Draw background first
        if background_img:
            screen.blit(background_img, (0, 0))

        # Draw text overlays
        screen.blit(text_os, rect_os)
        for line_surface, line_rect in wrapped_path_lines:
            screen.blit(line_surface, line_rect)

        pygame.display.flip()

    pygame.quit()


def main():
    screen = init_pygame()
    font = load_font()
    os_name = detect_os_name()
    local_path = get_local_path(os_name)

    (text_os, rect_os), wrapped_path_lines = create_text_surfaces(
        font, os_name, local_path
    )

    background_img = load_random_image(local_path)

    run_main_loop(screen, text_os, rect_os, wrapped_path_lines, background_img)


if __name__ == '__main__':
    main()