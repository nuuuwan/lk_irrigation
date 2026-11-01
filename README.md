# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_06:10:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,624 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 06:10:11 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:08:15 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-01 06:07:51 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-01 06:07:22 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.018 |  |
| 2026-11-01 06:06:30 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-01 06:05:33 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 06:05:28 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.005 |  |
| 2026-11-01 06:04:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.142 |  |
| 2026-11-01 06:04:38 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:04:29 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 06:04:18 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-11-01 06:04:11 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.048 |  |
| 2026-11-01 06:04:05 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 06:04:04 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.003 |  |
| 2026-11-01 06:03:28 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:03:27 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.076 |  |
| 2026-11-01 06:03:12 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-11-01 06:03:05 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.010 |  |
| 2026-11-01 06:03:05 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.052 |  |
| 2026-11-01 06:02:56 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.051 |  |
| 2026-11-01 06:02:49 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.061 |  |
| 2026-11-01 06:02:37 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:02:35 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:02:31 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 06:02:30 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.063 |  |
| 2026-11-01 06:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:01:55 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-11-01 06:01:47 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-01 06:01:46 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-11-01 06:01:42 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-11-01 06:01:41 | Galgamuwa (Mee Oya) | 1.06 | 🟢 Normal | -0.003 |  |
| 2026-11-01 06:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.460 |  |
| 2026-11-01 06:01:15 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:01:10 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-11-01 06:00:48 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.012 |  |
| 2026-11-01 06:00:44 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-01 05:48:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | -0.460 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 06:04:11 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.048 |  |
| 2026-11-01 06:01:46 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-11-01 06:01:47 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-01 06:06:30 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-01 06:04:29 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 06:08:15 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-01 06:02:31 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 06:05:33 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 06:04:05 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 06:07:51 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-01 06:04:38 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 05:02:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:03:28 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:10:11 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:02:37 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:02:35 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:01:15 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 06:01:41 | Galgamuwa (Mee Oya) | 1.06 | 🟢 Normal | -0.003 |  |
| 2026-11-01 06:04:04 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.003 |  |
| 2026-11-01 06:05:28 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.005 |  |
| 2026-11-01 06:04:18 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-11-01 06:03:05 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 06:00:44 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-01 06:03:12 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-11-01 06:01:55 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-11-01 06:00:48 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.012 |  |
| 2026-11-01 06:07:22 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.018 |  |
| 2026-11-01 06:01:42 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-11-01 06:01:10 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-11-01 06:02:56 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.051 |  |
| 2026-11-01 06:03:05 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.052 |  |
| 2026-11-01 06:02:49 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.061 |  |
| 2026-11-01 06:02:30 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.063 |  |
| 2026-11-01 06:03:27 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.076 |  |
| 2026-11-01 06:04:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.142 |  |
| 2026-11-01 05:02:18 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.224 |  |
| 2026-11-01 06:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.460 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)