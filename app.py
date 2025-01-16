import subprocess
import json
import sys

def evaluate_risk(weight, smoking, diet):
    # Prepare input for s(CASP)
    scasp_input = f"bmi({weight}). smoking_status({smoking}). diet_quality({diet})."
    
    # Run the s(CASP) program
    process = subprocess.run(
        ['scasp', 'health_risk.pl'],
        input=scasp_input, text=True, capture_output=True
    )
    
    return process.stdout

if __name__ == "__main__":
    # Read the data from the command line (JSON format)
    input_data = json.loads(sys.stdin.read())
    weight = input_data['weight']
    smoking = input_data['smoking']
    diet = input_data['diet']
    
    result = evaluate_risk(weight, smoking, diet)
    print(json.dumps({"result": result}))
