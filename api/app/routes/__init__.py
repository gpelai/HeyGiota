from .bills import bp as bills_bp
from .investments import bp as investments_bp
from .health import bp as health_bp


def register_blueprint(app):
    app.register_blueprint(investments_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(bills_bp)
