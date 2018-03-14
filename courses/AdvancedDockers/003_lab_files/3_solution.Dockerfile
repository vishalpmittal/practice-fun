FROM alpine

CMD ["/app/src/bin/run"]
COPY src /app/src

# Assume the root build context looks like this:
# .git
# .gitignore
# secret_keys/
# etc/
# src/

# src/ is self-contained and does not rely on any other paths
