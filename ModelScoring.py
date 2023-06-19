from AHPModel import ahp_model_weights

def model_scoring(user_scores, output='final_score'):
    
    weights_dict = ahp_model_weights()
    
    user_scores_weighted = {}
    
    for key, value in user_scores.items():
        weighted_score = round((value * weights_dict[key] / 5),4)
        user_scores_weighted[key] = weighted_score
        
    final_score = sum(user_scores_weighted.values())*100
    
    if output == 'final_score':
        
        return final_score
    
    if output == 'user_scores_weighted':
        
        return user_scores_weighted