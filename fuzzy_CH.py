# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:23:04 2018

@author: lenovo
"""


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership functions
energy = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'energy')
prev_count = ctrl.Antecedent(np.arange(0, 1100, 100), 'prev_count')
no_of_rounds = ctrl.Consequent(np.arange(0, 11, 1), 'no_of_rounds')

# Custom membership functions are built interactively with a Pythonic API
energy['low'] = fuzz.trimf(energy.universe, [0, 0.2, 0.3])
energy['medium'] = fuzz.trimf(energy.universe, [0.25, 0.6, 0.75])
energy['high'] =  fuzz.trimf(energy.universe, [0.7, 0.9, 1.0])

prev_count['small'] = fuzz.trimf(prev_count.universe, [0, 100, 300] )
prev_count['inter'] = fuzz.trimf(prev_count.universe, [300, 500, 750])
prev_count['large'] = fuzz.trimf(prev_count.universe, [700, 900, 1000])

no_of_rounds['highly low'] = fuzz.trimf(no_of_rounds.universe, [0, 1.5, 2])
no_of_rounds['inter low'] = fuzz.trimf(no_of_rounds.universe, [1, 3, 3.5])
no_of_rounds['less low'] = fuzz.trimf(no_of_rounds.universe, [3, 4, 5])
no_of_rounds['less med'] = fuzz.trimf(no_of_rounds.universe, [5, 5.5, 7])
no_of_rounds['highly med'] = fuzz.trimf(no_of_rounds.universe, [5, 6, 7])
no_of_rounds['inter med'] = fuzz.trimf(no_of_rounds.universe, [5, 6, 6.5])
no_of_rounds['less high'] = fuzz.trimf(no_of_rounds.universe, [7, 7.5, 8.5])
no_of_rounds['inter high'] = fuzz.trimf(no_of_rounds.universe, [7.5, 8, 8.5])
no_of_rounds['highly high'] = fuzz.trimf(no_of_rounds.universe, [8, 8.5, 10])

"""
# To see how these look with .view()
energy.view()

prev_count.view()

no_of_rounds.view()
"""

rule1 = ctrl.Rule(energy['high'] & prev_count['large'], no_of_rounds['less med'])
rule2 = ctrl.Rule(energy['high'] & prev_count['inter'], no_of_rounds['less high'])
rule3 = ctrl.Rule(energy['high'] & prev_count['small'], no_of_rounds['highly high'])
rule4 = ctrl.Rule(energy['medium'] & prev_count['large'], no_of_rounds['less low'])
rule5 = ctrl.Rule(energy['medium'] & prev_count['inter'], no_of_rounds['highly med'])
rule6 = ctrl.Rule(energy['medium'] & prev_count['small'], no_of_rounds['inter high'])
rule7 = ctrl.Rule(energy['low'] & prev_count['large'], no_of_rounds['highly low'])
rule8 = ctrl.Rule(energy['low'] & prev_count['inter'], no_of_rounds['inter low'])
rule9 = ctrl.Rule(energy['low'] & prev_count['small'], no_of_rounds['inter med'])


rounds_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

rounds = ctrl.ControlSystemSimulation(rounds_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
"""
# Uncomment this section to compute on given inputs
rounds.input['energy'] = 0.7
rounds.input['prev_count'] = 500

rounds.compute()

no_of_rounds.view(sim=rounds)
"""
