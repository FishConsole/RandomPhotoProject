@main.route('/baidu_verify_codeva-b8U4HkFtUO.html')
def baidusearchtool():
    return '26b65257dc54a668432117dd10a11fc3'


@main.route('/sogousiteverification.txt')
def sougousearchtool():
    return '2BiIHwawrq'


@main.route('/robots.txt', methods=['GET'])
def robots():
    return 'User-agent: *'
