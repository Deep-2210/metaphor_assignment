from django.shortcuts import render
from metaphor_python import Metaphor
from .models import MusicPiece

def generate_music(request):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'

    try:
        metaphor = Metaphor("9105eac0-2cf8-4264-8b2f-11245109f27b")
    except Exception as e:
        return render(request, 'music_generator/error.html', {'error_message': str(e)})

    if request.method == 'POST':
        # Get the description of the music piece from the form
        description = request.POST.get('description', '')
        description = description+' youtube link'

        try:
            # Generate the music piece using the Metaphor API
            music_piece = metaphor.search(description, num_results=1, use_autoprompt=True)

        except Exception as e:
            # Render the error template with the error message
            return render(request, 'music_generator/error.html', {'error_message': str(e)})

        if music_piece.results:
            # Extract the URL from the first result
            music_url = music_piece.results[0].url
        else:
            # Handle the case when there are no results
            music_url = ''

        # Save the generated music piece to the database
        MusicPiece.objects.create(description=description, music_notes=music_url)

        # Retrieve all generated music pieces from the database
    music_pieces = MusicPiece.objects.all()

    return render(request, 'music_generator/generate_music.html', {'music_pieces': music_pieces})
