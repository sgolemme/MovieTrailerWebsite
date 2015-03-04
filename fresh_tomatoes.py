import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>2015 Oscars</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        .navbar-inverse {
            background-color: #CFB53B;
            border-color: #DAA520;
            background-image: -webkit-linear-gradient(top,#CFB53B 0,#DAA520 100%);
            background-image: linear-gradient(to bottom,#CFB53B 0,#DAA520 100%);
        }
        .navbar-inverse .navbar-brand, .navbar-inverse .navbar-nav>li>a {
            text-shadow: none;
            color: white;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            height:580px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .winner.movie-tile {
            background: rgba(207, 181, 59, 0.5);
            cursor: pointer;
        }
        .winner.movie-tile:hover {
            background: rgba(207, 181, 59, 0.75);
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        small {
          font-style: italic;
          margin: 0 20px 10px;
        }
        h3 {
          margin-bottom: 0;
        }
        p {
          margin: 0 20px 10px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <span class="navbar-brand">2015 Oscar Winners and Nominees</span>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single category html template
category_content = '''
<div class="col-md-12 category">
  <h2>{categoryN}</h2>
  {category_nominees}
</div>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center {winner}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{image_url}" width="220" height="342">
    <h3>{nominee_name}</h3>
    {additional_info}
</div>
'''

def create_category_nominees(category):
  #The HTML content for this section of the page
  content = ''
  for nominee in category.nominees:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', nominee.video)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', nominee.video)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        #highlight the winners in each category
        winner = ''
        if nominee.winner:
          winner='winner'

        #Builds the extra info for each class
        additional=''
        if nominee.__class__.__name__ == "Movie":
          additional += "<small>"+nominee.producers+"</small>"
          additional += "<br/><br/>"
          additional += "<p>" + nominee.synopsis + "</p>"
        else:
          additional += "<small>"+nominee.history+"</small>"
          additional += "<br/><br/>"
          additional += nominee.role+"<br/>"
          additional += "<small>" + nominee.film + "</small>"

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            nominee_name=nominee.name,
            image_url=nominee.picture,
            trailer_youtube_id=trailer_youtube_id,
            winner=winner,
            additional_info=additional
        )
  return content

def create_movie_tiles_content(categories):
    # The HTML content for this section of the page
    content = ''

    #Create a new section for category with the category title
    for category in categories:
      #Append each individual nominee in a category
      content += category_content.format(
        categoryN = category.categoryName, 
        category_nominees = create_category_nominees(category))
    return content

def open_movies_page(categories):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(categories))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
