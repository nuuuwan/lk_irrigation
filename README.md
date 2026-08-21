# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_23:14:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,893 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 23:14:24 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-21 23:13:30 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:11:02 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:10:56 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:10:35 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:09:05 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 23:07:08 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:07:03 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-21 23:06:57 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-21 23:06:52 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:06:33 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 23:06:20 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:05:13 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 23:04:54 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -2.842 |  |
| 2026-08-21 23:04:49 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-08-21 23:03:38 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -2.842 |  |
| 2026-08-21 23:03:36 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:03:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:02:53 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-21 23:02:51 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:02:40 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:02:40 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:02:33 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 23:02:31 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.050 |  |
| 2026-08-21 23:02:27 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-08-21 23:02:17 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-08-21 23:02:09 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-08-21 23:01:44 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-08-21 23:01:33 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 23:01:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:01:15 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-08-21 23:00:49 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:00:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:00:13 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:00:12 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:55:15 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 23:04:49 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-08-21 23:14:24 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-21 23:06:57 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-21 23:07:03 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-21 22:11:24 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-21 23:05:13 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 23:06:33 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 23:09:05 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 23:02:53 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-21 23:02:33 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 23:01:33 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 23:02:51 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:38 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:00:12 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:01:15 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:00:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:11:02 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:00:49 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:24 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:07:08 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:10:35 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:00:13 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:02:40 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:03:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:01:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:13:30 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:06:52 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:03:36 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:10:56 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:02:40 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-08-21 23:02:27 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-08-21 23:02:17 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-08-21 23:01:44 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-08-21 23:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-08-21 23:02:09 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-08-21 23:02:31 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.050 |  |
| 2026-08-21 23:04:54 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -2.842 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)