# Football Match Visualizer

This project is a desktop application in Python that allows users to view the matches of football teams drawn into groups. It uses `tkinter` for the graphical interface and enables users to see the matches for a specific team using a series of buttons. It also includes the option to retry the draw if it fails.

## Features

- **Graphical Interface**: Uses `tkinter` to create an intuitive interface with buttons for each team and a text area to display matches.
- **Match Draw**: Conducts a draw for matches between teams from different pots, ensuring that teams do not play against teams from the same country more than twice and that no rivals are repeated.
- **Retry Draw**: Allows automatic retry of the draw until successful and manual retry from the menu.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your_username/football-match-visualizer.git
    ```

2. **Install Dependencies**:

    Make sure you have Python installed (Python 3.6 or higher). Then, install the required dependencies using `pip`:

    ```bash
    pip install tkinter
    ```

    Note: `tkinter` is usually bundled with Python. If you encounter issues, check your operating system's documentation for installing `tkinter`.

## Usage

1. **Run the Application**:

    Navigate to the project directory and run the main script:

    ```bash
    python football_match_visualizer.py
    ```

2. **Interact with the Interface**:

    - **Team Buttons**: Click on the team buttons to view the assigned matches for each team.
    - **Retry Draw**: Use the "Options" menu to manually retry the draw if the initial draw fails.

## Code Structure

- **`football_match_visualizer.py`**: The main file containing the code for match generation, draw logic, and graphical interface.

## Contributing

If you wish to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a branch for your feature or fix (`git checkout -b my-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin my-feature`).
5. Open a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For more information, please contact [your_email@example.com](mailto:your_email@example.com).
