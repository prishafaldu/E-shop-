from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm ,MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),


    
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('profile/', views.profile, name='profile'),
    
    # path('changepassword/', views.change_password, name='changepassword'),
     path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('checkout/', views.checkout, name='checkout'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
    path('serum/', views.serum, name='serum'),
    path('serum/<slug:data>', views.serum, name='serumdata'),


    path('livingroom/', views.livingroom, name='livingroom'),
    path('livingroom/<slug:data>', views.livingroom, name='livingroomdata'),

    path('kitchen/', views.kitchen, name='kitchen'),
    path('kitchen/<slug:data>', views.kitchen, name='kitchendata'),

    path('decor/', views.decor, name='decor'),
    path('decor/<slug:data>', views.decor, name='decordata'),


    path('headphone/', views.headphone, name='headphone'),
    path('headphone/<slug:data>', views.headphone, name='headphonedata'),


    path('facewash/', views.facewash, name='facewash'),
    path('facewash/<slug:data>', views.facewash, name='facewashdata'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name="password_reset_complete"),

    # path('login/', views.login, name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    
    path('Bottom Wear/', views.bottomwear, name='bottomwear'),
    path('Bottom Wear/<slug:data>', views.bottomwear, name='bottomweardata'),


    path('Top Wear/', views.topwear, name='topwear'),
    path('Top Wear/<slug:data>', views.topwear, name='topweardata'),

    path('search/', views.search, name='search'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
