// Search:
void CMapOutdoor::UnloadWaterTexture()
{
	for (int i = 0; i < 30; ++i)
		m_WaterInstances[i].Destroy();
}

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
void CMapOutdoor::LoadOzelSu(const char * szDosyaAdi){UnloadWaterTexture();char buf[256];for (BYTE i = 0; i < 30; ++i){snprintf(buf, sizeof(buf), ((std::string)szDosyaAdi+"/%02d.dds").c_str(), i + 1);m_WaterInstances[i].SetImagePointer((CGraphicImage *)CResourceManager::Instance().GetResourcePointer(buf));}}
void CMapOutdoor::LoadOzelSu2(const char * szDosyaAdi2){UnloadWaterTexture();char buf[256];for (BYTE i = 0; i < 30; ++i){_snprintf(buf, sizeof(buf), ((std::string)szDosyaAdi2+"/%02d.dds").c_str(), i + 1);m_WaterInstances[i].SetImagePointer((CGraphicImage *)CResourceManager::Instance().GetResourcePointer(buf));}}
void CMapOutdoor::LoadOzelSu3(const char * szDosyaAdi3){UnloadWaterTexture();char buf[256];for (BYTE i = 0; i < 30; ++i){_snprintf(buf, sizeof(buf), ((std::string)szDosyaAdi3+"/%02d.dds").c_str(), i + 1);m_WaterInstances[i].SetImagePointer((CGraphicImage *)CResourceManager::Instance().GetResourcePointer(buf));}}
void CMapOutdoor::LoadOzelSu4(const char * szDosyaAdi4){UnloadWaterTexture();char buf[256];for (BYTE i = 0; i < 30; ++i){_snprintf(buf, sizeof(buf), ((std::string)szDosyaAdi4+"/%02d.dds").c_str(), i + 1);m_WaterInstances[i].SetImagePointer((CGraphicImage *)CResourceManager::Instance().GetResourcePointer(buf));}}
void CMapOutdoor::LoadOzelSu5(const char * szDosyaAdi5){UnloadWaterTexture();char buf[256];for (BYTE i = 0; i < 30; ++i){_snprintf(buf, sizeof(buf), ((std::string)szDosyaAdi5+"/%02d.dds").c_str(), i + 1);m_WaterInstances[i].SetImagePointer((CGraphicImage *)CResourceManager::Instance().GetResourcePointer(buf));}}
void CMapOutdoor::LoadOzelSu6(const char * szDosyaAdi6){UnloadWaterTexture();char buf[256];for (BYTE i = 0; i < 30; ++i){_snprintf(buf, sizeof(buf), ((std::string)szDosyaAdi6+"/%02d.dds").c_str(), i + 1);m_WaterInstances[i].SetImagePointer((CGraphicImage *)CResourceManager::Instance().GetResourcePointer(buf));}}
void CMapOutdoor::LoadOzelSu7(const char * szDosyaAdi7){UnloadWaterTexture();char buf[256];for (BYTE i = 0; i < 30; ++i){_snprintf(buf, sizeof(buf), ((std::string)szDosyaAdi7+"/%02d.dds").c_str(), i + 1);m_WaterInstances[i].SetImagePointer((CGraphicImage *)CResourceManager::Instance().GetResourcePointer(buf));}}
void CMapOutdoor::LoadOzelSu8(const char * szDosyaAdi8){UnloadWaterTexture();char buf[256];for (BYTE i = 0; i < 30; ++i){_snprintf(buf, sizeof(buf), ((std::string)szDosyaAdi8+"/%02d.dds").c_str(), i + 1);m_WaterInstances[i].SetImagePointer((CGraphicImage *)CResourceManager::Instance().GetResourcePointer(buf));}}
#endif