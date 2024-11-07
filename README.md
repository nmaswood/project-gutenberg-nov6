# Project Gutenberg

This project enables users to retrieve and analyze text from books in the Project Gutenberg collection. By entering a Project Gutenberg book ID, users can access book metadata, texts, and perform plot summary analysis.

## Features

### Core Functionality
- **Input Book ID**: Users can enter a Project Gutenberg book ID to retrieve information about the book.
- **Fetch & Display**: Retrieves and displays the book's text and metadata based on the entered book ID.
- **Book History**: Displays a list of all previously accessed books for easy reference.

### Text Analysis
The application offers several text analysis options to help users understand and explore the content. Current we support:
- **Plot Summary**: Summarizes the main plot of the book, providing a brief overview.

## Getting Started

### Prerequisites
- Python (version 3.7+)
- Flask
- Frontend dependencies (Next.js)
- Gorq AI Cloud for text analysis

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/project-gutenberg-text-analysis.git
    cd project-gutenberg-text-analysis
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the frontend environment as per Next.js documentation

4. Set up the server to handle book fetching, saving, and analysis.

### Usage

1. **Start the Backend**:
    ```bash
    flask run
    ```

2. **Access the Application**: 
   Open the frontend in a browser to access the input field for entering a Project Gutenberg book ID.

3. **Analyze Text**:
    - Enter a Project Gutenberg book ID and fetch the book’s content.
    - Use the toggle provided on the top right corner to get plot summary

## Technologies Used
- **Flask** for backend API handling
- **React/Next.js** for frontend interface
- **Groq AI** for text analysis

## Live Demo
- Access the website at http://3.110.221.124:3000/
