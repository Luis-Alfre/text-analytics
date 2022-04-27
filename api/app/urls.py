from api.app.analytics.views import AnalyticsApi, AnalyticsApiPdf
#importar todas las rutas aqui

def initialize_routes(api):
    api.add_resource(AnalyticsApi, '/analytics/text')
    api.add_resource(AnalyticsApiPdf, '/analytics/pdf')



