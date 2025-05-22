{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.nodejs_23
    pkgs.pnpm
    pkgs.rsync
    pkgs.tree
  ];
}

