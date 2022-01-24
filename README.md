# SecSysPhone

SecSysPhone (/'sɛksizfoʊn/, a bit like "saxiphone", also known as SSP) is a SECure SYStem for PHONEs.
It supports any system Linux does, but the window manager is designed for mobile interfaces.
It uses SELinux's robust permissions system -- and hefty doses of automation -- to keep processes well-sandboxed.
Apps are built on WASM, with a customized system interface to support GUI.

If you have questions or concerns, feel free to [open an issue](https://github.com/nic-hartley/SecSysPhone/issues/new).
if you have *security-relevant* questions or concerns, please [email me directly](mailto:the@redfennec.dev).

## Purpose

The point of SecSysPhone is to:

* Offer strong security by default, so even laypeople get good security.
  For example, building in features like LUKS and TTY locking.
* Keep experienced users informed so they can take security risks for themselves.
  If they want to grant some permissions to everything, disable automatic updates, or modify things with a root shell, they should be able to.
* Make it easy for third-party devs to build apps, and users to install them, while knowing all the potential risks.
  The more software is available, the easier it'll be to switch for more people.

The point is **not** to:

* Modularize at all costs.
  The main design goal of SSP is security, and if pieces have to be tightly interconnected, that's acceptable.
* Easily customize everything.
  If you've installed SSP, you probably don't mind having to drop into a shell for advanced configuration.
  Either you're keeping it simple, or you're comfortable with Linux.

## Structure

The custom window manager, the Sweet Phone App Display, is implemented in `spad/`.

SELinux is managed indirectly by `selinuxd/`, which is operated at a high level by the Settings app.
Note this is *not* a general-purpose SELinux control daemon; it's specifically implementing the handful of things this system needs.

The WASM system interface used is described in `wasm-sys/`, in the API documentation.
Some notes on implementation will be in `wasm-bin/`, too.

First-party apps are in `apps/`.
Expect to see:

* `apps/2fa/`, an implementation of TOTP with support for scanning barcodes.
* `apps/internet/`, a very close fork of Firefox.
