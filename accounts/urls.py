
from django.conf.urls import url,include
from django.views.generic.base import RedirectView

# from .views import tweet_detail_view, tweet_list_view, TweetDetailView, TweetListView
from django.contrib.auth.views import PasswordChangeView
from .views import (
	UserDetailView,
	UserFollowView,
	edit_profile,
	#change_password

	)

urlpatterns = [
    # #url(r'^admin/', admin.site.urls),
    # url(r'^$', RedirectView.as_view(url="/")),
    # url(r'^search/$', TweetListView.as_view(), name='list'),
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
	url(r'^profile/edit/$', edit_profile, name='edit_profile'),
    url(r'^profile/password/$',PasswordChangeView.as_view(template_name='accounts/change_password.html'), name='password_change')
    #url(r'^profile/password/$', change_password, name='change_password'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
