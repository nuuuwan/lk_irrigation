# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_19:35:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,245 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 19:35:09 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-21 19:09:49 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.226 |  |
| 2026-10-21 19:09:45 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.017 |  |
| 2026-10-21 19:09:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.036 |  |
| 2026-10-21 19:09:09 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 19:08:11 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-21 19:07:54 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-21 19:07:24 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.018 |  |
| 2026-10-21 19:06:43 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-10-21 19:06:32 | Kithulgala (Kelani Ganga) | 2.73 | 🟢 Normal | -0.047 |  |
| 2026-10-21 19:05:52 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 19:05:30 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 19:05:22 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 19:05:11 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:04:57 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:04:54 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-21 19:04:34 | Deraniyagala (Kelani Ganga) | 3.32 | 🟢 Normal | 1.662 | 🔺 Rising |
| 2026-10-21 19:04:28 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-21 19:04:21 | Wellawaya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.365 |  |
| 2026-10-21 19:04:20 | Nakkala (Kumbukkan Oya) | 2.01 | 🟢 Normal | -0.088 |  |
| 2026-10-21 19:04:09 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.019 |  |
| 2026-10-21 19:04:07 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:04:02 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:03:23 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:03:22 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 19:03:13 | Peradeniya (Mahaweli Ganga) | 4.22 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-21 19:03:06 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:02:43 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-21 19:02:23 | Nawalapitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-10-21 19:02:20 | Yaka Wewa (Ma Oya) | 1.85 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-10-21 19:02:16 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-10-21 19:01:37 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-10-21 19:01:34 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:00:48 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-21 19:00:22 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:00:12 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 19:04:34 | Deraniyagala (Kelani Ganga) | 3.32 | 🟢 Normal | 1.662 | 🔺 Rising |
| 2026-10-21 19:02:23 | Nawalapitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-10-21 19:02:20 | Yaka Wewa (Ma Oya) | 1.85 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-10-21 19:03:13 | Peradeniya (Mahaweli Ganga) | 4.22 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-21 19:35:09 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-21 19:00:48 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-21 19:02:43 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-21 19:07:54 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-21 19:08:11 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-21 19:04:28 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-21 19:04:54 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-21 19:09:09 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-21 19:05:30 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 19:05:22 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 19:03:22 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 19:05:52 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 19:04:07 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:05:11 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:00:22 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:01:34 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:04:02 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:03:23 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:03:06 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:04:57 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:00:12 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 19:09:45 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.017 |  |
| 2026-10-21 19:07:24 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.018 |  |
| 2026-10-21 19:04:09 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.019 |  |
| 2026-10-21 19:02:16 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-10-21 19:06:43 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-10-21 19:01:37 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-10-21 19:09:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.036 |  |
| 2026-10-21 19:06:32 | Kithulgala (Kelani Ganga) | 2.73 | 🟢 Normal | -0.047 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-21 19:04:20 | Nakkala (Kumbukkan Oya) | 2.01 | 🟢 Normal | -0.088 |  |
| 2026-10-21 19:09:49 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.226 |  |
| 2026-10-21 19:04:21 | Wellawaya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.365 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)