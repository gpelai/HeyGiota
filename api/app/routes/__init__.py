from .bills import bp as bills_bp
from .health import bp as health_bp
from .savings import bp as saving_bp


def register_blueprint(app):
    app.register_blueprint(saving_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(bills_bp)
