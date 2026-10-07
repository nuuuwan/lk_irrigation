# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_16:25:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,507 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 16:25:44 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.686 | 🔺 Rising |
| 2026-10-07 16:23:12 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:20:51 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.008 |  |
| 2026-10-07 16:15:59 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.008 |  |
| 2026-10-07 16:12:21 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.034 |  |
| 2026-10-07 16:12:16 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.017 |  |
| 2026-10-07 16:11:10 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | -0.046 |  |
| 2026-10-07 16:11:03 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-10-07 16:08:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.026 |  |
| 2026-10-07 16:07:05 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.105 |  |
| 2026-10-07 16:06:21 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-07 16:06:10 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:06:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:05:58 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 16:05:27 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-10-07 16:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-07 16:04:04 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:03:59 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-07 16:03:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:03:40 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-07 16:03:33 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-10-07 16:03:12 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2026-10-07 16:03:03 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-10-07 16:02:56 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | -0.073 |  |
| 2026-10-07 16:02:52 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:02:48 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:02:36 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-07 16:02:29 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.051 |  |
| 2026-10-07 16:01:54 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.031 |  |
| 2026-10-07 16:01:43 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:01:38 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-10-07 16:01:34 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:01:26 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-10-07 16:01:22 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.030 |  |
| 2026-10-07 16:01:13 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-10-07 16:00:55 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:00:28 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:00:11 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:59:55 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 16:25:44 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.686 | 🔺 Rising |
| 2026-10-07 16:03:59 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-07 16:06:21 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-07 16:05:58 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 16:00:28 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:03:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:00:55 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:06:10 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:02:48 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:01:43 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:23:12 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:06:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:02:52 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:00:11 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:01:34 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:04:04 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:20:51 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.008 |  |
| 2026-10-07 16:15:59 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.008 |  |
| 2026-10-07 16:11:03 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-10-07 16:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-07 16:03:40 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-07 16:02:36 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-07 16:01:13 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-10-07 16:12:16 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.017 |  |
| 2026-10-07 16:03:33 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-10-07 16:05:27 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-10-07 16:01:26 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-10-07 16:08:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.026 |  |
| 2026-10-07 16:03:03 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-10-07 16:01:22 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.030 |  |
| 2026-10-07 16:03:12 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2026-10-07 15:01:34 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-10-07 16:01:54 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.031 |  |
| 2026-10-07 16:01:38 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-10-07 16:12:21 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.034 |  |
| 2026-10-07 16:11:10 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | -0.046 |  |
| 2026-10-07 16:02:29 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.051 |  |
| 2026-10-07 16:02:56 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | -0.073 |  |
| 2026-10-07 16:07:05 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)