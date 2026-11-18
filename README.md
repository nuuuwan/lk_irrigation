# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_06:17:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,914 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 06:17:29 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-18 06:12:56 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-18 06:12:21 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:10:24 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:09:07 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:08:47 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:07:53 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:06:16 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-11-18 06:04:55 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-11-18 06:04:36 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.050 |  |
| 2026-11-18 06:04:32 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:04:22 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:04:21 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-11-18 06:04:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-11-18 06:03:33 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:03:22 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-18 06:02:47 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:02:38 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:02:28 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.987 |  |
| 2026-11-18 06:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:02:21 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 06:02:10 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:01:53 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 06:01:51 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:01:41 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:01:33 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-18 06:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-11-18 06:01:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-18 06:01:25 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-18 06:01:20 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:01:16 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-18 06:01:11 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-18 06:01:02 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.026 |  |
| 2026-11-18 06:00:57 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-11-18 06:00:17 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-11-18 05:48:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-11-18 05:40:04 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-18 05:37:37 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.026 |  |
| 2026-11-18 05:37:36 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 06:01:16 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-18 06:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-11-18 06:01:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-18 06:03:22 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-18 06:02:21 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 06:01:25 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-18 06:17:29 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-18 06:01:33 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-18 06:01:53 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 06:12:56 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-18 06:01:41 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:08:47 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:02:38 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:41 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-18 03:22:42 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 05:03:35 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:02:10 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:07:53 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:09:07 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:10:24 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:04:22 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:02:47 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:04:32 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:03:33 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:01:51 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:12:21 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:01:20 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:04:55 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-11-18 06:00:57 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-11-18 06:00:17 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-11-18 06:06:16 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-11-18 06:04:21 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-11-18 06:01:11 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-18 06:01:02 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.026 |  |
| 2026-11-18 06:04:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-11-18 06:04:36 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.050 |  |
| 2026-11-18 06:02:28 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.987 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)