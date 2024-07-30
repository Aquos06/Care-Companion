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

                                Always prioritize patient safety, confidentiality, and ethical medical practices in all interactions.
                            """
        
    def __reformat_history__(self, history_list: List[str]) -> List[dict]:
        formatted_history = [{"role":"system", "content":self.system_prompt}]
        
        if history_list:
            for index, history in enumerate(history_list):
                if index % 2 == 0:
                    formatted_history.append({"role":"user","content": history})
                else:
                    formatted_history.append({"role": "assistant","content": history})
                    
        return formatted_history
        
        
    def inference(self,query:str, history: List[str]=None):
        formated_history = self.__reformat_history__(history_list=history)
        formated_history.append({"role": "user","content": query})
        
        temp_chunk = ""
        for chunk in self.client.chat.completions.create(
            messages=formated_history,
            model="tiiuae/falcon-180B-chat",
            stream=True
        ):
            delta_content = chunk.choices[0].delta.content
            if delta_content:
                temp_chunk += delta_content
                print(temp_chunk)
                
if __name__ == '__main__':
    ai_inference = AI71Inference()
    ai_inference.inference(query="Hai")
    