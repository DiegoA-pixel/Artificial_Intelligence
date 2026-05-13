AI-Powered Daily Routine Generator
Overview

This project is a web application that generates personalized daily routines based on user input such as age and goal.

The app is designed with a hybrid approach:

AI-based generation using external models when available
Rule-based fallback system for reliability

Live Demo
https://rutina-ia.streamlit.app

Features
Personalized routine generation
AI-powered generation via Hugging Face API
Robust fallback system (rule-based engine)
Visual analytics with charts
Interactive UI

Tech Stack
Python
Streamlit
Matplotlib
Requests
Hugging Face Inference API

Architecture

The system follows a hybrid logic:

Try AI-generated routine via API
If API fails → fallback to rule-based generator
Display structured routine + visualization

Output Example
Exercise plan
Study/productivity routines
Sleep and hydration recommendations
Daily distribution chart

Purpose

To demonstrate how AI can be integrated into real applications with robust fallback mechanisms to ensure reliability.

Note

This project focuses on applied AI concepts and practical software development rather than complex model training.
