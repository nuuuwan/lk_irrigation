# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_04:03:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,211 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Thawalama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 04:03:57 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.090 |  |
| 2026-09-15 04:03:40 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-15 04:03:34 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.013 |  |
| 2026-09-15 04:02:58 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:02:58 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:02:57 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:02:44 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.557 | 🔺 Rising |
| 2026-09-15 04:02:39 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:02:39 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-09-15 04:02:29 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 04:02:06 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 04:01:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.072 |  |
| 2026-09-15 04:01:58 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:01:49 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:01:48 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-09-15 04:01:33 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.040 |  |
| 2026-09-15 04:01:16 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-15 04:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-15 03:38:08 | Thawalama (Gin Ganga) | 4.38 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-09-15 03:29:57 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-15 03:24:03 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 03:02:42 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-15 03:38:08 | Thawalama (Gin Ganga) | 4.38 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-09-15 03:02:15 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-09-15 04:02:44 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.557 | 🔺 Rising |
| 2026-09-15 04:02:39 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-09-15 03:05:49 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-15 04:03:40 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-15 02:01:00 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 03:29:57 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-15 02:03:10 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 04:01:16 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-15 04:02:29 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 04:02:06 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 03:03:51 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 03:08:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:00:56 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:01:49 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:02:39 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:04:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:13:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:03:34 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:01:58 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:49 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:02:58 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:05:01 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 04:02:58 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-15 04:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-15 04:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.013 |  |
| 2026-09-15 04:01:48 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-09-15 04:01:33 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.040 |  |
| 2026-09-15 04:01:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.072 |  |
| 2026-09-15 03:07:05 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.084 |  |
| 2026-09-15 04:03:57 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.090 |  |
| 2026-09-15 03:13:34 | Holombuwa (Kelani Ganga) | 2.09 | 🟢 Normal | -0.173 |  |
| 2026-09-15 03:04:48 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.200 |  |
| 2026-09-15 03:05:17 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)