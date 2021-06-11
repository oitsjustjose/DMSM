# DMSM Flags

These flags have been manually documented just for you :grinning:

### allow_flight | Type: `bool` | Default: `false`

Controls whether players are allowed to fly (outside of Spectator/Creative Mode). Can be changed at any time via `server.properties`.

### allow_nether | Type: `bool` | Default: `true`

Controls whether players are allowed to enter the nether. Can be changed at any time via `server.properties`.

### announce_player_achievements | Type: `bool` | Default: `true`

Controls whether players' advancements are broadcasted accross the server. Can be changed at any time via `server.properties`.

### autopause_knock_interface | Type: `str` | Default: `eth0`

The network interface (i.e. `eth0`) used to listen for "knocks" to resume the server after being autopaused.

### autopause_period | Type: `int` | Default: `10` (Seconds)

The period of the daemonized state machine, that handles the pausing of the process (resuming is done independently)

### autopause_timeout_est | Type: `int` | Default: `3600` (Seconds)

The time between the last client disconnect and the pausing of the process (read as timeout established)

### autopause_timeout_init | Type: `int` | Default: `600` (Seconds)

The time between server start and the pausing of the process, when no client connects inbetween (read as timeout initialized)

### autopause_timeout_kn | Type: `int` | Default: `120` (Seconds)

The time between knocking of the port (e.g. by the main menu ping) and the pausing of the process, when no client connects inbetween (read as timeout knocked)

### broadcast_console_to_ops | Type: `bool` | Default: `true`

Controls whether console commands are sent to all operator users that are online. Can be changed at any time via `server.properties`.

### broadcast_rcon_to_ops | Type: `bool` | Default: `true`

Controls whether console commands issued via RCON are sent to all operator users that are online. Can be changed at any time via `server.properties`.

### build_from_source | Type: `bool`

A flag issued to build Spigot from source.

### bukkit_download_url | Type: `str`

The URL from which to download the bukkit server jar.

### canyon_build | Type: `int` | Default: Latest Build

The build number for Canyon Server.

### cf_base_dir | Type: `str` | Default: `/data/FeedTheBeast`

Changes the subdirectory the mod `.zip` folder is extracted to.

### cf_server_mod | Type: `str`

Path to the `.zip` file containing a CurseForge server mod.

### console | Type: `bool`

Allows you to perform the equivalent of pre-1.14-Spigot's required `--noconsole` flag.

### copy_config_dest | Type: `str` | Default: `/data/config`

Determines where the output configs from a mod/plugin should go.

### copy_mods_dest | Type: `str` | Default: `/data/mods`

Determines where the mods should be output to

### custom_server | Type: `str`

### USE WITH `--type CUSTOM`. Allows you to run a custom server JAR, whether that be a local path or a URL to the JAR-file

### difficulty | Type: `str` | Default: `'easy'`

Allows you to set the difficulty of the server. Can be changed at any time via `server.properties`.

### disable_healthcheck | Type: `bool`

Disables the ability to check the health/status of the Minecraft server (such as starting, healthy, etc.).

### enable_autopause | Type: `bool`

Controls whether or not the autopause feature can be enabled. Read up on it [here](https://github.com/itzg/docker-minecraft-server/blob/master/README.md#autopause).

### enable_command_block | Type: `bool` | Default: `false`

Controls whether or not command blocks can be used. Can be changed at any time via `server.properties`.

### enable_jmx | Type: `bool` | Default: `false`

Controls whether JMX Profiling is enabled or disabled. Can be changed at any time via `server.properties`.

### enable_query | Type: `bool` | Default: `true`

Controls whether or not server can be queried. Can be changed at any time via `server.properties`.

### enable_rcon | Type: `bool` | Default: `true`

Controls whether or not RCON is enabled for this server. Can be changed at any time via `server.properties`.

### enable_rolling_logs | Type: `bool`

Controls whether or not logs can be rolled to prevent lag when writing/reading them

### enable_status | Type: `bool` | Default: `true`

Controls whether the server appear as "online" on the server list. Can be changed at any time via `server.properties`.

### enforce_whitelist | Type: `bool` | Default: ...

When this option is enabled, users who are not present on the whitelist (if it's enabled) get kicked from the server after the server reloads the whitelist file. Can be changed at any time via `server.properties`.

### entity_broadcast_range_percentage | Type: `float` | Default: `100`

Controls how close entities need to be before being sent to clients. Higher values means they'll be rendered from farther away, potentially causing more lag. Can be changed at any time via `server.properties`.

### env_variable_prefix | Type: `str` | Default: `CFG_`

Allows you to define a prefix to only match predefined environment variables.

### exec_directly | Type: `bool`

Allows you to attach to the Minecraft server console with color and interactive ### pabilities. **NOTE: this will bypass graceful server shutdown handling when using docker stop, so be sure to use rcon-cli or console commands to stop the server.

### fabric_installer | Type: `str`

The path to the Fabric Installer to use for the server

### fabric_installer_url | Type: `str`

The url to the Fabric Installer to use for the server

### fabric_installer_version | Type: `str` | Default: Latest Version

Allows you to specify an installer version.

### force_gamemode | Type: `bool` | Default: `false`

Controls whether the gamemode of a user can be changed. Can be changed at any time via `server.properties`.

### force_redownload | Type: `bool`

Forces the server JAR to be redownloaded.

### force_world_copy | Type: `bool`

Forces the world to be copied/redownloaded if located on a container or online.

### forge_installer | Type: `str`

The path to a local Forge installer.

### forge_installer_url | Type: `str` | Default: ...

The URL to a remote Forge installer.

### forgeversion | Type: `str` | Default: Forge Recommended

Allows you to choose which version of Forge to use

### ftb_legacyjavafixer | Type: `bool`

Fixes error `unable to launch forgemodloader` if you happen to see it

### ftb_modpack_id | Type: `str`

### REQUIRED when using FTB Modpacks. The numerical ID of the modpack to install. The ID can be located by finding the modpack and using the "ID" displayed next to the name.

### ftb_modpack_version_id | Type: `str`

Numerical Id of the version to install. If not specified, the latest version will be installed. The "Version ID" can be obtained by drilling into the Versions tab and clicking a specific version.

### function_permission_level | Type: `int` | Default: `2`

Sets the default permission level for functions. Can be changed at any time via `server.properties`.

### generate_structures | Type: `bool` | Default: `true`

Defines whether structures (such as villages) can be generated. Can be changed at any time via `server.properties`.

### hardcore | Type: `bool` | Default: `false`

Defines whether the world is in hardcore mode. Can be changed at any time via `server.properties`.

### icon | Type: `str`

Allows you to define an override for the `server-icon.png` icon that shows up in the Multiplayer server list.

### init_memory | Type: `str`

Independently sets the initial heap size. Sizes can be `g|G|m|M|k|K`.

### jmx_host | Type: `str`

To enable remote JMX, such as for profiling with VisualVM or JMC, use this to set JMX_HOST to the IP/host running the Docker container, and add a port forwarding of TCP port 7091.

### jvm_dd_opts | Type: `str`

Builds the params from a given list of values separated by space, but without the `-D` prefix.

### jvm_opts | Type: `str`

Allows you to pass general JVM options to the server

### jvm_xx_opts | Type: `str`

Allows you to `-X` JVM flags to the server

### level | Type: `str` | Default: `'world'`

Allows you to set a default level name. Can be changed at any time via `server.properties`.

### level_type | Type: `str` | Default: `'default'`

Allows you to set the server's world type. Can be changed at any time via `server.properties`.

### max_build_height | Type: `int` | Default: `255`

Allows you to set the maximum build height for the server. Can be changed at any time via `server.properties`.

### max_memory | Type: `str`

Allows independent control of the max heap size. Sizes can be `g|G|m|M|k|K`.

### max_players | Type: `int` | Default: `20`

Allows you to set the max number of players on the server. Can be changed at any time via `server.properties`.

### max_tick_time | Type: `int` | Default: `60000`

The maximum number of milliseconds a single tick may take before the server watchdog stops the server with the message, A single server tick took 60.00 seconds (should be max 0.05); Considering it to be crashed, server will forcibly shutdown. Once this criterion is met, it calls System.exit(1). Can be changed at any time via `server.properties`.

### max_world_size | Type: `int` | Default: `29999984`

Controls the maximum size of the world, in blocks. Can be changed at any time via `server.properties`.

### memory | Type: `str` | Default: `'1G'`

Allows you to adjust both initial (`Xms`) and max (`Xmx`) memory heap settings of the JVM. Sizes can be `g|G|m|M|k|K`.

### modpack | Type: `str`

Best explained [here](https://github.com/itzg/docker-minecraft-server/blob/master/README.md#downloadable-modplugin-pack-for-forge-bukkit-and-spigot-servers)

### mohist_build | Type: `int` | Default: Latest Build

Allows you to specify a build number to be used by the server.

### motd | Type: `str` | Default: `'A Minecraft Server powered by Docker'`

Allows you to set the MOTD of the server, seen in the multiplayer menu. Can be changed at any time via `server.properties`.

### network_compression_threshold | Type: `int` | Default: `256`

By default it allows packets that are n-1 bytes big to go normally, but a packet of n bytes or more gets compressed down. So, a lower number means more compression but compressing small amounts of bytes might actually end up with a larger result than what went in.

### -1 - disable compression entirely

### 0 - compress everything

Can be changed at any time via `server.properties`.

### online_mode | Type: `bool` | Default: `true`

Allows you to control whether or not Mojang Server Authentication must be used for a player to log in. Can be changed at any time via `server.properties`.

### op_permission_level | Type: `int` | Default: ...

Sets the default permission level for ops when using `/op`. All levels inherit abilities and commands from levels before them.

1. Ops can bypass spawn protection.
2. Ops can use all singleplayer cheats commands (except `/publish`, as it is not on servers; along with `/debug`) and use command blocks. Command blocks, along with Realms owners/operators, have the same permissions as this level.
3. Ops can use most multiplayer-exclusive commands, including `/debug`, and commands that manage players (`/ban`, `/op`, etc).
4. Ops can use all commands including `/stop`, `/save-all`, `/save-on`, and `/save-off`.

Can be changed at any time via `server.properties`.

### ops | Type: `str`

Allows you to preemptively define ops instead of adding them later via console or `ops.json`. Allows for a comma-delimited list.

### override_icon | Type: `bool` | Default: `false`

The server icon which has been set doesn't get overridden by default. It can be changed and overridden with this flag.

### override_ops | Type: `bool` | Default: `false`

Forces the `ops.json` file will be recreated on each server startup.

### override_server_properties | Type: `bool` | Default: `false`

Forces `server.properties` to be recreated on each server startup.

### override_whitelist | Type: `bool` | Default: `false`

Forces `whitelist.json` to be recreated on each server startup.

### paper_download_url | Type: `str`

Allows you to specify your own download url for a Paper server JAR.

### paperbuild | Type: `int` | Default: Latest Build

Allows you to specify which build of Paper to use for the JAR.

### player_idle_timeout | Type: `int` | Default: `0`

If non-zero, players are kicked from the server if they are idle for more than that many minutes. Can be changed at any time via `server.properties`.

### plugins_sync_update | Type: `bool`

Allows you to specify if plugins located in `/plugins` should take precedence over newer files in `/data/plugins`.

### prevent_proxy_connections | Type: `bool` | Default: `false`

If the ISP/AS sent from the server is different from the one from Mojang Studios' authentication server, the player is kicked. Can be changed at any time via `server.properties`.

### proxy | Type: `str`

Allows you to configure the use of an HTTP/HTTPS proxy by passing the proxy's URL.

### purpur_build | Type: `str` | Default: Latest Build

Allows you to specify which build of Purpur to use for the JAR.

### pvp | Type: `bool` | Default: `true`

Allows you to choose whether PVP is enabled. Can be changed at any time via `server.properties`.

### query_port | Type: `str` | Default: `'25565'`

Allows you to define which port is used to query the server. Can be changed at any time via `server.properties`.

### rcon_passord | Type: `str` | Default: `'minecraft'`

Allows you to specify the password for an RCON Connection.

### rcon_port | Type: `str` | Default: `'25575'`

Allows you to specify the port for an RCON Connection.

### remove_old_mods | Type: `bool`

Allows you to control whether old mods/plugins are removed before the new content is brought over from attach points.

### remove_old_mods_depth | Type: `int` | Default: `16`

Allows you to define to what level deletion should occur.

### remove_old_mods_exclude | Type: `str`

Allows for fine-tuning the old mod removal process.

### remove_old_mods_include | Type: `str`

Allows for fine-tuning the old mod removal process.

### replace_env_variables | Type: `bool`

Whether the startup script should go through all files inside the /data volume and replace variables that match your defined environment variables

### replace_env_variables_exclude_paths | Type: `bool`

Paths to be excluded from the environment variable replacement process stated above.

### replace_env_variables_excludes | Type: `bool` | Default: ...

Files to be excluded from the environment variable replacement process stated above.

### resource_pack | Type: `str` | Default: `''`

Allows you to add an optional URI to a resource pack that the player must choose to use.  Can be changed at any time via `server.properties`.

### resource_pack_sha1 | Type: `str`

The SHA1 digest of the resource pack controlled by the above flag.  Can be changed at any time via `server.properties`.

### seed | Type: `str` | Default: `''`

The world seed to use for the level. Can be changed at any time via `server.properties`.

### server_name | Type: `str`

The server name to use for some server types, such as Bungeecord.

### server_port | Type: `str` | Default: `'25565'`

The port to use for the minecraft server. Keep in mind, this is the port to use INTERNALLY and you should use the `-p|--port` flag unless you know exactly what you're doing. Can be changed at any time via `server.properties`.

### snooper_enabled | Type: `bool` | Default: `true`

Sets whether the server sends snoop data regularly to http://snoop.minecraft.net. Can be changed at any time via `server.properties`.

### spawn_animals | Type: `bool` | Default: `true'`

Controls whether animals can spawn in the world. Can be changed at any time via `server.properties`.

### spawn_monsters | Type: `bool` | Default: `true'`

Controls whether monsters can spawn in the world. Can be changed at any time via `server.properties`.

### spawn_npcs | Type: `bool` | Default: `true'`

Controls whether npcs can spawn in the world. Can be changed at any time via `server.properties`.

### spawn_protection | Type: `int` | Default: `10`

The radius around world spawn which cannot be modified/interacted with by non-OP players. Can be changed at any time via `server.properties`.

### spiget_resources | Type: `str`

Not mispelled :wink:. See [here](https://github.com/itzg/docker-minecraft-server/blob/master/README.md#auto-downloading-spigotmcbukkitpapermc-plugins) for an explanation.

### spigot_download_url | Type: `str`

Allows you to specify your own download url for a Spigot server JAR.

### spongeversion | Type: `str` | Default: Latest Build

Allows you to specify what version of Sponge to use.

### stop_duration | Type: `int` | Default: `60` (seconds)

Wait-time until the Minecraft `/stop` command will be waited on when the Docker container is stopped.

### sync_chunk_writes | Type: `bool` | Default: `true`

Allows control over synchronous chunk writes. Can be changed at any time via `server.properties`.

### tune_nursery_sizes | Type: `bool`

See [here](https://github.com/itzg/docker-minecraft-server/blob/master/README.md#openj9-specific-options) for a thorough explanation.

### tune_virtualized | Type: `bool`

See [here](https://github.com/itzg/docker-minecraft-server/blob/master/README.md#openj9-specific-options) for a thorough explanation.

### type | Type: `str` | Default: 

The type of server you wish to run. You may pick one of:

* `AIRPLANE`
* `BUKKIT`
* `CANYON`
* `CATSERVER`
* `CURSEFORGE`
* `CUSTOM`
* `FABRIC`
* `FORGE`
* `FTBA` - Used for FTB modpacks, the 'A' is required.
* `MAGMA`
* `MOHIST`
* `PAPER`
* `PURPUR`
* `SPIGOT`
* `SPONGEVANILLA`
* `TUINITY`
* `YATOPIA`

### tz | Type: `str`

Allows you to set the timezone of the docker container/server.

### use_aikar_flags | Type: `bool`

Allows you to enable the use of Aikar's Flags. Read [here](https://mcflags.emc.gs) for more info.

### use_flare_flags | Type: `bool`

Used to add appropriate flags for the [Flare](https://blog.airplane.gg/flare/) profiler.

### use_large_pages | Type: `bool`

Enables support for large page sizes

### use_modpack_start_script | Type: `bool`

Whether to use a FTB/Curseforge Modpack's default `start.bat` batch script over the one built into this utility.

### use_native_transport | Type: `bool` | Default: `true`

Control over optimized packet sending/receiving on Linux 

### view_distance | Type: `int` | Default: `10`

Allows control over the radius of chunks that are loaded. Can be changed at any time via `server.properties`.

### whitelist | Type: `str`

Allows you to preload the server with a whitelist of usernames, comma-delimited.

### world | Type: `str`

Allows you to provide a URL or Container which can provide a world for your server.

### world_index | Type: `int` | Default: `1`

Used if your world (from the above flag) has more than one `level.dat` file
