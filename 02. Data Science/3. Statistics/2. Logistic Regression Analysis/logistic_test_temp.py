# 목적 : 로지스틱 모델을 통해 이탈고객 예측하기
import pandas as pd
import numpy as np
from math import exp
import statsmodels.api as sm
import itertools

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
# 빅데이터 분석을 위한 데이터 보정

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['vmail_plan01'] = np.where(churn['vmail_plan'] == 'yes', 1, 0)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']
churn['total_mins'] = churn['day_mins'] + churn['eve_mins'] + churn['night_mins'] + churn['intl_mins']
churn['total_calls'] = churn['day_calls'] + churn['eve_calls'] + churn['night_calls'] + churn['intl_calls']

column_list = ['account_length', 'area_code', 'vmail_plan01', 'vmail_message', 'total_charges', 'total_mins', 'total_calls', 'custserv_calls']

# Fit a logistic regression model
dependent_variable = churn['churn01']

answer_list = []
answer_index = 1
for c_len in range(1, len(column_list)+1) :
        a_list =list(map(','.join, itertools.combinations(column_list, c_len)))
        for a_len in range(len(a_list)) :
            b_list = a_list[a_len].split(',') # 조합
            # temp_list = ['account_length', 'area_code', 'vmail_plan01', 'vmail_message', 'total_charges', 'total_mins',
            #              'total_calls', 'custserv_calls']
            # print(b_list)
            # for b in b_list:
            #     if b in column_list:
            #         temp_list.remove(b)

            # independent_variables = churn[temp_list]
            independent_variables = churn[b_list]
            independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
            logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

            new_observations = churn.loc[churn.index, independent_variables.columns]
            new_observations_with_constant = sm.add_constant(new_observations, prepend=True)

            y_predicted = logit_model.predict(new_observations_with_constant)
            y_predicted_rounded = [round(score, 0) for score in y_predicted]

            # print(y_predicted_rounded)
            count = 0
            for idx in range(len(churn.index)):
                if churn['churn01'][idx] == y_predicted_rounded[idx]:
                    count += 1
            print(b_list)
            print("%s. %s" %(answer_index, round(count / len(churn.index) * 100, 2)))
            answer_index+=1
            # answer_list.append(round(count / len(churn.index) * 100, 2))
            # answer_list.sort(reverse=True)
#
# print(answer_list)

