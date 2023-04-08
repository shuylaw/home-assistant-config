def call_tts(entity_id, message, delay):
    hass.services.call(
            'tts',
            'google_translate_say',
            {
                'entity_id': entity_id,
                'message': message,
            },
            blocking=True,
            limit=10,
        )
    time.sleep(delay)


def read_sentences_with_tts(sentences, entity_id='media_player.ke_ting_speaker', delay=2):
    """Read a list of sentences with Google TTS."""
    random.shuffle(sentences)
    start_msg = f"Hello! It's time for spelling. Please get ready with your pencil and paper. We will now begin"
    end_msg = "Spelling has ended. We will now check your answers"
    words = []
    call_tts(entity_id, start_msg, 10)

    for sentence in sentences:
        word, sent = sentence.split(".")
        words.append(word)
        spelling_msg = f'{word}. {sent}. Please spell the word {word}'
        call_tts(entity_id, spelling_msg, 15)

    call_tts(entity_id, end_msg, 10)

    for word in words:
        time.sleep(2)
        word_intro = f'{word} is spelled'
        call_tts(entity_id, word_intro, 4)
        for letter in word:
            call_tts(entity_id, letter, 1)

    time.sleep(5)
    call_tts(entity_id, "Thank you for spelling with Google", 10)

def main():
    sentences = data.get("sentences")
    delay = data.get("delay")
    entity = data.get("entity_id")
    read_sentences_with_tts(sentences, entity_id=entity, delay=delay)

# Execute the script
main()