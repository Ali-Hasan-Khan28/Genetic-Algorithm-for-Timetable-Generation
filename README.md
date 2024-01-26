# Genetic-Algorithm-for-Timetable-Generation
![127 0 0 1_5000_ (2)](https://github.com/Ali-Hasan-Khan28/Genetic-Algorithm-for-Timetable-Generation/assets/101451471/6369610b-328c-43c7-9511-e354ef248170)

This web application generates a timetable for lecture halls using a genetic algorithm. The timetable is created based on various constraints such as consecutive lectures for teachers and students, maximum credit hours, and other specific conditions.

## Prerequisites

- Python
- Flask
- NumPy
- Random

## Usage

1. Install the required dependencies:

   ```bash
   pip install flask numpy

   Run the main function in the provided Python script (timetable_generator.py) to generate the timetable and start the Flask web application.

Access the web application at http://localhost:5000/ to view the generated timetable.

## Timetable Generation Algorithm
The timetable is generated using a genetic algorithm with the following key components:

### Chromosome Representation: Each individual in the population is represented as a chromosome, consisting of genes corresponding to different courses.

### Fitness Calculation: The fitness of an individual is determined based on constraints such as consecutive lectures for teachers and students, maximum credit hours, and other specific conditions.

### Crossover and Mutation: Individuals are selected for mating based on their fitness scores. Crossover and mutation operations are applied to create a new generation of individuals.

### Elitism: The top 10% of the fittest individuals are preserved in each generation to maintain the best solutions.

## Web Application
The Flask web application displays the generated timetable for various lecture halls.
The timetable is organized by days and time slots.
Lecture halls are labeled as "Lecture Hall 01 FCSE," "Lecture Hall 02 FCSE," and so on.
Customize
Feel free to modify the code and parameters to suit your specific requirements or constraints. For further details on the genetic algorithm, refer to the comments in the provided Python script (timetable_generator.py).

Note: The application runs in debug mode (debug=True), which is suitable for development but not recommended for production use. Ensure that you have the required dependencies installed and configured.

Enjoy generating timetables efficiently with the genetic algorithm!


## Timetable Representation

The generated timetable is presented in a structured format, organized by days and time slots. Each lecture hall's timetable is displayed separately.

### Timetable Format

The timetable includes the following information:

- **DAYS:** The days of the week (Monday to Friday).
- **8-9 to 5-6:** Time slots for lectures.

### Lecture Halls

The timetable is provided for the following lecture halls:

1. Lecture Hall 01 FCSE
2. Lecture Hall 02 FCSE
3. Lecture Hall 03 FCSE
4. Room no. 4 ACB
5. Room No 05 FCSE
6. Room no. 5 ACB
7. Room no. 6 ACB

### Viewing the Timetable

Access the web application at [http://localhost:5000/](http://localhost:5000/) and navigate to the respective pages for each lecture hall to view the generated timetable.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the developers of Flask, NumPy, and other open-source libraries used in this project.

Feel free to contribute, report issues, or suggest improvements!

