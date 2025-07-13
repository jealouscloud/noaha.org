I'm a developer at heart.

## Perspectives
- Technology isn't magic, not even generative AI
- Computers were faster when we built for the CPU and not the browser
- Apple knows what you want but if you don't want to be exploited 
  you'll have to intuit their lessons yourself

## Projects

Some things I can show you:

#### LineRider Advanced
- 2015 - 2019
- Website: [LineRider Advanced](https://linerideradvanced.com) ([git](https://github.com/jealouscloud/linerider-advanced))
- Spiritual successor to a deterministic physics flash game.
- Built with raw OpenGL / no game engine. 
  The spirit of the project reverse engineered the physics of the original flash game.
- As part of this project I had to fork the Gwen UI library originally by Garry Newman in [gwen-lra](https://github.com/jealouscloud/gwen-lra).  
  At 188 commits, +36,221/-10,248 lines, this was a pretty deep dive.  
  Far from the only time I've gotten deep into the technicals of UI display, though.
- Due to the deterministic nature of physics in this project, floating-point serialization had to be exact. To support compatibility with another project, I implemented the Google double-float conversion procedure in a [Utf8Json pull request](https://github.com/neuecc/Utf8Json/commit/8cd16c6f08d93c0763ec715a84a110b780855152)

#### html-compose

- Python Library: [GitHub](https://github.com/jealouscloud/html-compose) / [pypi](https://pypi.org/project/html-compose/) and [documentation](https://jealouscloud.github.io/html-compose/html_compose.html)
- Thesis statement: Add just a little abstraction to the HTML generation process and you can solve friction in writing markup.
- Fun fact: This website is built with html-compose.

#### Misc
- KDE Improvements
  - [Activity switch hotkeys extension](https://github.com/jealouscloud/kwin-activity-hotkeys) - mimic missing i3 features
  - Rofi based [Keyboard shortcut selector](https://github.com/jealouscloud/kshortcut-rofi). I built this because I like tiling but not memorizing the keys for every layout.
- [SaltStack TLS CA](https://github.com/jealouscloud/salt-tls-ca)
  - Orchestation for TLS certificates in distributed systems


## Proprietary Work

I can't show you much here, but I can tell you
> Why go with a vendor, when you can go with me?

I have done:

* Scaled up [Wazuh](https://wazuh.com/) Integration with a bunch of bespoke use-case specific code
* Integrated "big data" monitoring pipelines where sometimes a vendor worked and sometimes I had to get my own hands dirty.
* Webauthn based security gateways mandating specific hardware security keys 
  & integraiton with a custom PAM module for SSH 2fa
* Hypervisor & platform R&D, most recently Incus
* Little small-purpose-high-impact workflow sites

## Other projects I've done
No sources here. Wouldn't wanna get in trouble.

- Multiplayer anticheat reverse-engineering and bypass.
  - Keywords: Themida, heartbeat emulation, VMProtect, CRC patches
- Multiplayer game packet editing tools.
  - Reminder to never trust the client
  - Keywords: Currency generation, my first SaaS, building my own anti-piracy