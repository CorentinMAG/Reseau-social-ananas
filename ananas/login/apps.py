from django.apps import AppConfig


class LoginConfig(AppConfig):
    name = 'login'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('CustomUser'))
