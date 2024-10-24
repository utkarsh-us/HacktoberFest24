# GitHub Profile Finder

GitHub Profile Finder is a sleek and interactive desktop application that allows users to search for GitHub profiles using their usernames. It fetches data directly from the GitHub API, displaying relevant user details such as profile image, bio, number of repositories, followers, and more.

This project is built using **Python** and **Tkinter**, along with the **CustomTkinter** library for a modern UI. It also uses **Pillow** to handle image processing and **requests** to communicate with the GitHub API.

---

## Features
- **Dark Mode UI**: The application uses a modern dark-themed interface provided by CustomTkinter.
- **Profile Information**: Retrieves and displays GitHub profile details, including:
  - Profile picture
  - Name
  - Bio
  - Location
  - Number of public repositories
  - Number of followers and following
  - Join date
- **Clickable GitHub Link**: Users can click a button to visit the profile directly on GitHub.
- **Error Handling**: Proper error messages for empty input, user not found, and request failures.

---

## Technologies Used
- **Python**: The programming language used for logic and API integration.
- **Tkinter**: Standard Python library for creating GUI applications.
- **CustomTkinter**: Provides a modern, dark-themed UI that enhances the overall user experience.
- **Pillow**: Library for image processing to handle the profile picture.
- **Requests**: A Python library used to make HTTP requests to the GitHub API.
- **GitHub API**: The application fetches GitHub user details using GitHub’s REST API.

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/github-profile-finder.git
    cd github-profile-finder
    ```

2. **Install required dependencies**:
    You can install the dependencies by running the following command:
    ```bash
    pip install -r requirements.txt
    ```

    The dependencies include:
    - `customtkinter`
    - `Pillow`
    - `requests`

3. **Run the application**:
    ```bash
    python github_profile_finder.py
    ```

---

## How to Use

1. **Enter a GitHub Username**: In the search bar, type the GitHub username of the profile you wish to view.
2. **Click Search**: Press the "Search" button to fetch the profile information.
3. **View Profile Details**: If the user is found, their profile picture, name, bio, and other relevant details will be displayed.
4. **Open GitHub Profile**: Click on the **"Visit GitHub Profile"** button to open the user's profile in your web browser.

---

## Screenshots

### Main Interface
![GitHub Profile Finder Main Interface](./screenshots/main_interface.png)

### Search Result
![Profile Information](./screenshots/profile_info.png)

### User Not Found
![Error Message](./screenshots/user_not_found.png)

---

## Error Handling

- **Invalid Username**: If the username does not exist on GitHub, the application will notify the user with a message: "User 'username' not found".
- **Empty Input**: If the search field is empty, the application will show a warning requesting the user to enter a username.
- **Network or API Errors**: In case of any network issues or GitHub API errors, an appropriate error message will be displayed.

---

## Future Improvements

- **Enhance Search Features**: Add more advanced search capabilities, such as filtering by followers or repositories.
- **Additional Data**: Fetch and display more details such as pinned repositories, organization memberships, etc.
- **Light Mode**: Add an option for users to switch between dark and light modes.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request. Make sure your code adheres to the project’s coding style and guidelines.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

---

## Credits

Created with ❤️ by [hari7261](https://github.com/hari7261).
