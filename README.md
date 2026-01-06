# Deep Nested Dictionary Cleaning and Aggregation

This project demonstrates practical techniques for working with deeply nested dictionaries in Python.  
It focuses on data cleaning, structural validation, flattening (uncoupling), and aggregation.

## Project Overview

The script performs the following tasks:

1. Data Cleaning
   - Traverses deeply nested dictionaries
   - Removes students with:
     - Missing names
     - Invalid or out-of-range scores
     - Null values

2. Structural Cleanup
   - Deletes empty departments
   - Deletes empty faculties
   - Deletes empty universities

3. Uncoupling (Flattening)
   - Converts nested student records into flat rows
   - Each row contains:
     - University
     - Faculty
     - Department
     - Student ID
     - Student name
     - Scores

4. Aggregation
   - Computes average calculus score per department
   - Computes average algebra score per faculty

## Technologies Used
* Python 3
* Core data structures (dict, list, tuple)

## How to Run

1. Clone or download the repository
2. Run the script using:

```bash
python nested_dic_project.py
