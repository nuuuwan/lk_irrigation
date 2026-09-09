# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_05:43:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,873 measurements** from **39** stations.
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
| 2026-09-09 05:43:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.077 |  |
| 2026-09-09 05:13:31 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.043 |  |
| 2026-09-09 05:12:52 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-09 05:08:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:08:31 | Peradeniya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.106 |  |
| 2026-09-09 05:08:12 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-09-09 05:07:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-09-09 05:06:02 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 05:05:33 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:05:07 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:04:07 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-09 05:04:07 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.034 |  |
| 2026-09-09 05:03:44 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-09 05:03:44 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:03:44 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-09-09 05:03:32 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.577 | 🔺 Rising |
| 2026-09-09 05:03:18 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:03:16 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-09 05:02:53 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:02:50 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:02:45 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-09 05:02:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:02:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-09-09 05:02:19 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:02:12 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-09 05:01:52 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:01:50 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:01:26 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:01:07 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-09-09 05:00:40 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:00:37 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:00:14 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:00:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 05:03:32 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.577 | 🔺 Rising |
| 2026-09-09 05:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-09-09 05:02:12 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-09 05:03:16 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-09 05:03:44 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-09 05:00:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-09 05:06:02 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 05:12:52 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-09 05:08:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:00:37 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 04:06:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:00:40 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:02:19 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:02:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:05:02 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:01:26 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:05:07 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:02:53 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:00:14 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:01:52 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:03:44 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:05:33 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:01:07 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:02:50 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:03:18 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:01:50 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:03:44 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-09 05:04:07 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-09 05:02:45 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-09 05:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-09-09 05:08:12 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-09-09 05:07:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-09-08 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.034 |  |
| 2026-09-09 05:04:07 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.034 |  |
| 2026-09-09 05:13:31 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.043 |  |
| 2026-09-09 05:02:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-09-09 05:43:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.077 |  |
| 2026-09-09 05:08:31 | Peradeniya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)