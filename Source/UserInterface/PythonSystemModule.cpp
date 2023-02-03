// Search:
PyObject * systemIsShowSalesText(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonSystem::Instance().IsShowSalesText());
}

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
PyObject * systemGetMaviRuhSuDegistir(PyObject * poSelf, PyObject * poArgs){return Py_BuildValue("i", CPythonSystem::Instance().GetMaviRuhSuDegistir());}
PyObject * systemSetMaviRuhSuDegistir(PyObject * poSelf, PyObject * poArgs){int iFlag;if (!PyTuple_GetInteger(poArgs, 0, &iFlag))return Py_BuildException();CPythonSystem::Instance().SetMaviRuhSuDegistir(iFlag);return Py_BuildNone();}
#endif

// Search:
		{ "GetShadowLevel",				systemGetShadowLevel,			METH_VARARGS },
		{ "SetShadowLevel",				systemSetShadowLevel,			METH_VARARGS },

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
		{ "GetMaviRuhSuDegistir",		systemGetMaviRuhSuDegistir,		METH_VARARGS },
		{ "SetMaviRuhSuDegistir",		systemSetMaviRuhSuDegistir,		METH_VARARGS },
#endif