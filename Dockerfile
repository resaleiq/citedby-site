FROM python:3.12-slim
WORKDIR /app
COPY server.py home.py pages.py shell.py proxy.py langroutes.py safefetch.py doorcheck.py analytics.py social.py withdraw_link.py legal_links.py hub_links.py follow_link.py trust.py backlinks.py backlinks_i18n.py mcp.py api_v1.py ./
COPY data/ data/
COPY public/ public/
ARG GIT_SHA=unknown
RUN echo "$GIT_SHA" > /app/DEPLOY_ID
RUN useradd -r -u 10001 app && mkdir /data && chown app /data
USER app
ENV DATA_DIR=/data PORT=8080
EXPOSE 8080
CMD ["python3", "-u", "server.py"]
