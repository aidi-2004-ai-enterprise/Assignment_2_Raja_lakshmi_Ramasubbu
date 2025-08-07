# Assignment_2_Raja_lakshmi_Ramasubbu

#  Penguin Species Prediction API

This project is a machine learning-powered FastAPI application deployed to Google Cloud Run. It predicts the species of a penguin based on its physical characteristics.

##  Project Overview

I built this application as part of my assignment to demonstrate:
- Building and containerizing a FastAPI app.
- Deploying it on Google Cloud Run.
- Writing automated tests.
- Performing load testing using Locust.
- Following best practices for CI/CD and documentation.

##  Features

- API endpoint: `/predict`
- Model: Trained on the Palmer Penguins dataset
- Input: JSON with features like `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`, and `island`.
- Output: Predicted penguin species (`Adelie`, `Gentoo`, or `Chinstrap`)

##  Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/penguin-predictor.git
cd penguin-predictor
