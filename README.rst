=============
quart-smorest 
=============

.. image:: https://img.shields.io/badge/marshmallow-2%20|%203-blue.svg
    :target: https://marshmallow.readthedocs.io/en/latest/upgrading.html
    :alt: marshmallow 2/3 compatible

.. image:: https://img.shields.io/badge/OAS-2%20|%203-green.svg
    :target: https://github.com/OAI/OpenAPI-Specification
    :alt: OpenAPI Specification 2/3 compatible

.. image:: https://img.shields.io/pypi/l/flask-smorest.svg
    :target: https://flask-smorest.readthedocs.io/en/latest/license.html
    :alt: License

.. image:: https://readthedocs.org/projects/flask-smorest/badge/
    :target: http://flask-smorest.readthedocs.io/
    :alt: Documentation

'cause everybody wants s'more
=============================

**quart-smorest** REST API framework built upon `Quart <https://pgjones.gitlab.io/quart/>`_ and
`marshmallow <https://github.com/marshmallow-code/marshmallow>`_. It's an adaptation or **flask-smorest** to use Quart primitives and make it work with that very close, yet sometimes different framework. It's currently under development. **Do not try to use it for something useful yet**.

- Serialization, deserialization and validation using marshmallow ``Schema``
- Explicit validation error messages returned in response
- Database-agnostic
- OpenAPI (Swagger) specification automatically generated and exposed with
  `ReDoc <https://github.com/Rebilly/ReDoc>`_ or
  `Swagger UI <https://swagger.io/tools/swagger-ui/>`_
- Pagination
- ETag

Install
=======

::

    pip install flask-smorest

flask-smorest supports Python >= 3.6.

Documentation
=============

Full documentation is available at http://flask-smorest.readthedocs.io/.

Support flask-smorest
======================

If you'd like to support the future of the original project, please consider
contributing to marshmallow's Open Collective:

.. image:: https://opencollective.com/marshmallow/donate/button.png
    :target: https://opencollective.com/marshmallow
    :width: 200
    :alt: Donate to our collective

License
=======

MIT licensed. See the `LICENSE <https://github.com/hadware/quart-smorest/blob/master/LICENSE>`_ file for more details.
