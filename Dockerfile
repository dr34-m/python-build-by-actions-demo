FROM dr34m/tao-sync:not-for-use-pip-req as builder
WORKDIR /app
COPY . /app
RUN pyinstaller demo.spec

FROM dr34m/tao-sync:not-for-use-alpine
VOLUME /app/data
WORKDIR /app
COPY --from=builder /app/dist/demo /app/
ENV TAO_EXPIRES=2 TAO_LOG_LEVEL=1 TAO_LOG_SAVE=7 TAO_TASK_TIMEOUT=72
EXPOSE 8080
CMD ["./demo"]
