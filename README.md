# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_10:29:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,241 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 10:29:10 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-25 10:12:07 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.084 |  |
| 2026-11-25 10:09:58 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -3.148 |  |
| 2026-11-25 10:09:46 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.080 |  |
| 2026-11-25 10:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-25 10:08:00 | Moraketiya (Walawe Ganga) | 2.60 | 🟢 Normal | -0.223 |  |
| 2026-11-25 10:07:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.136 |  |
| 2026-11-25 10:06:40 | Peradeniya (Mahaweli Ganga) | 3.11 | 🟢 Normal | -0.130 |  |
| 2026-11-25 10:06:25 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.026 |  |
| 2026-11-25 10:06:19 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.177 |  |
| 2026-11-25 10:06:05 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-11-25 10:05:43 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-11-25 10:05:25 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | -0.105 |  |
| 2026-11-25 10:05:16 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | -0.114 |  |
| 2026-11-25 10:05:10 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.146 |  |
| 2026-11-25 10:04:41 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-11-25 10:04:27 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.164 |  |
| 2026-11-25 10:04:12 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:03:51 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:03:47 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-25 10:03:33 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 10:03:30 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-11-25 10:03:30 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-11-25 10:03:22 | Giriulla (Maha Oya) | 2.51 | 🟢 Normal | -0.091 |  |
| 2026-11-25 10:03:12 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-11-25 10:02:58 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:02:41 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:02:32 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 10:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-25 10:02:20 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:40 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.042 |  |
| 2026-11-25 10:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:22 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:13 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -1.150 |  |
| 2026-11-25 10:01:12 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-25 10:01:10 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-25 10:01:06 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:01:06 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 10:01:12 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-25 10:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-25 10:01:10 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-25 10:03:47 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-25 10:02:32 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-25 10:03:33 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 10:29:10 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-25 10:01:22 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:06 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:02:20 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:03:51 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:04:12 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:06 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:02:58 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:02:41 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-11-25 10:03:12 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-11-25 10:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-25 10:03:30 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 10:06:25 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.026 |  |
| 2026-11-25 10:05:43 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-11-25 10:04:41 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-11-25 10:06:05 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-11-25 10:03:30 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-11-25 10:01:40 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.042 |  |
| 2026-11-25 10:09:46 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.080 |  |
| 2026-11-25 10:12:07 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.084 |  |
| 2026-11-25 10:03:22 | Giriulla (Maha Oya) | 2.51 | 🟢 Normal | -0.091 |  |
| 2026-11-25 10:05:25 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | -0.105 |  |
| 2026-11-25 10:05:16 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | -0.114 |  |
| 2026-11-25 10:06:40 | Peradeniya (Mahaweli Ganga) | 3.11 | 🟢 Normal | -0.130 |  |
| 2026-11-25 10:07:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.136 |  |
| 2026-11-25 10:05:10 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.146 |  |
| 2026-11-25 10:04:27 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.164 |  |
| 2026-11-25 10:06:19 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.177 |  |
| 2026-11-25 10:08:00 | Moraketiya (Walawe Ganga) | 2.60 | 🟢 Normal | -0.223 |  |
| 2026-11-25 10:01:13 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -1.150 |  |
| 2026-11-25 10:09:58 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -3.148 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)