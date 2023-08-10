# Python-OOP-Flatmate-bills-Web-App
Created an OOP based web app to manage the bills according to the period stayed between 2 flatmates living in the same house.

### Description
Created an OOP based web app to manage the bills according to the period stayed between 2 flatmates living in the same house.

### Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

### Features
The Flatmate Bills Web App consists of the following objects and their respective attributes and methods:

- **Bill**: Represents a bill for a specific period.
  - Attributes: `amount`, `period`
- **Flatmate**: Represents a person living in the house.
  - Attributes: `name`, `days_in_house`
  - Methods: `pays(Bill)`
- **PdfReport**: Generates a PDF report for the bill.
  - Attributes: `filename`
  - Methods: `generate(flatmate1, flatmate2, bill)`

### Usage
To use the Flatmate Bills Web App, go to:

```
[tea.eu.pythonanywhere.com](http://tea.eu.pythonanywhere.com/)
```

### Deployment
The Flatmate Bills Web App is deployed at [tea.eu.pythonanywhere.com](http://tea.eu.pythonanywhere.com/) using Flask.

### Contributing
If you would like to contribute to the Flatmate Bills Web App, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with a meaningful commit message.
4. Create a pull request describing the changes you made.

### License
This project is licensed under the MIT License. For more information, please refer to the [LICENSE](LICENSE) file.
