import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
import dash_bootstrap_components as dbc

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# owner: shivp Kaggle. Source: https://data.mendeley.com/datasets
# dataset was modified. Original data: https://www.kaggle.com/shivkp/customer-behaviour
dfv = pd.read_csv(DATA_PATH.joinpath("completely_cleaned_anime2.csv")) 
num_list = ['duration', 'votes', 'user_review', 'Episodes']
v=['top10-rank','top20-rank','top100-rank']
year=dfv.sort_values('start_year', ascending=True)
m=list(year.start_year.unique())
l=list(year.start_year.value_counts(ascending=True))
fig2=px.line(x=m,y=l,title="Yearly releases of animes").update_layout(xaxis_title="Year", yaxis_title="anime_count")
layout = html.Div([
    
    
    html.Div(
    [
        html.H4("Life expectancy plot with a selectable hover mode"),
        html.P("Select hovermode:"),
        dcc.RadioItems(
            id="hovermode",
            inline=True,
            options=["genre1", "genre2", "Total genre"],
            value="closest",
        ),
        dcc.Graph(id="graph"),    
        dbc.Container([
                dbc.Row([
                    #Header span the whole row
                    #className: Often used with CSS to style elements with common properties.
                    dbc.Col(html.H5("From the above graph we can tell that subgenre for the anie is quite different hence we can explain it more by the total genre ", className="text-center")
                            , className="mb-5 mt-5")
                ]),])
    ]
),
    html.Div([
    html.H4('Scatterplot between votes and user_reviews'),
    dcc.Graph(id="scatter-plot"),
    html.P("Filter with ratings"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=9.8, step=0.5,
        marks={0: '0', 9.8: '9.8'},
        value=[0, 9.8]
    ),        dbc.Container([
                    dbc.Row([
                        #Header span the whole row
                        #className: Often used with CSS to style elements with common properties.
                        dbc.Col(html.H5("There seems to be a relationship between the 2 ", className="text-center")
                                , className="mb-5 mt-5")
                    ]),])
]),
    html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Graph(id='g1',figure=fig2)
        ], className="six columns"),
        
        html.Div([
            html.H3('Column 3'),
            dcc.Graph(id='g2',figure=fig2)
        ], className="six columns"),
        
        html.Div([
            html.H3('Column 2'),
            dcc.Graph(id='g3', figure=px.line(x=m,y=l,title="Yearly releases of animes").update_layout(xaxis_title="Year", yaxis_title="anime_count"))
        ], className="six columns"),
    ], className="row")
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

@app.callback(
    Output("graph", "figure"),
    Input("hovermode", "value"),
)


def display_value(x):
    s=dfv.genre1.value_counts()
    genre1= pd.DataFrame({'genre1':s.index, 'Count':s.values})
    s=dfv.genre2.value_counts().head(11)
    genre2= pd.DataFrame({'genre2':s.index, 'Count':s.values})

            
        
     
    if x=='genre1':
        genre1=genre1.sort_values('Count', ascending=False)
        fig = px.bar(genre1,x='genre1', y='Count', 
              title = 'votes of top10 anime')
        return fig

    elif x=='genre2':
         genre2=genre2.sort_values('Count', ascending=False)
         fig = px.bar(genre2,x='genre2', y='Count', 
               title = 'votes of top10 anime')
         return fig       
        
    else:
        for i in range(0,11):
            for j in range(0,11):
                if genre1.genre1[i]==genre2.genre2[j]:
                    genre1.Count[i]=genre1.Count[i]+genre2.Count[j]
        genre1=genre1.sort_values('Count', ascending=False)
        fig = px.bar(genre1,x='genre1', y='Count', 
               title = 'votes of top10 anime')
        return fig   

@app.callback(
    Output("scatter-plot", "figure"), 
    Input("range-slider", "value"))
def update_bar_chart(slider_range):

    low, high = slider_range
    mask = (dfv['ratings'] > low) & (dfv['ratings'] < high)
    fig = px.scatter(
        dfv[mask], x="votes", y="user_review", 
        hover_data=['name'],trendline="ols")
    return fig