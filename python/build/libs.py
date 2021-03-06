import re
from os.path import abspath

from build.project import Project
from build.zlib import ZlibProject
from build.autotools import AutotoolsProject
from build.ffmpeg import FfmpegProject
from build.boost import BoostProject

libogg = AutotoolsProject(
    'http://downloads.xiph.org/releases/ogg/libogg-1.3.3.tar.xz',
    '4f3fc6178a533d392064f14776b23c397ed4b9f48f5de297aba73b643f955c08',
    'lib/libogg.a',
    [
        '--disable-shared', '--enable-static',
    ],
)

libvorbis = AutotoolsProject(
    'http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.6.tar.xz',
    'af00bb5a784e7c9e69f56823de4637c350643deedaf333d0fa86ecdba6fcb415',
    'lib/libvorbis.a',
    [
        '--disable-shared', '--enable-static',
    ],

    edits={
        # this option is not understood by clang
        'configure': lambda data: data.replace('-mno-ieee-fp', ' '),
    }
)

opus = AutotoolsProject(
    'https://archive.mozilla.org/pub/opus/opus-1.2.1.tar.gz',
    'cfafd339ccd9c5ef8d6ab15d7e1a412c054bf4cb4ecbbbcc78c12ef2def70732',
    'lib/libopus.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-doc',
        '--disable-extra-programs',
    ],

    # suppress "visibility default" from opus_defines.h
    cppflags='-DOPUS_EXPORT=',
)

flac = AutotoolsProject(
    'http://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz',
    '91cfc3ed61dc40f47f050a109b08610667d73477af6ef36dcad31c31a4a8d53f',
    'lib/libFLAC.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-xmms-plugin', '--disable-cpplibs',
        '--disable-doxygen-docs',
    ],
    subdirs=['include', 'src/libFLAC'],
)

zlib = ZlibProject(
    'http://zlib.net/zlib-1.2.11.tar.xz',
    '4ff941449631ace0d4d203e3483be9dbc9da454084111f97ea0a2114e19bf066',
    'lib/libz.a',
)

libid3tag = AutotoolsProject(
    'ftp://ftp.mars.org/pub/mpeg/libid3tag-0.15.1b.tar.gz',
    'e5808ad997ba32c498803822078748c3',
    'lib/libid3tag.a',
    [
        '--disable-shared', '--enable-static',

        # without this, libid3tag's configure.ac ignores -O* and -f*
        '--disable-debugging',
    ],
    autogen=True,

    edits={
        # fix bug in libid3tag's configure.ac which discards all but the last optimization flag
        'configure.ac': lambda data: re.sub(r'optimize="\$1"', r'optimize="$optimize $1"', data, count=1),
    }
)

libmad = AutotoolsProject(
    'ftp://ftp.mars.org/pub/mpeg/libmad-0.15.1b.tar.gz',
    '1be543bc30c56fb6bea1d7bf6a64e66c',
    'lib/libmad.a',
    [
        '--disable-shared', '--enable-static',

        # without this, libmad's configure.ac ignores -O* and -f*
        '--disable-debugging',
    ],
    autogen=True,
)

liblame = AutotoolsProject(
    'http://downloads.sourceforge.net/project/lame/lame/3.100/lame-3.100.tar.gz',
    'ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e',
    'lib/libmp3lame.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-gtktest', '--disable-analyzer-hooks',
        '--disable-decoder', '--disable-frontend',
    ],
)

ffmpeg = FfmpegProject(
    'http://ffmpeg.org/releases/ffmpeg-4.0.tar.xz',
    'ed945daf40b124e77a685893cc025d086f638bc703183460aff49508edb3a43f',
    'lib/libavcodec.a',
    [
        '--disable-shared', '--enable-static',
        '--enable-gpl',
        '--enable-small',
        '--disable-pthreads',
        '--disable-programs',
        '--disable-doc',
        '--disable-avdevice',
        '--disable-swresample',
        '--disable-swscale',
        '--disable-postproc',
        '--disable-avfilter',
        '--disable-lzo',
        '--disable-faan',
        '--disable-pixelutils',
        '--disable-network',
        '--disable-encoders',
        '--disable-muxers',
        '--disable-protocols',
        '--disable-devices',
        '--disable-filters',
        '--disable-v4l2_m2m',

        '--disable-parser=bmp',
        '--disable-parser=cavsvideo',
        '--disable-parser=dvbsub',
        '--disable-parser=dvdsub',
        '--disable-parser=dvd_nav',
        '--disable-parser=flac',
        '--disable-parser=g729',
        '--disable-parser=gsm',
        '--disable-parser=h261',
        '--disable-parser=h263',
        '--disable-parser=h264',
        '--disable-parser=hevc',
        '--disable-parser=mjpeg',
        '--disable-parser=mlp',
        '--disable-parser=mpeg4video',
        '--disable-parser=mpegvideo',
        '--disable-parser=opus',
        '--disable-parser=vc1',
        '--disable-parser=vp3',
        '--disable-parser=vp8',
        '--disable-parser=vp9',
        '--disable-parser=png',
        '--disable-parser=pnm',
        '--disable-parser=xma',

        '--disable-demuxer=aqtitle',
        '--disable-demuxer=ass',
        '--disable-demuxer=bethsoftvid',
        '--disable-demuxer=bink',
        '--disable-demuxer=cavsvideo',
        '--disable-demuxer=cdxl',
        '--disable-demuxer=dvbsub',
        '--disable-demuxer=dvbtxt',
        '--disable-demuxer=h261',
        '--disable-demuxer=h263',
        '--disable-demuxer=h264',
        '--disable-demuxer=ico',
        '--disable-demuxer=image2',
        '--disable-demuxer=jacosub',
        '--disable-demuxer=lrc',
        '--disable-demuxer=microdvd',
        '--disable-demuxer=mjpeg',
        '--disable-demuxer=mjpeg_2000',
        '--disable-demuxer=mpegps',
        '--disable-demuxer=mpegvideo',
        '--disable-demuxer=mpl2',
        '--disable-demuxer=mpsub',
        '--disable-demuxer=pjs',
        '--disable-demuxer=rawvideo',
        '--disable-demuxer=realtext',
        '--disable-demuxer=sami',
        '--disable-demuxer=scc',
        '--disable-demuxer=srt',
        '--disable-demuxer=stl',
        '--disable-demuxer=subviewer',
        '--disable-demuxer=subviewer1',
        '--disable-demuxer=swf',
        '--disable-demuxer=tedcaptions',
        '--disable-demuxer=vobsub',
        '--disable-demuxer=vplayer',
        '--disable-demuxer=webvtt',
        '--disable-demuxer=yuv4mpegpipe',

        # we don't need these decoders, because we have the dedicated
        # libraries
        '--disable-decoder=flac',
        '--disable-decoder=opus',
        '--disable-decoder=vorbis',

        # audio codecs nobody uses
        '--disable-decoder=atrac1',
        '--disable-decoder=atrac3',
        '--disable-decoder=atrac3al',
        '--disable-decoder=atrac3p',
        '--disable-decoder=atrac3pal',
        '--disable-decoder=binkaudio_dct',
        '--disable-decoder=binkaudio_rdft',
        '--disable-decoder=bmv_audio',
        '--disable-decoder=dsicinaudio',
        '--disable-decoder=dvaudio',
        '--disable-decoder=metasound',
        '--disable-decoder=paf_audio',
        '--disable-decoder=ra_144',
        '--disable-decoder=ra_288',
        '--disable-decoder=ralf',
        '--disable-decoder=qdm2',
        '--disable-decoder=qdmc',

        # disable lots of image and video codecs
        '--disable-decoder=ass',
        '--disable-decoder=asv1',
        '--disable-decoder=asv2',
        '--disable-decoder=apng',
        '--disable-decoder=avrn',
        '--disable-decoder=avrp',
        '--disable-decoder=bethsoftvid',
        '--disable-decoder=bink',
        '--disable-decoder=bmp',
        '--disable-decoder=bmv_video',
        '--disable-decoder=cavs',
        '--disable-decoder=ccaption',
        '--disable-decoder=cdgraphics',
        '--disable-decoder=clearvideo',
        '--disable-decoder=dirac',
        '--disable-decoder=dsicinvideo',
        '--disable-decoder=dvbsub',
        '--disable-decoder=dvdsub',
        '--disable-decoder=dvvideo',
        '--disable-decoder=exr',
        '--disable-decoder=ffv1',
        '--disable-decoder=ffvhuff',
        '--disable-decoder=ffwavesynth',
        '--disable-decoder=flic',
        '--disable-decoder=flv',
        '--disable-decoder=fraps',
        '--disable-decoder=gif',
        '--disable-decoder=h261',
        '--disable-decoder=h263',
        '--disable-decoder=h263i',
        '--disable-decoder=h263p',
        '--disable-decoder=h264',
        '--disable-decoder=hevc',
        '--disable-decoder=hnm4_video',
        '--disable-decoder=hq_hqa',
        '--disable-decoder=hqx',
        '--disable-decoder=idcin',
        '--disable-decoder=iff_ilbm',
        '--disable-decoder=indeo2',
        '--disable-decoder=indeo3',
        '--disable-decoder=indeo4',
        '--disable-decoder=indeo5',
        '--disable-decoder=interplay_video',
        '--disable-decoder=jacosub',
        '--disable-decoder=jpeg2000',
        '--disable-decoder=jpegls',
        '--disable-decoder=microdvd',
        '--disable-decoder=mimic',
        '--disable-decoder=mjpeg',
        '--disable-decoder=mmvideo',
        '--disable-decoder=mpl2',
        '--disable-decoder=motionpixels',
        '--disable-decoder=mpeg1video',
        '--disable-decoder=mpeg2video',
        '--disable-decoder=mpeg4',
        '--disable-decoder=mpegvideo',
        '--disable-decoder=mscc',
        '--disable-decoder=msmpeg4_crystalhd',
        '--disable-decoder=msmpeg4v1',
        '--disable-decoder=msmpeg4v2',
        '--disable-decoder=msmpeg4v3',
        '--disable-decoder=msvideo1',
        '--disable-decoder=mszh',
        '--disable-decoder=mvc1',
        '--disable-decoder=mvc2',
        '--disable-decoder=on2avc',
        '--disable-decoder=paf_video',
        '--disable-decoder=png',
        '--disable-decoder=qdraw',
        '--disable-decoder=qpeg',
        '--disable-decoder=rawvideo',
        '--disable-decoder=realtext',
        '--disable-decoder=roq',
        '--disable-decoder=roq_dpcm',
        '--disable-decoder=rscc',
        '--disable-decoder=rv10',
        '--disable-decoder=rv20',
        '--disable-decoder=rv30',
        '--disable-decoder=rv40',
        '--disable-decoder=sami',
        '--disable-decoder=sheervideo',
        '--disable-decoder=snow',
        '--disable-decoder=srt',
        '--disable-decoder=stl',
        '--disable-decoder=subrip',
        '--disable-decoder=subviewer',
        '--disable-decoder=subviewer1',
        '--disable-decoder=svq1',
        '--disable-decoder=svq3',
        '--disable-decoder=tiff',
        '--disable-decoder=tiertexseqvideo',
        '--disable-decoder=truemotion1',
        '--disable-decoder=truemotion2',
        '--disable-decoder=truemotion2rt',
        '--disable-decoder=twinvq',
        '--disable-decoder=utvideo',
        '--disable-decoder=vc1',
        '--disable-decoder=vmdvideo',
        '--disable-decoder=vp3',
        '--disable-decoder=vp5',
        '--disable-decoder=vp6',
        '--disable-decoder=vp7',
        '--disable-decoder=vp8',
        '--disable-decoder=vp9',
        '--disable-decoder=vqa',
        '--disable-decoder=webvtt',
        '--disable-decoder=wmv1',
        '--disable-decoder=wmv2',
        '--disable-decoder=wmv3',
        '--disable-decoder=yuv4',
    ],
)

curl = AutotoolsProject(
    'http://curl.haxx.se/download/curl-7.59.0.tar.xz',
    'e44eaabdf916407585bf5c7939ff1161e6242b6b015d3f2f5b758b2a330461fc',
    'lib/libcurl.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-debug',
        '--enable-http',
        '--enable-ipv6',
        '--disable-ftp', '--disable-file',
        '--disable-ldap', '--disable-ldaps',
        '--disable-rtsp', '--disable-proxy', '--disable-dict', '--disable-telnet',
        '--disable-tftp', '--disable-pop3', '--disable-imap', '--disable-smtp',
        '--disable-smb',
        '--disable-gopher',
        '--disable-manual',
        '--disable-threaded-resolver', '--disable-verbose', '--disable-sspi',
        '--disable-crypto-auth', '--disable-ntlm-wb', '--disable-tls-srp', '--disable-cookies',
        '--without-ssl', '--without-gnutls', '--without-nss', '--without-libssh2',
    ],

    patches='src/lib/curl/patches',
)

libnfs = AutotoolsProject(
    'https://github.com/sahlberg/libnfs/archive/libnfs-2.0.0.tar.gz',
    '7ea6cd8fa6c461d01091e584d424d28e137d23ff4b65b95d01a3fd0ef95d120e',
    'lib/libnfs.a',
    [
        '--disable-shared', '--enable-static',
        '--disable-debug',

        # work around -Wtautological-compare
        '--disable-werror',
    ],
    base='libnfs-libnfs-2.0.0',
    autoreconf=True,
)

boost = BoostProject(
    'http://downloads.sourceforge.net/project/boost/boost/1.66.0/boost_1_66_0.tar.bz2',
    '5721818253e6a0989583192f96782c4a98eb6204965316df9f5ad75819225ca9',
    'include/boost/version.hpp',
)
