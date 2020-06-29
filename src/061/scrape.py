from matplotlib import pyplot as plt
import OpenBlender
import pandas as pd
import json

# action = 'API_getObservationsFromDataset'
# parameters = { 
#  'token':'5ef7b9a69516293fcff68edfymBnHFQMsINhqhewGIGxyI37nHSbjr',
#  'id_dataset':'5e7a0d5d9516296cb86c6263',
#  'date_filter':{
#                "start_date":"2020-01-01T06:00:00.000Z",
#                "end_date":"2020-03-11T06:00:00.000Z"},
#  'consumption_confirmation':'on',
#  'add_date' : 'date'
# }

# df_confirmed = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
# df_confirmed.reset_index(drop=True, inplace=True)
# df_confirmed.head(10)
# plt.show(df_confirmed.head)

action = 'API_getOpenTextData'
parameters = {
    'token':'5ef7b9a69516293fcff68edfymBnHFQMsINhqhewGIGxyI37nHSbjr',
    'consumption_confirmation':'on',
    'date_filter':{"start_date":"2020-01-01T06:00:00.000Z", 
                   "end_date":"2020-03-10T06:00:00.000Z"},
    'sources':[
                # Wall Street Journal
               {'id_dataset' : '5e2ef74e9516294390e810a9', 
                 'features' : ['text']},
                # ABC News Headlines
               {'id_dataset':"5d8848e59516294231c59581", 
                'features' : ["headline", "title"]},
                # USA Today Twitter
               {'id_dataset' : "5e32fd289516291e346c1726", 
                'features' : ["text"]},
                # CNN News
               {'id_dataset' : "5d571b9e9516293a12ad4f5c", 
                'features' : ["headline", "title"]}
    ],
    'aggregate_in_time_interval' : {
              'time_interval_size' : 60 * 60 * 24
    },
    'text_filter_search':['covid', 'coronavirus', 'ncov'],
    'add_date' : 'date'    
}
df_news = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df_news.reset_index(drop=True, inplace=True)

print(df_news)
