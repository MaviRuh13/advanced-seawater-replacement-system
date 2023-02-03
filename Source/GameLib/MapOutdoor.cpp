// Search:
void CMapOutdoor::SetEnvironmentScreenFilter()
{
	if (!mc_pEnvironmentData)
		return;

	m_ScreenFilter.SetEnable(mc_pEnvironmentData->bFilteringEnable);
	m_ScreenFilter.SetBlendType(mc_pEnvironmentData->byFilteringAlphaSrc, mc_pEnvironmentData->byFilteringAlphaDest);
	m_ScreenFilter.SetColor(mc_pEnvironmentData->FilteringColor);
}

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
void CMapOutdoor::SuDegistir(const char * c_szFileName){LoadOzelSu(c_szFileName);}
void CMapOutdoor::SuDegistir2(const char * c_szFileName){LoadOzelSu2(c_szFileName);}
void CMapOutdoor::SuDegistir3(const char * c_szFileName){LoadOzelSu3(c_szFileName);}
void CMapOutdoor::SuDegistir4(const char * c_szFileName){LoadOzelSu4(c_szFileName);}
void CMapOutdoor::SuDegistir5(const char * c_szFileName){LoadOzelSu5(c_szFileName);}
void CMapOutdoor::SuDegistir6(const char * c_szFileName){LoadOzelSu6(c_szFileName);}
void CMapOutdoor::SuDegistir7(const char * c_szFileName){LoadOzelSu7(c_szFileName);}
void CMapOutdoor::SuDegistir8(const char * c_szFileName){LoadOzelSu8(c_szFileName);}
#endif