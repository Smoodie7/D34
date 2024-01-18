from flask import render_template

def register_error_handlers(app):
    # Register error handlers dynamically
    for code in [404, 500, 400, 401, 403, 405]:
        app.register_error_handler(code, lambda e, code=code: render_error_template(code))

def render_error_template(code):
    return render_template("errors.html", error_code=f"{code}: {error_messages.get(code, 'Unknown error')}")

error_messages = {
    404: "Not Found",
    500: "Internal Server Error",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    405: "Method Not Allowed"
}
