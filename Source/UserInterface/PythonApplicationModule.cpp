// Search:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
	PyModule_AddIntConstant(poModule, "MAVIRUH_WATER_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "MAVIRUH_WATER_SYSTEM", 0);
#endif