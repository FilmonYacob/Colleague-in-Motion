from django.shortcuts import render
from .models import Player
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# path = 'C:\\Users\\Filmon\\Desktop\\And Those\\IIPStpChallenge\\IIPStpSite\\db.sqlite3'
# conn = sqlite3.connect(path, check_same_thread=False)
# curr = conn.cursor()

# def index(request):
# 	command = "SELECT name, Steps, Percentage,Predicted FROM TestTable ORDER BY Steps DESC"
# 	data  = curr.execute(command)
# 	dataAll = data.fetchall()
# 	players_list = []
# 	num_steps =[]
# 	percentages = []
# 	predictedStps = []
# 	for item in dataAll:
# 		players_list.append(item[0])
# 		num_steps.append(item[1])
# 		percentages.append(item[2])
# 		predictedStps.append(item[3])
# 	player_stp_dict = dict(zip(players_list,num_steps))
# 	player_perc_dict = dict(zip(players_list,percentages))
# 	player_peredicted_dict = dict(zip(players_list,predictedStps))

# 	return render(request, 'personal/base.html',{'players_list': players_list,
# 				'player_stp_dict':player_stp_dict,
# 				'player_perc_dict':player_perc_dict,
# 				'player_peredicted_dict':player_peredicted_dict})

# def login(request):
# 	render(request,'personal/registation/loginForm.html', {'players_list': players_list})
# def logout(request):
# 	render(request,'personal/base.html',{'players_list': players_list})


## copied and pasted

class IndexView(generic.ListView):
    template_name = 'iipinmotion/home1.html'
    context_object_name = 'all_players'
    queryset = Player.objects.all()


class DetailedView(generic.DetailView):
    model = Player
    template_name = 'iipinmotion/detail.html'


class PlayerCreate(CreateView):
    model = Player
    fields = ['first_name', 'last_name', 'email', 'num_stps', 'stps_date']


from django.contrib.auth import authenticate, login

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #'Redirect to a success page.'
        ...
    else:
        return  'invalid login error message'

def logout_view(request):
    logout(request)
    # Redirect to a success page.

def login_view_before(request):
	return render(request,'iipinmotion/loginForm.html', {})

def registation_view(request):
	return render(request,'iipinmotion/registrationForm.html', {})

def home_view(request):
	return render(request,'home1.html', {})