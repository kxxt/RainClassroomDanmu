import danmu
from functools import partial
import traceback


def generate_custom_send_function_from_input():
    print('雨课堂弹幕发送程序: 要启动一个会话/Bot, 请先提供以下基本信息')
    cookies = input('请把 Cookie 粘贴在这里: ')
    lesson_id = input('请输入 Lesson ID: ')
    presentation_id = input('请输入 Presentation ID: ')
    return partial(danmu.send, cookies=cookies, lesson_id=lesson_id, presentation_id=presentation_id)


if __name__ == '__main__':
    send_it = generate_custom_send_function_from_input()
    while True:
        msg = input('请输入弹幕: ')
        ppt_num = input('(可选)输入发送弹幕时所在PPT号(不是PPT页码): ')
        if not msg:
            print('消息不能为空!')
            continue
        try:
            if ppt_num:
                rsp = send_it(msg=msg, ppt=ppt_num)
            else:
                rsp = send_it(msg=msg)
            if 'success' in rsp and rsp['success']:
                print(f'弹幕{rsp["danmuID"]}发送成功!')
            else:
                print(f'发送失败: 服务器回应: {rsp.json()}')
        except:
            traceback.print_exc()
