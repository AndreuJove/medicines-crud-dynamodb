import json

from chalice import Blueprint

from src.logging_config import logger

medicine_crud_routes = Blueprint(__name__)


@medicine_crud_routes.route("/", methods=["GET"])
def get_users():
    logger.info("Called endpoint health")
    return {
        "status": "healthy",
        "version": "1.0.0",
    }


@medicine_crud_routes.route("/users/{userId}", methods=["GET"])
def get_user(userId: str):
    return {"statusCode": 200, "body": json.dumps(f"The user id recieved is: {userId}")}
