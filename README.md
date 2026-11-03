# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_20:29:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,002 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 20:29:52 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | -0.014 |  |
| 2026-11-03 20:17:39 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:12:43 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-11-03 20:09:09 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-03 20:08:47 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | 0.747 | 🔺 Rising |
| 2026-11-03 20:08:37 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | 0.444 | 🔺 Rising |
| 2026-11-03 20:08:08 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-03 20:07:29 | Holombuwa (Kelani Ganga) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-11-03 20:07:00 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-03 20:06:41 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-11-03 20:06:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-03 20:06:16 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.031 |  |
| 2026-11-03 20:06:12 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-03 20:05:31 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-11-03 20:04:17 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.068 |  |
| 2026-11-03 20:04:13 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.201 |  |
| 2026-11-03 20:04:01 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:03:43 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.039 |  |
| 2026-11-03 20:03:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:03:16 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-11-03 20:03:12 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-11-03 20:03:12 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-03 20:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.022 |  |
| 2026-11-03 20:03:05 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.054 |  |
| 2026-11-03 20:02:52 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-03 20:02:44 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.092 |  |
| 2026-11-03 20:02:42 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:02:31 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:02:29 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-03 20:02:21 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.069 |  |
| 2026-11-03 20:02:09 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.120 |  |
| 2026-11-03 20:01:48 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-03 20:01:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:01:17 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:00:32 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:00:21 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 20:08:37 | Urawa (Nilwala Ganga) | 2.70 | 🟡 Alert | 0.444 | 🔺 Rising |
| 2026-11-03 20:08:47 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | 0.747 | 🔺 Rising |
| 2026-11-03 20:06:41 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-11-03 20:01:48 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-03 20:03:12 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-03 20:03:16 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-11-03 20:05:31 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-11-03 20:03:12 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-03 20:08:08 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 20:09:09 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-03 20:06:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-03 20:02:29 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-03 20:06:12 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-03 20:02:31 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:02:09 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:01:17 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 20:07:00 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-03 20:17:39 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:01:45 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:04:01 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:03:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:00:32 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-03 20:12:43 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-11-03 20:29:52 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | -0.014 |  |
| 2026-11-03 20:02:52 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-03 20:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.022 |  |
| 2026-11-03 20:07:29 | Holombuwa (Kelani Ganga) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-11-03 20:06:16 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.031 |  |
| 2026-11-03 20:03:43 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.039 |  |
| 2026-11-03 20:03:05 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.054 |  |
| 2026-11-03 20:04:17 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.068 |  |
| 2026-11-03 20:02:21 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.069 |  |
| 2026-11-03 20:02:44 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.092 |  |
| 2026-11-03 20:00:21 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.110 |  |
| 2026-11-03 20:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.120 |  |
| 2026-11-03 20:04:13 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)