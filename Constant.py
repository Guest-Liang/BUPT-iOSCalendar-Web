#个人信息Personal Information
SchoolID=''
Password_jwgl=''

#用于登录的URL以及UA
USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.0.0'
LOGIN_URL='https://jwgl.bupt.edu.cn/jsxsd/'
GET_API='https://jwgl.bupt.edu.cn/jsxsd/xskb/xskb_list.do'
POST_URL='https://jwgl.bupt.edu.cn/jsxsd/xk/LoginToXk'
KBJCMSID={
    '0':'9475847A3F3033D1E05377B5030AA94D', #默认节次模式
    '1':'857D7D63586B4AF4B4C59B1DFEEB56E4' #海南校区课表时间
} #由[https://jwgl.bupt.edu.cn/jsxsd/framework/xsMain.jsp]的html代码得到的'课表节次模式id'

KBLB={
    '0':'kckb', #课程课表
    '1':'tzdkb' #通知单课表
} #由[https://jwgl.bupt.edu.cn/jsxsd/framework/xsMain.jsp]的html代码得到的'课表类别'

#教务系统加密算法，由[https://jwgl.bupt.edu.cn/jsxsd/framework/xsMain.jsp]得到
KEYSTRING="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
CONWORK_JS='''
eval(function (p, a, c, k, e, d)
{
    e = function (c){return (c < a ? "": e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))};
    if (!''.replace(/^/, String))
    {
        while (c--) d[e(c)] = k[c] || e(c);
        k = [function (e){return d[e]}];
        e = function() {return '\\w+'};
        c = 1;
    };
    while (c--) if (k[c]) p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
    return p;
} ('b 9="o+/=";p q(a){b e="";b 8,5,7="";b f,g,c,1="";b i=0;m{8=a.h(i++);5=a.h(i++);7=a.h(i++);f=8>>2;g=((8&3)<<4)|(5>>4);c=((5&s)<<2)|(7>>6);1=7&t;k(j(5)){c=1=l}v k(j(7)){1=l}e=e+9.d(f)+9.d(g)+9.d(c)+9.d(1);8=5=7="";f=g=c=1=""}u(i<a.n);r e}', 32, 32, '|enc4||||chr2||chr3|chr1|keyStr|input|var|enc3|charAt|output|enc1|enc2|charCodeAt||isNaN|if|64|do|length|ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789|function|encodeInp|return|15|63|while|else'.split('|'), 0, {}));
'''

#很明显是eval加密，解压一下就得到原始js代码
CONWORK_JS_DECODED='''
var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

function encodeInp(input) {
	var output = "";
	var chr1, chr2, chr3 = "";
	var enc1, enc2, enc3, enc4 = "";
	var i = 0;
	do {
		chr1 = input.charCodeAt(i++);
		chr2 = input.charCodeAt(i++);
		chr3 = input.charCodeAt(i++);
		enc1 = chr1 >> 2;
		enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
		enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
		enc4 = chr3 & 63;
		if (isNaN(chr2)) {
			enc3 = enc4 = 64
		} else if (isNaN(chr3)) {
			enc4 = 64
		}
		output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2) + keyStr.charAt(enc3) + keyStr.charAt(enc4);
		chr1 = chr2 = chr3 = "";
		enc1 = enc2 = enc3 = enc4 = ""
	} while (i < input.length);
	return output
}
'''

#referer_get_api='https://jwgl.bupt.edu.cn/jsxsd/framework/xsMain.jsp'
#userAccount_xpath='/html/body/div/div[2]/div[3]/form/ul[1]/li[2]/input' #由LOGIN_API的html代码得到
#userPassword_xpath='/html/body/div/div[2]/div[3]/form/ul[1]/li[3]/input' #由LOGIN_API的html代码得到