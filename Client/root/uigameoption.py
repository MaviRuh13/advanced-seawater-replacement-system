# Search:
		self.RefreshShowSalesText()

# Add:
		if app.MAVIRUH_WATER_SYSTEM:
			self.RefreshWaterOption()

# Search:
		self.showsalesTextButtonList = []

# Add:
		if app.MAVIRUH_WATER_SYSTEM:
			self.maviruhWaterButtonList = []

# Search:
			self.showsalesTextButtonList.append(GetObject("salestext_off_button"))

# Add:
			if app.MAVIRUH_WATER_SYSTEM:
				self.maviruhWaterButtonList.append(GetObject("maviruh_water_0"))
				self.maviruhWaterButtonList.append(GetObject("maviruh_water_1"))
				self.maviruhWaterButtonList.append(GetObject("maviruh_water_2"))
				self.maviruhWaterButtonList.append(GetObject("maviruh_water_3"))
				self.maviruhWaterButtonList.append(GetObject("maviruh_water_4"))
				self.maviruhWaterButtonList.append(GetObject("maviruh_water_5"))
				self.maviruhWaterButtonList.append(GetObject("maviruh_water_6"))
				self.maviruhWaterButtonList.append(GetObject("maviruh_water_7"))

# Search:
		self.showsalesTextButtonList[1].SAFE_SetEvent(self.__OnClickSalesTextOffButton)

# Add:
		if app.MAVIRUH_WATER_SYSTEM:
			self.maviruhWaterButtonList[0].SAFE_SetEvent(self.__OnClickWater0Button)
			self.maviruhWaterButtonList[1].SAFE_SetEvent(self.__OnClickWater1Button)
			self.maviruhWaterButtonList[2].SAFE_SetEvent(self.__OnClickWater2Button)
			self.maviruhWaterButtonList[3].SAFE_SetEvent(self.__OnClickWater3Button)
			self.maviruhWaterButtonList[4].SAFE_SetEvent(self.__OnClickWater4Button)
			self.maviruhWaterButtonList[5].SAFE_SetEvent(self.__OnClickWater5Button)
			self.maviruhWaterButtonList[6].SAFE_SetEvent(self.__OnClickWater6Button)
			self.maviruhWaterButtonList[7].SAFE_SetEvent(self.__OnClickWater7Button)

# Search:
	def __OnClickSalesTextOffButton(self):
		systemSetting.SetShowSalesTextFlag(False)
		self.RefreshShowSalesText()

# Add:
	if app.MAVIRUH_WATER_SYSTEM:
		def __OnClickWater0Button(self):
			systemSetting.SetMaviRuhSuDegistir(0)
			background.SuDegistir("d:/ymir Work/special/water")
			self.RefreshWaterOption()
		def __OnClickWater1Button(self):
			systemSetting.SetMaviRuhSuDegistir(1)
			background.SuDegistir2("d:/ymir Work/special/eski_saltanat_suyu")
			self.RefreshWaterOption()
		def __OnClickWater2Button(self):
			systemSetting.SetMaviRuhSuDegistir(2)
			background.SuDegistir3("d:/ymir Work/special/saltanat_suyu")
			self.RefreshWaterOption()
		def __OnClickWater3Button(self):
			systemSetting.SetMaviRuhSuDegistir(3)
			background.SuDegistir4("d:/ymir Work/special/deniz_suyu")
			self.RefreshWaterOption()
		def __OnClickWater4Button(self):
			systemSetting.SetMaviRuhSuDegistir(4)
			background.SuDegistir5("d:/ymir Work/special/maviruh_deniz_suyu")
			self.RefreshWaterOption()
		def __OnClickWater5Button(self):
			systemSetting.SetMaviRuhSuDegistir(5)
			background.SuDegistir6("d:/ymir Work/special/comedy_water")
			self.RefreshWaterOption()
		def __OnClickWater6Button(self):
			systemSetting.SetMaviRuhSuDegistir(6)
			background.SuDegistir6("d:/ymir Work/special/new_water")
			self.RefreshWaterOption()
		def __OnClickWater7Button(self):
			systemSetting.SetMaviRuhSuDegistir(7)
			background.SuDegistir6("d:/ymir Work/special/lava")
			self.RefreshWaterOption()
		def RefreshWaterOption(self):
			if systemSetting.GetMaviRuhSuDegistir() == 0:
				self.maviruhWaterButtonList[0].Down()
				self.maviruhWaterButtonList[1].SetUp()
				self.maviruhWaterButtonList[2].SetUp()
				self.maviruhWaterButtonList[3].SetUp()
				self.maviruhWaterButtonList[4].SetUp()
				self.maviruhWaterButtonList[5].SetUp()
				self.maviruhWaterButtonList[6].SetUp()
				self.maviruhWaterButtonList[7].SetUp()
			elif systemSetting.GetMaviRuhSuDegistir() == 1:
				self.maviruhWaterButtonList[0].SetUp()
				self.maviruhWaterButtonList[1].Down()
				self.maviruhWaterButtonList[2].SetUp()
				self.maviruhWaterButtonList[3].SetUp()
				self.maviruhWaterButtonList[4].SetUp()
				self.maviruhWaterButtonList[5].SetUp()
				self.maviruhWaterButtonList[6].SetUp()
				self.maviruhWaterButtonList[7].SetUp()
			elif systemSetting.GetMaviRuhSuDegistir() == 2:
				self.maviruhWaterButtonList[0].SetUp()
				self.maviruhWaterButtonList[1].SetUp()
				self.maviruhWaterButtonList[2].Down()
				self.maviruhWaterButtonList[3].SetUp()
				self.maviruhWaterButtonList[4].SetUp()
				self.maviruhWaterButtonList[5].SetUp()
				self.maviruhWaterButtonList[6].SetUp()
				self.maviruhWaterButtonList[7].SetUp()
			elif systemSetting.GetMaviRuhSuDegistir() == 3:
				self.maviruhWaterButtonList[0].SetUp()
				self.maviruhWaterButtonList[1].SetUp()
				self.maviruhWaterButtonList[2].SetUp()
				self.maviruhWaterButtonList[3].Down()
				self.maviruhWaterButtonList[4].SetUp()
				self.maviruhWaterButtonList[5].SetUp()
				self.maviruhWaterButtonList[6].SetUp()
				self.maviruhWaterButtonList[7].SetUp()
			elif systemSetting.GetMaviRuhSuDegistir() == 4:
				self.maviruhWaterButtonList[0].SetUp()
				self.maviruhWaterButtonList[1].SetUp()
				self.maviruhWaterButtonList[2].SetUp()
				self.maviruhWaterButtonList[3].SetUp()
				self.maviruhWaterButtonList[4].Down()
				self.maviruhWaterButtonList[5].SetUp()
				self.maviruhWaterButtonList[6].SetUp()
				self.maviruhWaterButtonList[7].SetUp()
			elif systemSetting.GetMaviRuhSuDegistir() == 5:
				self.maviruhWaterButtonList[0].SetUp()
				self.maviruhWaterButtonList[1].SetUp()
				self.maviruhWaterButtonList[2].SetUp()
				self.maviruhWaterButtonList[3].SetUp()
				self.maviruhWaterButtonList[4].SetUp()
				self.maviruhWaterButtonList[5].Down()
				self.maviruhWaterButtonList[6].SetUp()
				self.maviruhWaterButtonList[7].SetUp()
			elif systemSetting.GetMaviRuhSuDegistir() == 6:
				self.maviruhWaterButtonList[0].SetUp()
				self.maviruhWaterButtonList[1].SetUp()
				self.maviruhWaterButtonList[2].SetUp()
				self.maviruhWaterButtonList[3].SetUp()
				self.maviruhWaterButtonList[4].SetUp()
				self.maviruhWaterButtonList[5].SetUp()
				self.maviruhWaterButtonList[6].Down()
				self.maviruhWaterButtonList[7].SetUp()
			else:
				self.maviruhWaterButtonList[0].SetUp()
				self.maviruhWaterButtonList[1].SetUp()
				self.maviruhWaterButtonList[2].SetUp()
				self.maviruhWaterButtonList[3].SetUp()
				self.maviruhWaterButtonList[4].SetUp()
				self.maviruhWaterButtonList[5].SetUp()
				self.maviruhWaterButtonList[6].SetUp()
				self.maviruhWaterButtonList[7].Down()