import plotly.graph_objects as go

from AHPModel import ahp_model_weights
from ModelScoring import model_scoring

def radar_chart(user_scores, version=1):
    
    if version==1:
    
        labels = [label.replace('_', ' ').title() for label in user_scores.keys()]
        values = list(user_scores.values())

        layout = go.Layout(
            polar=dict(
                radialaxis=dict(
                    visible=False,
                    range=[0, 5]  # Set the range according to your data values
                )
            )
        )

        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=labels,
            fill='toself'
        ))

        fig.update_layout(layout)
    
    if version==2:
        
        model_weights = ahp_model_weights()
        
        weighted_user_scores = model_scoring(user_scores, output='user_scores_weighted')

        labels = [label.replace('_', ' ').title() for label in weighted_user_scores.keys()]
        values_user = list(weighted_user_scores.values())
        values_best = list(model_weights.values())

        layout = go.Layout(
            polar=dict(
                radialaxis=dict(
                    visible=False,
                    range=[0, max(values_best)]
                )
            )
        )

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=values_user,
            theta=labels,
            fill='toself',
            name='User Inputs'
        ))

        fig.add_trace(go.Scatterpolar(
            r=values_best,
            theta=labels,
            fill='toself',
            name='Best Possible Score'
        ))

        fig.update_layout(layout)
        
    return fig