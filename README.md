# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_01:09:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,020 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 01:09:41 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:08:56 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 01:08:32 | Hanwella (Kelani Ganga) | 3.67 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-26 01:07:39 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 01:06:12 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | -0.105 |  |
| 2026-10-26 01:05:48 | Putupaula (Kalu Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 01:05:40 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 01:05:34 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-26 01:05:28 | Rathnapura (Kalu Ganga) | 6.12 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-26 01:04:47 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.138 |  |
| 2026-10-26 01:04:42 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 01:04:32 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.102 |  |
| 2026-10-26 01:03:42 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 01:03:40 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-26 01:03:29 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:02:52 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.110 |  |
| 2026-10-26 01:02:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 01:02:21 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.040 |  |
| 2026-10-26 01:02:18 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 01:02:09 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 01:02:03 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:01:55 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 01:01:49 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-10-26 01:01:46 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:01:44 | Ellagawa (Kalu Ganga) | 7.84 | 🟢 Normal | -0.041 |  |
| 2026-10-26 01:01:42 | Moragaswewa (Deduru Oya) | 2.05 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-10-26 01:00:57 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:00:55 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-26 01:00:24 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.074 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 01:05:28 | Rathnapura (Kalu Ganga) | 6.12 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-26 00:06:38 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | -0.029 |  |
| 2026-10-26 01:01:42 | Moragaswewa (Deduru Oya) | 2.05 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-10-26 01:00:55 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-26 01:05:34 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-26 00:02:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-26 01:08:32 | Hanwella (Kelani Ganga) | 3.67 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 01:03:40 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-26 01:00:24 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-25 22:04:38 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-26 01:03:42 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 00:06:27 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 01:05:40 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 01:01:55 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 01:02:18 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 01:02:09 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 01:08:56 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 00:06:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-26 01:04:42 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 01:05:48 | Putupaula (Kalu Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 01:02:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 01:07:39 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 00:03:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:09:41 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:01:46 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:03:29 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:00:57 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:02:03 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:08:55 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-10-26 01:01:49 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.031 |  |
| 2026-10-26 01:02:21 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.040 |  |
| 2026-10-26 01:01:44 | Ellagawa (Kalu Ganga) | 7.84 | 🟢 Normal | -0.041 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-26 01:04:32 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.102 |  |
| 2026-10-26 01:06:12 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | -0.105 |  |
| 2026-10-26 01:02:52 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.110 |  |
| 2026-10-26 01:04:47 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)