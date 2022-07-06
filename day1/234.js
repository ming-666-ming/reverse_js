function getApiKey(){
    var e = (new Date).getTime() // 时间戳
        // 对应的三个方法
        , t = encryptApiKey();
    return e = encryptTime(e),
        comb(t, e) // comb t | e
}

function encryptApiKey() {
        var e = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
          , t = e.split("") // 8个之后的 -b31e-4547-9299-b6d07b7631ab
          , o = t.splice(0, 8); // e前面的8个 a2c903cc
        return t.concat(o).join("") // t拼接了o   -b31e-4547-9299-b6d07b7631aba2c903cc
}

function encryptTime(e) {
    // 时间戳 t = 1 * 时间戳 + 1111111111111
        var t = (1 * e + 1111111111111).toString().split("")
            // parseInt => int  o r n 随机数
          , o = parseInt(10 * Math.random(), 10)
          , r = parseInt(10 * Math.random(), 10)
          , n = parseInt(10 * Math.random(), 10);
        return t.concat([o, r, n]).join("") //  t
}


function comb(e, t) {
  var o = "".concat(e, "|").concat(t);
  // 处理 base64 处理
  return o
}


// console.log(getApiKey())


