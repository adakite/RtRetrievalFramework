# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _l2_fp_configuration.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_l2_fp_configuration', [dirname(__file__)])
        except ImportError:
            import _l2_fp_configuration
            return _l2_fp_configuration
        if fp is not None:
            try:
                _mod = imp.load_module('_l2_fp_configuration', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _l2_fp_configuration = swig_import_helper()
    del swig_import_helper
else:
    import _l2_fp_configuration
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


SHARED_PTR_DISOWN = _l2_fp_configuration.SHARED_PTR_DISOWN
def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.generic_object
class L2FpConfiguration(full_physics_swig.generic_object.GenericObject):
    """
    Before running L2 full physics, we need to create the solver that we
    will be using, along with registering whatever output we will be
    generating.

    This class gives the minimum interface needed for the configuration,
    so we can use different methods of actually doing this.

    C++ includes: l2_fp_configuration.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _l2_fp_configuration.delete_L2FpConfiguration
    def _v_logger(self):
        """
        virtual boost::shared_ptr<LogImp> FullPhysics::L2FpConfiguration::logger() const =0
        Logger to use. 
        """
        return _l2_fp_configuration.L2FpConfiguration__v_logger(self)

    @property
    def logger(self):
        return self._v_logger()

    def _v_forward_model(self):
        """
        virtual boost::shared_ptr<ForwardModel> FullPhysics::L2FpConfiguration::forward_model() const =0
        Forward model. Everything should be initialized to the initial guess.

        """
        return _l2_fp_configuration.L2FpConfiguration__v_forward_model(self)

    @property
    def forward_model(self):
        return self._v_forward_model()

    def _v_solver(self):
        """
        virtual boost::shared_ptr<ConnorSolver> FullPhysics::L2FpConfiguration::solver() const =0
        Solver. 
        """
        return _l2_fp_configuration.L2FpConfiguration__v_solver(self)

    @property
    def solver(self):
        return self._v_solver()

    def _v_initial_guess(self):
        """
        virtual boost::shared_ptr<InitialGuess> FullPhysics::L2FpConfiguration::initial_guess() const =0
        Initial guess. 
        """
        return _l2_fp_configuration.L2FpConfiguration__v_initial_guess(self)

    @property
    def initial_guess(self):
        return self._v_initial_guess()

    def output(self):
        """
        virtual void FullPhysics::L2FpConfiguration::output(boost::shared_ptr< Output > &Regular_output, boost::shared_ptr<
        Output > &Error_output) const =0
        Create output, for both a normal run and for an error run (either or
        both can be null if we don't want output).

        This should have all the RegisterOutputBase applied to it that the
        configuration says should be. 
        """
        return _l2_fp_configuration.L2FpConfiguration_output(self)

L2FpConfiguration._v_logger = new_instancemethod(_l2_fp_configuration.L2FpConfiguration__v_logger,None,L2FpConfiguration)
L2FpConfiguration._v_forward_model = new_instancemethod(_l2_fp_configuration.L2FpConfiguration__v_forward_model,None,L2FpConfiguration)
L2FpConfiguration._v_solver = new_instancemethod(_l2_fp_configuration.L2FpConfiguration__v_solver,None,L2FpConfiguration)
L2FpConfiguration._v_initial_guess = new_instancemethod(_l2_fp_configuration.L2FpConfiguration__v_initial_guess,None,L2FpConfiguration)
L2FpConfiguration.output = new_instancemethod(_l2_fp_configuration.L2FpConfiguration_output,None,L2FpConfiguration)
L2FpConfiguration.__str__ = new_instancemethod(_l2_fp_configuration.L2FpConfiguration___str__,None,L2FpConfiguration)
L2FpConfiguration_swigregister = _l2_fp_configuration.L2FpConfiguration_swigregister
L2FpConfiguration_swigregister(L2FpConfiguration)


