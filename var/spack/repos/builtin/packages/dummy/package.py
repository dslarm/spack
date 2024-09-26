# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install dummy
#
# You can edit this file again by typing:
#
#     spack edit dummy
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Dummy(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url = "file:///home/ubuntu/dummy-main.tar.gz"
    manual_download = True
    redistribute(source=False, binary=False)

    depends_on("blas")
    version("main")
    

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        with working_dir(self.build_directory):
            make()
            mkdir(prefix.bin)
            installer = Executable("/bin/cp")
            installer("hello_cxx", prefix.bin)

