def parse_video_id(video_id):
    """
    Parses the video ID from the provided URL.
    Returns the first character, six numbers combination, and six characters after the dash.
    """

    # Input Validation
    if not isinstance(video_id, str) or len(video_id) < 14:
        raise ValueError("Invalid video ID format: Video ID must be at least 14 characters long")

    # Extract the components of the video ID
    category = video_id[0]
    release_date = video_id[1:7]
    
    # Find the dash
    dash_index = video_id.find('-')
    if dash_index == -1 or dash_index + 6 == len(video_id):
        raise ValueError("Invalid video ID format: Missing dash or insufficient characters after dash")
    
    # Extract special_id
    special_id = video_id[dash_index + 1:dash_index + 7]

    return category, release_date, special_id

