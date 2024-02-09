def parse_video_id(video_id):
    """
    Parses the video ID from the provided URL.
    
    Video ID format: [category][release_date]-[special_id]
    Returns the category, release date (6 characters), and special ID (6 characters).
    """
    if not isinstance(video_id, str) or len(video_id) < 14:
        raise ValueError("Invalid video ID format: Video ID must be at least 14 characters long")

    # Extract the components of the video ID
    category, release_date, special_id = video_id[0], video_id[1:7], None
    
    # Find the dash and extract special_id
    dash_index = video_id.find('-')
    if dash_index == -1 or dash_index + 7 > len(video_id):
        raise ValueError("Invalid video ID format: Missing dash or insufficient characters after dash")
    special_id = video_id[dash_index + 1:dash_index + 7]

    return category, release_date, special_id
