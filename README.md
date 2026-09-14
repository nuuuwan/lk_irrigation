# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_03:29:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,191 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thawalama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 03:29:57 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-15 03:24:03 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-09-15 03:15:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-09-15 03:13:34 | Holombuwa (Kelani Ganga) | 2.09 | 🟢 Normal | -0.173 |  |
| 2026-09-15 03:13:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:11:57 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:08:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:07:05 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.084 |  |
| 2026-09-15 03:06:19 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:05:49 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-15 03:05:17 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -252.000 |  |
| 2026-09-15 03:05:16 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -252.000 |  |
| 2026-09-15 03:05:04 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 03:05:01 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:04:48 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.200 |  |
| 2026-09-15 03:04:14 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:04:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:03:51 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 03:03:33 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.056 |  |
| 2026-09-15 03:03:10 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.003 |  |
| 2026-09-15 03:03:02 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 03:02:58 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-09-15 03:02:56 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 03:02:49 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:44 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.851 | 🔺 Rising |
| 2026-09-15 03:02:42 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:42 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-15 03:02:24 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-09-15 03:02:15 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-09-15 03:02:15 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:48 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-09-15 03:01:47 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:44 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-09-15 03:00:56 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 02:19:23 | Thawalama (Gin Ganga) | 4.27 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-09-15 03:02:42 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-15 03:02:44 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.851 | 🔺 Rising |
| 2026-09-15 03:02:15 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-09-15 03:02:24 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-09-15 03:02:58 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-09-15 03:05:49 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-15 02:01:00 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 03:29:57 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-15 02:03:10 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 03:02:56 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 03:03:02 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 03:03:51 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 03:05:04 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 03:08:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:00:56 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:02:01 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:42 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:47 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:04:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:13:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:06:19 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:44 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:49 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:15 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:05:01 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:03:10 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.003 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-15 03:01:48 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-09-15 03:15:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-09-15 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-09-15 03:24:03 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-09-15 03:03:33 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.056 |  |
| 2026-09-15 03:07:05 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.084 |  |
| 2026-09-15 03:13:34 | Holombuwa (Kelani Ganga) | 2.09 | 🟢 Normal | -0.173 |  |
| 2026-09-15 03:04:48 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.200 |  |
| 2026-09-15 03:05:17 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)