# Tyler J. Skluzacek, Ph.D. - Personal Website

This repository contains the code for my personal website.

## How to View Locally

There are several ways to view this website locally without pushing to GitHub:

### Method 1: Using Python's Built-in HTTP Server

1. Open a terminal
2. Navigate to the website directory: `cd /path/to/tskluzac.github.io`
3. Run: `python3 -m http.server 8000`
4. Open a browser and go to: `http://localhost:8000`

### Method 2: Using Node.js and http-server

1. Install http-server if you don't have it: `npm install -g http-server`
2. Navigate to the website directory: `cd /path/to/tskluzac.github.io`
3. Run: `http-server -p 8000`
4. Open a browser and go to: `http://localhost:8000`

### Method 3: Using VS Code Live Server Extension

1. Install the "Live Server" extension in VS Code
2. Right-click on `index.html` in VS Code
3. Select "Open with Live Server"
4. The website will automatically open in your default browser

### Method 4: Simply Open the HTML File

For basic viewing without server features:
1. Navigate to the website directory in your file explorer
2. Double-click on `index.html` to open it directly in your browser
   - Note: Some features might not work correctly with this method

## Features

The website includes:

- Responsive design that works on mobile, tablet, and desktop
- Dark/light mode toggle with system preference detection
- Smooth animations using AOS (Animate On Scroll) library
- Modern card-based layout for news items
- Timeline display for older news
- Font Awesome icons for social media links
- Google Fonts integration for typography
- Bootstrap 5 for layout and components

## File Structure

- `index.html` - Main HTML file
- `static/css/styles.css` - Custom CSS styles
- `static/js/script.js` - JavaScript functionality
- `static/images/` - Image assets
- `static/cv/` - CV PDF file
