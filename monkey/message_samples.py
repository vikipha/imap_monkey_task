BANANA_MESSAGE = (
    b"Received: from mail-yb1-xb35.google.com\r\n\t(mail-yb1-xb35.google.com [260"
    b"7:f8b0:4864:20::b35])\r\n\tby smtpd-mx-59d667b877-w2j8p (smtpd/2.0.17) with"
    b" ESMTP\r\n\tid 268edf02-8dcc-4cc3-a0f7-5a9e4c8ae216;\r\n\tThu, 18 Jan 2024"
    b" 12:07:55 +0100\r\nReceived: by mail-yb1-xb35.google.com with SMTP id 3f14"
    b"90d57ef6-dc21d7a7042so3389916276.2\r\n        for <viktor.lacina@seznam.cz"
    b">; Thu, 18 Jan 2024 03:07:55 -0800 (PST)\r\nDKIM-Signature: v=1; a=rsa-sha"
    b"256; c=relaxed/relaxed;\r\n        d=gmail.com; s=20230601; t=1705576073; "
    b"x=1706180873; darn=seznam.cz;\r\n        h=to:subject:message-id:date:from"
    b":mime-version:from:to:cc:subject\r\n         :date:message-id:reply-to"
    b";\r\n        bh=0xhOJL5K6biC8HSo0bfmtxUxI+wotNk/YZiF5LbJLSs=;\r\n       "
    b" b=kW6IyGiX7jjWzTHOGu8cESkI4eXwJYSI1eOhnIpsweDeAX/qB/JPypsCDNSLPTnwHg\r\n "
    b"        meFT92jcVaDMw0Eg0735dY+WnsQaRLYJdPSxuBQHdny1WWfGL57FcDcJbbphimf9"
    b"Le0N\r\n         WD3OgOM6cCIBH0+L7gAqJnTW12CQd6bZtkJFjuxGCT/5tYByJfzaV02iN"
    b"ryxxO5TIkOy\r\n         ZwUH5g/2Igmd1Z+3iruBUzXDq9dPZZLYxLyF4ZNDG/MXY1NDJj"
    b"aQ4FYRIbmFb5jnqD3y\r\n         L+XI3mkv1qtkwaVxfISP3jYqWH9dagUJEmPJc8ivhql"
    b"K5xKGCTLaBZsfP0CYCNvb5BHQ\r\n         8Lgw==\r\nX-Google-DKIM-Signature:"
    b" v=1; a=rsa-sha256; c=relaxed/relaxed;\r\n        d=1e100.net; s=20230601;"
    b" t=1705576073; x=1706180873;\r\n        h=to:subject:message-id:date:from:"
    b"mime-version:x-gm-message-state\r\n         :from:to:cc:subject:date:messa"
    b"ge-id:reply-to;\r\n        bh=0xhOJL5K6biC8HSo0bfmtxUxI+wotNk/YZiF5LbJLSs="
    b";\r\n        b=xLJOM91KTBEBrFVnKb8JBNPAhKPFB8NXmi3jcjaTgJqBkngRubE8uPZf28L"
    b"Xk13oLb\r\n         QbpdFR8EjuRCI+3vwcZjDljTYxKKXHo/y0BcNthUpzk1GiKd0J/aTB"
    b"YAqOtJ6rWkgXi8\r\n         bIpLfmRMJhfZfWPG2jGm9wmzBUCnvrq1vg2GVLYdvKd68ua"
    b"MEkQdnDAEO85W81dZNLsR\r\n         eKxhdjEXcmv0wtK74SVpMdLBfdFpqs9nXkGRrBgd"
    b"+B3oQpVJFz3HiLsshqZmHaApqyqS\r\n         xwr3LeS8rPb8/o0QAT4Tod00GuqXE9RhU"
    b"Gg/Gn29U6jisv8YqNm37UlA6AAPRhpQ0Xgl\r\n         hn9Q==\r\nX-Gm-Message-S"
    b"tate: AOJu0Yy3VyEkADEUF5TPrf1uYp8w0T0WHTNTI8i71Fum2YklSgGnMG3e\r\n\t+6v3MUk"
    b"5NkaEoAhq5gqlxsPIarVl4ASlbcSbjBhcDlrGp1wQJG4a44z78xe5L9zs5HuE/mkCQgh\r\n\t8"
    b"D8UGPLXWVMiw7Oj8lPrAgmxzH1+haXfK8/k=\r\nX-Google-Smtp-Source: AGHT+IEAhWwl"
    b"O4Gp7buefZgV4uCtWgpFB7pVM9ilYRmcJH+D5TFTX1Ec+WeS4MaJO3eGeGMVugDKqX9i2d9v"
    b"ECeW+D0=\r\nX-Received: by 2002:a25:d24a:0:b0:dbf:501b:2bba with SMTP "
    b"id\r\n j71-20020a25d24a000000b00dbf501b2bbamr503659ybg.83.1705576073482; T"
    b"hu, 18 Jan\r\n 2024 03:07:53 -0800 (PST)\r\nMIME-Version: 1.0\r\nFrom: Vik"
    b"tor Lacina <viktor.lacina@gmail.com>\r\nDate: Thu, 18 Jan 2024 12:07:42 +0"
    b"100\r\nMessage-ID: <CACduWksexfPPwcTQyEKdcT19SywMWh1qc8pPeOWOFOvfOAzPZQ@ma"
    b"il.gmail.com>\r\nSubject: Test\r\nTo: viktor.lacina@seznam.cz\r\nContent-T"
    b'ype: multipart/mixed; boundary="000000000000ff65d0060f365fd7"\r\n\r\n--0'
    b"00000000000ff65d0060f365fd7\r\nContent-Type: multipart/alternative; bounda"
    b'ry="000000000000ff65cd060f365fd5"\r\n\r\n--000000000000ff65cd060f365fd5\r'
    b'\nContent-Type: text/plain; charset="UTF-8"\r\n\r\noh, *banana*?\r\n\r\n-'
    b'-000000000000ff65cd060f365fd5\r\nContent-Type: text/html; charset="UTF-8"\r'
    b'\n\r\n<div dir="ltr">oh, <b>banana</b>?</div>\r\n\r\n--000000000000ff65cd06'
    b"0f365fd5--\r\n--000000000000ff65d0060f365fd7\r\nContent-Type: text/x-pyt"
    b'hon; charset="US-ASCII"; name="banana.py"\r\nContent-Disposition: attachme'
    b'nt; filename="banana.py"\r\nContent-Transfer-Encoding: base64\r\nContent'
    b"-ID: <f_lrj3xvse0>\r\nX-Attachment-Id: f_lrj3xvse0\r\n\r\ncHJpbnQoIkJhbmFh"
    b"YWFhYW5hIikKCg==\r\n--000000000000ff65d0060f365fd7--\r\n"
)

NO_BANANA_MESSAGE = (
    b"Received: from mail-yb1-xb35.google.com\r\n\t(mail-yb1-xb35.google.com [260"
    b"7:f8b0:4864:20::b35])\r\n\tby smtpd-mx-59d667b877-w2j8p (smtpd/2.0.17) with"
    b" ESMTP\r\n\tid 268edf02-8dcc-4cc3-a0f7-5a9e4c8ae216;\r\n\tThu, 18 Jan 2024"
    b" 12:07:55 +0100\r\nReceived: by mail-yb1-xb35.google.com with SMTP id 3f14"
    b"90d57ef6-dc21d7a7042so3389916276.2\r\n        for <viktor.lacina@seznam.cz"
    b">; Thu, 18 Jan 2024 03:07:55 -0800 (PST)\r\nDKIM-Signature: v=1; a=rsa-sha"
    b"256; c=relaxed/relaxed;\r\n        d=gmail.com; s=20230601; t=1705576073; "
    b"x=1706180873; darn=seznam.cz;\r\n        h=to:subject:message-id:date:from"
    b":mime-version:from:to:cc:subject\r\n         :date:message-id:reply-to"
    b";\r\n        bh=0xhOJL5K6biC8HSo0bfmtxUxI+wotNk/YZiF5LbJLSs=;\r\n       "
    b" b=kW6IyGiX7jjWzTHOGu8cESkI4eXwJYSI1eOhnIpsweDeAX/qB/JPypsCDNSLPTnwHg\r\n "
    b"        meFT92jcVaDMw0Eg0735dY+WnsQaRLYJdPSxuBQHdny1WWfGL57FcDcJbbphimf9"
    b"Le0N\r\n         WD3OgOM6cCIBH0+L7gAqJnTW12CQd6bZtkJFjuxGCT/5tYByJfzaV02iN"
    b"ryxxO5TIkOy\r\n         ZwUH5g/2Igmd1Z+3iruBUzXDq9dPZZLYxLyF4ZNDG/MXY1NDJj"
    b"aQ4FYRIbmFb5jnqD3y\r\n         L+XI3mkv1qtkwaVxfISP3jYqWH9dagUJEmPJc8ivhql"
    b"K5xKGCTLaBZsfP0CYCNvb5BHQ\r\n         8Lgw==\r\nX-Google-DKIM-Signature:"
    b" v=1; a=rsa-sha256; c=relaxed/relaxed;\r\n        d=1e100.net; s=20230601;"
    b" t=1705576073; x=1706180873;\r\n        h=to:subject:message-id:date:from:"
    b"mime-version:x-gm-message-state\r\n         :from:to:cc:subject:date:messa"
    b"ge-id:reply-to;\r\n        bh=0xhOJL5K6biC8HSo0bfmtxUxI+wotNk/YZiF5LbJLSs="
    b";\r\n        b=xLJOM91KTBEBrFVnKb8JBNPAhKPFB8NXmi3jcjaTgJqBkngRubE8uPZf28L"
    b"Xk13oLb\r\n         QbpdFR8EjuRCI+3vwcZjDljTYxKKXHo/y0BcNthUpzk1GiKd0J/aTB"
    b"YAqOtJ6rWkgXi8\r\n         bIpLfmRMJhfZfWPG2jGm9wmzBUCnvrq1vg2GVLYdvKd68ua"
    b"MEkQdnDAEO85W81dZNLsR\r\n         eKxhdjEXcmv0wtK74SVpMdLBfdFpqs9nXkGRrBgd"
    b"+B3oQpVJFz3HiLsshqZmHaApqyqS\r\n         xwr3LeS8rPb8/o0QAT4Tod00GuqXE9RhU"
    b"Gg/Gn29U6jisv8YqNm37UlA6AAPRhpQ0Xgl\r\n         hn9Q==\r\nX-Gm-Message-S"
    b"tate: AOJu0Yy3VyEkADEUF5TPrf1uYp8w0T0WHTNTI8i71Fum2YklSgGnMG3e\r\n\t+6v3MUk"
    b"5NkaEoAhq5gqlxsPIarVl4ASlbcSbjBhcDlrGp1wQJG4a44z78xe5L9zs5HuE/mkCQgh\r\n\t8"
    b"D8UGPLXWVMiw7Oj8lPrAgmxzH1+haXfK8/k=\r\nX-Google-Smtp-Source: AGHT+IEAhWwl"
    b"O4Gp7buefZgV4uCtWgpFB7pVM9ilYRmcJH+D5TFTX1Ec+WeS4MaJO3eGeGMVugDKqX9i2d9v"
    b"ECeW+D0=\r\nX-Received: by 2002:a25:d24a:0:b0:dbf:501b:2bba with SMTP "
    b"id\r\n j71-20020a25d24a000000b00dbf501b2bbamr503659ybg.83.1705576073482; T"
    b"hu, 18 Jan\r\n 2024 03:07:53 -0800 (PST)\r\nMIME-Version: 1.0\r\nFrom: Vik"
    b"tor Lacina <viktor.lacina@gmail.com>\r\nDate: Thu, 18 Jan 2024 12:07:42 +0"
    b"100\r\nMessage-ID: <CACduWksexfPPwcTQyEKdcT19SywMWh1qc8pPeOWOFOvfOAzPZQ@ma"
    b"il.gmail.com>\r\nSubject: Test\r\nTo: viktor.lacina@seznam.cz\r\nContent-T"
    b'ype: multipart/mixed; boundary="000000000000ff65d0060f365fd7"\r\n\r\n--0'
    b"00000000000ff65d0060f365fd7\r\nContent-Type: multipart/alternative; bounda"
    b'ry="000000000000ff65cd060f365fd5"\r\n\r\n--000000000000ff65cd060f365fd5\r'
    b'\nContent-Type: text/plain; charset="UTF-8"\r\n\r\noh, *orange*?\r\n\r\n-'
    b'-000000000000ff65cd060f365fd5\r\nContent-Type: text/html; charset="UTF-8"\r'
    b'\n\r\n<div dir="ltr">oh, <b>orange</b>?</div>\r\n\r\n--000000000000ff65cd06'
    b"0f365fd5--\r\n--000000000000ff65d0060f365fd7\r\nContent-Type: text/x-pyt"
    b'hon; charset="US-ASCII"; name="banana.py"\r\nContent-Disposition: attachme'
    b'nt; filename="banana.py"\r\nContent-Transfer-Encoding: base64\r\nContent'
    b"-ID: <f_lrj3xvse0>\r\nX-Attachment-Id: f_lrj3xvse0\r\n\r\ncHJpbnQoIkJhbmFh"
    b"YWFhYW5hIikKCg==\r\n--000000000000ff65d0060f365fd7--\r\n"
)

MISSING_ATTACHMENT_BANANA_MESSAGE = (
    b"Received: from mail-yb1-xb35.google.com\r\n\t(mail-yb1-xb35.google.com [260"
    b"7:f8b0:4864:20::b35])\r\n\tby smtpd-mx-59d667b877-w2j8p (smtpd/2.0.17) with"
    b" ESMTP\r\n\tid 268edf02-8dcc-4cc3-a0f7-5a9e4c8ae216;\r\n\tThu, 18 Jan 2024"
    b" 12:07:55 +0100\r\nReceived: by mail-yb1-xb35.google.com with SMTP id 3f14"
    b"90d57ef6-dc21d7a7042so3389916276.2\r\n        for <viktor.lacina@seznam.cz"
    b">; Thu, 18 Jan 2024 03:07:55 -0800 (PST)\r\nDKIM-Signature: v=1; a=rsa-sha"
    b"256; c=relaxed/relaxed;\r\n        d=gmail.com; s=20230601; t=1705576073; "
    b"x=1706180873; darn=seznam.cz;\r\n        h=to:subject:message-id:date:from"
    b":mime-version:from:to:cc:subject\r\n         :date:message-id:reply-to"
    b";\r\n        bh=0xhOJL5K6biC8HSo0bfmtxUxI+wotNk/YZiF5LbJLSs=;\r\n       "
    b" b=kW6IyGiX7jjWzTHOGu8cESkI4eXwJYSI1eOhnIpsweDeAX/qB/JPypsCDNSLPTnwHg\r\n "
    b"        meFT92jcVaDMw0Eg0735dY+WnsQaRLYJdPSxuBQHdny1WWfGL57FcDcJbbphimf9"
    b"Le0N\r\n         WD3OgOM6cCIBH0+L7gAqJnTW12CQd6bZtkJFjuxGCT/5tYByJfzaV02iN"
    b"ryxxO5TIkOy\r\n         ZwUH5g/2Igmd1Z+3iruBUzXDq9dPZZLYxLyF4ZNDG/MXY1NDJj"
    b"aQ4FYRIbmFb5jnqD3y\r\n         L+XI3mkv1qtkwaVxfISP3jYqWH9dagUJEmPJc8ivhql"
    b"K5xKGCTLaBZsfP0CYCNvb5BHQ\r\n         8Lgw==\r\nX-Google-DKIM-Signature:"
    b" v=1; a=rsa-sha256; c=relaxed/relaxed;\r\n        d=1e100.net; s=20230601;"
    b" t=1705576073; x=1706180873;\r\n        h=to:subject:message-id:date:from:"
    b"mime-version:x-gm-message-state\r\n         :from:to:cc:subject:date:messa"
    b"ge-id:reply-to;\r\n        bh=0xhOJL5K6biC8HSo0bfmtxUxI+wotNk/YZiF5LbJLSs="
    b";\r\n        b=xLJOM91KTBEBrFVnKb8JBNPAhKPFB8NXmi3jcjaTgJqBkngRubE8uPZf28L"
    b"Xk13oLb\r\n         QbpdFR8EjuRCI+3vwcZjDljTYxKKXHo/y0BcNthUpzk1GiKd0J/aTB"
    b"YAqOtJ6rWkgXi8\r\n         bIpLfmRMJhfZfWPG2jGm9wmzBUCnvrq1vg2GVLYdvKd68ua"
    b"MEkQdnDAEO85W81dZNLsR\r\n         eKxhdjEXcmv0wtK74SVpMdLBfdFpqs9nXkGRrBgd"
    b"+B3oQpVJFz3HiLsshqZmHaApqyqS\r\n         xwr3LeS8rPb8/o0QAT4Tod00GuqXE9RhU"
    b"Gg/Gn29U6jisv8YqNm37UlA6AAPRhpQ0Xgl\r\n         hn9Q==\r\nX-Gm-Message-S"
    b"tate: AOJu0Yy3VyEkADEUF5TPrf1uYp8w0T0WHTNTI8i71Fum2YklSgGnMG3e\r\n\t+6v3MUk"
    b"5NkaEoAhq5gqlxsPIarVl4ASlbcSbjBhcDlrGp1wQJG4a44z78xe5L9zs5HuE/mkCQgh\r\n\t8"
    b"D8UGPLXWVMiw7Oj8lPrAgmxzH1+haXfK8/k=\r\nX-Google-Smtp-Source: AGHT+IEAhWwl"
    b"O4Gp7buefZgV4uCtWgpFB7pVM9ilYRmcJH+D5TFTX1Ec+WeS4MaJO3eGeGMVugDKqX9i2d9v"
    b"ECeW+D0=\r\nX-Received: by 2002:a25:d24a:0:b0:dbf:501b:2bba with SMTP "
    b"id\r\n j71-20020a25d24a000000b00dbf501b2bbamr503659ybg.83.1705576073482; T"
    b"hu, 18 Jan\r\n 2024 03:07:53 -0800 (PST)\r\nMIME-Version: 1.0\r\nFrom: Vik"
    b"tor Lacina <viktor.lacina@gmail.com>\r\nDate: Thu, 18 Jan 2024 12:07:42 +0"
    b"100\r\nMessage-ID: <CACduWksexfPPwcTQyEKdcT19SywMWh1qc8pPeOWOFOvfOAzPZQ@ma"
    b"il.gmail.com>\r\nSubject: Test\r\nTo: viktor.lacina@seznam.cz\r\nContent-T"
    b'ype: multipart/mixed; boundary="000000000000ff65d0060f365fd7"\r\n\r\n--0'
    b"00000000000ff65d0060f365fd7\r\nContent-Type: multipart/alternative; bounda"
    b'ry="000000000000ff65cd060f365fd5"\r\n\r\n--000000000000ff65cd060f365fd5\r'
    b'\nContent-Type: text/plain; charset="UTF-8"\r\n\r\noh, *banana*?\r\n\r\n-'
    b'-000000000000ff65cd060f365fd5\r\nContent-Type: text/html; charset="UTF-8"\r'
    b'\n\r\n<div dir="ltr">oh, <b>banana</b>?</div>\r\n\r\n--000000000000ff65cd06'
    b"0f365fd5--\r\n--000000000000ff65d0060f365fd7\r\nContent-Type: text/x-xxx"
    b'xxx; charset="US-ASCII"; name="banana.js"\r\nContent-Disposition: attachme'
    b'nt; filename="banana.js"\r\nContent-Transfer-Encoding: base64\r\nContent'
    b"-ID: <f_lrj3xvse0>\r\nX-Attachment-Id: f_lrj3xvse0\r\n\r\ncHJpbnQoIkJhbmFh"
    b"YWFhYW5hIikKCg==\r\n--000000000000ff65d0060f365fd7--\r\n"
)
