from AHPModel.AHPModel import ahp_model_weights

def model_scoring(user_scores, output='final_score'):
    
    weights_dict = ahp_model_weights()
    
    user_scores_weighted = {}
    
    for key, value in user_scores.items():
        weighted_score = round((value * weights_dict[key])/5,4)
        user_scores_weighted[key] = weighted_score
        
    final_score = sum(user_scores_weighted.values())*100
    
    difference = {}

    for key in weights_dict:
        if key in user_scores_weighted:
            difference[key] = round(weights_dict[key] - user_scores_weighted[key],4)
    
    sorted_difference = dict(sorted(difference.items(), key=lambda x: -x[1]))    
    
    improvement_areas = list(sorted_difference.keys())[:3]
    
    if output == 'user_scores_weighted':
        
        return user_scores_weighted
    
    if output == 'final_score':
        
        return final_score
    
    if output == 'improvement_areas':
    
        return improvement_areas