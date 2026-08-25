# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_05:08:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 05:08:38 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:08:23 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:07:28 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:07:21 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-26 05:05:58 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-26 05:05:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:05:34 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:05:31 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.054 |  |
| 2026-08-26 05:05:21 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:05:11 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-08-26 05:05:00 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-26 05:04:03 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 05:03:42 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-08-26 05:03:34 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:03:11 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:03:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-26 05:03:04 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:02:24 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:02:12 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:01:37 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-26 05:01:30 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-08-26 05:01:06 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.022 |  |
| 2026-08-26 05:00:42 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:51:08 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:49:25 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.031 |  |
| 2026-08-26 04:46:32 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:31:11 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:25:09 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:21:50 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 04:09:19 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-08-26 04:00:57 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-08-26 01:09:27 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-26 04:11:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-08-26 05:05:00 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-26 05:05:11 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-08-26 04:09:29 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-26 05:05:58 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-26 05:01:37 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-26 05:03:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-26 04:05:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-26 05:07:21 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-26 05:04:03 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 04:20:19 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-26 05:08:23 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:05:34 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:00:48 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:00:42 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:04:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:02:24 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:01:54 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:03:25 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:46:32 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:08:38 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:03:11 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:07:28 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:03:34 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:05:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:05:21 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:02:21 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:03:04 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:02:12 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:01:30 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-08-25 18:08:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.019 |  |
| 2026-08-26 05:01:06 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.022 |  |
| 2026-08-26 05:03:42 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-08-26 04:49:25 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.031 |  |
| 2026-08-26 05:05:31 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.054 |  |
| 2026-08-26 04:03:52 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)