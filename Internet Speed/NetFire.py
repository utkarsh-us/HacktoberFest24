import customtkinter as ctk
import speedtest
import threading
from datetime import datetime
import time
import socket

class SpeedTestApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("600x400")
        self.window.title("Internet Speed Test")
        
        # Set the theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self.window)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Internet Speed Test",
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(pady=20)
        
        # Speed indicators
        self.speed_frame = ctk.CTkFrame(self.main_frame)
        self.speed_frame.pack(pady=20, fill="x", padx=20)
        
        # Download speed
        self.download_label = ctk.CTkLabel(
            self.speed_frame,
            text="Download Speed",
            font=("Helvetica", 16)
        )
        self.download_label.pack(pady=5)
        
        self.download_speed = ctk.CTkLabel(
            self.speed_frame,
            text="-- Mbps",
            font=("Helvetica", 20, "bold")
        )
        self.download_speed.pack()
        
        # Upload speed
        self.upload_label = ctk.CTkLabel(
            self.speed_frame,
            text="Upload Speed",
            font=("Helvetica", 16)
        )
        self.upload_label.pack(pady=5)
        
        self.upload_speed = ctk.CTkLabel(
            self.speed_frame,
            text="-- Mbps",
            font=("Helvetica", 20, "bold")
        )
        self.upload_speed.pack()
        
        # Ping
        self.ping_label = ctk.CTkLabel(
            self.speed_frame,
            text="Ping",
            font=("Helvetica", 16)
        )
        self.ping_label.pack(pady=5)
        
        self.ping_speed = ctk.CTkLabel(
            self.speed_frame,
            text="-- ms",
            font=("Helvetica", 20, "bold")
        )
        self.ping_speed.pack()
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.main_frame)
        self.progress_bar.pack(pady=20, padx=20, fill="x")
        self.progress_bar.set(0)
        
        # Status label
        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="Click Start to begin speed test",
            font=("Helvetica", 12)
        )
        self.status_label.pack(pady=5)
        
        # Start button
        self.start_button = ctk.CTkButton(
            self.main_frame,
            text="Start Test",
            command=self.start_speed_test
        )
        self.start_button.pack(pady=20)
        
        # Last test time
        self.last_test_label = ctk.CTkLabel(
            self.main_frame,
            text="Last tested: Never",
            font=("Helvetica", 10)
        )
        self.last_test_label.pack(pady=5)
        
        self.is_testing = False

    def check_internet_connection(self):
        try:
            # Try to connect to a reliable host
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False
    
    def update_progress(self, value, status):
        self.progress_bar.set(value)
        self.status_label.configure(text=status)
        self.window.update_idletasks()  # Force UI update
    
    def run_speed_test(self):
        try:
            if not self.check_internet_connection():
                raise ConnectionError("No internet connection detected")

            self.is_testing = True
            self.start_button.configure(state="disabled")
            
            # Initialize speedtest with config
            self.update_progress(0.1, "Initializing speed test...")
            st = speedtest.Speedtest()
            st.get_best_server()  # Get best server first
            
            # Configure test
            st.download(threads=None)  # Let the library decide the optimal thread count
            st.upload(threads=None)    # Same for upload
            
            # Test download speed with progress updates
            self.update_progress(0.4, "Testing download speed...")
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            self.download_speed.configure(text=f"{download_speed:.2f} Mbps")
            
            # Test upload speed with progress updates
            self.update_progress(0.7, "Testing upload speed...")
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            self.upload_speed.configure(text=f"{upload_speed:.2f} Mbps")
            
            # Get ping
            self.update_progress(0.9, "Getting ping...")
            ping = st.results.ping
            self.ping_speed.configure(text=f"{ping:.2f} ms")
            
            # Update last test time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.last_test_label.configure(text=f"Last tested: {current_time}")
            
            self.update_progress(1.0, "Speed test completed!")
            
        except ConnectionError as e:
            self.status_label.configure(text="Error: No internet connection. Please check your connection and try again.")
        except speedtest.ConfigRetrievalError:
            self.status_label.configure(text="Error: Could not retrieve speedtest configuration. Please try again later.")
        except speedtest.NoMatchedServers:
            self.status_label.configure(text="Error: No matching speedtest servers found. Please try again later.")
        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}")
        finally:
            self.is_testing = False
            self.start_button.configure(state="normal")
            
    def start_speed_test(self):
        if not self.is_testing:
            # Reset displays
            self.download_speed.configure(text="-- Mbps")
            self.upload_speed.configure(text="-- Mbps")
            self.ping_speed.configure(text="-- ms")
            self.progress_bar.set(0)
            
            # Start test in separate thread
            thread = threading.Thread(target=self.run_speed_test)
            thread.daemon = True
            thread.start()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = SpeedTestApp()
    app.run()
