# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_00:10:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,415 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 00:10:06 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.062 |  |
| 2026-10-22 00:08:58 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-22 00:07:47 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | -1.196 |  |
| 2026-10-22 00:07:32 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:06:15 | Siyambalanduwa (Heda Oya) | 2.47 | 🟢 Normal | -0.543 |  |
| 2026-10-22 00:06:01 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 00:06:00 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-10-22 00:05:52 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-22 00:05:39 | Rathnapura (Kalu Ganga) | 5.30 | 🟡 Alert | 0.401 | 🔺 Rising |
| 2026-10-22 00:05:37 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -0.078 |  |
| 2026-10-22 00:05:01 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-22 00:05:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-22 00:04:33 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-22 00:04:22 | Yaka Wewa (Ma Oya) | 1.60 | 🟢 Normal | -0.095 |  |
| 2026-10-22 00:04:14 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 00:04:05 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.041 |  |
| 2026-10-22 00:03:26 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.024 |  |
| 2026-10-22 00:03:17 | Deraniyagala (Kelani Ganga) | 2.68 | 🟢 Normal | -0.495 |  |
| 2026-10-22 00:02:58 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:02:58 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:02:58 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-10-22 00:02:54 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.115 |  |
| 2026-10-22 00:02:53 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | -0.070 |  |
| 2026-10-22 00:02:48 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:02:46 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | -1.196 |  |
| 2026-10-22 00:02:30 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 00:02:15 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.130 |  |
| 2026-10-22 00:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-22 00:01:22 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 00:05:39 | Rathnapura (Kalu Ganga) | 5.30 | 🟡 Alert | 0.401 | 🔺 Rising |
| 2026-10-21 23:07:06 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-10-21 22:08:34 | Holombuwa (Kelani Ganga) | 1.89 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-10-22 00:06:00 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-22 00:05:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-21 23:05:37 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-22 00:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-21 23:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-22 00:01:22 | Kuda Oya (Kirindi Oya) | 2.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-22 00:05:52 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-22 00:04:33 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 23:04:34 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 00:04:14 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 00:02:30 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 00:06:01 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 00:08:58 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-22 00:05:01 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 00:02:48 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:02:58 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:07:32 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:02:58 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-21 23:06:43 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-10-22 00:02:58 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-10-21 22:01:52 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.021 |  |
| 2026-10-22 00:03:26 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.024 |  |
| 2026-10-22 00:04:05 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.041 |  |
| 2026-10-22 00:10:06 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.062 |  |
| 2026-10-22 00:02:53 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | -0.070 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-22 00:05:37 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -0.078 |  |
| 2026-10-22 00:04:22 | Yaka Wewa (Ma Oya) | 1.60 | 🟢 Normal | -0.095 |  |
| 2026-10-22 00:02:54 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.115 |  |
| 2026-10-22 00:02:15 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.130 |  |
| 2026-10-22 00:03:17 | Deraniyagala (Kelani Ganga) | 2.68 | 🟢 Normal | -0.495 |  |
| 2026-10-22 00:06:15 | Siyambalanduwa (Heda Oya) | 2.47 | 🟢 Normal | -0.543 |  |
| 2026-10-22 00:07:47 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | -1.196 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)