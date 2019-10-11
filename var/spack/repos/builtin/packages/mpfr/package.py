# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mpfr(AutotoolsPackage):
    """The MPFR library is a C library for multiple-precision
       floating-point computations with correct rounding."""

    homepage = "https://www.mpfr.org/"
    url      = "https://ftpmirror.gnu.org/mpfr/mpfr-4.0.2.tar.bz2"

    version('4.0.2', sha256='c05e3f02d09e0e9019384cdd58e0f19c64e6db1fd6f5ecf77b4b1c61ca253acc')
    version('4.0.1', sha256='a4d97610ba8579d380b384b225187c250ef88cfe1d5e7226b89519374209b86b')
    version('4.0.0', sha256='6aa31fbf3bd1f9f95bcfa241590a9d11cb0f874e2bb93b99c9e2de8eaea6d5fd')
    version('3.1.6', sha256='cf4f4b2d80abb79e820e78c8077b6725bbbb4e8f41896783c899087be0e94068')
    version('3.1.5', sha256='ca498c1c7a74dd37a576f353312d1e68d490978de4395fa28f1cbd46a364e658')
    version('3.1.4', sha256='d3103a80cdad2407ed581f3618c4bed04e0c92d1cf771a65ead662cc397f7775')
    version('3.1.3', sha256='f63bb459157cacd223caac545cb816bcdb5a0de28b809e7748b82e9eb89b0afd')
    version('3.1.2', sha256='79c73f60af010a30a5c27a955a1d2d01ba095b72537dab0ecaad57f5a7bb1b6b')

    # mpir is a drop-in replacement for gmp
    depends_on('gmp@4.1:')  # 4.2.3 or higher is recommended
    depends_on('gmp@5.0:', when='@4.0.0:')  # https://www.mpfr.org/mpfr-4.0.0/

    # Check the Bugs section of old release pages for patches.
    # https://www.mpfr.org/mpfr-X.Y.Z/#bugs
    patches = {
        '4.0.2': 'f2d2a530acb5e70e1a9d5b80881dbb4a504d56535c4bc103d83e0bb630172029',
        '4.0.1': '5230aab653fa8675fc05b5bdd3890e071e8df49a92a9d58c4284024affd27739',
        '3.1.6': '66a5d58364113a21405fc53f4a48f4e8',
        '3.1.5': '1dc5fe65feb5607b89fe0f410d53b627',
        '3.1.4': 'd124381573404fe83654c7d5a79aeabf',
        '3.1.3': 'ebd1d835e0ae2fd8a9339210ccd1d0a8',
        '3.1.2': '9f96a5c7cac1d6cd983ed9cf7d997074',
    }

    for ver, checksum in patches.items():
        patch('https://www.mpfr.org/mpfr-{0}/allpatches'.format(ver),
              when='@' + ver, sha256=checksum)

    def configure_args(self):
        args = [
            '--with-gmp=' + self.spec['gmp'].prefix,
        ]
        return args
