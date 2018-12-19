# This file was contributed to the Volatility Framework Version 3.
# Copyright (C) 2018 Volatility Foundation.
#
# THE LICENSED WORK IS PROVIDED UNDER THE TERMS OF THE Volatility Contributors
# Public License V1.0("LICENSE") AS FIRST COMPLETED BY: Volatility Foundation,
# Inc. ANY USE, PUBLIC DISPLAY, PUBLIC PERFORMANCE, REPRODUCTION OR DISTRIBUTION
# OF, OR PREPARATION OF SUBSEQUENT WORKS, DERIVATIVE WORKS OR DERIVED WORKS BASED
# ON, THE LICENSED WORK CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS LICENSE AND ITS
# TERMS, WHETHER OR NOT SUCH RECIPIENT READS THE TERMS OF THE LICENSE. "LICENSED
# WORK,” “RECIPIENT" AND “DISTRIBUTOR" ARE DEFINED IN THE LICENSE. A COPY OF THE
# LICENSE IS LOCATED IN THE TEXT FILE ENTITLED "LICENSE.txt" ACCOMPANYING THE
# CONTENTS OF THIS FILE. IF A COPY OF THE LICENSE DOES NOT ACCOMPANY THIS FILE, A
# COPY OF THE LICENSE MAY ALSO BE OBTAINED AT THE FOLLOWING WEB SITE:
# https://www.volatilityfoundation.org/license/vcpl_v1.0
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
# specific language governing rights and limitations under the License.
#

from volatility.framework import interfaces
from volatility.framework.symbols import intermed
from volatility.framework.symbols.linux import extensions


class LinuxKernelIntermedSymbols(intermed.IntermediateSymbolTable):
    provides = {"type": "interface"}

    def __init__(self, context: interfaces.context.ContextInterface, config_path: str, name: str, isf_url: str) -> None:
        super().__init__(context = context, config_path = config_path, name = name, isf_url = isf_url)

        # Set-up Linux specific types
        self.set_type_class('file', extensions.struct_file)
        self.set_type_class('list_head', extensions.list_head)
        self.set_type_class('mm_struct', extensions.mm_struct)
        self.set_type_class('super_block', extensions.super_block)
        self.set_type_class('task_struct', extensions.task_struct)
        self.set_type_class('vm_area_struct', extensions.vm_area_struct)
        self.set_type_class('qstr', extensions.qstr)
        self.set_type_class('dentry', extensions.dentry)
        self.set_type_class('fs_struct', extensions.fs_struct)
        self.set_type_class('files_struct', extensions.files_struct)
        self.set_type_class('vfsmount', extensions.vfsmount)
        self.set_type_class('module', extensions.module)

        if 'mount' in self.types:
            self.set_type_class('mount', extensions.mount)
