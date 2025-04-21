
import json
import uuid  # For generating unique IDs
import re
from searchengine import search_engine
from llm import get_model
from refinery import fetch_data
from questions import Aasker
from validator import validate
# Extract answer function
def extract_answer(response: str) -> str:
    """Extract the content between <BoA> tags"""
    pattern = r'<BoA>(.*?)</BoA>'
    match = re.search(pattern, response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "No properly formatted answer found"

# Function to generate questions for each org

# Function to generate structured JSON data
def generate_json_schema(organization_name, extracted_data):
    return {
        "_id": {"$oid": str(uuid.uuid4())},  # Generating a unique object ID
        "organization_name": organization_name,  # Storing the organization name separately
        "organization_description": extracted_data.get("organization_description", ""),
        "organizational_structure": extracted_data.get("organizational_structure", ""),
        "departments": extracted_data.get("departments", ""),
        "leadership": extracted_data.get("leadership", ""),
        "headquarters": extracted_data.get("headquarters", ""),
        "established_year": extracted_data.get("established_year", ""),
        "career_opportunities": extracted_data.get("career_opportunities", ""),
        "employee_benefits": extracted_data.get("employee_benefits", ""),
        "culture_and_values": extracted_data.get("culture_and_values", ""),
        "partnerships": extracted_data.get("partnerships", ""),
        "community_outreach": extracted_data.get("community_outreach", ""),
        "financial_overview": extracted_data.get("financial_overview", ""),
        "customer_feedback": extracted_data.get("customer_feedback", ""),
        "innovation_strategies": extracted_data.get("innovation_strategies", ""),
        "international_presence": extracted_data.get("international_presence", ""),
        "research_and_development": extracted_data.get("research_and_development", ""),
        "diversity_and_inclusion": extracted_data.get("diversity_and_inclusion", ""),
        "sustainability_commitment": extracted_data.get("sustainability_commitment", ""),
        "data_privacy_and_security": extracted_data.get("data_privacy_and_security", ""),
    }


# Main function to fetch and store data
import json
from refinery import fetch_data, Fo, ReFT

def demo(name_list, output_file="Org_research.json"):
    final_data = []
    
    ignore = ["_id", "organization_name"]
    never = ["_id", "organization_name"]

    for idx, org in enumerate(name_list, start=1):
        try:
            questions = Aasker(org)
            college_data = {"organization_name": org}  # Store org name directly
            print(f"\nProcessing {org} ({idx}/{len(name_list)})")

            for field, question in questions.items():
                flag = 0
                print(f"Field: {field}")
                websearch = search_engine(question)
                # print("===================Quesion ==============",question)
                # print("=================== WebSearch ==============",websearch)

                if field not in ignore and flag == 0:
                    print("First")
                    response = validate(question, websearch)
                    extracted_text = ReFT(response)  # Extracting relevant text
                    flag = 1  # Prevent further processing for this iteration
                    
                elif field not in never and flag == 0:
                    print("Second")
                    response = validate(question, websearch)
                    extracted_text = Fo(response)
                    flag = 1
                    
                else:
                    print("Third")
                    response = fetch_data(question, websearch)
                    extracted_text = extract_answer(response)
                    flag = 0  # Reset flag for the next iteration
                    
                
                print(f"\nQuestion: {question}\nExtracted Answer: {extracted_text}")

                # Handle nested fields (e.g., "important_links.admissions")
                if "." in field:
                    main_key, sub_key = field.split(".")
                    college_data.setdefault(main_key, {})[sub_key] = extracted_text
                else:
                    college_data[field] = extracted_text

            # Generate final structured JSON
            structured_data = generate_json_schema(org, college_data)
            final_data.append(structured_data)
            # Keep the original saving mechanism
            with open(output_file, "w", encoding="utf-8") as json_file:
                json.dump(final_data, json_file, indent=4, ensure_ascii=False)
                print(f"\nData saved after processing {idx} colleges.")

            # Save after processing every 1 org (as per original logic)
            if idx % 1 == 0:
                with open(output_file, "w", encoding="utf-8") as json_file:
                    json.dump(final_data, json_file, indent=4, ensure_ascii=False)
                print(f"\nData saved after processing {idx} colleges.")

        except Exception as e:
            print(f"Error processing {org}: {e}")

    if len(name_list) % 1 != 0:
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(final_data, json_file, indent=4, ensure_ascii=False)
        print(f"\nFinal data saved after processing {len(name_list)} colleges.")

    print("\nData successfully saved to", output_file)
def load_college_names(filename):
    """Reads a text file and returns a list of org names"""
    with open(filename, "r", encoding="utf-8") as file:
        college_names = [line.strip() for line in file if line.strip()]  # Remove empty lines
    return college_names

# Load org names from file
name_list = load_college_names("org.txt")

# Call the demo function with the lo aded names
demo(name_list)