from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import os.path as p
import datetime
# from django.shortcuts import render_to_response
from django.contrib import messages


def index(request):
    return render(request, 'polls/index.html')


def survey(request):
    return render(request, 'polls/survey.html')
# def survey(request):
#     queryDict = request.GET
#     agreement_dict = dict(queryDict)
#     print(agreement_dict)
#     print(agreement_dict['chk'])
#     print(len(agreement_dict['chk']))
#     if len(agreement_dict['chk']) == 1:
#         chk_policy = 0
#     else:
#         chk_policy = 1
#     privacyPolicy = {
#         'privacyPolicy':chk_policy
#     }

#     return render(request, 'polls/survey.html', privacyPolicy)


def results(request):
    username = request.GET.get('username')
    q1 = request.GET.get('q1')
    q2 = request.GET.get('q2')
    q3 = request.GET.get('q3')
    q4 = request.GET.get('q4')
    q5 = request.GET.get('q5')
    q6 = request.GET.get('q6')
    q7 = request.GET.get('q7')
    q8 = request.GET.get('q8')
    q9 = request.GET.get('q9')
    q10 = request.GET.get('q10')
    q11 = request.GET.get('q11')
    q12 = request.GET.get('q12')
    q13 = request.GET.get('q13')
    q14 = request.GET.get('q14')
    q15 = request.GET.get('q15')
    q16 = request.GET.get('q16')
    q17 = request.GET.get('q17')
    q18 = request.GET.get('q18')
    q19 = request.GET.get('q19')
    q20 = request.GET.get('q20')
    q21 = request.GET.get('q21')
    # privacyPolicy = request.GET.get('privacyPolicy')

    MONTH = datetime.date.today().month    # the current month
    DATE = datetime.date.today().day      # the current day
    HOUR = datetime.datetime.now().hour   # the current hour
    MINUTE = datetime.datetime.now().minute # the current minute
    
    content = {
        'username':username,
        'q1':q1,
        'q2':q2,
        'q3':q3,
        'q4':q4,
        'q5':q5,
        'q6':q6,
        'q7':q7,
        'q8':q8,
        'q9':q9,
        'q10':q10,
        'q11':q11,
        'q12':q12,
        'q13':q13,
        'q14':q14,
        'q15':q15,
        'q16':q16,
        'q17':q17,
        'q18':q18,
        'q19':q19,
        'q20':q20,
        'q21':q21
    }

    policy_dict = {
        '1':'agree',
        '0':'disagree'
    }

    # optional_content = {
    #     'username':username,
    #     'privacyPolicy':policy_dict[privacyPolicy]
    # }
    
    print(content)

    if not p.exists("./results/questionnaire/results.csv"):
        df = pd.DataFrame(data=content, index=[0])
        df.to_csv(f"./results/questionnaire/results.csv", sep='\t', na_rep="")
        df.to_csv(f"./results/questionnaire/q_{username}_{MONTH}_{DATE}_{HOUR}_{MINUTE}.csv", sep='\t', na_rep="")

    else:
        df = pd.read_csv("./results/questionnaire/results.csv", sep='\t')
        df = df.append(content, ignore_index=True)
        df = df.reset_index(drop=True)
        df.to_csv(f"./results/questionnaire/results.csv", sep='\t', na_rep="", index=False)
        user_df = pd.DataFrame(data=content, index=[0])
        user_df.to_csv(f"./results/questionnaire/q_{username}_{MONTH}_{DATE}_{HOUR}_{MINUTE}.csv", sep='\t', na_rep="")

    # user_df = pd.DataFrame(data=optional_content, index=[0])
    # user_df.to_csv(f"./results/optional/{username}_agree.csv", sep='\t', na_rep="")

    content = {
        'username':username,
        'q1':q1,
        'q2':q2,
        'q3':q3,
        'q4':q4,
        'q5':q5,
        'q6':q6,
        'q7':q7,
        'q8':q8,
        'q9':q9,
        'q10':q10,
        'q11':q11,
        'q12':q12,
        'q13':q13,
        'q14':q14,
        'q15':q15,
        'q16':q16,
        'q17':q17,
        'q18':q18,
        'q19':q19,
        'q20':q20,
        'q21':q21,
        # 'privacyPolicy':privacyPolicy
    }

    return render(request, 'polls/results.html', content)

def values(request):
    return render(request, 'polls/values.html')

def policy(request):
    return render(request, 'polls/policy.html')

def finish(request):

    # print(request.GET)
    # print(request.method)
    # print(request.path)

    username = request.GET.get('username')
    uni = request.GET.get('universalism')
    ben = request.GET.get('benevolence')
    con = request.GET.get('conformity')
    tra = request.GET.get('tradition')
    sec = request.GET.get('security')
    power = request.GET.get('power')
    ach = request.GET.get('achievement')
    hed = request.GET.get('hedonism')
    sti = request.GET.get('stimulation')
    sel = request.GET.get('self-direction')
    privacyPolicy = request.GET.get('privacyPolicy')
    correct = request.GET.get('Correctness')
    gender = request.GET.get('Gender')
    age = request.GET.get('Age')
    race = request.GET.get('Race')
    
    # print(gender)
    MONTH = datetime.date.today().month    # the current month
    DATE = datetime.date.today().day      # the current day
    HOUR = datetime.datetime.now().hour   # the current hour
    MINUTE = datetime.datetime.now().minute # the current minute
    
    policy_dict = {
        '1':'agree',
        '0':'disagree'
    }
    correct_dict = {
        '1':'yes',
        '0':'no'
    }
    gender_dict = {
        '1':'man',
        '0':'woman',
        None:'none'
    }
    age_dict = {
        '1':'10+',
        '2':'20+',
        '3':'30+',
        '4':'40+',
        '5':'50+',
        '6':'60+',
        None:'none'
    }
    race_dict = {
        '1':'white',
        '0':'non-white',
        None:'none'
    }

    content = {
        'username':username,
        'universalism':uni,
        'benevolence':ben,
        'conformity':con,
        'tradition':tra,
        'security':sec,
        'power':power,
        'achievement':ach,
        'hedonism':hed,
        'stimulation':sti,
        'self-direction':sel
    }

    optional_content = {
        'username':username,
        'privacyPolicy':policy_dict[privacyPolicy],
        'correct':correct_dict[correct],
        'gender':gender_dict[gender],
        'age':age_dict[age],
        'race':race_dict[race]
    }

    if not p.exists("./results/value/results.csv"):
        df = pd.DataFrame(data=content, index=[0])
        df.to_csv(f"./results/value/results.csv", sep='\t', na_rep="")
        df.to_csv(f"./results/value/v_{username}_{MONTH}_{DATE}_{HOUR}_{MINUTE}.csv", sep='\t', na_rep="")

    else:
        df = pd.read_csv("./results/value/results.csv", sep='\t')
        df = df.append(content, ignore_index=True)
        df = df.reset_index(drop=True)
        df.to_csv(f"./results/value/results.csv", sep='\t', na_rep="", index=False)
        user_df = pd.DataFrame(data=content, index=[0])
        user_df.to_csv(f"./results/value/v_{username}_{MONTH}_{DATE}_{HOUR}_{MINUTE}.csv", sep='\t', na_rep="")
    
    if not p.exists("./results/optional/results.csv"):
        df = pd.DataFrame(data=optional_content, index=[0])
        df.to_csv(f"./results/optional/results.csv", sep='\t', na_rep="")
        df.to_csv(f"./results/optional/{username}_{MONTH}_{DATE}_{HOUR}_{MINUTE}.csv", sep='\t', na_rep="")

    else:
        df = pd.read_csv("./results/optional/results.csv", sep='\t')
        df = df.append(content, ignore_index=True)
        df = df.reset_index(drop=True)
        df.to_csv(f"./results/optional/results.csv", sep='\t', na_rep="", index=False)
        user_df = pd.DataFrame(data=optional_content, index=[0])
        user_df.to_csv(f"./results/optional/{username}_{MONTH}_{DATE}_{HOUR}_{MINUTE}.csv", sep='\t', na_rep="")

    messages.success(request, 'Thank you for completing our survey!!')

    return render(request, 'polls/index.html')