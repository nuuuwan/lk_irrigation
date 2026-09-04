# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_11:05:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 11:05:17 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.029 |  |
| 2026-09-04 11:04:50 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:04:37 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:04:34 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-04 11:04:26 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:04:22 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.020 |  |
| 2026-09-04 11:04:10 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.021 |  |
| 2026-09-04 11:04:01 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 11:03:25 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-09-04 11:03:10 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:03:01 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:57 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-09-04 11:02:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:28 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:27 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-04 11:02:27 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-09-04 11:02:22 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-09-04 11:02:10 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:09 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:01:44 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-04 11:01:42 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:01:39 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.030 |  |
| 2026-09-04 11:01:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:00:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-09-04 11:00:50 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:00:21 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.091 |  |
| 2026-09-04 11:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:00:09 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 10:25:57 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 10:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-09-04 11:01:44 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-04 11:02:27 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-04 10:02:41 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-04 10:02:05 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-04 11:04:01 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 10:04:15 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 11:02:10 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:00:09 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:09 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:01:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:03:10 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:04:50 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 10:08:32 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:03:01 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-04 10:05:06 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:04:26 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:28 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:04:37 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 10:05:38 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:00:50 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:01:42 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:22 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 10:03:06 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.005 |  |
| 2026-09-04 10:03:52 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-09-04 11:04:34 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-04 11:04:22 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.020 |  |
| 2026-09-04 11:03:25 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-09-04 11:04:10 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.021 |  |
| 2026-09-04 11:02:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2026-09-04 11:05:17 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.029 |  |
| 2026-09-04 11:01:39 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.030 |  |
| 2026-09-04 11:02:27 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-09-04 11:02:57 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-09-04 10:03:11 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-09-04 11:00:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-09-04 11:00:21 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)