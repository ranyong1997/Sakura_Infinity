from django.contrib.auth.mixins import LoginRequiredMixin


class LoginMixin(LoginRequiredMixin):
    """
    没登录跳转到登录页面
    """
    login_url = 'login'
