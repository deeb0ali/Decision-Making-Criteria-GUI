# Decision-Making Criteria GUI

This repository contains a Graphical User Interface (GUI) for Decision-Making Criteria. The GUI is developed using the PyQt5 framework and provides users with the ability to input a decision matrix and apply various decision-making criteria to determine the best alternative.

## Introduction

This document provides an overview of the Decision-Making Criteria GUI. It explains the implemented decision-making criteria and describes the components of the GUI.

## Decision-Making Criteria

The implemented decision-making criteria are as follows:

- Maximum of Minimums (Maximin)
- Maximum of Maximums (Maximax)
- Maximum of Averages
- Maximum of *l* Values
- Laplace Criterion
- Savage Criterion

For a detailed explanation of each criterion, please refer to the document above.

## Graphical User Interface

The Decision-Making Criteria GUI consists of the following components:

- Decision matrix: Allows users to input a decision matrix with user-defined dimensions.
- Calculation buttons: Buttons for each decision-making criterion to calculate the best alternative.
- Result label: Displays the outcome of the selected criterion.
- Weight input: Text input for specifying the weight *a* in the Maximum of *l* Values criterion.

To use the GUI, follow these steps:

1. Input the decision matrix values.
2. Choose a decision-making criterion by clicking the corresponding button.
3. Observe the result displayed in the result label.

For more details on the GUI components, please refer to the document above.

## How to Run

To run the Decision-Making Criteria GUI, ensure you have the following dependencies installed:

- Python 3.x
- PyQt5

Then, follow these steps:

1. Clone the repository: `git clone https://github.com/deeb0ali/Decision-Making-Criteria-GUI`
2. Navigate to the repository directory: `cd <repository-directory>`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the GUI: `python gui.py`

## Conclusion

The Decision-Making Criteria GUI provides a user-friendly tool for making decisions under uncertainty. By implementing various decision-making criteria, users can find the best alternative based on their preferences and the specific problem at hand.

**Author**: deeb0ali
