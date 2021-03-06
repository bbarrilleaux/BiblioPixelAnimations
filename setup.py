from distutils.core import setup
import BiblioPixelAnimations
import urllib2, json
_ver = "BAD_INSTALL"

try:
    head = urllib2.urlopen("https://api.github.com/repos/ManiacalLabs/BiblioPixelAnimations/git/refs/head").read()
    head_data = json.loads(head)
    if len(head_data) > 0:
        _ver = head_data[0]["object"]["sha"]
except:
    pass

if not 'pip' in __file__:
    print """
    This installer MUST be run from pip!
    Please install using the following command:
    pip install https://github.com/ManiacalLabs/BiblioPixelAnimations/archive/master.zip --upgrade
    """
else:
    setup(
        name='BiblioPixelAnimations',
        version=_ver,
        description='BiblioPixelAnimations is an animation repository for animation classes that work with BiblioPixel: http://github.com/maniacallabs/BiblioPixel',
        author='Adam Haile',
        author_email='adam@maniacallabs.com',
        url='http://github.com/maniacallabs/BiblioPixelAnimations/',
        license='MIT',
        packages=['BiblioPixelAnimations', 'BiblioPixelAnimations.matrix', 'BiblioPixelAnimations.strip', 'BiblioPixelAnimations.game'],
        classifiers = [
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
        ],
    )
