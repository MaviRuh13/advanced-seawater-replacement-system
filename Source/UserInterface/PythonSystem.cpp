// Search:
	m_Config.bShowSalesText		= true;

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
	m_Config.bMaviRuhSuDegistir	= 0;
#endif

// Search:
void CPythonSystem::SetShowSalesTextFlag(int iFlag)
{
	m_Config.bShowSalesText = iFlag == 1 ? true : false;
}

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
int CPythonSystem::GetMaviRuhSuDegistir(){return m_Config.bMaviRuhSuDegistir;}
void CPythonSystem::SetMaviRuhSuDegistir(unsigned int level){m_Config.bMaviRuhSuDegistir = MIN(level, 8);}
#endif

// Search:
		else if (!stricmp(command, "SHOW_SALESTEXT"))
			m_Config.bShowSalesText = atoi(value) == 1 ? true : false;

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
		else if (!stricmp(command, "MAVIRUH_SU_DEGISTIR"))
			m_Config.bMaviRuhSuDegistir = atoi(value);
#endif

// Search:
	fprintf(fp, "SHADOW_LEVEL				%d\n", m_Config.iShadowLevel);

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
	fprintf(fp, "MAVIRUH_SU_DEGISTIR		%d\n", m_Config.bMaviRuhSuDegistir);
#endif