{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    (python312.withPackages (ps: [ ps.pygame ]))
    glib
    SDL2
    SDL2_mixer
  ];

  shellHook = ''
    echo "Python environment with pygame set up."
    exec zsh
  '';
}

