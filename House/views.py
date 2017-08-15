from django.shortcuts import render
from .models import House, Message
from Factor.models import Hospital, Accident, Library, Market, Stolen
import operator
from .forms import FactorForm, QueryForm, MessageForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils import timezone
from django.contrib import auth
from .forms import UserCreateForm
from itertools import chain
import re

count_factor = 0
user_query = ''


# 將使用者輸入的因素之分數集合
def GatherFactorScore(strFactor):
    global count_factor
    calculate = []
    count_factor += 1
    if strFactor == 'None':
        count_factor -= 1
    elif strFactor == 'Hospitals':
        score = Hospital.objects.all()
        # print(score)
        for i in range(0, 13):
            s1 = score[i]
            calculate.append(s1.h_score)
    elif strFactor == 'Accidents':
        score = Accident.objects.all()
        for i in range(0, 13):
            s1 = score[i]
            calculate.append(s1.a_score)
    elif strFactor == 'Librarys':
        score = Library.objects.all()
        for i in range(0, 13):
            s1 = score[i]
            calculate.append(s1.l_score)
    elif strFactor == 'Markets':
        score = Market.objects.all()
        for i in range(0, 13):
            s1 = score[i]
            calculate.append(s1.m_score)
    elif strFactor == 'Stolens':
        score = Stolen.objects.all()
        for i in range(0, 13):
            s1 = score[i]
            calculate.append(s1.s_score)
    return calculate


# 加權後加總
def CalculateFactorScore(s1, s2, s3):
    global count_factor
    score_result = []
    if count_factor == 3:
        for i in range(0, len(s1)):
            s1[i] *= 0.5
            s2[i] *= 0.3
            s3[i] *= 0.2
            tmp = s1[i] + s2[i] + s3[i]
            score_result.append(float("%.2f" % tmp))
    elif count_factor == 2:
        for i in range(0, len(s1)):
            s1[i] *= 0.6
            s2[i] *= 0.4
            tmp = s1[i] + s2[i]
            score_result.append(float("%.2f" % tmp))
    elif count_factor == 1:
        if s1 != []:
            score_result = s1
        elif s2 != []:
            score_result = s2
        elif s3 != []:
            score_result = s3
    return score_result

# 由小到大排序並轉換為字典

def SortedFactorScore(score_list):
    Ranking_Section = []
    Factor_Dictionary = {
        '八德區': score_list[0],
        '大溪區': score_list[1],
        '大園區': score_list[2],
        '復興區': score_list[3],
        '觀音區': score_list[4],
        '龜山區': score_list[5],
        '龍潭區': score_list[6],
        '蘆竹區': score_list[7],
        '平鎮區': score_list[8],
        '桃園區': score_list[9],
        '新屋區': score_list[10],
        '楊梅區': score_list[11],
        '中壢區': score_list[12],
    }
    Ranking_Section = sorted(Factor_Dictionary.items(), key=operator.itemgetter(1))
    return Ranking_Section


ranking_section = []


# 擷取使用者注重的因素並做一連串的處理，且redirect到結果頁面
def factor_choice(request):
    global count_factor, ranking_section, user_query, f1, f2, f3
    house_list = House.objects.all().order_by('?')[:8]
    q_form = QueryForm(request.POST or None)
    form = FactorForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        f1 = form.cleaned_data.get("FirstChoices")
        score_set1 = GatherFactorScore(f1)
        f2 = form.cleaned_data.get("SecondChoices")
        score_set2 = GatherFactorScore(f2)
        f3 = form.cleaned_data.get("ThirdChoices")
        score_set3 = GatherFactorScore(f3)
        score_list = CalculateFactorScore(score_set1, score_set2, score_set3)
        if score_list == []:
            return HttpResponseRedirect('/factor_empty')
        ranking_section = SortedFactorScore(score_list)
        # print('第一名：' + ranking_section[12][0] + ' 第二名：' + ranking_section[11][0] + ' 第三名：' + ranking_section[10][0])
        count_factor = 0
        return HttpResponseRedirect('/result')
    if q_form.is_valid():
        user_query = q_form.cleaned_data.get("HouseQuery")
        return HttpResponseRedirect('/qresult')
    return render(request, "home.html", {
        "form": form,
        'house_list': house_list,  # 只顯示前六筆資料
        'q_form': q_form
    })


def translation(f):
    if f == 'Accidents':
        f = '車禍事故'
    elif f == 'Hospitals':
        f = '醫療資源'
    elif f == 'Librarys':
        f = '圖書館'
    elif f == 'Markets':
        f = '市場'
    elif f == 'Stolens':
        f = '竊盜案件'
    else:
        f = ''
    return f


# 根據使用者選擇的因素，顯示出相對應的房屋區域
def house_result(request):
    global f1, f2, f3

    num1 = House.objects.filter(section__contains=ranking_section[12][0])
    num2 = House.objects.filter(section__contains=ranking_section[11][0])
    num3 = House.objects.filter(section__contains=ranking_section[10][0])
    house_result_list = list(chain(num1, num2, num3))
    t1 = translation(f1)
    t2 = translation(f2)
    t3 = translation(f3)

    return render(request, 'result.html', {
        'house_result_list': house_result_list,
        'first': ranking_section[12],
        'second': ranking_section[11],
        'third': ranking_section[10],
        'f1': t1,
        'f2': t2,
        'f3': t3
    })


# 查詢標題或地區
def query_result(request):
    query_result_list = House.objects.filter(
        Q(title__contains=user_query) |
        Q(section__contains=user_query)
    )

    return render(request, 'qresult.html', {
        'query_result_list': query_result_list,
        'user_query': user_query
    })


def get_member_name(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return username


# 顯示房屋詳細資料，跟留言綁一起

def house_detail(request, pk):
    house = House.objects.get(pk=pk)  # 將httpRequest裡的pk值，丟給models，找到相對應的pk值的Post資料表
    message_list = Message.objects.filter(h_fk=pk)
    user_name = get_member_name(request)
    # print(user_name)
    if request.method == 'POST':
        guestbook = MessageForm(request.POST)
        if guestbook.is_valid():
            message = Message(h_fk=house, user=user_name,
                              comment=guestbook.cleaned_data['comment'],
                              publication_date=timezone.now())

            message.save()
            guestbook = MessageForm()
    else:
        guestbook = MessageForm()
    return render(request, 'detail.html',
                  {'house': house, 'message_list': message_list,
                   'guestbook': guestbook, 'user_name': user_name})
    # 回傳httpResponse，將取得的post傳入 Template post.html


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        current = re.search(r'\?next=(?P<goNext>.+)', request.get_full_path())
        if current is not None:
            return HttpResponseRedirect(current.group('goNext'))  # 若登入成功 導到首頁
        else:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'registration/login.html')  # 若失敗，回到登入畫面


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreateForm()
    return render(request, 'register.html', locals())


def factor_empty(request):
    err_message = "您沒有選擇任何因素，請重新選擇"
    return render(request, 'error.html', locals())
