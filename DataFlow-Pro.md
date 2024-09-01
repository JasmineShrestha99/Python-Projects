# Data Master - Automated Data Processing Tool

Author: Jasmine Shrestha

## Overview

Data Master is an advanced Python-based automation tool designed to streamline the process of data fetching, parsing, cleaning, visualization, and email reporting. This tool leverages web scraping, data manipulation, and automated reporting to deliver comprehensive data analysis directly to your inbox. It is equipped with a user-friendly GUI for ease of use, making it accessible for both technical and non-technical users.

## Features

- **Data Fetching**: Automatically fetches data from a specified URL using HTTP requests.
- **Data Parsing**: Extracts and organizes relevant information from HTML content using BeautifulSoup.
- **Data Cleaning**: Processes and cleans data with Pandas, including handling missing values and type conversions.
- **Data Visualization**: Generates visual representations of the data using Seaborn and Matplotlib, saving the results as PNG files.
- **Email Reporting**: Sends the data visualizations and reports via email with customizable subject and body content.
- **Logging**: Logs all significant actions and errors for auditing and troubleshooting.
- **Graphical User Interface (GUI)**: An intuitive Tkinter-based GUI to enter required parameters like URL, email addresses, and credentials.

## Requirements

- **Python 3.x**
- **Required Libraries**:
  - `requests`
  - `BeautifulSoup4`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `smtplib`
  - `tkinter`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/datamaster.git
   cd datamaster
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tool**:
   ```bash
   python datamaster.py
   ```

## Usage

### Running the Automation

1. Launch the GUI by running the script.
2. Enter the required fields:
   - **Data Source URL**: The URL from which data will be fetched.
   - **Sender Email Address**: Your email address.
   - **Receiver Email Address**: The recipient’s email address.
   - **Sender Email Password**: Your email account’s password.
3. Click "Start Automation" to begin the process.

### Logging

All activities, including successful operations and errors, are logged in `automation_log.txt`. Review this file to monitor the process or troubleshoot issues.

### Visualization and Reporting

After processing, the tool generates a visualization saved as `data_visualization.png`. This image is attached to an email report sent to the specified recipient.

## Notes

- Ensure your email provider allows SMTP access and that the credentials provided are correct.
- The GUI is designed with a responsive layout, adapting to different screen sizes and resolutions.

## Contribution

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
