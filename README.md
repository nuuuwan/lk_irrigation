# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_05:38:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,054 measurements** from **39** stations.
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
| 2026-09-07 05:38:30 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:31:21 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:31:20 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:31:19 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:30:58 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:30:18 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.034 |  |
| 2026-09-07 05:27:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 05:18:57 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-07 05:14:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-09-07 05:14:02 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -1.257 |  |
| 2026-09-07 05:12:22 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.056 |  |
| 2026-09-07 05:08:47 | Glencourse (Kelani Ganga) | 9.39 | 🟢 Normal | -1.257 |  |
| 2026-09-07 05:07:26 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-09-07 05:07:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:07:12 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-09-07 05:06:51 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:06:28 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.015 |  |
| 2026-09-07 05:06:00 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:05:29 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:04:22 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.115 |  |
| 2026-09-07 05:04:14 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:59 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:59 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:34 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-07 05:03:27 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:02:57 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:02:40 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-09-07 05:02:14 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-07 05:02:06 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:55 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:53 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:15 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 05:01:09 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:09 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:08 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:01 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 05:14:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-09-07 05:02:14 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-07 05:03:34 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-07 05:27:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 05:01:15 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 05:18:57 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-07 05:03:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:27 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:09 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:01 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:07:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:55 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:02:57 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:06:01 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:06:51 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:31:21 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:05:29 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:06:00 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:09 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:00:38 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:04:14 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:59 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:02:06 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:01:51 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:38:30 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:03:59 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:01:53 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:30:58 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:02:06 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 05:07:12 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-09-07 05:02:40 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-09-07 05:07:26 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-09-07 05:06:28 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.015 |  |
| 2026-09-07 05:30:18 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.034 |  |
| 2026-09-07 05:12:22 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.056 |  |
| 2026-09-06 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.114 |  |
| 2026-09-07 05:04:22 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.115 |  |
| 2026-09-07 05:14:02 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -1.257 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)