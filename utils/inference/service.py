from ai71 import AI71
from utils.const import AI71_API_KEY
from typing import List

class AI71Inference:
    def __init__(self) -> None:
        self.client = AI71(AI71_API_KEY)
        self.system_prompt = """
                                **System Prompt:**

                                You are an AI assistant designed to assist doctors in their daily tasks, including patient diagnosis, treatment recommendations, medical record management, and providing up-to-date medical information. Your responses should be accurate, concise, and based on the latest medical guidelines and research. Here are your main functions:

                                1. **Patient Diagnosis:**
                                - Ask relevant questions to gather symptoms and medical history.
                                - Provide potential diagnoses based on the information given.
                                - Suggest further tests or examinations if necessary.

                                2. **Treatment Recommendations:**
                                - Recommend treatment plans based on the diagnosed conditions.
                                - Provide information on medications, including dosages and potential side effects.
                                - Offer advice on lifestyle changes and preventive measures.

                                4. **Medical Information:**
                                - Offer up-to-date information on diseases, conditions, and medical procedures.
                                - Provide references to the latest medical research and guidelines.

                                5. **Patient Infromation**
                                - The Latest Patient infromation will be given, you need to summarize the patient Information
                                
                                Always prioritize patient safety, confidentiality, and ethical medical practices in all interactions.
                                DO NOT use User: in your response.
                            """
        
    def __reformat_history__(self, history_list: List[dict]) -> List[dict]:
        formatted_history = [{"role":"system", "content":self.system_prompt}]
        formatted_history.extend(history_list)
        return formatted_history
        
    def inference(self,links,history: List[dict]=None):
        formated_history = self.__reformat_history__(history_list=history)
        
        for chunk in self.client.chat.completions.create(
            messages=formated_history,
            model="tiiuae/falcon-180B-chat",
            top_p=0.2,
            top_k=50,
            stream=True,
            temperature=0.1
        ):
            delta_content = chunk.choices[0].delta.content
            if delta_content:
                yield delta_content
            
        if links:
            yield links
                
    def patient_inference(self, history: List[dict]):
        
        for chunk in self.client.chat.completions.create(
            messages=history,
            model="tiiuae/falcon-11B-chat",
            top_p=0.2,
            top_k=50,
            stream= True
        ):
            delta_content = chunk.choices[0].delta.content
            if delta_content:
                yield delta_content
       
    def make_suggestion(self, history: List[dict]):
        response = self.client.chat.completions.create(
            messages=history,
            model="tiiuae/falcon-180B-chat",
            top_k=50,
            top_p=0.2,
        )
        
        delta_content = response.choices[0].message.content
        return delta_content
                
if __name__ == '__main__':
    ai_inference = AI71Inference()
    ai_inference.inference(query="Hai")
    