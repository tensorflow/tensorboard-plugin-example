load("@org_tensorflow_tensorboard//tensorboard/defs:vulcanize.bzl", "tensorboard_html_binary")
load("@org_tensorflow_tensorboard//tensorboard/defs:web.bzl", "tf_web_library")
load("@org_tensorflow_tensorboard//tensorboard/defs:zipper.bzl", "tensorboard_zip_file")

licenses(["notice"])  # Apache 2.0

py_binary(
    name = "gr_tensorboard",
    srcs = ["main.py"],
    data = ["assets.zip"],
    main = "main.py",
    srcs_version = "PY2AND3",
    deps = [
        "//paramplot:paramplot_loader",
        "@org_pocoo_werkzeug",
        "@org_tensorflow_tensorboard//tensorboard:default",
        "@org_tensorflow_tensorboard//tensorboard:program",
    ],
)

tf_web_library(
    name = "index",
    srcs = ["index.html"],
    path = "/",
    deps = [
        "//paramplot:paramplot_dashboard",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_imports:webcomponentsjs",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_tensorboard",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_tensorboard:default_plugins",
    ],
)

tensorboard_zip_file(
    name = "assets",
    deps = [":index"],
)
