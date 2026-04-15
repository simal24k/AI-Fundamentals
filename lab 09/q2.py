from pgmpy.models import DiscreteBayesianNetwork as BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

cpd_I = TabularCPD(
    variable='Intelligence',
    variable_card=2,
    values=[[0.7], [0.3]],
    state_names={'Intelligence': ['High', 'Low']}
)

cpd_S = TabularCPD(
    variable='StudyHours',
    variable_card=2,
    values=[[0.6], [0.4]],
    state_names={'StudyHours': ['Sufficient', 'Insufficient']}
)

cpd_D = TabularCPD(
    variable='Difficulty',
    variable_card=2,
    values=[[0.4], [0.6]],
    state_names={'Difficulty': ['Hard', 'Easy']}
)


cpd_G = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.70, 0.85, 0.45, 0.60, 0.35, 0.50, 0.15, 0.25],
        [0.20, 0.10, 0.35, 0.30, 0.40, 0.35, 0.40, 0.45],
        [0.10, 0.05, 0.20, 0.10, 0.25, 0.15, 0.45, 0.30],
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2],
    state_names={
        'Grade': ['A', 'B', 'C'],
        'Intelligence': ['High', 'Low'],
        'StudyHours': ['Sufficient', 'Insufficient'],
        'Difficulty': ['Hard', 'Easy']
    }
)

cpd_P = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.95, 0.80, 0.50],
        [0.05, 0.20, 0.50],
    ],
    evidence=['Grade'],
    evidence_card=[3],
    state_names={
        'Pass': ['Yes', 'No'],
        'Grade': ['A', 'B', 'C']
    }
)

model.add_cpds(cpd_I, cpd_S, cpd_D, cpd_G, cpd_P)
assert model.check_model(), "Model is invalid"
print("\nModel validated successfully.")

inference = VariableElimination(model)

q1 = inference.query(
    variables=['Pass'],
    evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'}
)
print("\nInference 1: P(Pass | StudyHours=Sufficient, Difficulty=Hard)")
for i, state in enumerate(q1.state_names['Pass']):
    print(f"  P(Pass={state}) = {q1.values[i]:.4f}")

q2 = inference.query(
    variables=['Intelligence'],
    evidence={'Pass': 'Yes'}
)
print("\nInference 2: P(Intelligence | Pass=Yes)")
for i, state in enumerate(q2.state_names['Intelligence']):
    print(f"  P(Intelligence={state}) = {q2.values[i]:.4f}")
