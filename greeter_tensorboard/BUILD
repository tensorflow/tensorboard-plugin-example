load("@org_tensorflow_tensorboard//tensorboard/defs:vulcanize.bzl", "tensorboard_html_binary")
load("@org_tensorflow_tensorboard//tensorboard/defs:web.bzl", "tf_web_library")
load("@org_tensorflow_tensorboard//tensorboard/defs:zipper.bzl", "tensorboard_zip_file")

licenses(["notice"])  # Apache 2.0

py_binary(
    name = "greeter_tensorboard",
    srcs = ["main.py"],
    data = ["assets.zip"],
    main = "main.py",
    srcs_version = "PY2AND3",
    deps = [
        "//greeter_plugin",
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
        "//greeter_plugin:greeter_dashboard",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_imports:webcomponentsjs",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_tensorboard",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_tensorboard:default_plugins",
    ],
)

# TODO(stephanwlee): Either allow modular html binary or make the interactive
# inference plugin's asset public. Otherwise, we cannot correctly compile a
# using Closure compiler.
# Interactive inference plugin does not work without the compilation.
#
# tensorboard_html_binary(
#     name = "index_bin",
#     # TODO(stephanwlee): removed with having modular html binaries.
#     compile = True,
#     input_path = "/index.html",
#     output_path = "/index_bin.html",
#     deps = [":index"],
# )
#
# tf_web_library(
#     name = "assets_lib",
#     srcs = [
#         ":index_bin.html",
#         "@org_tensorflow_tensorboard//tensorboard/plugins/interactive_inference/tf_interactive_inference_dashboard:wit_assets",
#     ],
#     path = "/",
# )

tensorboard_zip_file(
    name = "assets",
    deps = [":index"],
)
