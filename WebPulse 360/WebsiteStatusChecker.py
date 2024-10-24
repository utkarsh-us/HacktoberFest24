import customtkinter as ctk
import requests
import threading
import time
from datetime import datetime
from urllib.parse import urlparse
import json
import os

class WebsiteStatusChecker:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("800x600")
        self.window.title("Website Status Checker")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Website list and status storage
        self.websites = {}
        self.monitoring = False
        self.check_interval = 300  # 5 minutes default
        
        self.load_websites()
        self.create_gui()
        
    def create_gui(self):
        # Create main container
        self.main_container = ctk.CTkFrame(self.window)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(
            self.main_container,
            text="Website Status Checker",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=10)
        
        # Add website frame
        self.add_website_frame = ctk.CTkFrame(self.main_container)
        self.add_website_frame.pack(fill="x", padx=10, pady=10)
        
        # URL entry
        self.url_entry = ctk.CTkEntry(
            self.add_website_frame,
            placeholder_text="Enter website URL (e.g., https://example.com)",
            width=400
        )
        self.url_entry.pack(side="left", padx=5)
        
        # Add button
        add_button = ctk.CTkButton(
            self.add_website_frame,
            text="Add Website",
            command=self.add_website
        )
        add_button.pack(side="left", padx=5)
        
        # Interval selection
        interval_frame = ctk.CTkFrame(self.main_container)
        interval_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(
            interval_frame,
            text="Check Interval:"
        ).pack(side="left", padx=5)
        
        self.interval_var = ctk.StringVar(value="5 minutes")
        interval_options = ["1 minute", "5 minutes", "15 minutes", "30 minutes", "1 hour"]
        interval_dropdown = ctk.CTkOptionMenu(
            interval_frame,
            values=interval_options,
            variable=self.interval_var,
            command=self.update_interval
        )
        interval_dropdown.pack(side="left", padx=5)
        
        # Start/Stop button
        self.start_stop_button = ctk.CTkButton(
            interval_frame,
            text="Start Monitoring",
            command=self.toggle_monitoring
        )
        self.start_stop_button.pack(side="right", padx=5)
        
        # Create scrollable frame for websites
        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_container)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Headers
        headers_frame = ctk.CTkFrame(self.scrollable_frame)
        headers_frame.pack(fill="x", pady=5)
        
        headers = ["Website", "Status", "Response Time", "Last Checked", ""]
        weights = [3, 1, 1, 2, 1]
        
        for header, weight in zip(headers, weights):
            label = ctk.CTkLabel(
                headers_frame,
                text=header,
                font=("Helvetica", 12, "bold")
            )
            label.pack(side="left", expand=True, fill="x", padx=5, pady=5)
        
        # Status indicators
        self.status_frames = {}
        
    def validate_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
        
    def add_website(self):
        url = self.url_entry.get().strip()
        
        if not url:
            self.show_error("Please enter a URL")
            return
            
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        if not self.validate_url(url):
            self.show_error("Please enter a valid URL")
            return
            
        if url in self.websites:
            self.show_error("Website already exists in the list")
            return
            
        # Create frame for website
        frame = ctk.CTkFrame(self.scrollable_frame)
        frame.pack(fill="x", pady=2)
        
        # Website URL
        url_label = ctk.CTkLabel(frame, text=url)
        url_label.pack(side="left", expand=True, fill="x", padx=5)
        
        # Status
        status_label = ctk.CTkLabel(frame, text="Pending")
        status_label.pack(side="left", expand=True, fill="x", padx=5)
        
        # Response time
        response_label = ctk.CTkLabel(frame, text="--")
        response_label.pack(side="left", expand=True, fill="x", padx=5)
        
        # Last checked
        last_checked_label = ctk.CTkLabel(frame, text="Never")
        last_checked_label.pack(side="left", expand=True, fill="x", padx=5)
        
        # Remove button
        remove_button = ctk.CTkButton(
            frame,
            text="Remove",
            command=lambda u=url: self.remove_website(u),
            width=70
        )
        remove_button.pack(side="left", padx=5)
        
        # Store website info
        self.websites[url] = {
            'frame': frame,
            'status_label': status_label,
            'response_label': response_label,
            'last_checked_label': last_checked_label,
            'last_status': None,
            'last_response_time': None,
            'last_checked': None
        }
        
        self.url_entry.delete(0, 'end')
        self.save_websites()
        
    def remove_website(self, url):
        if url in self.websites:
            self.websites[url]['frame'].destroy()
            del self.websites[url]
            self.save_websites()
            
    def check_website(self, url):
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10)
            response_time = (time.time() - start_time) * 1000  # Convert to ms
            
            status = "✅ Online" if response.status_code == 200 else f"⚠️ Error ({response.status_code})"
            response_time_text = f"{response_time:.0f}ms"
            
        except requests.RequestException as e:
            status = "❌ Offline"
            response_time_text = "--"
            
        last_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Update UI in the main thread
        self.window.after(0, self.update_website_status, url, status, response_time_text, last_checked)
        
    def update_website_status(self, url, status, response_time, last_checked):
        if url in self.websites:
            self.websites[url]['status_label'].configure(text=status)
            self.websites[url]['response_label'].configure(text=response_time)
            self.websites[url]['last_checked_label'].configure(text=last_checked)
            
            # Store the latest status
            self.websites[url]['last_status'] = status
            self.websites[url]['last_response_time'] = response_time
            self.websites[url]['last_checked'] = last_checked
            
    def monitor_websites(self):
        while self.monitoring:
            threads = []
            for url in self.websites:
                thread = threading.Thread(target=self.check_website, args=(url,))
                thread.daemon = True
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()
                
            time.sleep(self.check_interval)
            
    def toggle_monitoring(self):
        if not self.monitoring:
            self.monitoring = True
            self.start_stop_button.configure(text="Stop Monitoring")
            
            # Start monitoring in a separate thread
            monitor_thread = threading.Thread(target=self.monitor_websites)
            monitor_thread.daemon = True
            monitor_thread.start()
        else:
            self.monitoring = False
            self.start_stop_button.configure(text="Start Monitoring")
            
    def update_interval(self, value):
        # Convert interval to seconds
        intervals = {
            "1 minute": 60,
            "5 minutes": 300,
            "15 minutes": 900,
            "30 minutes": 1800,
            "1 hour": 3600
        }
        self.check_interval = intervals.get(value, 300)
        
    def show_error(self, message):
        error_window = ctk.CTkToplevel(self.window)
        error_window.title("Error")
        error_window.geometry("300x100")
        
        error_label = ctk.CTkLabel(error_window, text=message)
        error_label.pack(pady=20)
        
        ok_button = ctk.CTkButton(
            error_window,
            text="OK",
            command=error_window.destroy
        )
        ok_button.pack(pady=10)
        
    def save_websites(self):
        websites_data = list(self.websites.keys())
        try:
            with open('websites.json', 'w') as f:
                json.dump(websites_data, f)
        except Exception as e:
            print(f"Error saving websites: {e}")
            
    def load_websites(self):
        try:
            if os.path.exists('websites.json'):
                with open('websites.json', 'r') as f:
                    websites_data = json.load(f)
                    for url in websites_data:
                        self.url_entry.insert(0, url)
                        self.add_website()
        except Exception as e:
            print(f"Error loading websites: {e}")
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = WebsiteStatusChecker()
    app.run()
