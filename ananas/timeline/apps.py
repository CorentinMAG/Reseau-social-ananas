from django.apps import AppConfig


class TimelineConfig(AppConfig):
    name = 'timeline'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Article'))
        registry.register(self.get_model('Commentaires'))
