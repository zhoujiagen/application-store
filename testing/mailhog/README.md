# MailHog

- https://github.com/mailhog/MailHog


Access `http://localhost:8025`.

```shell
# in container
~ $ which MailHog
/usr/local/bin/MailHog
~ $ which sendmail
/usr/sbin/sendmail

$ sendmail -S localhost:1025 <<EOF
From: App <app@mailhog.local>
To: Test <test@mailhog.local>
Subject: Test message

Some content!
EOF
```

## Clients

### Python

- https://docs.python.org/3/library/email.examples.html

```shell
$ python ex_mailhog.py
```