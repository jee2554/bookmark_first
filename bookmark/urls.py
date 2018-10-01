from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # # /bookmark/ 요청을 처리할 뷰 클래스를 BookmarkLV로 지정하고, URL 패턴 이름 지정
    # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    # # /bookmark/숫자/ 요청을 처리할 뷰 클래스를 BookmarkDV로 지정하고, URL 패턴 이름 지정
    # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),

    url(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$', views.BookmarkDV.as_view(), name='detail'),
    url(r'^bookmark_t_CBV/$', views.BookmarkLV.as_view(), name='index_t_CBV'),
    # url(r'^bookmark_t_FBV/$', views.tabularBookmark, name='index_t_FBV'),
]