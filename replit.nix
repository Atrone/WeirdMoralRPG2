{pkgs}: {
  deps = [
    pkgs.ollama
    pkgs.glibcLocales
    pkgs.xsimd
    pkgs.pkg-config
    pkgs.libxcrypt
  ];
}
