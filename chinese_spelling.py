def call_tts(entity_id, message, delay):
    hass.services.call(
            'tts',
            'google_translate_say',
            {
                'entity_id': entity_id,
                'message': message,
                'language': "zh-cn",
            },
            blocking=True,
            limit=10,
        )
    time.sleep(delay)


def read_sentences_with_tts(pinyin, sentences, entity_id='media_player.ke_ting_speaker', delay=2):
    """Read a list of sentences with Google TTS."""
    random.shuffle(sentences)
    random.shuffle(pinyin)
    start_msg = f"Hello! It's time for spelling. Please get ready with your pencil and paper. We will now begin"
    end_msg = "Spelling has ended. Please ask 爸爸 to check your answers"
    words = []
    call_tts(entity_id, start_msg, 10)

    for item in pinyin:
        spelling_msg = f'{item}. 请写 {item} 的拼音'
        call_tts(entity_id, spelling_msg, 15)

    for sentence in sentences:
        spelling_msg = f'{sentence}. 请写 {sentence} 的中文字'
        call_tts(entity_id, spelling_msg, 15)

    call_tts(entity_id, end_msg, 10)

    time.sleep(5)
    call_tts(entity_id, "Thank you for spelling with Google", 10)

def main():
    pinyin = data.get("pinyin")
    sentences = data.get("sentences")
    delay = data.get("delay")
    entity = data.get("entity_id")
    read_sentences_with_tts(pinyin, sentences, entity_id=entity, delay=delay)

# Execute the script
main()