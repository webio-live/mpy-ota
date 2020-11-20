from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    # token = "e3a13a733a72b224491edf0a3ebbe83011e43f55"
    # o = OTAUpdater('https://github.com/janoist1/webio-mpy',
    #                headers={'Authorization': 'token {}'.format(token)})
    o = OTAUpdater('https://github.com/webio-live/mpy-ota')

    o.using_network('.', 'Q1w2e3r4t5')
    o.download_updates_if_available()
    # o.download_and_install_update_if_available('.', 'Q1w2e3r4t5')


def start():
    print("start")


def boot():
    download_and_install_update_if_available()
    start()


boot()
