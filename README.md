# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_07:09:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,703 measurements** from **39** stations.
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
| 2026-08-17 07:09:50 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.028 |  |
| 2026-08-17 07:08:30 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:07:55 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-17 07:07:45 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:07:44 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-17 07:07:42 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-17 07:06:29 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | -0.005 |  |
| 2026-08-17 07:06:22 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-17 07:06:16 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 07:06:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.094 |  |
| 2026-08-17 07:05:51 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:05:26 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-08-17 07:05:01 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:05:01 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:04:38 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 07:04:30 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-08-17 07:04:29 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:04:21 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.019 |  |
| 2026-08-17 07:04:21 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:03:43 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:03:38 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 1.006 | 🔺 Rising |
| 2026-08-17 07:03:13 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:03:02 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:02:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:02:47 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.045 |  |
| 2026-08-17 07:02:03 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.001 |  |
| 2026-08-17 07:01:43 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-08-17 07:01:28 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:26 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:14 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.123 |  |
| 2026-08-17 07:01:12 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:10 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:00:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 07:03:38 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 1.006 | 🔺 Rising |
| 2026-08-17 07:06:22 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-17 07:07:55 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-17 06:01:35 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-17 07:04:38 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 07:06:16 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 07:07:42 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-17 07:04:21 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:03:43 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:00:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:05:51 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:03:02 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:12 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:04:48 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:05:35 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:03:13 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:02:47 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:02:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:08:30 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:26 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:05:01 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:05:01 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:10 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:04:29 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:07:45 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:01:28 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 07:02:03 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.001 |  |
| 2026-08-17 07:06:29 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | -0.005 |  |
| 2026-08-17 07:07:44 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-17 07:01:43 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-08-17 07:04:30 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-08-17 07:04:21 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.019 |  |
| 2026-08-17 06:02:12 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-08-17 07:09:50 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.028 |  |
| 2026-08-17 07:05:26 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-08-17 07:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.045 |  |
| 2026-08-17 07:06:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.094 |  |
| 2026-08-17 07:01:14 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)