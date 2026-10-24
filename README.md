# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_06:12:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,414 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 06:12:07 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-24 06:10:04 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:08:07 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:08:01 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 06:06:57 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.009 |  |
| 2026-10-24 06:05:44 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-10-24 06:05:29 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.099 |  |
| 2026-10-24 06:04:54 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | -0.028 |  |
| 2026-10-24 06:04:40 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-10-24 06:04:36 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:04:17 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-24 06:03:00 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.082 |  |
| 2026-10-24 06:02:58 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-24 06:02:50 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.21 | 🟢 Normal | -0.190 |  |
| 2026-10-24 06:02:39 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.051 |  |
| 2026-10-24 06:02:34 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.041 |  |
| 2026-10-24 06:02:22 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.020 |  |
| 2026-10-24 06:02:17 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.031 |  |
| 2026-10-24 06:02:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:01:41 | Hanwella (Kelani Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:01:40 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:01:34 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-24 06:01:28 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-24 06:01:22 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.871 |  |
| 2026-10-24 06:01:18 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:01:16 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.015 |  |
| 2026-10-24 06:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-10-24 06:00:58 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-10-24 06:00:42 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-24 06:00:42 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:00:40 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-24 06:00:12 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-24 05:57:10 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.871 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 06:04:17 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-24 06:00:12 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-24 06:00:40 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-24 06:00:42 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-24 06:12:07 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-24 06:01:34 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-24 06:08:01 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 02:01:16 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 06:02:50 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:00:42 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:01:41 | Hanwella (Kelani Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:08:07 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:02:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:04:36 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:10:04 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:01:18 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:01:40 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-24 06:06:57 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.009 |  |
| 2026-10-24 06:02:58 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-24 06:05:44 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-10-24 06:04:40 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.011 |  |
| 2026-10-24 06:01:16 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.015 |  |
| 2026-10-24 06:01:28 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-24 06:02:22 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.020 |  |
| 2026-10-24 06:00:58 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 06:04:54 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | -0.028 |  |
| 2026-10-24 06:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-10-24 06:02:17 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.031 |  |
| 2026-10-24 06:02:34 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.041 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-24 06:02:39 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.051 |  |
| 2026-10-24 06:03:00 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.082 |  |
| 2026-10-24 06:05:29 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.099 |  |
| 2026-10-24 05:02:16 | Moragaswewa (Deduru Oya) | 3.59 | 🟢 Normal | -0.111 |  |
| 2026-10-24 06:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.21 | 🟢 Normal | -0.190 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-24 06:01:22 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.871 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)