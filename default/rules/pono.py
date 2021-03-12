from src.base import SourceLocation, Target

SourceLocation(
	name = 'smt-switch',
	vcs = 'git',
	location = 'https://github.com/makaimann/smt-switch',
	revision = 'c3957b2e7fec8af4fab24df089230c88e523c0e6'
)

SourceLocation(
	name = 'pono',
	vcs = 'git',
	location = 'https://github.com/upscale-project/pono',
	revision = 'origin/master'
)

Target(
	name = 'smt-switch',
	sources = [ 'smt-switch' ],
	arch = [ 'linux-x64', 'darwin-x64', 'linux-arm', 'linux-arm64' ],
	license_file = 'smt-switch/LICENSE',
)

Target(
	name = 'pono',
	sources = [ 'pono' ],
	dependencies = [ 'smt-switch' ],
	arch = [ 'linux-x64', 'darwin-x64', 'linux-arm', 'linux-arm64' ],
	license_file = 'pono/LICENSE',
)
