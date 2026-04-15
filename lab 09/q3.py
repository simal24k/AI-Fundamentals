disease_model = BayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.3], [0.7]],
    state_names={'Disease': ['Flu', 'Cold']}
)

cpd_fever = TabularCPD(
    variable='Fever', variable_card=2,
    values=[[0.9, 0.5], [0.1, 0.5]],
    evidence=['Disease'], evidence_card=[2],
    state_names={'Fever': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']}
)

cpd_cough = TabularCPD(
    variable='Cough', variable_card=2,
    values=[[0.8, 0.6], [0.2, 0.4]],
    evidence=['Disease'], evidence_card=[2],
    state_names={'Cough': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']}
)

cpd_fatigue = TabularCPD(
    variable='Fatigue', variable_card=2,
    values=[[0.7, 0.3], [0.3, 0.7]],
    evidence=['Disease'], evidence_card=[2],
    state_names={'Fatigue': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']}
)

cpd_chills = TabularCPD(
    variable='Chills', variable_card=2,
    values=[[0.6, 0.4], [0.4, 0.6]],
    evidence=['Disease'], evidence_card=[2],
    state_names={'Chills': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']}
)

disease_model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)
assert disease_model.check_model(), "Disease model invalid"

d_infer = VariableElimination(disease_model)

t3q1 = d_infer.query(
    variables=['Disease'],
    evidence={'Fever': 'Yes', 'Cough': 'Yes'}
)
print("\nInference 1: P(Disease | Fever=Yes, Cough=Yes)")
for i, state in enumerate(t3q1.state_names['Disease']):
    print(f"  P(Disease={state}) = {t3q1.values[i]:.4f}")

t3q2 = d_infer.query(
    variables=['Disease'],
    evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'}
)
print("\nInference 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)")
for i, state in enumerate(t3q2.state_names['Disease']):
    print(f"  P(Disease={state}) = {t3q2.values[i]:.4f}")
print("\nInference 3: P(Fatigue=Yes | Disease=Flu) = 0.70 (from CPT)")
