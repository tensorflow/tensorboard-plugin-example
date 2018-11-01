workspace(name = "io_github_tensorflow_tensorboard_plugin_example")

################################################################################
# CLOSURE RULES - Build rules and libraries for JavaScript development
#
# NOTE: SHA should match what's in TensorBoard's WORKSPACE file.
# NOTE: All the projects depended upon in this file use highly
#       available redundant URLs. They are strongly recommended because
#       they hedge against GitHub outages and allow Bazel's downloader
#       to guarantee high performance and 99.9% reliability. That means
#       practically zero build flakes on CI systems, without needing to
#       configure an HTTP_PROXY.

http_archive(
    name = "io_bazel_rules_closure",
    sha256 = "a80acb69c63d5f6437b099c111480a4493bad4592015af2127a2f49fb7512d8d",
    strip_prefix = "rules_closure-0.7.0",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_closure/archive/0.7.0.tar.gz",
        "https://github.com/bazelbuild/rules_closure/archive/0.7.0.tar.gz",  # 2018-05-09
    ],
)

load("@io_bazel_rules_closure//closure:defs.bzl", "closure_repositories")

# Inherit external repositories defined by Closure Rules.
closure_repositories(
    omit_com_google_protobuf = True,
    omit_com_google_protobuf_js = True,
)

################################################################################
# GO RULES - Build rules and libraries for Go development
#
# NOTE: TensorBoard does not require Go rules; they are a transitive
#       dependency of rules_webtesting.
# NOTE: SHA should match what's in TensorBoard's WORKSPACE file.

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "8c333df68fb0096221e2127eda2807384e00cc211ee7e7ea4ed08d212e6a69c1",
    strip_prefix = "rules_go-0.5.4",
    urls = [
        "http://mirror.bazel.build/github.com/bazelbuild/rules_go/archive/0.5.4.tar.gz",
        "https://github.com/bazelbuild/rules_go/archive/0.5.4.tar.gz",
    ],
)

load("@io_bazel_rules_go//go:def.bzl", "go_repositories")

# Inherit external repositories defined by Go Rules.
go_repositories()

# Needed as a transitive dependency of rules_webtesting below.
http_archive(
    name = "bazel_skylib",
    sha256 = "bbccf674aa441c266df9894182d80de104cabd19be98be002f6d478aaa31574d",
    strip_prefix = "bazel-skylib-2169ae1c374aab4a09aa90e65efe1a3aad4e279b",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/archive/2169ae1c374aab4a09aa90e65efe1a3aad4e279b.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/archive/2169ae1c374aab4a09aa90e65efe1a3aad4e279b.tar.gz",  # 2018-01-12
    ],
)

# TODO(stephanwlee): Remove this after ai_google_pair_facets move to
# third_party/workspace.bzl in tensorflow/tensorboard repo.
http_archive(
    name = "ai_google_pair_facets",
    sha256 = "e3f7b7b3c194c1772d16bdc8b348716c0da59a51daa03ef4503cf06c073caafc",
    strip_prefix = "facets-0.2.1",
    urls = [
        "http://mirror.bazel.build/github.com/pair-code/facets/archive/0.2.1.tar.gz",
        "https://github.com/pair-code/facets/archive/0.2.1.tar.gz",
    ],
)

http_archive(
    name = "org_tensorflow",
    sha256 = "88324ad9379eae4fdb2aefb8e0d6c7cd0dc748b44daa5cc96ffd9415705c00c3",
    strip_prefix = "tensorflow-9752b117ff63f204c4975cad52b5aab5c1f5e9a9",
    urls = [
        "https://mirror.bazel.build/github.com/tensorflow/tensorflow/archive/9752b117ff63f204c4975cad52b5aab5c1f5e9a9.tar.gz",  # 2018-04-16
        "https://github.com/tensorflow/tensorflow/archive/9752b117ff63f204c4975cad52b5aab5c1f5e9a9.tar.gz",
    ],
)

load("@org_tensorflow//tensorflow:workspace.bzl", "tf_workspace")

tf_workspace()

################################################################################
# WEBTESTING RULES - Build rules and libraries for Go development
#
# NOTE: SHA should match what's in TensorBoard's WORKSPACE file.
# NOTE: Some external repositories are omitted because they were already
#       defined by closure_repositories().

http_archive(
    name = "io_bazel_rules_webtesting",
    sha256 = "a1264301424f2d920fca04f2d3c5ef5ca1be4f2bbf8c84ef38006e54aaf22753",
    strip_prefix = "rules_webtesting-9f597bb7d1b40a63dc443d9ef7e931cfad4fb098",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_webtesting/archive/9f597bb7d1b40a63dc443d9ef7e931cfad4fb098.tar.gz",  # 2017-01-29
        "https://github.com/bazelbuild/rules_webtesting/archive/9f597bb7d1b40a63dc443d9ef7e931cfad4fb098.tar.gz",
    ],
)

load("@io_bazel_rules_webtesting//web:repositories.bzl", "browser_repositories", "web_test_repositories")

web_test_repositories(
    omit_com_google_code_findbugs_jsr305 = True,
    omit_com_google_code_gson = True,
    omit_com_google_errorprone_error_prone_annotations = True,
    omit_com_google_guava = True,
    omit_junit = True,
    omit_org_hamcrest_core = True,
)

################################################################################
# TENSORBOARD - Framework for visualizing machines learning
#
# NOTE: If the need should arise to patch TensorBoard's codebase, then
#       git clone it to local disk and use local_repository() instead of
#       http_archive(). This should be a temporary measure until a pull
#       request can be merged upstream. It is an anti-pattern to
#       check-in a WORKSPACE file that uses local_repository() since,
#       unlike http_archive(), it isn't automated. If upstreaming a
#       change takes too long, then consider checking in a change where
#       http_archive() points to the forked repository.

http_archive(
    name = "org_tensorflow_tensorboard",
    sha256 = "e263f1ebeadaef246ebbd6d81faa02292ecf0193e5f0ecd279ee38416f2be4b3",
    strip_prefix = "tensorboard-1.12.0",
    urls = [
        "http://mirror.bazel.build/github.com/tensorflow/tensorboard/archive/1.12.0.tar.gz",
        "https://github.com/tensorflow/tensorboard/archive/1.12.0.tar.gz",
    ],
)

load("@org_tensorflow_tensorboard//third_party:workspace.bzl", "tensorboard_workspace")

# Inherit external repositories defined by Closure Rules.
tensorboard_workspace()
