#!/usr/bin/env python
import os
from pathlib import Path
from collections import defaultdict

fns_seq = [ '1d', 'forrester', 'levy', 'levy_hard', 'bohachevsky', 'bohachevsky_hard', 'branin', 'camelback',  'hartmann6', 'robot_pushing3d', 'robot_pushing4d' ]
fns_seq = [ 'np_1d', 'np_forrester', 'np_bohachevsky' ]
fns_seq = [ 'var_forrester', 'var_camelback', 'var_robot_pushing3d' ]
fns_seq = [ 'levy_def_C0_5_S0_01', 'levy_def_C0_5_S0_1', 'levy_def_C0_5_S1', 'levy_def_C2_S0_01', 'levy_def_C2_S0_1', 'levy_def_C2_S1', 'levy_def_C8_S0_01', 'levy_def_C8_S0_1', 'levy_def_C8_S1']
fns_seq = [ 'branin_rbf', 'branin', 'branin_matern32', 'camelback_rbf', 'camelback', 'camelback_matern32' ]
fns_seq = [ '1d_dynamic', 'forrester_dynamic', 'levy_dynamic' ]
charts = []

fn_name_dict = {
    '1d':'\\synthetic', 
    '1d_dynamic':'\\synthetic-\\dynamic', 
    'bohachevsky':'\\bohachevsky', 
    'bohachevsky_hard':'\\bohachevskyhard', 
    'branin':'\\branin', 
    'branin_matern32':'\\branin-\\maternx{3}{2}', 
    'branin_rbf':'\\branin-\\rbf', 
    'camelback':'\\camelback', 
    'camelback_matern32':'\\camelback-\\maternx{3}{2}', 
    'camelback_rbf':'\\camelback-\\rbf', 
    'forrester':'\\forrester', 
    'forrester_dynamic':'\\forrester-\\dynamic', 
    'hartmann6':'\\hartmann', 
    'levy':'\\levy', 
    'levy_hard':'\\levyhard', 
    'robot_pushing3d':'\\robotsmall', 
    'robot_pushing4d':'\\robotlarge',
    'np_1d':'\\npsynthetic', 
    'np_forrester':'\\npforrester', 
    'np_levy':'\\nplevy', 
    'np_bohachevsky':'\\np_bohachevsky',
    'levy_def_C0_5_S0_01':'\\levydef{0.5}{0.01}', 
    'levy_def_C0_5_S0_1':'\\levydef{0.5}{0.1}', 
    'levy_def_C0_5_S1':'\\levydef{0.5}{1}', 
    'levy_def_C2_S0_01':'\\levydef{2}{0.01}', 
    'levy_def_C2_S0_1':'\\levydef{2}{0.1}', 
    'levy_def_C2_S1':'\\levydef{2}{1}', 
    'levy_def_C8_S0_01':'\\levydef{8}{0.01}', 
    'levy_def_C8_S0_1':'\\levydef{8}{0.1}', 
    'levy_def_C8_S1':'\\levydef{8}{1}',
    'levy_dynamic':'\\levy-\\dynamic',  
    'var_forrester':'\\varforrester', 
    'var_camelback':'\\varcamelback', 
    'var_robot_pushing3d':'\\varrobotsmall', 
}

# \newcommand{\synthetic}{Synthetic1D\xspace}
# \newcommand{\forrester}{Forrester1D\xspace}
# \newcommand{\levy}{Levy1D\xspace}
# \newcommand{\bohachevsky}{Bohachevsky2D\xspace}
# \newcommand{\branin}{Branin2D\xspace}
# \newcommand{\camelback}{Camelback2D\xspace}
# \newcommand{\hartmann}{Hartmann6D\xspace}
# \newcommand{\robotsmall}{Robot3D\xspace}
# \newcommand{\robotlarge}{Robot4D\xspace}

# Must be prepended with Chart Type
chart_type_dict = {
    'Illustration_example-Illustration': 'Illustration',
    'Scatter_overall_avg_log_log_rev-Scatter-success_rate-norm_cum_c_t' : 'SuccessRate_Cost_Avg',
    'Scatter_overall_log_log_rev-Scatter-success_rate-norm_cum_c_t' : 'SuccessRate_Cost',
    'Scatter_dynamic_overall_avg_log_log_rev-Scatter-success_rate-norm_cum_c_t': 'Dynamic_SuccessRate_Cost_Avg',
    'Scatter_dynamic_overall_log_log_rev-Scatter-success_rate-norm_cum_c_t': 'Dynamic_SuccessRate_Cost',
    'CostParam_best_param-CostParam-success_rate-norm_cum_c_t' : 'Cost',
    'TripleAxisParam_AggressiveSubtractionAttack-TripleAxisParam-norm_cum_c_t-success_rate' : '\\aggressivesubtraction',
    'TripleAxisParam_ClippingAttack-TripleAxisParam-norm_cum_c_t-success_rate' : '\\clipping',
    'TripleAxisParam_SubtractionAttackRnd-TripleAxisParam-norm_cum_c_t-success_rate' : '\\subtractionrnd',
    'TripleAxisParam_SubtractionAttackSq-TripleAxisParam-norm_cum_c_t-success_rate' : '\\subtractionsq',
}

root = './img'

charts = defaultdict(dict)
for path, subdirs, files in os.walk(root):
    for name in files:

        path_parts_lst = list(Path(path).parts)
        if len(path_parts_lst) != 3:
            continue
        
        path_parts = list(path_parts_lst[1:]) + [name[:-4]]
        chart_ref = '_'.join(path_parts)

        fn_name_ref = path_parts_lst[1]
        if not fn_name_ref in fn_name_dict:
            continue
        fn_name = fn_name_dict[fn_name_ref]
        chart_type_ref = '_'.join(path_parts[1:])
        if not chart_type_ref in chart_type_dict:
            continue
        
        chart_type = chart_type_dict[chart_type_ref]

        chart_name = f"{fn_name}"

        img_path = os.path.join(path, name)[2:]

        output = '\\subfloat['+chart_name+']{\\includegraphics[width=0.32\\textwidth]{'+img_path+'}\\label{fig:appendix-'+chart_ref+'}}'
        charts[chart_type_ref][fn_name_ref] = output

for chart_type, chart_data_dict in charts.items():
    i = 1
    for fn_ref in fns_seq:
        if fn_ref in chart_data_dict:
            if i % 3 == 0:
                delim = '\\\\'
            else:
                delim = ''
            print(chart_data_dict[fn_ref] + delim)
            i += 1
    print("==================================")
