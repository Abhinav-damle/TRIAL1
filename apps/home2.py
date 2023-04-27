import dash
from dash import html
import dash_bootstrap_components as dbc


# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

from app import app

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            #Header span the whole row
            #className: Often used with CSS to style elements with common properties.
            dbc.Col(html.H1("Welcome to Anime Hub ", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='Whats your fav anime' 
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='It consists of two main pages: Top, which tells about the top animes '
                                     'rank:which tells you the rank ')
                    , className="mb-5")
        ]),

        dbc.Row([
            # 2 columns of width 6 with a border
            dbc.Col(dbc.Card(children=[html.H3(children='Go to the code',
                                               className="text-center"),
                                       dbc.Button("Gapminder Data",
                                                  href="https://github.com/Abhinav-damle/dataset.git",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access the link for the dataset',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://github.com/Abhinav-damle/dataset.git",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

        ], className="mb-5"),
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url('anime2.jfif'), 
            style={'height':'30%', 'width':'80%'}))
        ]),
        html.A("Anime for lifeee",
               href="https://www.gapminder.org/tag/hans-rosling/")

    ])

])

# needed only if running this as a single page app
#if __name__ == '__main__':
#    app.run_server(port=8098,debug=True)