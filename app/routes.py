from flask import Blueprint, render_template, send_from_directory, request, jsonify, abort
from app.video_manager import parse_video_id
import os, subprocess

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

    video_data = {
        'new_category_title': 'NEW',
        'quality_category_title': 'HD',
        'time_category_title': '12:34',
        'video_title': 'Video title Video',
        'times_ago': '6 hours ago',
        'views_amount': '12,000 views'
    }

    return render_template("index.html", website_name=website_name, logo_path=logo_path, **video_data)


@bp.route('/watch')
def video_link_handler():
    """
    Handles video requests
    """
    video_id = request.args.get('v')  # Get the value of 'v' from the query parameters
    if video_id is None:
        abort(404)

    try:
        # Parse the video ID
        video_principal_category, video_release_date, video_special_id = parse_video_id(video_id)
        print(video_principal_category, video_release_date, video_special_id)
        if not os.path.exists(f"videos/{video_principal_category}/{video_release_date}/{video_special_id}/video.webm"):
            abort(404)

        print(f"Principal Category: {video_principal_category}, Release Date: {video_release_date}, Special ID: {video_special_id}")
        return render_template('watch.html', principal_category=video_principal_category, release_date=video_release_date, special_id=video_special_id)
    except ValueError as e:
        print("Error:", e)
        abort(404)


@bp.route('/onlyleaks.html')
def onlyleaks():
    return render_template('onlyleaks.html')


# Others
@bp.route('/robots.txt')
def static_from_root():
    return send_from_directory(bp.static_folder, 'robots.txt')

