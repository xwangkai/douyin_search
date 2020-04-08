import random

import frida
import sys
import time
import json


def on_message(message, data):
    print("[%s] => %s" % (message, data))


def start_hook():
    device = frida.get_usb_device(timeout=5)

    # 应用包名
    app_package_name = "com.ss.android.ugc.aweme"  # 抖音极速
    try:
        pid = device.spawn([app_package_name])
        device.resume(pid)
        time.sleep(1)  # 2
        session = device.attach(pid)
        print("[*] start hook")
        print(session)

        # 加载脚本
        with open("douyin.js", "r", encoding="utf-8") as file:
            js_code = file.read()
        script = session.create_script(js_code)
        script.on('message', on_message)
        script.load()
        return script
    except frida.NotSupportedError as e:
        print("请检查包名的有效性.", e)


if __name__ == '__main__':
    script = start_hook()

    args = script.exports.a(
        "https://api3-normal-c-lf.amemv.com/tfe/api/request_combine/v1/?oid=1&cpu_model=Qualcomm+MSM8974PRO-AC&source=1&follow_tab_position=1&longitude=null&second_tab_type=0&latitude=null&api_list=%2Faweme%2Fv1%2Fuser%2Fsettings%2F%2C%2Faweme%2Fv1%2Fcommerce%2Fsettings%2F%2C%2Faweme%2Fv1%2Fcompliance%2Fsettings%2F%2C%2Fwebcast%2Fsetting%2F%2C%2Faweme%2Fv2%2Fplatform%2Fshare%2Fsettings%2F%2C%2Faweme%2Fv1%2Fnotice%2Fcount%2F%2C%2Faweme%2Fv1%2Fsettings%2F%2C%2Faweme%2Fv1%2Fuser%2Fyellow_point%2F%2C%2Faweme%2Fv1%2Fabtest%2Fparam%2F%2C%2Faweme%2Fv1%2Fpoi%2Fsamecity%2Factive%2F&webcast_sdk_version=1460&webcast_locale=zh_CN&has_local_cache=1&os_api=23&device_type=MI%204LTE&device_platform=android&ssmix=a&iid=110943176729&manifest_version_code=100501&dpi=480&uuid=867323023216243&version_code=100500&app_name=aweme&cdid=3f512a4d-b8c6-41a9-8411-7d86b540ffb4&version_name=10.5.0&ts=1586333404&openudid=24a010888138aec&device_id=51790275446&resolution=1080*1920&os_version=6.0.1&language=zh&device_brand=Xiaomi&app_type=normal&ac=wifi&update_version_code=10509900&aid=1128&channel=xiaomi&_rticket=1586333404873")
    print(args)
    print("#################################")
    args = script.exports.a(
        "https://api3-normal-c-lf.amemv.com/tfe/api/request_combine/v1/?oid=1&cpu_model=Qualcomm+MSM8974PRO-AC&source=1&follow_tab_position=1&longitude=null&second_tab_type=0&latitude=null&api_list=%2Faweme%2Fv1%2Fuser%2Fsettings%2F%2C%2Faweme%2Fv1%2Fcommerce%2Fsettings%2F%2C%2Faweme%2Fv1%2Fcompliance%2Fsettings%2F%2C%2Fwebcast%2Fsetting%2F%2C%2Faweme%2Fv2%2Fplatform%2Fshare%2Fsettings%2F%2C%2Faweme%2Fv1%2Fnotice%2Fcount%2F%2C%2Faweme%2Fv1%2Fsettings%2F%2C%2Faweme%2Fv1%2Fuser%2Fyellow_point%2F%2C%2Faweme%2Fv1%2Fabtest%2Fparam%2F%2C%2Faweme%2Fv1%2Fpoi%2Fsamecity%2Factive%2F&webcast_sdk_version=1460&webcast_locale=zh_CN&has_local_cache=1&os_api=23&device_type=MI%204LTE&device_platform=android&ssmix=a&iid=110943176729&manifest_version_code=100501&dpi=480&uuid=867323023216243&version_code=100500&app_name=aweme&cdid=3f512a4d-b8c6-41a9-8411-7d86b540ffb4&version_name=10.5.0&ts=1586333404&openudid=24a010888138aec&device_id=51790275446&resolution=1080*1920&os_version=6.0.1&language=zh&device_brand=Xiaomi&app_type=normal&ac=wifi&update_version_code=10509900&aid=1128&channel=xiaomi&_rticket=1586333404873")
    print(args)
    input()
