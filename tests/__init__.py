#!/usr/bin/env python
"""
Tests for python-mime

>>> import os
>>> from mime import MimeType
>>> mime = MimeType.fromName("foo.txt")
>>> mime.name()
'text/plain'
>>> mime.comment()
'plain text document'
>>> mime.comment(lang="fr")
'document texte brut'
>>> mime.type()
'text'
>>> mime.subtype()
'plain'
>>> mime.genericMime()
<MimeType: text/x-generic>
>>> mime.genericMime().name()
'text/x-generic'
>>> MimeType.fromName("foo.TXT").name()
'text/plain'
>>> MimeType.fromName("foo.C").name()
'text/x-c++src'
>>> MimeType.fromName("foo.c").name()
'text/x-csrc'
>>> MimeType.fromInode("/dev/sda").name()
'inode/blockdevice'
>>> MimeType.fromInode("/dev/null").name()
'inode/chardevice'
>>> MimeType.fromInode("/").name()
'inode/mount-point'
>>> MimeType.fromInode(".").name()
'inode/directory'
>>> MimeType("text/x-lua").comment()
'Lua script'
>>> MimeType("application/x-does-not-exist")
<MimeType: application/x-does-not-exist>
>>> MimeType("application/x-does-not-exist").comment()
>>> MimeType.fromName("foo.mkv").name()
'video/x-matroska'
>>> MimeType("application/javascript").aliases()
['application/x-javascript', 'text/javascript']
>>> MimeType("text/xml").aliasOf()
'application/xml'
>>> MimeType("text/x-python").subClassOf()
[<MimeType: application/x-executable>, <MimeType: text/plain>]
>>> MimeType("application/zip").genericIcon()
'package-x-generic'
>>> MimeType("application/zip").icon()
'application-zip'
>>> MimeType("text/plain").genericIcon()
'text-x-generic'
>>> MimeType("application/zip").isInstance("application/zip")
True
>>> MimeType("application/x-chrome-extension").isInstance("application/zip")
True
>>> MimeType("text/plain").isInstance("application/zip")
False
>>> MimeType.fromScheme("http://example.com").name()
'x-scheme-handler/http'
>>> MimeType.fromScheme("ftp://example.com").name()
'x-scheme-handler/ftp'
>>> MimeType.fromScheme("mailto:user@example.com").name()
'x-scheme-handler/mailto'
>>> MimeType.fromScheme("file:///").name()
'x-scheme-handler/file'
>>> f = open("test.tmp", "w")
>>> f.close()
>>> MimeType.fromContent(f.name).name()
'application/x-zerosize'
>>> os.remove(f.name)


Tests for MIME actions

>>> from mime.xdg.actions import ActionsFile
>>> f = open("mimeapps.list.tmp", "w")
>>> _ = f.write('''
... [Added Associations]
... application/xml=juffed.desktop;
... audio/x-mpegurl=smplayer2.desktop;juffed.desktop;
... audio/x-scpls=smplayer2.desktop;;
... video/x-msvideo=smplayer2.desktop;;;mplayer.desktop;
... text/xml=chromium.desktop;
...
... [Default Applications]
... text/html=chromium.desktop
...
... [Removed Associations]
... application/xml=wine-extension-xml.desktop;kde4-kwrite.desktop;wine-extension-txt.desktop;
... '''
... )
>>> f.close()
>>> mimeapps = ActionsFile()
>>> mimeapps.parse(f.name)
>>> assocs = mimeapps.get("Added Associations")
>>> assocs["video/x-msvideo"]
['mplayer.desktop', 'smplayer2.desktop']
>>> assocs["audio/x-scpls"]
['smplayer2.desktop']
>>> assocs["audio/x-mpegurl"]
['juffed.desktop', 'smplayer2.desktop']
>>> assocs["application/xml"]
['chromium.desktop', 'juffed.desktop']

>>> MimeType("text/html").defaultApplication()
'chromium.desktop'
>>> MimeType("text/html").bestApplication()
'chromium.desktop'
>>> MimeType("x-scheme-handler/http").bestApplication()
'chromium.desktop'
>>> 'juffed.desktop' in MimeType("text/plain").associations()
True

>>> os.remove(f.name)
"""

if __name__ == "__main__":
	import doctest
	doctest.testmod()
