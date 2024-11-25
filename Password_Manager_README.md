
# Password Manager

A simple password manager built with Python and Tkinter that allows you to generate, save, and retrieve passwords for various websites. The passwords are stored securely in a JSON file and can be accessed or modified with ease.

## Features
- **Password Generation**: Automatically generate secure passwords with a combination of letters, numbers, and symbols.
- **Password Storage**: Save website credentials (username/email and password) in a JSON file.
- **Search Functionality**: Retrieve stored passwords based on the website name.
- **GUI Interface**: Built with Tkinter for a simple and user-friendly interface.

## Requirements
- Python 3.x
- Tkinter (usually pre-installed with Python)
- `pyperclip` library (for copying the generated password to the clipboard)

### Installation

To install the required libraries, you can use `pip`:

```bash
pip install pyperclip
```

## Setup

1. Clone or download the repository.
2. Ensure you have the `final.png` image and `lock.ico` icon files in the same directory for the logo and icon to display properly.
3. The password manager stores passwords in a `data.json` file. You can create this file automatically when you add credentials for the first time.

## Usage

1. **Generate Password**: Click the "Generate Password" button to automatically generate a secure password that is copied to your clipboard.
2. **Add Credentials**: Enter the website name, your email/username, and password in the respective fields. Click the "Add" button to save them. The credentials are saved in `data.json` and `data.txt`.
3. **Search for Credentials**: Enter the website name and click "Search" to find the saved email/username and password for that website.

### Password File Format

The credentials are saved in a JSON file with the following structure:

```json
{
  "website1.com": {
    "email": "user@example.com",
    "password": "generatedpassword"
  },
  "website2.com": {
    "email": "anotheruser@example.com",
    "password": "anotherpassword"
  }
}
```

## Notes

- Make sure to keep your `data.json` file safe, as it contains your stored passwords.
- The `data.txt` file is an additional output file that stores the current data in JSON format.
- The password manager does not require user authentication or encryption, so it's recommended to use it in a secure environment.

## Troubleshooting

- **No data found for a website**: If you cannot find the credentials for a particular website, make sure they were previously added correctly and that you’re entering the correct website name.
- **Icon or Image Missing**: Ensure that you have the `final.png` image and `lock.ico` icon in the same directory as the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
