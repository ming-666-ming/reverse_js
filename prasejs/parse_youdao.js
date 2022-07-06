function e() {
    return Math.floor(65536 * (1 + Math.random())).toString(16).substring(1)
}

function t(e) {
                var t = e.match(/[\d]+/g);
                return t.length = 3,
                t.join(".")
            }

// define("newweb/common/service/utils", ["./utils", "./md5", "./jquery-1.7"], function(e, t) {
//     var n = e("./jquery-1.7");
//     e("./utils");
//     e("./md5");
//     var r = function(e) {
//         var t, r, i;
//         t = n.md5(2.1);
//         r = "" + (new Date).getTime();
//         i = r + parseInt(10 * Math.random(), 10);
//         return {
//             ts: r,
//             bv: t,
//             salt: i,
//             sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
//         }
//     }
    function r(e) {
        var t, r, i;
        // t = n.md5(navigator.appVersion); //加密版本
        r = "" + (new Date).getTime();
        i = r + parseInt(10 * Math.random(), 10);
        console.log("fanyideskweb" + "newweb/common/service/utils"+ 16539718893708 + "Ygy_4c=r#e#4EX^NUGUc5");
        // console.log(i);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
        }}
        function n(e) {
                return !!e && (e = e.toLowerCase()) && (/^(pepflashplayer\.dll|libpepflashplayer\.so|pepperflashplayer\.plugin)$/.test(e) || "chrome.plugin" === e.slice(-13))
            }
        r(e())