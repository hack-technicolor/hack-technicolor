# hack-technicolor - insider's README

[![Gitter](https://badges.gitter.im/Hack-Technicolor/community.svg)](https://gitter.im/Hack-Technicolor/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

The new Wiki for openwrt-based Homeware releases, migrated from [Whirlpool](https://whirlpool.net.au/wiki/hack_technicolor)

| Wiki Version                                        | Git Branch | Target         |
|-----------------------------------------------------|------------|----------------|
| [Stable](https://hack-technicolor.rtfd.io)          | `stable`   | General Public |
| [Latest](https://hack-technicolor.rtfd.io/en/latest)| `master`   | Insiders/Devs  |

## Editing

[VSCode](https://code.visualstudio.com/) is used with [Code Spell Checker (cSpell)](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) by Street Side Software and [Markdown Lint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) by David Anson.

For pushing docs, [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) by Eric Armodeo, [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) and [Git Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.git-extension-pack) both by Don Jayamanne, is used to improve VSCode's Git SCM base.

## Testing

For testing page rendering you can serve a local instance of this wiki from your local git clone. Read [here](Host%20this%20Locally.md) for detailed instructions.

## Branches

Please push all edits to the `master` branch. When they are ready and everyone is happy, they will be pused over to the stable branch, which will be the branch that readthedocs uses.

## Conventions

### Firmware Types

| Type Number |     Definition     |
|-------------|--------------------|
|      1      |  No direct root strategy known (*yet*), however it is easy to replace with a directly rootable firmware. Can also be rooted indirectly from `Type 2` firmware. |
|      2      |  Direct and easy root strategy is known. Can be used for indirect root strategies for other firmware *Types*. |
|      3      |  No direct root strategy known (*yet*), hard to replace with a directly rootable firmware. Also can be rooted indirectly from `Type 2` firmware. |
|     ???     |   No known direct root strategy tested yet, some of them may work just fine, may be hard, to replace with a directly rootable firmware. May be able to be rooted indirectly from `Type 2` firmware. No experience has been shared from users on such firmware. If you think you know something more about that please tell us. |
