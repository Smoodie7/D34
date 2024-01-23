from flask import Blueprint, render_template, send_from_directory,request

bp = Blueprint("main", __name__, static_folder='app')

def get_website_info(website_name):
    website_name_mapping = {
        'sluttyleaks': "SluttyLeaks",
        'nsfwvids': "NSFWVids"
    }

    formatted_name = website_name_mapping.get(website_name.lower(), website_name.capitalize())
    return formatted_name

@bp.route("/home")
@bp.route("/")
def home():
    default_website_name = "sluttyleaks"  # Default value in case the URL parameter is not provided
    requested_website_name = request.args.get('website_name', default_website_name)

    website_name = get_website_info(requested_website_name)
    logo_path = f"assets/png/logo/{requested_website_name.lower()}-logo.png"

    return render_template("index.html", website_name=website_name, logo_path=logo_path)

# Others
@bp.route('/robots.txt')
def static_from_root():
    return send_from_directory(bp.static_folder, 'robots.txt')

