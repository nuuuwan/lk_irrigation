# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_07:22:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,120 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 07:22:58 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.047 |  |
| 2026-11-25 07:18:19 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:18:07 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-11-25 07:16:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-11-25 07:15:16 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.008 |  |
| 2026-11-25 07:13:58 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-11-25 07:10:04 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:08:08 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-11-25 07:07:42 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.092 |  |
| 2026-11-25 07:07:41 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.163 |  |
| 2026-11-25 07:06:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:06:45 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-25 07:06:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.047 |  |
| 2026-11-25 07:05:46 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | -96.000 |  |
| 2026-11-25 07:05:43 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -96.000 |  |
| 2026-11-25 07:05:18 | Badalgama (Maha Oya) | 4.18 | 🟢 Normal | -0.066 |  |
| 2026-11-25 07:05:15 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 07:05:00 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.086 |  |
| 2026-11-25 07:04:58 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:04:47 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.283 |  |
| 2026-11-25 07:04:26 | Peradeniya (Mahaweli Ganga) | 3.45 | 🟢 Normal | -0.170 |  |
| 2026-11-25 07:03:54 | Siyambalanduwa (Heda Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-11-25 07:03:49 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.240 |  |
| 2026-11-25 07:03:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.215 |  |
| 2026-11-25 07:02:49 | Giriulla (Maha Oya) | 2.83 | 🟢 Normal | -0.099 |  |
| 2026-11-25 07:02:20 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.096 |  |
| 2026-11-25 07:02:20 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | 0.000 |  |
| 2026-11-25 07:02:16 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.040 |  |
| 2026-11-25 07:02:05 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-25 07:01:45 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:01:37 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 07:01:34 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:01:32 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:01:31 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-25 07:00:52 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.100 |  |
| 2026-11-25 07:00:25 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-25 07:00:11 | Magura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.166 |  |
| 2026-11-25 06:58:20 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 07:02:20 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | 0.000 |  |
| 2026-11-25 06:20:55 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | 18.720 | 🔺 Rising |
| 2026-11-25 07:08:08 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-11-25 07:16:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-11-25 07:00:25 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-25 07:01:37 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 07:02:05 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-25 07:01:31 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-25 07:05:15 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 07:01:32 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:01:45 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:06:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:10:04 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:01:34 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:18:19 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-25 07:15:16 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.008 |  |
| 2026-11-25 07:13:58 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-11-25 07:06:45 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-25 05:02:54 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-11-25 07:18:07 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 07:03:54 | Siyambalanduwa (Heda Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-11-25 07:02:16 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.040 |  |
| 2026-11-25 07:22:58 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.047 |  |
| 2026-11-25 07:06:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.047 |  |
| 2026-11-25 07:05:18 | Badalgama (Maha Oya) | 4.18 | 🟢 Normal | -0.066 |  |
| 2026-11-25 07:05:00 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.086 |  |
| 2026-11-25 07:07:42 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.092 |  |
| 2026-11-25 07:02:20 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.096 |  |
| 2026-11-25 07:02:49 | Giriulla (Maha Oya) | 2.83 | 🟢 Normal | -0.099 |  |
| 2026-11-25 07:00:52 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.100 |  |
| 2026-11-25 07:07:41 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.163 |  |
| 2026-11-25 07:00:11 | Magura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.166 |  |
| 2026-11-25 07:04:26 | Peradeniya (Mahaweli Ganga) | 3.45 | 🟢 Normal | -0.170 |  |
| 2026-11-25 07:03:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.215 |  |
| 2026-11-25 07:03:49 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.240 |  |
| 2026-11-25 07:04:47 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.283 |  |
| 2026-11-25 07:05:46 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | -96.000 |  |
| 2026-11-25 06:05:00 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | -396.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)