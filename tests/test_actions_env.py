from config.base_settings import project_settings


def test_show_env():
    qwe = project_settings.api.operators.user_name
    print(qwe)
    assert qwe == 'andkor_oper1@gmail.com'
