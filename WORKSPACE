workspace(name = "io_github_tensorflow_tensorboard_plugin_example")

################################################################################
# CLOSURE RULES - Build rules and libraries for JavaScript development
#
# NOTE: SHA should match what's in TensorBoard's WORKSPACE file.
# NOTE: All the projects dependeded upon in this file use highly
#       available redundant URLs. They are strongly recommended because
#       they hedge against GitHub outages and allow Bazel's downloader
#       to guarantee high performance and 99.9% reliability. That means
#       practically zero build flakes on CI systems, without needing to
#       configure an HTTP_PROXY.

http_archive(
    name = "io_bazel_rules_closure",
    sha256 = "110fe68753413777944b473c25eed6368c4a0487cee23a7bac1b13cc49d3e257",
    strip_prefix = "rules_closure-4af89ef1db659eb41f110df189b67d4cf14073e1",
    urls = [
        "http://mirror.bazel.build/github.com/bazelbuild/rules_closure/archive/4af89ef1db659eb41f110df189b67d4cf14073e1.tar.gz",
        "https://github.com/bazelbuild/rules_closure/archive/4af89ef1db659eb41f110df189b67d4cf14073e1.tar.gz",  # 2017-08-28
    ],
)

load("@io_bazel_rules_closure//closure:defs.bzl", "closure_repositories")

# Inherit external repositories defined by Closure Rules.
closure_repositories()

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

################################################################################
# WEBTESTING RULES - Build rules and libraries for Go development
#
# NOTE: SHA should match what's in TensorBoard's WORKSPACE file.
# NOTE: Some external repositories are omitted because they were already
#       defined by closure_repositories().

http_archive(
    name = "io_bazel_rules_webtesting",
    sha256 = "4a34918cdb57b7c0976c1d6a9a7af1d657266b239c9c1066c87d6f9a4058bc7d",
    strip_prefix = "rules_webtesting-a9f624ac542d2be75f6f0bdd255f108f2795924a",
    urls = [
        "http://mirror.bazel.build/github.com/bazelbuild/rules_webtesting/archive/a9f624ac542d2be75f6f0bdd255f108f2795924a.tar.gz",  # 2017-09-11
        "https://github.com/bazelbuild/rules_webtesting/archive/a9f624ac542d2be75f6f0bdd255f108f2795924a.tar.gz",
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
    sha256 = "4f57a58463885ffcff5ac66e192c180a42526ef8dd822376518c15e23a65e918",
    strip_prefix = "tensorboard-c2a83736477f53cac88d4bc45f55b6f22d3ceb62",
    urls = [
        "http://mirror.bazel.build/github.com/tensorflow/tensorboard/archive/c2a83736477f53cac88d4bc45f55b6f22d3ceb62.tar.gz",
        "https://github.com/tensorflow/tensorboard/archive/c2a83736477f53cac88d4bc45f55b6f22d3ceb62.tar.gz",  # 2017-10-05
    ],
)

load("@org_tensorflow_tensorboard//third_party:workspace.bzl", "tensorboard_workspace")

# Inherit external repositories defined by Closure Rules.
tensorboard_workspace()
