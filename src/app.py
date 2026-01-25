from chalice import Chalice

from medicines.infrastructure.controller.routes import medicine_routes

app = Chalice(app_name="medicines")
app.register_blueprint(medicine_routes)
