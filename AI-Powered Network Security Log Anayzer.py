import os
from google import genai
import numpy as np
# initialize the GenAI client
client = genai.Client()
# 2dnumpy matrix : 5 days (m to f) * 3 server nodes (a,b,c)
threat log = np.array([ , , , , [18,9,15] ])
# compute matrix using numpy
total_attacks_per_node = np.sum(threat_log, axis=0)
total_attacks_per_day = np.sum(threat_log, axis=1)
peak_attack_day = np.argmax(total_attacks_per_day)
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#prompt compiler: structuring math results into an ai brief
security_brief = f"""
SECURE NETWORK INFRASTRUCTURE METRICS:
- Node Attack Totals: {total_attacks_per_node.tolist()}
- Daily Attack Totals: {total_attacks_per_day.tolist()}
- Peak Danger Day: {days_of_week[peak_attack_day_index]}

As a SecOps Cyber Security AI, evaluate these numbers. Give me a sharp 3-sentence report identifying the weakest node and the danger day.
"""
print('Reading NumPy Matrix dimensions locally...')
print('Sending metrics securely via Environment Memory to Gemini 2.5 Flash...\n')

# Generate anaysis using Google's AI
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=security_brief
)
#output thefinal report
print( 'AI SECURITY THREAT REPORT:')
print(response.text)