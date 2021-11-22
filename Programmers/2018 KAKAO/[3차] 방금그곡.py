def solution(m, musicinfos):
    def get_playing_time():
        start_m = int(start[:2]) * 60 + int(start[3:5])
        end_m = int(end[:2]) * 60 + int(end[3:5])
        return end_m - start_m

    def replace_sharp(temp_music):
        result = temp_music
        for sharp_note, small_letter in sharp_notes.items():
            result = result.replace(sharp_note, small_letter)
        return result

    def match_melody():
        music_len = len(music)
        total_music = music * (playing_time // music_len + 1)
        total_music = total_music[:playing_time]
        if total_music.find(m) == -1:
            return False
        else:
            return True

    sharp_notes = {'C#': 'c',
                   'D#': 'd',
                   'F#': 'f',
                   'G#': 'g',
                   'A#': 'a'}

    answer = "(None)"
    max_length = 0
    for music_info in musicinfos:
        start, end, title, music = music_info.split(',')
        playing_time = get_playing_time()
        m = replace_sharp(m)
        music = replace_sharp(music)
        if match_melody() and max_length < playing_time:
            max_length = playing_time
            answer = title

    return answer
