from chalice import Chalice

from medicines.application.controller.routes import medicine_crud_routes

app = Chalice(app_name="medicine_crud")
app.register_blueprint(medicine_crud_routes)
