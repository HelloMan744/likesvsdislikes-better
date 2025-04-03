import os
import webview

def main():
    print("Starting the Likes vs Dislikes Better app...")
    # Get the absolute path to index.html
    html_path = os.path.abspath("index.html")
    print("HTML file path:", html_path)
    
    if not os.path.exists(html_path):
        print("Error: index.html was not found!")
        return

    # Convert the path to a file URL
    file_url = "file:///" + html_path.replace("\\", "/")
    print("Loading HTML from:", file_url)
    
    try:
        # Create the window with a minimum size of 10x10
        window = webview.create_window("Likes vs Dislikes Better", file_url, width=1079, height=663, min_size=(10,10))
        print("Window created. Launching app...")
        webview.start()
    except Exception as e:
        print("Error launching webview:", e)

if __name__ == "__main__":
    main()
