# MusicalMusic v0.1.2

## __init__(username, password)

Creates your instance using your Musescore account.

## MusicalMusic.search(query)

Searches MuseScore for a query.  
Returns <span class="inline">list</span>

    import MusicalMusic

    result = MyInstance.search("radioactive")
    print(result)

Output:

    [{'id': '3924896', 'title': 'Radioactive- Imagine Dragons', 'instruments': 'Piano', 'duration': '03:29'}, {'id': '3783076', 'title': 'Imagine dragons Radioactive', 'instruments': 'Piano', 'duration': '03:24'}, {'id': '3260776', 'title': 'Radioactive', 'instruments': 'Violin(2)', 'duration': '03:28'}, {'id': '4636696', 'title': 'Imagine dragons - Radioactive (lead sheet)', 'instruments': 'Piano', 'duration': '02:16'}, {'id': '4874647', 'title': 'Radioactive by Imagine Dragons ~ Arrangement for Vocals and Piano', 'instruments': 'Voice, Piano', 'duration': '03:32'}, {'id': '1597251', 'title': 'Radioactive Saxophone Duet', 'instruments': 'Tenor Saxophone, Baritone Saxophone', 'duration': '00:50'}, {'id': '3404976', 'title': 'Radioactive', 'instruments': 'Violin, Cello', 'duration': '03:30'}, {'id': '4038706', 'title': 'Radioactive - Imagine Dragons (AJ)', 'instruments': 'Piano', 'duration': '03:12'}, {'id': '2882516', 'title': 'Radioactive Imagine Dragons Marching Band Stand Tune (11/30 Edit)', 'instruments': 'Flute, Clarinet, Alto Saxophone, Trumpet, French Horn, Tenor Saxophone, Tuba(2), Trombone, Percussion(4)', 'duration': '01:22'}, {'id': '1715766', 'title': 'Linsey Stirling Radioactive', 'instruments': 'Violin', 'duration': '03:12'}, {'id': '666506', 'title': 'Roar Brave Radioactive Mashup A capella', 'instruments': 'Piano(3)', 'duration': '02:28'}, {'id': '3560061', 'title': 'Radioactive', 'instruments': 'Trumpet, Trombone, Piano, Guitar', 'duration': '02:57'}, {'id': '2231936', 'title': 'Radioactive (Paul Murtha)', 'instruments': 'Flute, Piccolo, Clarinet, Alto Saxophone, Tenor Saxophone, Trumpet(2), French Horn, Trombone, Tuba(2), Baritone Saxophone, Bass, Percussion(8)', 'duration': '01:58'}, {'id': '1262546', 'title': 'Radioactive Trumpet Trio', 'instruments': 'Trumpet(3)', 'duration': '02:20'}, {'id': '2764146', 'title': 'Radioactive', 'instruments': 'Piano, Trumpet, Trombone, French Horn, Tuba(2), Flute, Clarinet, Soprano Saxophone, Alto Saxophone, Tenor Saxophone, Baritone Saxophone', 'duration': '03:17'}, {'id': '4870557', 'title': 'Imagine Dragons - Radioactive', 'instruments': 'Piano', 'duration': '03:01'}, {'id': '3648286', 'title': 'Radioactive Imagine Dragons', 'instruments': 'Violin(2), Piano(2)', 'duration': '03:01'}, {'id': '4053766', 'title': 'Radioactive - Imagine Dragons', 'instruments': 'Piano', 'duration': '03:24'}, {'id': '3324526', 'title': 'Radioactive by Imagine Dragons', 'instruments': 'Tenor Saxophone, Alto Saxophone, Trombone(3), Percussion', 'duration': '03:30'}, {'id': '4837679', 'title': 'Radioactive', 'instruments': 'Piano', 'duration': '03:24'}]

## download(id, filename, extension="mp3")

Downloads Musescore file using its ID.  
**id**: The ID of the MuseScore song.  
**filename**: The filename to save the file as (include extension).  
**extension**: The file format to download. Supports mp3, pdf, mid, xml, and mscz.

    import MusicalMusic

    MyInstance = MusicalMusic.MusicalMusic("xX_Username_Xx","Password123")
    query = input("What's your favourite song? ")
    results = MusicalMusic.search(query)
    song = results[0]

    id = song["id"]
    title = song["title"]
    instruments = song["instruments"]
    duration = song["duration"]

    MyInstance.download(id, "song.mp3")

    print(f'''Title: {title}
    Duration: {duration}
    Instruments: {instruments}
    ''')

Output:

    What's your favourite song? radioactive
    Title: Radioactive- Imagine Dragons
    Duration: 03:29
    Instruments: Piano

## retrieve(id, extension="mp3")

Returns Musescore file using its ID  
**id**: The ID of the MuseScore song.  
**extension**: The file format to retrieve. Supports mp3, pdf, mid, xml, and mscz.  
Returns <span class="inline">bytes</span>
