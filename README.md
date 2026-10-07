# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_03:28:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 03:28:43 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-10-08 03:12:46 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:10:57 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.243 |  |
| 2026-10-08 03:09:40 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.029 |  |
| 2026-10-08 03:08:05 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.056 |  |
| 2026-10-08 03:07:13 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 03:06:35 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 03:06:15 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.148 |  |
| 2026-10-08 03:05:58 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.051 |  |
| 2026-10-08 03:05:42 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-08 03:05:09 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-08 03:05:03 | Pitabeddara (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-08 03:04:48 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:04:41 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:04:30 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:04:28 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-08 03:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-08 03:04:15 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 03:04:02 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-08 03:03:47 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-10-08 03:03:27 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:03:27 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-08 03:03:27 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | 0.504 | 🔺 Rising |
| 2026-10-08 03:03:20 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 03:03:18 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-10-08 03:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.012 |  |
| 2026-10-08 03:02:30 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-08 03:02:22 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-10-08 03:02:14 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:01:21 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:01:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:00:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:00:18 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 02:55:41 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-10-08 02:50:22 | Dunamale (Aththanagalu Oya) | 2.81 | 🟢 Normal | 0.504 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 03:02:22 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-10-08 03:03:27 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | 0.504 | 🔺 Rising |
| 2026-10-08 03:28:43 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-10-08 03:03:47 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-10-08 03:07:13 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 03:05:09 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-08 03:03:27 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 03:03:20 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 03:04:15 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 02:06:48 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 03:06:35 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 03:00:18 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:01:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:00:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:02:14 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:03:27 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:12:46 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:04:41 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:04:30 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:01:21 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:04:48 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 03:04:28 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-08 03:05:42 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-08 03:02:30 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-08 03:05:03 | Pitabeddara (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-08 03:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.012 |  |
| 2026-10-08 03:04:02 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-08 03:03:18 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-10-08 03:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-08 03:09:40 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.029 |  |
| 2026-10-08 01:03:23 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-10-08 03:05:58 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.051 |  |
| 2026-10-08 03:08:05 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.056 |  |
| 2026-10-08 03:06:15 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.148 |  |
| 2026-10-08 03:10:57 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.243 |  |
| 2026-10-08 02:07:51 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | -648.000 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)