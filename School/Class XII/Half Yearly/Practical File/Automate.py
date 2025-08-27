import re
import os
import subprocess
import pyautogui
import time
import pygetwindow as gw
from PIL import Image, ImageGrab
import win32gui
import win32ui
from ctypes import windll

def extract_questions_and_code(tex_file):
    """Extracts question numbers and Python code from a LaTeX file."""
    with open(tex_file, 'r') as file:
        tex_content = file.read()

    # Regex to match \subsection*{Q + number) and \begin{lstlisting} code \end{lstlisting}
    pattern = re.compile(r"\\subsection\*\{Q(\d+)\).*?\}\s*\\begin\{lstlisting\}.*?\n(.*?)\\end\{lstlisting\}", re.S)
    matches = pattern.findall(tex_content)
    return matches

def save_code_to_file(code, question_number):
    """Saves extracted Python code to a temporary Python file."""
    file_name = f"temp_{question_number}.py"
    with open(file_name, 'w') as file:
        file.write(code)
    return file_name

def find_cmd_window(unique_title):
    """Find the CMD window with the given title."""
    print(f"Looking for window with title containing: {unique_title}")
    for window in gw.getAllWindows():
        print(f"Found window: {window.title}")
        # More lenient title matching
        if unique_title.lower() in window.title.lower():
            return window
    return None

def capture_window(hwnd):
    """Capture a window's content using Win32 API."""
    # Get the window size
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    # Get the window DC
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    # Create bitmap object
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)

    # Copy window content
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    # Convert to PIL Image
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    image = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    # Clean up
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    return image

def run_code_and_capture_output(script_file, question_number, images_dir):
    """Runs the Python script in a new command prompt and captures the output as a screenshot."""
    while True:  # Add retry loop
        unique_title = f"Q{question_number}"
        terminal_command = f'start "Q{question_number}" cmd /k "title Q{question_number} && python {script_file}"'
        subprocess.Popen(terminal_command, shell=True)
        time.sleep(3)

        terminal_window = None
        max_attempts = 10

        for attempt in range(max_attempts):
            print(f"Attempt {attempt + 1} to find window...")
            terminal_window = find_cmd_window(unique_title)
            if terminal_window:
                break
            time.sleep(1)

        if not terminal_window:
            raise Exception(f"Could not find CMD window for question {question_number}")

        try:
            # Resize window without activating it
            terminal_window.resizeTo(800, 400)
            terminal_window.moveTo(0, 0)
            time.sleep(1)

            print(f"Waiting for user to complete inputs for question {question_number}.")
            print("Press Enter to continue, or 'A' + Enter to try again.")
            user_input = input().strip().upper()
            
            if user_input == 'A':
                terminal_window.close()
                time.sleep(1)
                continue  # Retry the current question
            
            # Capture window content using Win32 API
            screenshot_path = os.path.join(images_dir, f"{question_number}.png")
            hwnd = terminal_window._hWnd
            screenshot = capture_window(hwnd)
            screenshot.save(screenshot_path)

            terminal_window.close()
            return screenshot_path

        except Exception as e:
            print(f"Error while handling window: {e}")
            if terminal_window:
                try:
                    terminal_window.close()
                except:
                    pass
            raise

def update_tex_with_image(tex_file, question_number, image_path):
    """Inserts the image path into the LaTeX document under the respective question."""
    with open(tex_file, 'r') as file:
        tex_content = file.read()

    # Regex to find the correct subsection and its lstlisting block
    subsection_pattern = rf"(\\subsection\*\{{Q{question_number}\).*?\}}.*?\\end\{{lstlisting\}})"
    match = re.search(subsection_pattern, tex_content, re.S)

    if match:
        # Add the \includegraphics command after the \end{lstlisting}
        relative_path = os.path.relpath(image_path, start=os.path.dirname(tex_file))
        updated_section = match.group(1) + f"\n\\includegraphics[width=\\linewidth]{{{relative_path.replace(os.sep, '/')}}}"
        tex_content = tex_content.replace(match.group(1), updated_section)

    with open(tex_file, 'w') as file:
        file.write(tex_content)

def clean_up_temp_files(files):
    """Deletes temporary files created during execution."""
    for file in files:
        if os.path.exists(file):
            os.remove(file)

def main():
    tex_file = r"/home/pranavverma/Github/Languages/Python3/School/Class XII/Half Yearly/Practical File/Practical File.tex"
    images_dir = os.path.join(os.path.dirname(tex_file), "images")

    # Create images directory if it doesn't exist
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Extract questions and code
    questions_and_code = extract_questions_and_code(tex_file)
    
    # Ask for starting question number
    while True:
        try:
            start_question = int(input("Enter the question number to start from: "))
            if any(int(qnum) == start_question for qnum, _ in questions_and_code):
                break
            print("Question number not found in the file. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    temp_files = []

    # Filter questions to start from the selected number
    filtered_questions = [(qnum, code) for qnum, code in questions_and_code 
                         if int(qnum) >= start_question]

    for question_number, code in filtered_questions:
        print(f"Processing question {question_number}...")
        
        # Save the Python code to a file
        script_file = save_code_to_file(code, question_number)
        temp_files.append(script_file)

        try:
            # Run the code and capture its output
            image_path = run_code_and_capture_output(script_file, question_number, images_dir)

            # Update the LaTeX file with the relative image path
            update_tex_with_image(tex_file, question_number, image_path)

        except Exception as e:
            print(f"Error processing question {question_number}: {e}")

    # Clean up temporary Python files
    clean_up_temp_files(temp_files)

if __name__ == "__main__":
    main()
