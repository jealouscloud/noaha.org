{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.nodejs_24
    pkgs.pnpm
    pkgs.rsync
    pkgs.tree
  ];
}

