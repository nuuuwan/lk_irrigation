# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_17:18:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,502 measurements** from **39** stations.
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
| 2026-11-25 17:18:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | 0.000 |  |
| 2026-11-25 17:08:09 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-25 17:07:24 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-25 17:06:45 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-25 17:06:20 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.028 |  |
| 2026-11-25 17:06:17 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-25 17:06:13 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.061 |  |
| 2026-11-25 17:05:57 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 17:05:54 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.020 |  |
| 2026-11-25 17:05:53 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-25 17:05:51 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-25 17:05:46 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 17:05:37 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-11-25 17:05:33 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 17:05:31 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-11-25 17:04:26 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.020 |  |
| 2026-11-25 17:04:21 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.032 |  |
| 2026-11-25 17:04:01 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.090 |  |
| 2026-11-25 17:03:46 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-25 17:03:45 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-25 17:03:33 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-25 17:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.145 |  |
| 2026-11-25 17:03:21 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.090 |  |
| 2026-11-25 17:03:20 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 17:03:08 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-25 17:03:05 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-11-25 17:03:04 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 17:02:50 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-11-25 17:02:48 | Wellawaya (Kirindi Oya) | 2.22 | 🟢 Normal | 0.685 | 🔺 Rising |
| 2026-11-25 17:01:55 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-11-25 17:01:41 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 17:01:40 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 17:01:29 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.033 |  |
| 2026-11-25 17:01:26 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-11-25 17:01:15 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.032 |  |
| 2026-11-25 17:01:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.183 |  |
| 2026-11-25 17:01:07 | Moraketiya (Walawe Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-11-25 17:00:17 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 17:02:48 | Wellawaya (Kirindi Oya) | 2.22 | 🟢 Normal | 0.685 | 🔺 Rising |
| 2026-11-25 17:01:55 | Holombuwa (Kelani Ganga) | 2.04 | 🟢 Normal | 0.589 | 🔺 Rising |
| 2026-11-25 17:02:50 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-11-25 17:06:45 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-25 17:06:17 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-25 17:03:46 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-25 17:05:51 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-25 17:03:08 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-25 17:08:09 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-25 17:05:57 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 17:05:33 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 17:01:41 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 17:03:20 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 17:05:46 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 17:01:40 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 17:05:53 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-25 17:03:04 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 17:18:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | 0.000 |  |
| 2026-11-25 17:03:33 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-25 17:03:45 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-25 17:01:07 | Moraketiya (Walawe Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-11-25 17:05:37 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-11-25 17:05:54 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.020 |  |
| 2026-11-25 17:04:26 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.020 |  |
| 2026-11-25 17:05:31 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-11-25 17:07:24 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 17:06:20 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.028 |  |
| 2026-11-25 17:03:05 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-11-25 17:01:26 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-11-25 17:04:21 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.032 |  |
| 2026-11-25 17:01:15 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.032 |  |
| 2026-11-25 17:01:29 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.033 |  |
| 2026-11-25 17:00:17 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-11-25 17:06:13 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.061 |  |
| 2026-11-25 17:03:21 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.090 |  |
| 2026-11-25 17:04:01 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.090 |  |
| 2026-11-25 17:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.145 |  |
| 2026-11-25 17:01:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)