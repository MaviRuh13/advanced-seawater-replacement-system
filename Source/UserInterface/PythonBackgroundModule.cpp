// Search:
PyObject * backgroundEnableSoftwareTiling(PyObject * poSelf, PyObject * poArgs)
{
	int nIsEnable;
	if (!PyTuple_GetInteger(poArgs, 0, &nIsEnable))
		return Py_BadArgument();

	bool isEnable=nIsEnable ? true : false;

	CPythonBackground& rkBG=CPythonBackground::Instance();
	rkBG.ReserveSoftwareTilingEnable(isEnable);

	CPythonSystem& rkSystem=CPythonSystem::Instance();
	rkSystem.SetSoftwareTiling(isEnable);
	return Py_BuildNone();
}

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
PyObject * backgroundSuDegistir(PyObject * poSelf, PyObject * poArgs){char * szFileName;if (!PyTuple_GetString(poArgs, 0, &szFileName)){ return Py_BuildException(); }CPythonBackground& rkBG = CPythonBackground::Instance();CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();rkMap.SuDegistir(szFileName);return Py_BuildNone();}
PyObject * backgroundSuDegistir2(PyObject * poSelf, PyObject * poArgs){char * szFileName;if (!PyTuple_GetString(poArgs, 0, &szFileName)){ return Py_BuildException(); }CPythonBackground& rkBG = CPythonBackground::Instance();CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();rkMap.SuDegistir2(szFileName);return Py_BuildNone();}
PyObject * backgroundSuDegistir3(PyObject * poSelf, PyObject * poArgs){char * szFileName;if (!PyTuple_GetString(poArgs, 0, &szFileName)){ return Py_BuildException(); }CPythonBackground& rkBG = CPythonBackground::Instance();CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();rkMap.SuDegistir3(szFileName);return Py_BuildNone();}
PyObject * backgroundSuDegistir4(PyObject * poSelf, PyObject * poArgs){char * szFileName;if (!PyTuple_GetString(poArgs, 0, &szFileName)){ return Py_BuildException(); }CPythonBackground& rkBG = CPythonBackground::Instance();CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();rkMap.SuDegistir4(szFileName);return Py_BuildNone();}
PyObject * backgroundSuDegistir5(PyObject * poSelf, PyObject * poArgs){char * szFileName;if (!PyTuple_GetString(poArgs, 0, &szFileName)){ return Py_BuildException(); }CPythonBackground& rkBG = CPythonBackground::Instance();CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();rkMap.SuDegistir5(szFileName);return Py_BuildNone();}
PyObject * backgroundSuDegistir6(PyObject * poSelf, PyObject * poArgs){char * szFileName;if (!PyTuple_GetString(poArgs, 0, &szFileName)){ return Py_BuildException(); }CPythonBackground& rkBG = CPythonBackground::Instance();CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();rkMap.SuDegistir6(szFileName);return Py_BuildNone();}
PyObject * backgroundSuDegistir7(PyObject * poSelf, PyObject * poArgs){char * szFileName;if (!PyTuple_GetString(poArgs, 0, &szFileName)){ return Py_BuildException(); }CPythonBackground& rkBG = CPythonBackground::Instance();CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();rkMap.SuDegistir7(szFileName);return Py_BuildNone();}
PyObject * backgroundSuDegistir8(PyObject * poSelf, PyObject * poArgs){char * szFileName;if (!PyTuple_GetString(poArgs, 0, &szFileName)){ return Py_BuildException(); }CPythonBackground& rkBG = CPythonBackground::Instance();CMapOutdoor& rkMap = rkBG.GetMapOutdoorRef();rkMap.SuDegistir8(szFileName);return Py_BuildNone();}
#endif

// Search:
		{ "IsSoftwareTiling",					backgroundIsSoftwareTiling,					METH_VARARGS }, 

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
		{ "SuDegistir",							backgroundSuDegistir,						METH_VARARGS },
		{ "SuDegistir2",						backgroundSuDegistir2,						METH_VARARGS },
		{ "SuDegistir3",						backgroundSuDegistir3,						METH_VARARGS },
		{ "SuDegistir4",						backgroundSuDegistir4,						METH_VARARGS },
		{ "SuDegistir5",						backgroundSuDegistir5,						METH_VARARGS },
		{ "SuDegistir6",						backgroundSuDegistir6,						METH_VARARGS },
		{ "SuDegistir7",						backgroundSuDegistir7,						METH_VARARGS },
		{ "SuDegistir8",						backgroundSuDegistir8,						METH_VARARGS },
#endif