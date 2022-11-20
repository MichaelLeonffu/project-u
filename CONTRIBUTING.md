# Contributing

*This document is a work in progress.*

Rules for consistency and scalability.

## Conventions

- Dimensions are given in pixels in WIDTHxHEIGHT
- This project uses 1080p which is 1920x1080
- Media files include audio, images, and movies

- Use `_` in place of the `space` character when spaces are not allowed
- Use `-` in between different groups of words
  - e.g: `chapter_000-location_name-any_other_detail_that_is_unique.rpy`

## Uploading changes

**Applies to all groups**

**`master` is reserved for fully working/tested features** except in `-alpha`.

### Versioning

Referenced from https://semver.org

Tags are placed on `master` for releasable versions of the project. Binaries should be included in the releases.

The regex is: `^v[0-9]+\.[0-9]+\.[0-9]+(\-alpha|\-beta)?$`
Examples are: `v0.0.1-alpha`, `v0.5.35-beta`, `v12.0.4`

There should be at least a patch version bump for newly added assets or changes to LICENSE/AUTHORS/README.md
There should be at least a minor version bump for newly added features
There should be at least a major version bump on long term milestones reached

### Branches

### Pull Requests/Merges

### Committing

## Script conventions

How to write script that is easily maintainable and scalable?

## File naming conventions

Script
: Any files that contain script code
: script files should be broken down by scenes
: Note, scenes are specific environments, with specific characters, at a specific time and are one-time only
: e.g John meets Joe in the Alley for the first time VS John meets Joe in the Alley for the final fight.

`chapter_000-location_name-any_other_detail_that_is_unique.rpy`

or maybe

`phase_000-location_name-any_other_detail_that_is_unique.rpy`

e.g

`phase_001-The_Alley.rpy`

But if that name is already taken then

`phase_001-The_Ally-Knife_Fight.rpy`

*Actually this depends on the type of game*

## Artwork

Dimensions:
- Avatars: X by X
- Background: X by X

All 300 DPI and ".png" file type

### Characters

Using character names in script:
TODO:

- X by X Maximum...?
- located in `/images/character_name/character_name expression1 expression2 expressionN.png`
  - e.g: if character name is "diego_lastname" then the path is `/images/diego_lastname/diego_lastname neutral.png`
  - Note: there can be as few as 0 expressions, expressions are separated by a space character.

### Backgrounds

- Exactly X by X
- located in `/images/bg/bg bg_name.png`

### Objects

- X by X maximum
- located in `/images/objects/object_name`

### Menus

Things like maps, where you can hover over buildings, are considered menus as well.

- Menu: X by X maximum, Recommended to fill the whole background and use alpha channel
- Menu items: less than menu size, same recommendation
- Menu located in `/images/menu/menu_name/menu.png`
- Menu items located in `images/menu/menu_name/menu_item_name.png`

## Audio

- Audio files should be in the format `.ogg`
- At most X length(?)
- At most X size(?)
- With a bit rate of (?)

## Mixed media

### Video

Video information can be found here on [videoproc](https://www.videoproc.com/resource/best-video-format.htm#webm)

    ffmpeg -i main_menu_bg.mp4 -b:v 6K -r 60 output.webm

(Actually when the video is made make sure these settings are used to keep the best quality as possible)
a.k.a changing bitrates can affect quality poorly

- Container:  `WebM`
- Codec: Google VP9
- Framerate: 60
- Bitrate: 6000
- Audio: Opus
- Dimensions: 1080p

- File format in X
- At most X by X
- At most X size
- Format with X; etc
- located in `/movies/movie_category/movie_name_000.mov`

## Development
