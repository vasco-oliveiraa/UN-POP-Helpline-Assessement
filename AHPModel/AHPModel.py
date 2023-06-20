import numpy as np
import pandas as pd
import os

def ahp_model_weights():
    
#     current_dir = os.path.dirname(os.path.abspath(__file__))
    
#     dataset_dir = os.path.join(current_dir, "Expert Insight Collection.csv")

#     expert_insights = pd.read_csv(dataset_dir)
    
#     # Melt the DataFrame to transform it into the desired structure
#     melted_expert_insights = pd.melt(expert_insights, id_vars='ExpertID', var_name='Criterion', value_name='Score')
    
#     criteria = melted_expert_insights['Criterion'].unique()
    
#     ahp_matrix = np.zeros(shape=(len(criteria),len(criteria)))
#     ahp_sum = np.zeros(len(criteria))
#     ahp_final = np.zeros(len(criteria))
    
#     pivoted_expert_insights = melted_expert_insights[['ExpertID','Criterion','Score']].pivot(index='ExpertID', columns='Criterion', values='Score')
    
#     for expert_id in range(len(pivoted_expert_insights)):
#         for criterion_index in range(len(criteria)):
#             for prev_criterion_index in range(criterion_index - 1, -1, -1):
#                 try:
#                     criterion_score = float(pivoted_expert_insights.iloc[expert_id].iloc[criterion_index])
#                     prev_criterion_score = float(pivoted_expert_insights.iloc[expert_id].iloc[prev_criterion_index])

#                     if criterion_score > prev_criterion_score:
#                         # Increment the preference count of the current criterion over the previous criterion
#                         ahp_matrix[prev_criterion_index, criterion_index] += 1.0
#                         # Increment the total preference count of the current criterion
#                         ahp_sum[criterion_index] += 1.0
#                     elif criterion_score < prev_criterion_score:
#                         # Increment the preference count of the previous criterion over the current criterion
#                         ahp_matrix[criterion_index, prev_criterion_index] += 1.0
#                         # Increment the total preference count of the previous criterion
#                         ahp_sum[prev_criterion_index] += 1.0
#                     else:
#                         # Increment the preference count of the current criterion and previous criterion equally
#                         ahp_matrix[criterion_index, prev_criterion_index] += 0.5
#                         ahp_matrix[prev_criterion_index, criterion_index] += 0.5
#                         # Increment the total preference count of the current criterion and previous criterion equally
#                         ahp_sum[criterion_index] += 0.5
#                         ahp_sum[prev_criterion_index] += 0.5
#                 except:
#                     pass

#     df_ahp_matrix = pd.DataFrame(ahp_matrix.copy(), index=criteria, columns=criteria)

#     for criterion_index1 in range(len(criteria)):
#         for criterion_index2 in range(len(criteria)):
#             ahp_matrix[criterion_index1, criterion_index2] = ahp_matrix[criterion_index1, criterion_index2] / ahp_sum[criterion_index1]

#     for criterion_index in range(len(criteria)):
#         ahp_final[criterion_index] = sum(ahp_matrix[:, criterion_index])

#     ahp_final_normalized = (ahp_final / np.sum(ahp_final))

#     df_ahp_final = pd.DataFrame(ahp_final_normalized, index=criteria, columns=['Score'])

#     df_ahp_final.index = df_ahp_final.index.str.replace(' ', '_').str.lower()
#     weights_dict = df_ahp_final.to_dict()['Score']
#    for key, value in weights_dict.items():
#        round_score = round(weights_dict[key],4)
#        weights_dict[key] = round_score

    # The code above is commented as the calculations do not need to be performed for each user input. It could be useful if there was a stream of data constantly improving the model. Refer to 'AHPModel_Notebook' to see the calculations used to reach this dictionary:
    
    weights_dict = {
        'digital_channel_implementation': 0.0947,
        'technology_stack': 0.0671,
        'fundraise_strategy': 0.1549,
        'confidentiality_data_protection': 0.1532,
        'responsiveness': 0.0774,
        'quality_impact': 0.1233,
        'staff_expertise': 0.097,
        'cultural_linguistic_needs': 0.0922,
        'age_appropriate_guidance': 0.0414,
        'accessibility': 0.0989
    }
    
    return weights_dict
