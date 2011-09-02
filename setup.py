from setuptools import setup, find_packages
import os


version = '1.0dev'


tests_require = [
    ]


setup(name='collective.sales',
      version=version,
      description='A simply online shop solution for plone',
      keywords='',

      long_description=open('README.rst').read() + '\n' + \
          open(os.path.join('docs', 'HISTORY.txt')).read(),

      classifiers=[
        'Framework :: Plone',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        ],

      author='Jonas Baumann',
      author_email='j.baumann@4teamwork.ch',

      url='http://github.com/jone/collective.sales/',
      license='GPL2',

      packages=find_packages('src/collective.sales'),
      package_dir={'': 'src/collective.sales'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        'z3c.autoinclude',
        'plone.app.dexterity [grok]',
        'plone.namedfile',
        ],
      tests_require=tests_require,
      extras_require={
        'tests': tests_require,
        },

      entry_points='''
      [z3c.autoinclude.plugin]
      target = plone
      ''',
      )
