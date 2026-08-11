{
  pkgs,
  lib,
  buildPythonPackage,
  fetchPypi,

  # build-system
  hatchling,

  # dependencies

  # tests
  pytestCheckHook,
}:

buildPythonPackage rec {
  pname = "altamiranoi";
  version = "0.3.1";
  # format = "pyproject";
  pyproject = true;

  # Update when necessary

  # Comment this if you want to build from source.
  src = fetchPypi {
    inherit pname version;
    hash = "sha256-vhNnECUxJhjeK0PjzHNGfEfuvAoNcJTf7j9Etg/Lsk0=";
  };

  # Uncomment this if you want to build from source.
  # src = lib.cleanSource ./.;

  postPatch = "";

  build-system = [
    hatchling
  ];

  dependencies = [ ];

  nativeCheckInputs = [
    pytestCheckHook
  ];

  doCheck = true;

  disabledTests = [
    # These tests require a network connection.
    "test_handle_repository_urls"
    "test_altamiranoi_main_function"
    "test_fetch_forge_repository_data"
    "test_get_repository_programming_language"
  ];

  pythonImportsCheck = [ "altamiranoi" ];

  meta = {
    description = "A repository collector.";
    homepage = "https://github.com/bormoge/altamiranoi";
    # changelog = "https://github.com/bormoge/altamiranoi/releases/tag/v${version}";
    changelog = "https://github.com/bormoge/altamiranoi/blob/main/CHANGELOG.md";
    license = lib.licenses.gpl3Plus;
    mainProgram = "altamiranoi";
    maintainers = with lib.maintainers; [ ];
  };
}
