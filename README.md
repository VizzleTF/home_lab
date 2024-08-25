# [Web App Home Lab](https://github.com/VizzleTF/home_lab)

This is a web application for managing Proxmox virtual machines. It provides a simple interface to view and control VMs hosted on a Proxmox server.

## Features

- Display a list of all VMs on the Proxmox server
- Start and reset VMs through a web interface
- Auto-refresh VM status every 3 seconds
- Quick links to other services in the home lab

## Setup

1. Clone this repository to your local machine or server.

2. Install the required Python packages:
   ```
   pip install flask proxmoxer
   ```

3. Create a file named `proxmox_password.txt` in the root directory of the project and add your Proxmox password to it.

4. Modify the Proxmox connection details in `proxmox.py`:
   ```python
   proxmox = ProxmoxAPI("10.11.12.13", user="root@pam", password=password, verify_ssl=False)
   ```
   Replace "10.11.12.13" with your Proxmox server's IP address and "root@pam" with your Proxmox username.

5. Run the application:
   ```
   python main.py
   ```

   The application will start and be accessible at `http://localhost:80`.

## File Structure

- `main.py`: The main Flask application
- `proxmox.py`: Contains functions for interacting with the Proxmox API
- `wsgi.py`: WSGI entry point for the application
- `templates/`: Contains HTML templates
  - `home.html`: The main page template
  - `containers.html`: Template for displaying VM information
- `static/`: Contains static files
  - `css/style.css`: Stylesheet for the application
  - `background.jpg`: Background image for the web interface
  - `favicon.ico` and `favicon.png`: Favicon files

## Security Note

This application uses `verify_ssl=False` when connecting to the Proxmox API. This is not recommended for production environments. In a production setting, ensure you have a valid SSL certificate for your Proxmox server and set `verify_ssl=True`.

## Customization

You can customize the quick links in `home.html` to point to your specific services. Modify the CSS in `static/css/style.css` to change the appearance of the application.
