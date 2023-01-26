from pymonad.either import Left
from bc.tools import checker

def monad_checker(*args):
    """Functions similiarly to checker, except returns either obj or a Left monad

    Returns:
        function: configured checker.
    """

    c = checker(*args)

    def inner(obj):
        """Configured checker

        Args:
            obj (): object being validated.

        Returns:
            obj (): If 'obj' passes validation, returns 'obj' as pass-through; otherwise, returns Left monad
        """

        passed = obj
        try: 
            errs = c(obj)
            if len(errs) > 0:
                raise Exception('; '.join(errs))
        except Exception as ex:
            passed = Left(str(ex))
        finally:
            return passed

    return inner
    