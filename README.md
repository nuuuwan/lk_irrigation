# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_18:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,916 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 18:03:22 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:03:20 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-11-22 18:03:19 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 18:02:57 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-22 18:02:53 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:51 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-11-22 18:02:44 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.031 |  |
| 2026-11-22 18:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-11-22 18:02:11 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.018 |  |
| 2026-11-22 18:02:10 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 3.214 | 🔺 Rising |
| 2026-11-22 18:02:10 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.043 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:01:57 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.148 |  |
| 2026-11-22 18:01:41 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-22 18:01:34 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.089 |  |
| 2026-11-22 18:01:25 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.033 |  |
| 2026-11-22 18:01:23 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:01:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-11-22 18:01:07 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 18:00:50 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:36 | Moragaswewa (Deduru Oya) | 3.56 | 🟢 Normal | -0.123 |  |
| 2026-11-22 18:00:21 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 18:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:09 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-22 17:28:13 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.018 |  |
| 2026-11-22 17:24:11 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 18:02:10 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 3.214 | 🔺 Rising |
| 2026-11-22 18:01:41 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-22 18:00:09 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 17:06:59 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-22 18:00:21 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 18:03:19 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 17:09:46 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:01:23 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:01:07 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:50 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:53 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 17:03:00 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:03:22 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-22 17:02:17 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-22 18:02:51 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-11-22 17:09:20 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-11-22 18:02:11 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.018 |  |
| 2026-11-22 18:02:57 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-22 17:24:11 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.024 |  |
| 2026-11-22 18:02:44 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.031 |  |
| 2026-11-22 17:02:20 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-11-22 18:01:25 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.033 |  |
| 2026-11-22 17:06:41 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | -0.039 |  |
| 2026-11-22 18:03:20 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-11-22 18:02:10 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.043 |  |
| 2026-11-22 18:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-11-22 18:01:10 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-11-22 17:04:21 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.080 |  |
| 2026-11-22 17:07:47 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.086 |  |
| 2026-11-22 17:06:49 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.089 |  |
| 2026-11-22 18:01:34 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.089 |  |
| 2026-11-22 18:00:36 | Moragaswewa (Deduru Oya) | 3.56 | 🟢 Normal | -0.123 |  |
| 2026-11-22 18:01:57 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)