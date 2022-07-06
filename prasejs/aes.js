            var getQueryString = function(name) {
                var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
                var r = window.location.search.substr(1).match(reg);
                if (r != null) return unescape(r[2]);
                return null;
            };

			var seed = decodeURIComponent(getQueryString("seed")) || "";
            var ts = getQueryString("ts");
            var fileName = getQueryString("name");

			var expiredate = new Date().getTime() + 32 * 60 * 60 * 1000 * 2;
			var code = "";
			var ABC = window.ABC || frame.contentWindow.ABC;
			try {
				//code = new ABC().z(seed, parseInt(ts)+(480+new Date().getTimezoneOffset())*60*1000);
				code = new ABC().z(seed, parseInt(ts));//+(480+new Date().getTimezoneOffset())*60*1000 时区相对于北京的偏移
			} catch (e) {}
			if (code ) Cookie.set("__zp_stoken__", code, expiredate, COOKIE_DOMAIN, "/"); //该方法会做一次 encodeURIComponent

