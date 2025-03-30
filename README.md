# Sorting Visualizer

Sorting Visualizer is an interactive program that demonstrates the process of various sorting algorithms on user-defined arrays of numbers. This tool helps users understand how different sorting algorithms operate through visual representation.

## Features

- **Multiple Sorting Algorithms**: Visualize the execution of various sorting algorithms.
- **Multiple Array Sizes**: See in-depth working of the algorithms on small arrays or understand their working patterns through faster sorting on big arrays.
- **Real-Time Visualization**: Watch the sorting process step-by-step in real-time.
- **Interactive Controls**: Start, pause, and reset the visualization at any time.

## Getting Started

Follow these instructions to set up and run the Sorting Visualizer on your local machine.

### Prerequisites

Ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Suyash-Abhishek-Kumar/sorting-visualizer.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd sorting-visualizer
   ```

3. **Install Required Dependencies**:

   Install the dependencies from `requirements.txt` file. Run:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Execute the main script to start the visualizer:

```bash
python main.py
```

Follow the on-screen instructions to select your array size and select the sorting algorithm to visualize.

## Project Structure

- `main.py`: The main script to run the application.
- `sorting_algorithms.py`: Contains implementations of various sorting algorithms.
- `display.py`: Manages the graphical display of the sorting process.
- `buttons.py`: Handles the interactive buttons in the GUI.
- `slider.py`: Manages slider controls for adjusting parameters like speed.
- `colors.py`: Defines color schemes used in the visualization.
- `graphics/`: Directory containing graphical assets and related modules.
- `basic_types/`: Contains basic font styles used in the project.

## Contributing

We welcome contributions to enhance the Sorting Visualizer. To contribute:

1. **Fork the Repository**: Click on the 'Fork' button at the top right of the repository page.
2. **Create a New Branch**: Name your branch descriptively, e.g., `feature/add-new-sort`.
3. **Make Your Changes**: Implement your feature or fix.
4. **Test Thoroughly**: Ensure that your changes do not break existing functionality.
5. **Submit a Pull Request**: Provide a clear description of your changes and any relevant issues.


*This README was created to provide a clear and concise overview of the Sorting Visualizer project. For more detailed information, please refer to the source code and comments within the project files.*
