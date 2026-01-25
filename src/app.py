from chalice import Chalice

from medicine_crud.application.controller.routes import medicine_crud_routes

app = Chalice(app_name="medicine_crud")
app.register_blueprint(medicine_crud_routes)
