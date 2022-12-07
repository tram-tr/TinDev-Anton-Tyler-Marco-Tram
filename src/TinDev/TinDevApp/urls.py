from django.urls import path
from . import views

app_name = "TinDev"
urlpatterns = [
    path('', views.homeView, name='home-page'),
    path('candidate/login/', views.candidateLoginPage, name='candidate-login'),
    path('recruiter/login/', views.recruiterLoginPage, name='recruiter-login'),

    path('recruiter/home/<slug:name>', views.RecruiterPage, name='recruiter-home'),
    path('candidate/home/<slug:name>', views.CandidatePage, name='candidate-home'),
    path('recruiter/home/<slug:name>/profile/update', views.RecruiterProfileUpdate, name='RecruiterProfile'),
    path('candidate/home/<slug:name>/profile/update', views.CandidateProfileUpdate, name='CandidateProfile'),

    path('candidate/add/', views.CandidateCreateView, name='candidateAdd'),
    path('recruiter/add/', views.RecruiterCreateView, name='recruiterAdd'),

    path('recruiter/home/<slug:name>/post/add', views.PostCreate, name = 'postAdd'),
    path('recruiter/home/<slug:name>/post/view/all', views.PostViewRecruiterAll, name = 'postViewAll'),
    path('recruiter/home/<slug:name>/post/view/active', views.PostViewRecruiterActive, name = 'postViewActive'),
    path('recruiter/home/<slug:name>/post/view/inactive', views.PostViewRecruiterInactive, name = 'postViewInactive'),
    path('recruiter/home/<slug:name>/post/update/<int:id_num>', views.PostUpdateRecruiter, name = 'postUpdate'),
    path('recruiter/home/<slug:name>/post/delete/<int:id_num>', views.PostDeleteRecruiter, name = 'postDelete'),
    path('recruiter/home/<slug:name>/post/view/<int:id_num>/applicant', views.PostViewRecruiterApplicant, name = 'postViewApplicant'),
    path('recruiter/home/<slug:name>/post/view/<int:id_num>/<int:app_id>/rejectApplicant', views.CandidateReject, name='CandidateReject'),

    path('candidate/home/<slug:name>/post/view/all', views.PostViewCandidateAll, name = 'CandidateViewAll'),
    path('candidate/home/<slug:name>/post/view/active', views.PostViewCandidateActive, name = 'CandidateViewActive'),
    path('candidate/home/<slug:name>/post/view/inactive', views.PostViewCandidateInactive, name = 'CandidateViewInactive'),
    path('candidate/home/<slug:name>/post/view/search/description', views.PostViewCandidateSearchDescription, name = 'CandidateSearchDescription'),
    path('candidate/home/<slug:name>/post/view/search/zipcode', views.PostViewCandidateSearchZipCode, name = 'CandidateSearchZipcode'),



    path('candidate/home/<slug:name>/post/<int:id_num>/apply', views.CandidateApply, name = 'CandidateApply'),
    path('candidate/home/<slug:name>/post/<int:id_num>/unapply', views.CandidateRemoveApplication, name = 'CandidateUnapply'),
    path('candidate/home/<slug:name>/post/<int:id_num>/hide', views.CandidateHideActivePost, name = 'CandidateHide'),

    path('candidate/home/<slug:name>/offer/view', views.CandidateViewOffer,name='OfferView'),
    path('candidate/home/<slug:name>/offer/<int:id_num>/reject', views.CandidateOfferReject, name='CandidateOfferReject'),
    path('candidate/home/<slug:name>/offer/<int:id_num>/accept', views.CandidateOfferAccept, name='CandidateOfferAccept'),

    path('candidate/home/<slug:name>/application/view', views.CandidateViewApplication, name = 'ApplicationView'),
   
    
]