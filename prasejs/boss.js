var rip = getRandIP();
var record = 999;
var pid = "h9614n96f5@7f36ca53ae12344";
var pageview = uu()

function getTraceId() {
    var e = this.rip
        , t = Date.now()
        , r = getSortNum(record)
        , a = e + t + r + getRandNum(pid);
    console.log(a);
    return this["EagleEye-TraceID"] = a,
        record = r,
        {
            "EagleEye-TraceID": a
        }
}

function getUberTraceId(e) {
    var t = this.rip
    r = Date.now()
    a = getSortNum(record)
    i = getRandNum(pid)
    o = t + r + a + getNum(2) + i
    s = o.substring(0, 16);
    console.log(o);
    return e = e ? "1" : "0",
        {
            "uber-trace-id": o + ":" + s + ":0:" + e,
            traceId: o
        }
}

function getPageviewId() {
    return {
        "EagleEye-SessionID": pageview
    }
}


function getSortNum(e) {
    return e ? (e += 1) >= 1e3 && e <= 9999 ? e : e < 1e3 ? e + 1e3 : e % 1e4 + 1e3 : 1e3
}

function getRandNum(e) {
    return e && "string" == typeof e ? e.length < 5 ? getNum(5) : e.substring(e.length - 5) : getNum(5)
}

function getRandIP() {
    for (var e = [], t = 0; t < 4; t++) {
        var r = Math.floor(256 * Math.random());
        e[t] = (r > 15 ? "" : "0") + r.toString(16)
    }
    return e.join("").replace(/^0/, "1")
}


function getNum(e) {
    for (var t = [], r = 0; r < e; r++) {
        var n = Math.floor(16 * Math.random());
        t[r] = n.toString(16)
    }
    return t.join("")
}

function uu() {
    for (var e, t, r = 20, n = new Array(r), a = Date.now().toString(36).split(""); r-- > 0;)
        t = (e = 36 * Math.random() | 0).toString(36),
            n[r] = e % 3 ? t : t.toUpperCase();
    for (var i = 0; i < 8; i++)
        n.splice(3 * i + 2, 0, a[i]);
    return n.join("")
}

getTraceId();
// getUberTraceId();