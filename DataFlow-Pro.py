import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox, filedialog

# Initialize logging
logging.basicConfig(filename="automation_log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_data(url):
    """Fetch data from a website."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        logging.info("Successfully fetched data from %s", url)
        return response.text
    except requests.RequestException as e:
        logging.error("Failed to fetch data: %s", e)
        return None

def parse_data(html):
    """Parse the HTML content and extract relevant data."""
    try:
        soup = BeautifulSoup(html, 'html.parser')
        data = []

        # Example: Extracting table data
        table = soup.find('table', {'id': 'data-table'})
        headers = [header.text for header in table.find_all('th')]
        rows = table.find_all('tr')

        for row in rows[1:]:
            values = [col.text for col in row.find_all('td')]
            data.append(values)

        df = pd.DataFrame(data, columns=headers)
        logging.info("Successfully parsed data")
        return df
    except Exception as e:
        logging.error("Failed to parse data: %s", e)
        return pd.DataFrame()

def clean_data(df):
    """Clean and process the DataFrame."""
    try:
        # Example: Converting columns to numeric and filling missing values
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        df['Value'].fillna(df['Value'].mean(), inplace=True)
        logging.info("Data cleaning completed")
        return df
    except Exception as e:
        logging.error("Data cleaning failed: %s", e)
        return df

def visualize_data(df):
    """Generate data visualizations."""
    try:
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Category', y='Value', data=df, palette='viridis')
        plt.title("Category vs Value")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot
        plt.savefig("data_visualization.png")
        logging.info("Data visualization created")
    except Exception as e:
        logging.error("Failed to create data visualization: %s", e)

def send_email(subject, body, attachment, sender_email, receiver_email, password):
    """Send an email with the report and visualization attached."""
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Attach the visualization
        attachment_name = os.path.basename(attachment)
        with open(attachment, "rb") as attach_file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attach_file.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={attachment_name}")
        msg.attach(part)

        # Send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)

        logging.info("Email sent successfully to %s", receiver_email)
    except Exception as e:
        logging.error("Failed to send email: %s", e)

def run_automation(url, sender_email, receiver_email, password):
    """Run the automation process."""
    html_content = fetch_data(url)

    if html_content:
        df = parse_data(html_content)
        df = clean_data(df)

        if not df.empty:
            visualize_data(df)
            send_email(
                subject="Automated Data Analysis Report",
                body="Please find the attached data visualization report.",
                attachment="data_visualization.png",
                sender_email=sender_email,
                receiver_email=receiver_email,
                password=password
            )
            messagebox.showinfo("Success", "Automation completed successfully.")
        else:
            logging.warning("No data to process")
            messagebox.showwarning("Warning", "No data to process.")
    else:
        logging.warning("Failed to retrieve or process data")
        messagebox.showerror("Error", "Failed to retrieve or process data.")

def create_gui():
    """Create the GUI for user input."""
    def on_run():
        url = url_entry.get()
        sender_email = sender_email_entry.get()
        receiver_email = receiver_email_entry.get()
        password = password_entry.get()

        if not all([url, sender_email, receiver_email, password]):
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        run_automation(url, sender_email, receiver_email, password)

    # Create the main window
    root = tk.Tk()
    root.title("Data Master - Automation Tool")
    root.geometry("1080x1200")  # Set initial window size to 1080x1200
    root.configure(bg="#1e3d59")  # Background color

    # Style Configuration
    label_font = ("Verdana", 14, "bold")
    entry_font = ("Verdana", 14)
    button_font = ("Verdana", 14, "bold")

    # Title
    title_label = tk.Label(root, text="Data Master - Automated Data Processing", font=("Verdana", 24, "bold"), bg="#1e3d59", fg="white")
    title_label.grid(row=0, columnspan=2, pady=20)

    # URL input
    tk.Label(root, text="Data Source URL:", font=label_font, bg="#1e3d59", fg="white").grid(row=1, column=0, sticky="e", padx=10, pady=10)
    url_entry = tk.Entry(root, font=entry_font, width=60)
    url_entry.grid(row=1, column=1, padx=10, pady=10)

    # Sender email input
    tk.Label(root, text="Sender Email Address:", font=label_font, bg="#1e3d59", fg="white").grid(row=2, column=0, sticky="e", padx=10, pady=10)
    sender_email_entry = tk.Entry(root, font=entry_font, width=60)
    sender_email_entry.grid(row=2, column=1, padx=10, pady=10)

    # Receiver email input
    tk.Label(root, text="Receiver Email Address:", font=label_font, bg="#1e3d59", fg="white").grid(row=3, column=0, sticky="e", padx=10, pady=10)
    receiver_email_entry = tk.Entry(root, font=entry_font, width=60)
    receiver_email_entry.grid(row=3, column=1, padx=10, pady=10)

    # Email password input
    tk.Label(root, text="Sender Email Password:", font=label_font, bg="#1e3d59", fg="white").grid(row=4, column=0, sticky="e", padx=10, pady=10)
    password_entry = tk.Entry(root, show="*", font=entry_font, width=60)
    password_entry.grid(row=4, column=1, padx=10, pady=10)

    # Run button
    run_button = tk.Button(root, text="Start Automation", font=button_font, bg="#e74c3c", fg="white", command=on_run)
    run_button.grid(row=5, columnspan=2, pady=20)

    # Make window responsive
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
