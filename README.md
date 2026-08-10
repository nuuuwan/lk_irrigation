# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_07:16:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,436 measurements** from **39** stations.
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
| 2026-08-10 07:16:24 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.013 |  |
| 2026-08-10 07:12:39 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-08-10 07:07:40 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 07:07:04 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.068 |  |
| 2026-08-10 07:06:53 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:06:33 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-08-10 07:06:01 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-10 07:05:59 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-10 07:05:27 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:05:26 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:05:20 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:05:12 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:05:09 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-10 07:04:46 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:04:31 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-10 07:04:25 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-10 07:04:07 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.020 |  |
| 2026-08-10 07:04:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.174 |  |
| 2026-08-10 07:04:02 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.078 |  |
| 2026-08-10 07:04:02 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 07:03:55 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:03:12 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.011 |  |
| 2026-08-10 07:03:09 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:02:55 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-10 07:02:46 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:02:19 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.047 |  |
| 2026-08-10 07:02:12 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:02:07 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:01:11 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-10 07:01:04 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:00:16 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:00:10 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.031 |  |
| 2026-08-10 06:31:49 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:31:11 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 07:05:09 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-10 07:05:59 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-10 07:01:11 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-10 07:04:02 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 07:04:25 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-10 06:10:00 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 06:01:02 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 07:02:55 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 07:07:40 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 07:02:07 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:00:10 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:05:27 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:02:12 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:00:16 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:05:20 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:03:09 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:04:46 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:05:12 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:06:53 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:02:46 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:03:55 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:05:26 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-10 06:02:38 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:01:04 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 07:12:39 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-08-10 07:06:01 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-10 07:04:31 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-10 07:03:12 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.011 |  |
| 2026-08-10 07:16:24 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.013 |  |
| 2026-08-10 07:06:33 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-08-10 07:04:07 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.020 |  |
| 2026-08-10 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.031 |  |
| 2026-08-10 06:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.046 |  |
| 2026-08-10 07:02:19 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.047 |  |
| 2026-08-10 07:07:04 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.068 |  |
| 2026-08-10 07:04:02 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.078 |  |
| 2026-08-10 07:04:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)