from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'demo.auth_'

    def ready(self):
        import demo.auth_.signals
