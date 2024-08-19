"""
@Author：dr34m
@Date  ：2024/8/16 13:52 
"""
from common.commonUtils import readOrSet

sysLanguage = None
allLng = {
    'zh_cn': {
        'success': '操作成功',
        'lost_part': '入参不全',
        'same_exists': '已存在相同数据，请检查！',
        'sign_in': '请登录',
        'login_expired': '登录失效',
        'user_not_found': '用户不存在',
        'log_del_success': '日志文件{}已被成功删除',
        'log_del_fail': '日志文件{}删除失败，原因为：{}',
        'log_rename_start': '日志定时更名任务启动成功',
        'keep_all_log': '日志保留时间为0，将保留所有日志',
        'clear_task_start': '定时清理任务启动成功',
        'passwd_wrong': '密码错误',
        'passwd_wrong_max_time': '5分钟内密码错误超过3次，请稍后再试'
    },
    'eng': {
        'success': 'success',
        'lost_part': 'Incomplete participation',
        'same_exists': 'The same data already exists, please check!',
        'sign_in': 'Please sign in',
        'login_expired': 'Login expired',
        'user_not_found': 'User does not exist',
        'log_del_success': 'The log file {} has been successfully deleted',
        'log_del_fail': 'Failed to delete log file {}, reason: {}',
        'log_rename_start': 'The log scheduled renaming task was started successfully',
        'keep_all_log': 'The log retention time is 0, all logs will be retained',
        'clear_task_start': 'The scheduled cleanup task was started successfully',
        'passwd_wrong': 'Wrong password',
        'passwd_wrong_max_time': 'The password was incorrect more than 3 times within 5 minutes. Please try again later'
    }
}


def language(lang=None):
    """
    获取或修改语言
    :param lang: 语言，不填为读取，否则是修改
    :return: 读取时为值，否则空
    """
    global sysLanguage
    fileName = 'data/language.txt'
    if lang is None:
        if sysLanguage is None:
            sysLanguage = readOrSet(fileName, 'zh_cn')
        return sysLanguage
    else:
        if lang not in allLng:
            raise Exception(f"no {lang}")
        sysLanguage = lang
        readOrSet(fileName, lang, True)


def G(params):
    """
    根据语言获取文字
    :param params: 文字关键字
    :return:
    """
    cu = allLng[language()]
    return cu[params]
