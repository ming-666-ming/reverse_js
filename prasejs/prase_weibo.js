 function getData() {
                    var t = this
                      , e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 0
                      , i = arguments.length > 1 && void 0 !== arguments[1] && arguments[1];
                    this.isLoading = !0,
                    this.isRetry = !1;
                    var a = "/ajax/statuses/mymblog";
                    0 === e ? this.searchParams.q && (a = "/ajax/profile/searchblog") : 3 === e ? a = "/ajax/statuses/likelist" : 2 === e && (a = "/ajax/profile/myhot");
                    var o = {
                        uid: this.owner_uid,
                        page: this.page,
                        feature: e,
                        since_id: this.since_id
                    };
                    0 === e && (o = Object(n["a"])(Object(n["a"])({}, o), this.searchParams)),
                    this.$http.get(a, {
                        params: o
                    }).then((function(a) {
                        if (a.data.ok > 0) {
                            var o = a.data.data
                              , n = o.list
                              , s = o.status_visible
                              , r = o.bottom_tips_visible
                              , c = o.bottom_tips_text
                              , l = o.since_id;
                            if (t.since_id = l,
                            i && window.scrollTo(0, 0),
                            t.data = t.data.concat(n),
                            r)
                                return t.isOver = !0,
                                t.isLoading = !1,
                                t.isNoData = !0,
                                t.noDataText = c || "博主设置仅展示半年内的微博",
                                0 === t.data.length && (t.emptyText = t.noDataText),
                                void (0 === t.data.length && (t.isEmpty = !0));
                            if (0 === n.length || -1 === +t.since_id) {
                                if (t.isOver = !0,
                                t.isLoading = !1,
                                t.showSkeleton = !1,
                                0 === t.data.length)
                                    t.isEmpty = !0;
                                else {
                                    if (s && !t.isOwner)
                                        return t.isNoData = !0,
                                        void (t.noDataText = "博主设置仅展示半年内的微博");
                                    t.isNoData = !0,
                                    t.noDataText = "没有更多内容了~去其他页面看看吧"
                                }
                                return
                            }
                            if (3 === e)
                                if (t.isOwner) {
                                    var u, d = Object(D["a"])(n);
                                    try {
                                        for (d.s(); !(u = d.n()).done; ) {
                                            var h = u.value;
                                            h.deleted && (h.deletedData = {
                                                type: "liked",
                                                text: "删除"
                                            })
                                        }
                                    } catch (p) {
                                        d.e(p)
                                    } finally {
                                        d.f()
                                    }
                                } else
                                    n.splice(n.findIndex((function(t) {
                                        return 1 === +t.deleted
                                    }
                                    )), 1);
                            if (t.page >= 2 && !t.config.isNormal)
                                return t.isNoData = !1,
                                t.showNotLoginBottom = !0,
                                void (t.isLoading = !1);
                            t.page++
                        }
                    }
                    )).catch((function(e) {
                        t.isLoading = !1,
                        t.isRetry = !0
                    }
                    ))
                }