from utils.data_loader import load_regulations, load_data
from models.llm_profiling import generate_profiling_rules
from models.ml_risk_scoring import risk_scoring
from validation.validate import validate_data
from remediation.remediation import suggest_remediation

# Load regulations
regulations = load_regulations()

# Step 1: Generate profiling rules
rules = generate_profiling_rules(regulations)

# Step 2: Load sample report data
data = load_data("sample_report.csv")

# Step 3: Perform risk scoring
data = risk_scoring(data)

# Step 4: Validate data
validated_data = validate_data("sample_report.csv", "rules/profiling_rules.json")

# Step 5: Generate remediation actions
flagged_data = validated_data[validated_data["Validation"] == False]
remediation_suggestions = suggest_remediation(flagged_data.to_string())

print("Remediation Suggestions:", remediation_suggestions)
