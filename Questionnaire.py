import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import chart_studio.plotly as py

print(dcc.__version__) # 0.6.0 or above is required


app = dash.Dash(__name__,external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]




)

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app.config.suppress_callback_exceptions = True

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',style={
    "background-color" : ' #e6e6e6',
    "height" :78,
    "position" : "relative"
    })
])


index_page = html.Div([
    # dcc.Link('Go to Page 1', href='/page-1'),
    # html.Br(),
    # dcc.Link('Go to Page 2', href='/page-2'),

    html.H1(dcc.Markdown(''' **Welcome to the Example Questionnaire !** '''),style={
           'top':130,
           'color': '#4a5062',
           "font-size" : 30,
           'position': 'relative',
           'font-family' : 'sans-serif',
           'textAlign': 'center',

       }),
    html.Br(),
       html.Label('Name : ',style={
              'top':130,
              'left' : 790,
              'color': '#4a5062',
              "font-size" : 28,
              'position': 'relative',
              'font-family' : 'sans-serif',

          }),
    dcc.Input(type='text' ,style={
           'top':90,
           'left' : 920,
           'color': '#1b93ee',
           "font-size" : 28,
           'position': 'relative',
           'font-family' : 'sans-serif',
           'border-radius' : 8,
           'height' : 43
       }),
       html.Br(),
       html.Label('Phone number : ',style={
              'top':135,
              'left' : 680,
              'color': '#4a5062',
              "font-size" : 28,
              'position': 'relative',
              'font-family' : 'sans-serif',

          }),
    dcc.Input(type='number' ,style={
           'top':92,
           'left' : 920,
           'color': '#1b93ee',
           "font-size" : 28,
           'position': 'relative',
           'font-family' : 'sans-serif',
           'border-radius' : 8,
           'height' : 43
       }),
        html.Br(),
        html.Label('Your email : ',style={
               'top':140,
               'left' : 735,
               'color': '#4a5062',
               "font-size" : 28,
               'position': 'relative',
               'font-family' : 'sans-serif',

           }),
     dcc.Input(type='email' ,style={
            'top':92,
            'left' : 920,
            'color': '#1b93ee',
            "font-size" : 28,
            'position': 'relative',
            'font-family' : 'sans-serif',
            'border-radius' : 8,
            'height' : 43
        }),
        html.Br(),
        html.A(html.Button('Get Started' , style={
               'width' : 180,
               'height'  : 55,
               'position': 'absolute',
            # 'text-align': 'center',
               'left': 730,
               'top' : 500,
               'border-radius': 12,
                'background' : '#1b93ee',
                'border-color':'#1b93ee',
               'color': '#fff',
               'border-width' : 1,
               "font-family": "sans-serif",
               "font-size" : 18,
           }),
    href='/page-1')

])

#Page 1
page_1_layout = html.Div([
    html.H1(dcc.Markdown(''' **Question 1 ?**''') ,style={
               'top':200,
               'left' : 700,
               'color': '#4a5062',
               "font-size" : 30,
               'position': 'relative',
               'font-family' : 'sans-serif',
            #    'textAlign': 'center',

           }),
    html.Div(id='page-1-content'),
    html.Br(),
    html.A(html.Button('Yes' , style={
           'width' : 100,
           'height'  : 55,
           'position': 'absolute',
        'text-align': 'center',
           'left': 720,
           'top' : 350,
           'border-radius': 12,
            'background' : '#fff',
            'border-color':'#1b93ee',
           'color': '#1b93ee',
           'border-width' : 1,
           "font-family": "sans-serif",
           "font-size" : 18,
       }),
       href='/page-2'),
       html.A(html.Button('No' , style={
              'width' : 100,
              'height'  : 55,
              'position': 'absolute',
           'text-align': 'center',
              'left': 980,
              'top' : 350,
              'border-radius': 12,
               'background' : '#fff',
               'border-color':'#1b93ee',
              'color': '#1b93ee',
              'border-width' : 1,
              "font-family": "sans-serif",
              "font-size" : 18,
          }),
          href='/page-2')

])

@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)

#page 2
page_2_layout = html.Div([
    html.Div(id='page-2-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **Question 2 ?**''') ,style={
               'top':150,
               'left':700,
               'color': '#4a5062',
               "font-size" : 30,
               'position': 'relative',
               'font-family' : 'sans-serif',
            #    'textAlign': 'center',

           }),
    #Checkbox's
        dcc.Checklist(
            options=[
                {'label': 'Option A', 'value': 'A'},
                {'label': 'Option B', 'value': 'B'},
                {'label': 'Option C', 'value': 'C'},
                {'label': 'Option D', 'value': 'D'}
            ],
            # values=['B'],
             labelStyle={'display': 'block'},
            style = {
            "font-size" : 24,
            'position': 'relative',
            'left': 800,
            'top' : 180,
            }
        ),
        html.A(html.Button('Back' , style={
               'width' : 140,
               'height'  : 55,
               'position': 'absolute',
            'text-align': 'center',
               'left': 700,
               'top' : 500,
               'border-radius': 12,
                'background' : '#fff',
                'border-color':'#1b93ee',
               'color': '#1b93ee',
               'border-width' : 1,
               "font-family": "sans-serif",
               "font-size" : 18,
           }),
           href='/page-1'),
           html.A(html.Button('Next' , style={
                  'width' : 140,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 940,
                  'top' : 500,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-3')
])

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)

#page 3
page_3_layout = html.Div([
    html.Div(id='page-3-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **Question 3 ?**''') ,style={
               'top':180,
               'left':620,
               'padding-right':800,
               'color': '#4a5062',
               "font-size" : 27,
               'position': 'relative',
               'font-family' : 'sans-serif',
               'align':"justify",
           }),
    dcc.RadioItems(
        options=[
            {'label': 'Option A','value' : 'R1'},
            {'label': 'Option B','value':'R2'},
            {'label': 'Option C','value':'R3'}
        ],
        value='R2',
        style = {
        "font-size" : 22,
        'position': 'relative',
        'left': 680,
        'top' : 210,
        }
    ),
        html.A(html.Button('Back' , style={
               'width' : 140,
               'height'  : 55,
               'position': 'absolute',
            'text-align': 'center',
               'left': 700,
               'top' : 450,
               'border-radius': 12,
                'background' : '#fff',
                'border-color':'#1b93ee',
               'color': '#1b93ee',
               'border-width' : 1,
               "font-family": "sans-serif",
               "font-size" : 18,
           }),
           href='/page-2'),
           html.A(html.Button('Next' , style={
                  'width' : 140,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 940,
                  'top' : 450,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-4')
])

@app.callback(dash.dependencies.Output('page-3-content', 'children'),
              [dash.dependencies.Input('page-3-radios', 'value')])
def page_3_radios(value):
    return 'You have selected "{}"'.format(value)

#page 4
page_4_layout = html.Div([
    html.Div(id='page-4-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **Question 4 ?**''') ,style={
               'top':200,
               'left':700,
               'padding-right':800,
               'color': '#4a5062',
               "font-size" : 27,
               'position': 'relative',
               'font-family' : 'sans-serif',
               'align':"justify"
           }),
           html.H1(dcc.Markdown(''' **$**'''),style={
                      'top':230,
                      'left':778,
                      'padding-right':800,
                      'color': '#4a5062',
                      "font-size" : 27,
                      'position': 'relative',
                      'font-family' : 'sans-serif',
                      'align':"justify"
                  }),
           dcc.Input(id='input', type='number',style={
                      'top':179,
                      'left':800,
                      'color': '#4a5062',
                      "font-size" : 27,
                      'position': 'relative',
                      'font-family' : 'sans-serif',

                  }),
            html.A(html.Button('Back' , style={
                   'width' : 115,
                   'height'  : 55,
                   'position': 'absolute',
                'text-align': 'center',
                   'left': 740,
                   'top' : 455,
                   'border-radius': 12,
                    'background' : '#fff',
                    'border-color':'#1b93ee',
                   'color': '#1b93ee',
                   'border-width' : 1,
                   "font-family": "sans-serif",
                   "font-size" : 18,
               }),
               href='/page-3'),
        html.A(html.Button('Skip' , style={
               'width' : 115,
               'height'  : 55,
               'position': 'absolute',
            'text-align': 'center',
               'left': 910,
               'top' : 455,
               'border-radius': 12,
                'background' : '#fff',
                'border-color':'#1b93ee',
               'color': '#1b93ee',
               'border-width' : 1,
               "font-family": "sans-serif",
               "font-size" : 18,
           }),
           href='/page-5'),
           html.A(html.Button('Next' , style={
                  'width' : 115,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 1080,
                  'top' : 455,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-5')
])

@app.callback(dash.dependencies.Output('page-4-content', 'children'),
              [dash.dependencies.Input('page-4-radios', 'value')])
def page_4_radios(value):
    return 'You have selected "{}"'.format(value)


#page 5
page_5_layout = html.Div([
    html.Div(id='page-5-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **Question 5 ?**''') ,style={
               'top':150,
               'left':500,
               'padding-right':800,
               'color': '#4a5062',
               "font-size" : 30,
               'position': 'relative',
               'font-family' : 'sans-serif',
               'align':"justify"
           }),
    html.Div(
           [
               dcc.Slider(
                      min=1,
                      max=20,
                   marks={i+1: '{}'.format(i+1) for i in range(20)},
                          value=5
                  ),
                  html.H1(dcc.Markdown(''' **Year**'''),style={
                             'top':25,
                             'left':1,
                            #  'padding-right':800,
                             'color': '#4a5062',
                             "font-size" : 20,
                             'position': 'relative',
                            #  'font-family' : 'sans-serif',

                         }),
           ],
           style={'position': 'relative','left': 600,'top' : 250,'width':800}
       ),
            html.A(html.Button('Back' , style={
                   'width' : 115,
                   'height'  : 55,
                   'position': 'absolute',
                'text-align': 'center',
                   'left': 750,
                   'top' : 500,
                   'border-radius': 12,
                    'background' : '#fff',
                    'border-color':'#1b93ee',
                   'color': '#1b93ee',
                   'border-width' : 1,
                   "font-family": "sans-serif",
                   "font-size" : 18,
               }),
               href='/page-4'),
        html.A(html.Button('Next' , style={
               'width' : 115,
               'height'  : 55,
               'position': 'absolute',
            'text-align': 'center',
               'left': 920,
               'top' : 500,
               'border-radius': 12,
                'background' : '#fff',
                'border-color':'#1b93ee',
               'color': '#1b93ee',
               'border-width' : 1,
               "font-family": "sans-serif",
               "font-size" : 18,
           }),
           href='/page-6'),
           html.A(html.Button('Skip' , style={
                  'width' : 115,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 1090,
                  'top' : 500,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-6')
])

@app.callback(dash.dependencies.Output('page-5-content', 'children'),
              [dash.dependencies.Input('page-5-radios', 'value')])
def page_5_radios(value):
    return 'You have selected "{}"'.format(value)

#page 6
page_6_layout = html.Div([
    html.Div(id='page-6-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **Question 6 ?**''') ,style={
               'top':200,
               'left':325,
            #    'padding-right':800,
               'color': '#4a5062',
               "font-size" : 30,
               'position': 'relative',
               'font-family' : 'sans-serif',
            #    'align':"justify"
           }),
           html.A(html.Button('Back' , style={
                  'width' : 110,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 700,
                  'top' : 400,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-5'),
                html.A(html.Button('Yes' , style={
                       'width' : 100,
                       'height'  : 55,
                       'position': 'absolute',
                    'text-align': 'center',
                       'left': 860,
                       'top' : 400,
                       'border-radius': 12,
                        'background' : '#fff',
                        'border-color':'#1b93ee',
                       'color': '#1b93ee',
                       'border-width' : 1,
                       "font-family": "sans-serif",
                       "font-size" : 18,
                   }),
                   href='/page-8'),
                   html.A(html.Button('No' , style={
                          'width' : 100,
                          'height'  : 55,
                          'position': 'absolute',
                       'text-align': 'center',
                          'left': 1010,
                          'top' : 400,
                          'border-radius': 12,
                           'background' : '#fff',
                           'border-color':'#1b93ee',
                          'color': '#1b93ee',
                          'border-width' : 1,
                          "font-family": "sans-serif",
                          "font-size" : 18,
                      }),
                      href='/page-8-1')
])

@app.callback(dash.dependencies.Output('page-6-content', 'children'),
              [dash.dependencies.Input('page-6-radios', 'value')])
def page_6_radios(value):
    return 'You have selected "{}"'.format(value)

#page 8
page_8_layout = html.Div([
    html.Div(id='page-8-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **Question 7 ?**''') ,style={
               'top':180,
               'left':620,
               'padding-right':800,
               'color': '#4a5062',
               "font-size" : 27,
               'position': 'relative',
               'font-family' : 'sans-serif',
               'align':"justify",
           }),
    dcc.RadioItems(
        options=[
            {'label': 'Option A','value' : 'R1'},
            {'label': 'Option B','value':'R2'},
            {'label': 'Option C','value':'R3'}
        ],
        value='R2',
        style = {
        "font-size" : 22,
        'position': 'relative',
        'left': 680,
        'top' : 210,
        }
    ),
        html.A(html.Button('Back' , style={
               'width' : 140,
               'height'  : 55,
               'position': 'absolute',
            'text-align': 'center',
               'left': 700,
               'top' : 450,
               'border-radius': 12,
                'background' : '#fff',
                'border-color':'#1b93ee',
               'color': '#1b93ee',
               'border-width' : 1,
               "font-family": "sans-serif",
               "font-size" : 18,
           }),
           href='/page-6'),
           html.A(html.Button('Next' , style={
                  'width' : 140,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 940,
                  'top' : 450,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-9')
])

@app.callback(dash.dependencies.Output('page-8-content', 'children'),
              [dash.dependencies.Input('page-8-radios', 'value')])
def page_8_radios(value):
    return 'You have selected "{}"'.format(value)

#page 8_1
page_8_1_layout = html.Div([
    html.Div(id='page-8-1-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **7. Question(Extra) ?**''') ,style={
               'top':180,
               'left':620,
               'padding-right':800,
               'color': '#4a5062',
               "font-size" : 27,
               'position': 'relative',
               'font-family' : 'sans-serif',
               'align':"justify",
           }),
    dcc.RadioItems(
        options=[
            {'label': 'Option 1','value' : 'R1'},
            {'label': 'Option 2','value':'R2'},
            {'label': 'Option 3','value':'R3'}
        ],
        value='R2',
        style = {
        "font-size" : 22,
        'position': 'relative',
        'left': 680,
        'top' : 210,
        }
    ),
        html.A(html.Button('Back' , style={
               'width' : 140,
               'height'  : 55,
               'position': 'absolute',
            'text-align': 'center',
               'left': 700,
               'top' : 450,
               'border-radius': 12,
                'background' : '#fff',
                'border-color':'#1b93ee',
               'color': '#1b93ee',
               'border-width' : 1,
               "font-family": "sans-serif",
               "font-size" : 18,
           }),
           href='/page-6'),
           html.A(html.Button('Next' , style={
                  'width' : 140,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 940,
                  'top' : 450,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-9')
])

@app.callback(dash.dependencies.Output('page-8-1-content', 'children'),
              [dash.dependencies.Input('page-8-1-radios', 'value')])
def page_8_1_radios(value):
    return 'You have selected "{}"'.format(value)

#page 9
page_9_layout = html.Div([
    html.Div(id='page-9-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **Question 8 ?**''') ,style={
               'top':180,
               'left':620,
               'padding-right':800,
               'color': '#4a5062',
               "font-size" : 27,
               'position': 'relative',
               'font-family' : 'sans-serif',
               'align':"justify",
           }),
    dcc.RadioItems(
        options=[
            {'label': 'Option A','value' : 'R1'},
            {'label': 'Option B','value':'R2'},
            {'label': 'Option C','value':'R3'}
        ],
        value='R2',
        style = {
        "font-size" : 22,
        'position': 'relative',
        'left': 680,
        'top' : 210,
        }
    ),
        html.A(html.Button('Back' , style={
               'width' : 140,
               'height'  : 55,
               'position': 'absolute',
            'text-align': 'center',
               'left': 700,
               'top' : 450,
               'border-radius': 12,
                'background' : '#fff',
                'border-color':'#1b93ee',
               'color': '#1b93ee',
               'border-width' : 1,
               "font-family": "sans-serif",
               "font-size" : 18,
           }),
           href='/page-8'),
           html.A(html.Button('Next' , style={
                  'width' : 140,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 940,
                  'top' : 450,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-10')
])

@app.callback(dash.dependencies.Output('page-9-content', 'children'),
              [dash.dependencies.Input('page-9-radios', 'value')])
def page_9_radios(value):
    return 'You have selected "{}"'.format(value)

#page 10
page_10_layout = html.Div([
    html.Div(id='page-10-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **Question 9 ?**''') ,style={
               'top':200,
               'left':420,
               'padding-right':800,
               'color': '#4a5062',
               "font-size" : 27,
               'position': 'relative',
               'font-family' : 'sans-serif',
            #    'align':"justify",
           }),
                       html.A(html.Button('Back' , style={
                              'width' : 110,
                              'height'  : 55,
                              'position': 'absolute',
                           'text-align': 'center',
                              'left': 690,
                              'top' : 400,
                              'border-radius': 12,
                               'background' : '#fff',
                               'border-color':'#1b93ee',
                              'color': '#1b93ee',
                              'border-width' : 1,
                              "font-family": "sans-serif",
                              "font-size" : 18,
                          }),
                          href='/page-9'),
                            html.A(html.Button('Yes' , style={
                                   'width' : 100,
                                   'height'  : 55,
                                   'position': 'absolute',
                                'text-align': 'center',
                                   'left': 860,
                                   'top' : 400,
                                   'border-radius': 12,
                                    'background' : '#fff',
                                    'border-color':'#1b93ee',
                                   'color': '#1b93ee',
                                   'border-width' : 1,
                                   "font-family": "sans-serif",
                                   "font-size" : 18,
                               }),
                               href='/page-11'),
                               html.A(html.Button('No' , style={
                                      'width' : 100,
                                      'height'  : 55,
                                      'position': 'absolute',
                                   'text-align': 'center',
                                      'left': 1020,
                                      'top' : 400,
                                      'border-radius': 12,
                                       'background' : '#fff',
                                       'border-color':'#1b93ee',
                                      'color': '#1b93ee',
                                      'border-width' : 1,
                                      "font-family": "sans-serif",
                                      "font-size" : 18,
                                  }),
                                  href='/page-11')
])

@app.callback(dash.dependencies.Output('page-10-content', 'children'),
              [dash.dependencies.Input('page-10-radios', 'value')])
def page_10_radios(value):
    return 'You have selected "{}"'.format(value)

#page 11
page_11_layout = html.Div([
    html.Div(id='page-11-content'),
    html.Br(),
    html.H1(dcc.Markdown(''' **RESULT**''') ,style={
               'top':120,
               'left':820,
               'padding-right':800,
               'color': '#4a5062',
               "font-size" : 40,
               'position': 'relative',
               'font-family' : 'sans-serif',
               'align':"justify"
           }),

            html.A(html.Button('Back' , style={
                   'width' : 130,
                   'height'  : 55,
                   'position': 'absolute',
                'text-align': 'center',
                   'left': 700,
                   'top' : 600,
                   'border-radius': 12,
                    'background' : '#fff',
                    'border-color':'#1b93ee',
                   'color': '#1b93ee',
                   'border-width' : 1,
                   "font-family": "sans-serif",
                   "font-size" : 18,
               }),
           href='/page-10'),

           html.A(html.Button('Done' , style={
                  'width' : 130,
                  'height'  : 55,
                  'position': 'absolute',
               'text-align': 'center',
                  'left': 1100,
                  'top' : 600,
                  'border-radius': 12,
                   'background' : '#fff',
                   'border-color':'#1b93ee',
                  'color': '#1b93ee',
                  'border-width' : 1,
                  "font-family": "sans-serif",
                  "font-size" : 18,
              }),
              href='/page-12')
])

@app.callback(dash.dependencies.Output('page-11-content', 'children'),
              [dash.dependencies.Input('page-11-radios', 'value')])

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-4':
        return page_4_layout
    elif pathname == '/page-5':
        return page_5_layout
    elif pathname == '/page-6':
        return page_6_layout
    # elif pathname == '/page-7':
    #     return page_7_layout
    elif pathname == '/page-8':
        return page_8_layout
    elif pathname == '/page-8-1':
        return page_8_1_layout
    elif pathname == '/page-9':
        return page_9_layout
    elif pathname == '/page-10':
        return page_10_layout
    elif pathname == '/page-11':
        return page_11_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

if __name__ == '__main__':
    app.run_server(debug=True)
