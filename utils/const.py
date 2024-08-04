import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

AI71_API_KEY = st.secrets["AI71_API_KEY"]
NEO4J_PASSWORD = st.secrets["NEO4J_PASSWORD"]
NEO4J_USERNAME = st.secrets["NEO4J_USERNAME"]
NEO4J_URI = st.secrets["NEO4J_URI"]
AURA_INSTANCEID = st.secrets["AURA_INSTANCEID"]
AURA_INSTANCENAME = st.secrets["AURA_INSTANCENAME"]
BRAVE_API_KEY=st.secrets["BRAVE_API_KEY"]
# AI71_API_KEY = os.getenv("AI71_API_KEY")
# NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
# NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
# NEO4J_URI = os.getenv("NEO4J_URI")
# AURA_INSTANCEID = os.getenv("AURA_INSTANCEID")
# AURA_INSTANCENAME = os.getenv("AURA_INSTANCENAME")
# BRAVE_API_KEY=os.getenv("BRAVE_API_KEY")
DOCTOR = [
    {"name": "Dr. John Smith", "specialization": "Cardiology", "award": "Best Cardiologist 2021", "school": "Harvard Medical School", "specialization_explanation": "Deals with disorders of the heart and blood vessels."},
    {"name": "Dr. Emily Davis", "specialization": "Neurology", "award": "Excellence in Neurology Award 2020", "school": "Johns Hopkins University", "specialization_explanation": "Treats disorders of the nervous system."},
    {"name": "Dr. Michael Brown", "specialization": "Orthopedics", "award": "Orthopedic Surgeon of the Year 2019", "school": "Stanford University", "specialization_explanation": "Focuses on the musculoskeletal system."},
    {"name": "Dr. Sarah Wilson", "specialization": "Pediatrics", "award": "Top Pediatrician 2021", "school": "University of California, San Francisco", "specialization_explanation": "Provides medical care for infants, children, and adolescents."},
    {"name": "Dr. David Martinez", "specialization": "Dermatology", "award": "Dermatology Innovator Award 2020", "school": "Yale School of Medicine", "specialization_explanation": "Treats skin, hair, and nail disorders."},
    {"name": "Dr. Laura Garcia", "specialization": "Oncology", "award": "Outstanding Oncologist 2019", "school": "University of Chicago", "specialization_explanation": "Specializes in the treatment of cancer."},
    {"name": "Dr. James Anderson", "specialization": "Gastroenterology", "award": "Gastroenterologist of the Year 2020", "school": "Duke University", "specialization_explanation": "Focuses on the digestive system and its disorders."},
    {"name": "Dr. Maria Hernandez", "specialization": "Endocrinology", "award": "Endocrinology Research Award 2021", "school": "University of Pennsylvania", "specialization_explanation": "Deals with hormones and gland-related disorders."},
    {"name": "Dr. Robert Lee", "specialization": "Nephrology", "award": "Top Nephrologist 2020", "school": "Columbia University", "specialization_explanation": "Focuses on kidney health and diseases."},
    {"name": "Dr. Jennifer Walker", "specialization": "Rheumatology", "award": "Rheumatologist of the Year 2019", "school": "Mayo Clinic College of Medicine", "specialization_explanation": "Treats autoimmune diseases and musculoskeletal disorders."},
    {"name": "Dr. Thomas Perez", "specialization": "Pulmonology", "award": "Pulmonology Excellence Award 2021", "school": "University of Michigan", "specialization_explanation": "Focuses on respiratory system disorders."},
    {"name": "Dr. Jessica Robinson", "specialization": "Ophthalmology", "award": "Top Ophthalmologist 2020", "school": "University of Washington", "specialization_explanation": "Deals with eye and vision care."},
    {"name": "Dr. Daniel Martinez", "specialization": "Psychiatry", "award": "Best Psychiatrist 2019", "school": "Cornell University", "specialization_explanation": "Treats mental health disorders."},
    {"name": "Dr. Sophia Evans", "specialization": "Hematology", "award": "Hematology Research Award 2020", "school": "University of Texas Southwestern Medical Center", "specialization_explanation": "Focuses on blood diseases and disorders."},
    {"name": "Dr. Anthony White", "specialization": "Radiology", "award": "Radiologist of the Year 2021", "school": "Vanderbilt University", "specialization_explanation": "Uses imaging techniques to diagnose and treat diseases."},
    {"name": "Dr. Linda Thompson", "specialization": "Urology", "award": "Top Urologist 2020", "school": "University of Pittsburgh", "specialization_explanation": "Deals with the urinary tract and male reproductive organs."},
    {"name": "Dr. Christopher Lewis", "specialization": "Plastic Surgery", "award": "Plastic Surgeon Innovator Award 2019", "school": "Emory University", "specialization_explanation": "Focuses on reconstructive and cosmetic surgery."},
    {"name": "Dr. Amanda Clark", "specialization": "Infectious Disease", "award": "Infectious Disease Excellence Award 2021", "school": "University of Virginia", "specialization_explanation": "Treats infections caused by bacteria, viruses, fungi, and parasites."},
    {"name": "Dr. Brian Hall", "specialization": "Anesthesiology", "award": "Top Anesthesiologist 2020", "school": "University of Florida", "specialization_explanation": "Administers anesthesia and manages pain during surgeries."},
    {"name": "Dr. Elizabeth Wright", "specialization": "Otolaryngology", "award": "Otolaryngologist of the Year 2019", "school": "University of Southern California", "specialization_explanation": "Focuses on disorders of the ear, nose, and throat (ENT)."}
]
