# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_08:22:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,532 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 08:22:08 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.008 |  |
| 2026-11-03 08:14:35 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-03 08:13:21 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.136 |  |
| 2026-11-03 08:09:14 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:08:15 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.034 |  |
| 2026-11-03 08:07:55 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.147 |  |
| 2026-11-03 08:07:54 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:07:54 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.032 |  |
| 2026-11-03 08:06:54 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.124 |  |
| 2026-11-03 08:06:47 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.019 |  |
| 2026-11-03 08:06:27 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.079 |  |
| 2026-11-03 08:06:23 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.098 |  |
| 2026-11-03 08:06:16 | Glencourse (Kelani Ganga) | 11.26 | 🟢 Normal | -0.185 |  |
| 2026-11-03 08:05:32 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.108 |  |
| 2026-11-03 08:05:23 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.061 |  |
| 2026-11-03 08:04:58 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:04:56 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 08:04:44 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-03 08:04:13 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.059 |  |
| 2026-11-03 08:04:05 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.116 |  |
| 2026-11-03 08:03:48 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-03 08:03:40 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 08:03:20 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.021 |  |
| 2026-11-03 08:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-03 08:03:06 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.096 |  |
| 2026-11-03 08:02:43 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -144.000 |  |
| 2026-11-03 08:02:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:02:42 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -144.000 |  |
| 2026-11-03 08:02:33 | Moragaswewa (Deduru Oya) | 3.82 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-03 08:02:18 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 08:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-03 08:02:12 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-03 08:02:11 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-03 08:02:04 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-03 08:01:57 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:01:56 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 08:01:45 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-11-03 08:01:36 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:01:25 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.089 |  |
| 2026-11-03 08:00:59 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.042 |  |
| 2026-11-03 08:00:57 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 08:04:44 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-03 08:02:33 | Moragaswewa (Deduru Oya) | 3.82 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-03 08:03:48 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-03 08:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-03 08:02:18 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 08:04:56 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 08:02:12 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-03 08:03:40 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 08:14:35 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-03 08:01:56 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 08:04:58 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:01:36 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:01:57 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:09:14 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:02:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:07:54 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:22:08 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.008 |  |
| 2026-11-03 08:02:04 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-03 08:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-03 08:06:47 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.019 |  |
| 2026-11-03 08:02:11 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-03 08:03:20 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.021 |  |
| 2026-11-03 08:01:45 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-11-03 08:07:54 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.032 |  |
| 2026-11-03 08:08:15 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.034 |  |
| 2026-11-03 08:00:59 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.042 |  |
| 2026-11-03 08:04:13 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.059 |  |
| 2026-11-03 08:05:23 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.061 |  |
| 2026-11-03 08:06:27 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.079 |  |
| 2026-11-03 08:01:25 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.089 |  |
| 2026-11-03 08:03:06 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.096 |  |
| 2026-11-03 08:06:23 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.098 |  |
| 2026-11-03 08:05:32 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.108 |  |
| 2026-11-03 08:04:05 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.116 |  |
| 2026-11-03 08:06:54 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.124 |  |
| 2026-11-03 08:13:21 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.136 |  |
| 2026-11-03 08:07:55 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.147 |  |
| 2026-11-03 08:06:16 | Glencourse (Kelani Ganga) | 11.26 | 🟢 Normal | -0.185 |  |
| 2026-11-03 08:02:43 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)