# <p align="center"> Care Companion </p>
Care Companion is a LLM companion for doctors and pantients. Using the ability of LLM, it aimed to be doctor's and patients personal assistant 
Here is our [demo](https://carecompanion.streamlit.app/)

![video](./assets/video.gif)

# Key Features of Care Companion ⭐
- **Chatbot for Doctor** : Utilizating RAG and Brave API, we give the every doctor its own personal assitant. You can ask any information about patients' information, latest medical paper, and many more
- **Doctor Assistant** : Utilizating RAG, it can help doctors to diagnose patient based on their sysmtomps and health record
- **Chatbot for Patient** : Using RAG and Brave API, the chatbot can answer most of patient's question about the hospital, including doctor's schedule, and any question about medical 
- **Patient Assistant** : When register / book time schedule, our system help the patients to determine the best doctors based on your sysmtomps

## Installation Process :minidisc: 
1. Clone the repository
```Python
git clone "https://github.com//Aquos06/Complit.git"
```
2. Install dependency
```Python
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements
```
3. Start application
```Python
streamlit run main.py
```