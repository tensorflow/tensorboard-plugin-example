# TensorBoard Build Reference

TensorBoard uses Bazel for building and testing. Since TensorBoard aims to
provide a framework for developers working in ML visualization, much work has
been done to provide robust build tooling that comes with third party
dependencies included.

## Bazel‽

Bazel is Google's build system. It was designed to scale to repositories with
gigabytes of code. It was only quite recently made available to the public in
2015. Before that happened, it was so highly sought after by external developers
that numerous open source clones were written, e.g. Buck, Pants, GN, etc.

These commands help one understand the great mystery of Bazel:

```sh
bazel build -s //greeter_tensorboard/tensorboard
ls $(bazel info output_base)/external
```

Bazel labels have the following semantics:

- `//foo:bar` means the rule named `bar` in `foo/BUILD`.
- `//foo` is shorthand for `//foo:foo`
- `@bar` is shorthand for `@bar//:bar`
- `:foo` means `//foo:foo` if specified in `foo/BUILD`
- `//bar` is sort of equivalent to `@foo//bar` if specified in a BUILD file
  within the `foo` repository.

## Build Rules

The following build rules, which don't come included with Bazel, are defined by
the external repositories defined in the `WORKSPACE` file.

- `load("@io_bazel_rules_closure//closure:defs.bzl", "closure_css_binary")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "closure_css_library")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "closure_java_template_library")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "closure_js_binary")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "closure_js_deps")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "closure_js_library")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "closure_js_proto_library")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "closure_js_template_library")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "web_library")`
- `load("@io_bazel_rules_web//webtesting:web.bzl", "web_test_archive")`
- `load("@io_bazel_rules_webtesting//web:py.bzl", "py_web_test_suite")`
- `load("@io_bazel_rules_webtesting//web:web.bzl", "browser")`
- `load("@org_tensorflow_tensorboard//tensorboard/defs:protos.bzl", "tb_proto_library")`
- `load("@org_tensorflow_tensorboard//tensorboard/defs:vulcanize.bzl", "tensorboard_html_binary")`
- `load("@org_tensorflow_tensorboard//tensorboard/defs:web.bzl", "tf_web_library")`
- `load("@org_tensorflow_tensorboard//tensorboard/defs:zipper.bzl", "tensorboard_zip_file")`
- `load("@protobuf//:protobuf.bzl", "py_proto_library")`

## Workspace Rules

These are special kinds of build rules intended for `WORKSPACE` files. They
can be used to download third party code and generate a synthetic `BUILD` file
for their contents.

- `load("@io_bazel_rules_closure//closure/private:java_import_external.bzl", "java_import_external")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "filegroup_external")`
- `load("@io_bazel_rules_closure//closure:defs.bzl", "web_library_external")`

## Build Rule Targets

Here's a curated list of some of the many build rule targets defined by
TensorBoard and Closure Rules that plugin authors may wish to depend upon.
These dependencies are all automatically downloaded by Bazel, via highly
available redundant mirrors, per the `WORKSPACE` file definition.

### py_library() rules

- `@org_mozilla_bleach`
- `@org_pocoo_werkzeug`
- `@org_pythonhosted_markdown`
- `@org_tensorflow_tensorboard//tensorboard/backend/event_processing:event_accumulator`
- `@org_tensorflow_tensorboard//tensorboard/backend/event_processing:event_file_inspector`
- `@org_tensorflow_tensorboard//tensorboard/backend/event_processing:event_multiplexer`
- `@org_tensorflow_tensorboard//tensorboard/backend:application`
- `@org_tensorflow_tensorboard//tensorboard/backend:http_util`
- `@org_tensorflow_tensorboard//tensorboard/backend:process_graph`
- `@org_tensorflow_tensorboard//tensorboard/plugins/audio:audio_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/core:core_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/distribution:distributions_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/graph:graphs_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/histogram:histograms_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/image:images_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/profile:profile_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/projector:projector_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/scalar:scalars_plugin`
- `@org_tensorflow_tensorboard//tensorboard/plugins/text:text_plugin`
- `@org_tensorflow_tensorboard//tensorboard` (Note: Provides `tensorboard.main`)
- `@org_tensorflow_tensorboard//tensorboard:db`
- `@org_tensorflow_tensorboard//tensorboard:loader`
- `@org_tensorflow_tensorboard//tensorboard:test_util`
- `@org_tensorflow_tensorboard//tensorboard:util`
- `@org_pythonhosted_six`

### web_library() rules

The following labels can be added to the `deps` list of `web_library`,
`tf_web_library`, `tensorboard_html_binary`, and `tensorboard_zip_file` rules.

- `@org_polymer_font_roboto`
- `@org_polymer_iron_ajax`
- `@org_polymer_iron_collapse`
- `@org_polymer_iron_component_page`
- `@org_polymer_iron_demo_helpers`
- `@org_polymer_iron_flex_layout`
- `@org_polymer_iron_icon`
- `@org_polymer_iron_icons`
- `@org_polymer_iron_list`
- `@org_polymer_paper_button`
- `@org_polymer_paper_checkbox`
- `@org_polymer_paper_dialog_scrollable`
- `@org_polymer_paper_dialog`
- `@org_polymer_paper_dropdown_menu`
- `@org_polymer_paper_header_panel`
- `@org_polymer_paper_icon_button`
- `@org_polymer_paper_input`
- `@org_polymer_paper_item`
- `@org_polymer_paper_listbox`
- `@org_polymer_paper_material`
- `@org_polymer_paper_menu`
- `@org_polymer_paper_progress`
- `@org_polymer_paper_radio_group`
- `@org_polymer_paper_slider`
- `@org_polymer_paper_spinner`
- `@org_polymer_paper_styles`
- `@org_polymer_paper_tabs`
- `@org_polymer_paper_toast`
- `@org_polymer_paper_toggle_button`
- `@org_polymer_paper_toolbar`
- `@org_polymer_paper_tooltip`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_backend`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_card_heading`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_categorization_utils`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_color_scale`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_dashboard_common`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:d3`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:dagre`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:graphlib`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:lodash`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:numericjs`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:plottable`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:polymer`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:threejs`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:web_component_tester`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:webcomponentsjs`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_imports:weblas`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_paginated_view`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_runs_selector`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_storage`
- `@org_tensorflow_tensorboard//tensorboard/components/tf_tensorboard`
- `@org_tensorflow_tensorboard//tensorboard/components/vz_sorting`
- `@org_tensorflow_tensorboard//tensorboard/plugins/audio/tf_audio_dashboard`
- `@org_tensorflow_tensorboard//tensorboard/plugins/distribution/tf_distribution_dashboard`
- `@org_tensorflow_tensorboard//tensorboard/plugins/graph/tf_graph_dashboard`
- `@org_tensorflow_tensorboard//tensorboard/plugins/histogram/tf_histogram_dashboard`
- `@org_tensorflow_tensorboard//tensorboard/plugins/image/tf_image_dashboard`
- `@org_tensorflow_tensorboard//tensorboard/plugins/profile/tf_profile_dashboard`
- `@org_tensorflow_tensorboard//tensorboard/plugins/projector/vz_projector`
- `@org_tensorflow_tensorboard//tensorboard/plugins/scalar/tf_scalar_dashboard`
- `@org_tensorflow_tensorboard//tensorboard/plugins/scalar/vz_line_chart`
- `@org_tensorflow_tensorboard//tensorboard/plugins/text/tf_text_dashboard`

### java_library() rules

- `@args4j`
- `@com_google_auto_common`
- `@com_google_auto_factory`
- `@com_google_auto_value`
- `@com_google_closure_stylesheets`
- `@com_google_code_findbugs_jsr305`
- `@com_google_code_gson`
- `@com_google_dagger_producers`
- `@com_google_dagger`
- `@com_google_errorprone_error_prone_annotations`
- `@com_google_guava`
- `@com_google_inject_extensions_guice_assistedinject`
- `@com_google_inject_extensions_guice_multibindings`
- `@com_google_inject_guice`
- `@com_google_protobuf_java`
- `@com_ibm_icu_icu4j`
- `@com_squareup_javawriter`
- `@io_bazel_rules_closure//closure/compiler`
- `@io_bazel_rules_closure//closure/templates`
- `@io_bazel_rules_closure//closure/templates:safe_html_types`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure/http/filter`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure/http`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure/webfiles/compiler`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure/webfiles:build_info_java_proto`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure/webfiles`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure/worker`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure:build_info_java_proto`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure:tarjan`
- `@io_bazel_rules_closure//java/io/bazel/rules/closure:webpath`
- `@io_bazel_rules_closure//java/org/jsoup/nodes` (Note: Provides `Html5Printer`)
- `@javax_inject` (Note: Implied by `@com_google_dagger`)
- `@org_json`
- `@org_jsoup`
- `@org_ow2_asm_analysis`
- `@org_ow2_asm_commons`
- `@org_ow2_asm_tree`
- `@org_ow2_asm_util`
- `@org_ow2_asm`

### closure_js_library() rules

- `@io_bazel_rules_closure//closure/library`
- `@io_bazel_rules_closure//closure/library:testing`
- `@io_bazel_rules_closure//closure/protobuf:jspb`
- `@io_bazel_rules_closure//third_party/javascript/incremental_dom`

### filegroup() rules

- `@com_google_javascript_closure_compiler_externs`
- `@com_google_javascript_closure_compiler_externs_polymer`

### browser() rules

- `@org_tensorflow_tensorboard//tensorboard/functionaltests/browsers:chromium`

### Notes

Many of the recommended targets are delegates. For example,
`@org_tensorflow_tensorboard//tensorboard/components/tf_imports:polymer` is
roughly equivalent to `@org_polymer`. The `tf_imports` version is preferred
because it adds additional value, such as TypeScript typings and Closure
Compiler externs.

In certain cases, the recommended delegate targets may appear to be superfluous.
For example, `@io_bazel_rules_closure//closure/compiler` is equivalent to
`@com_google_javascript_closure_compiler`. Those labels exist to make life
easier for Googlers. In Google's internal repository, they export more than one
build targets. By using these delegates, Googlers can make the open source sync
process easier by regex replacing build labels.
