from api.app.analytics.views import AnalyticsApi
#importar todas las rutas aqui

def initialize_routes(api):
    api.add_resource(AnalyticsApi, '/analy')



