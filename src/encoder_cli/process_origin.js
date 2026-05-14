const crypto = require('crypto');
const Jm = {
    MD5: (str) => {
        return crypto.createHash("md5").update(String(str)).digest("hex");
    }
};

var Wm = ["a", "b", "e", "g", "h", "i", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w"];

var lv = {
    a: function(e, t, n) {
        return ov(e, t - 1, n)
    },
    b: function(e, t, n) {
        return ov(e, t - 2, n)
    },
    c: function(e, t, n) {
        return ov(e, t - 3, n)
    },
    d: function(e, t, n) {
        return ov(e, t - 4, n)
    },
    e: function(e, t, n) {
        return ov(e, t - 5, n)
    },
    f: function(e, t, n) {
        return ov(e, t, n)
    },
    g: function(e, t, n) {
        return ov(e, t + 1, n)
    },
    h: function(e, t, n) {
        return ov(e, t + 2, n)
    },
    i: function(e, t, n) {
        return ov(e, t + 3, n)
    },
    j: function(e, t, n) {
        return ov(e, t + 4, n)
    },
    k: function(e, t, n) {
        return ov(e, t + 5, n)
    },
    l: function(e, t, n) {
        return ov("/".concat(e, "/"), t - 1, n)
    },
    m: function(e, t, n) {
        return ov("/".concat(e, "/"), t - 2, n)
    },
    w: function() {
        return new Date
    },
    n: function(e, t, n) {
        return ov("/".concat(e, "/"), t - 3, n)
    },
    o: function(e, t, n) {
        return ov("/".concat(e, "/"), t - 4, n)
    },
    p: function(e, t, n) {
        return ov("/".concat(e, "/"), t - 5, n)
    },
    q: function(e, t, n) {
        return ov("/".concat(e, "/"), t, n)
    },
    r: function(e, t, n) {
        return ov("/".concat(e, "/"), t + 1, n)
    },
    s: function(e, t, n) {
        return ov("/".concat(e, "/"), t + 2, n)
    },
    t: function(e, t, n) {
        return ov("/".concat(e, "/"), t + 3, n)
    },
    u: function(e, t, n) {
        return ov("/".concat(e, "/"), t + 4, n)
    },
    v: function(e, t, n) {
        return ov("/".concat(e, "/"), t + 5, n)
    }
};

function Vm(e) {
    return 128 & e ? 255 & (e << 1 ^ 27) : e << 1
}
function qm(e) {
    return Vm(e) ^ e
}
function $m(e) {
    return qm(Vm(e))
}
function Ym(e) {
    return $m(qm(Vm(e)))
}
function Gm(e) {
    return Ym(e) ^ $m(e) ^ qm(e)
}

function Km(e) {
    var t = [0, 0, 0, 0];
    return t[0] = Gm(e[0]) ^ Ym(e[1]) ^ $m(e[2]) ^ qm(e[3]),
    t[1] = qm(e[0]) ^ Gm(e[1]) ^ Ym(e[2]) ^ $m(e[3]),
    t[2] = $m(e[0]) ^ qm(e[1]) ^ Gm(e[2]) ^ Ym(e[3]),
    t[3] = Ym(e[0]) ^ $m(e[1]) ^ qm(e[2]) ^ Gm(e[3]),
    e[0] = t[0],
    e[1] = t[1],
    e[2] = t[2],
    e[3] = t[3],
    e
}

function Nm(e) {
    return (Nm = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
        return typeof e
    }
    : function(e) {
        return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
    }
    )(e)
}

function Fm(e) {
    var t = function(e, t) {
        if ("object" !== Nm(e) || null === e)
            return e;
        var n = e[Symbol.toPrimitive];
        if (void 0 !== n) {
            var r = n.call(e, t);
            if ("object" !== Nm(r))
                return r;
            throw new TypeError("@@toPrimitive must return a primitive value.")
        }
        return ("string" === t ? String : Number)(e)
    }(e, "string");
    return "symbol" === Nm(t) ? t : String(t)
}

function Hm(e, t, n) {
    return (t = Fm(t))in e ? Object.defineProperty(e, t, {
        value: n,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : e[t] = n,
    e
}

function rv(e, t) {
    (null == t || t > e.length) && (t = e.length);
    for (var n = 0, r = new Array(t); n < t; n++)
        r[n] = e[n];
    return r
}

function iv(e) {
    return function(e) {
        if (Array.isArray(e))
            return rv(e)
    }(e) || function(e) {
        if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
            return Array.from(e)
    }(e) || function(e, t) {
        if (e) {
            if ("string" == typeof e)
                return rv(e, t);
            var n = Object.prototype.toString.call(e).slice(8, -1);
            return "Object" === n && e.constructor && (n = e.constructor.name),
            "Map" === n || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? rv(e, t) : void 0
        }
    }(e) || function() {
        throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
    }()
}

function av(e, t, n) {
    for (var r = "", i = t.slice(0, n), o = 0; o < e.length; o++)
        r += i[e.charCodeAt(o) % i.length];
    return r
}

function sv(e, t) {
    for (var n = "", r = 0; r < e.length; r++)
        n += t[e.charCodeAt(r) % t.length];
    return n
}

function ov(e, t, n) {
    e = "/".concat(e.split("/").filter(function(e) {
        return e
    }).join("/"), "/");
    var r = "AB45STUVWZEFGJ6CH01D237IXYPQRKLMN89"
      , i = function(e) {
        for (var t = "", n = function(n) {
            e.forEach(function(e) {
                n < e.length && (t += e[n])
            })
        }, r = 0; r < Math.max.apply(Math, iv(e.map(function(e) {
            return e.length
        }))); r++)
            n(r);
        return t
    }([av(String(t), r, -2), sv(e, r), sv(n, r)]).slice(0, 20)
      , o = (0,
    Jm.MD5)(i).toString()
      , a = "".concat(Km(o.slice(-6).split("").map(function(e) {
        return e.charCodeAt()
    })).reduce(function(e, t) {
        return e + t
    }, 0) % 100);
    a = a.length < 2 ? "0".concat(a) : a;
    var s = av(o.substring(0, 5), r, -4);
    return "".concat(s).concat(a)
}


function vv(e) {
    var t, n, r, i = Wm[3];
    return t = ~~(+lv.w() / 1e3),
    r = (0,
    Jm.MD5)(t + Math.random((new Date).getTime()).toString()).toString().toLocaleUpperCase(),
    n = lv[i](e, t, r),
    Hm(Hm(Hm({}, "".concat(Wm[4], "k").concat(Wm[2], "y"), n), "_".concat(Wm[13]).concat(Wm[5]).concat(Wm[6]).concat(Wm[2]), t), "".concat(Wm[7]).concat(Wm[8]).concat(Wm[7], "c").concat(Wm[2]), r)
}

function getKeys(path) {
    return vv(path);
}








