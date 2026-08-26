# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_06:16:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,701 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 06:16:30 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:16:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-26 06:13:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:11:57 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-26 06:11:35 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-26 06:08:36 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-26 06:07:52 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.005 |  |
| 2026-08-26 06:07:19 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-26 06:06:23 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:06:20 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 06:06:15 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:05:36 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:05:28 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-26 06:05:08 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-08-26 06:05:04 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-26 06:04:38 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:04:30 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-26 06:04:15 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-26 06:04:14 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-26 06:04:13 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-26 06:04:12 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-26 06:04:10 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-26 06:04:02 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:03:57 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-26 06:03:42 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-26 06:03:42 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-08-26 06:03:41 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.051 |  |
| 2026-08-26 06:03:32 | Rathnapura (Kalu Ganga) | 3.77 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-26 06:03:29 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:03:05 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.019 |  |
| 2026-08-26 06:02:19 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:02:17 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 06:02:14 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:02:12 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 06:01:40 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-26 06:01:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.095 |  |
| 2026-08-26 06:01:31 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:01:20 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:01:07 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:00:54 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:00:41 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-26 05:44:14 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:32:14 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.255 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 06:04:15 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-08-26 06:05:08 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-08-26 06:11:57 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-26 06:11:35 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-26 06:01:40 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-26 06:03:57 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-26 06:03:32 | Rathnapura (Kalu Ganga) | 3.77 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-26 06:00:41 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-26 06:04:30 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-26 06:07:19 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-26 06:03:42 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-26 06:16:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-26 06:05:04 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-26 06:05:28 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-26 06:08:36 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-26 06:06:20 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 06:02:12 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 06:02:17 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 06:04:02 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:00:54 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:01:31 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:02:14 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:16:30 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:06:15 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-26 05:44:14 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:03:29 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:04:38 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:01:07 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:01:20 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:13:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:05:36 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:02:21 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:06:23 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 06:07:52 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.005 |  |
| 2026-08-26 06:03:42 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-08-26 06:03:05 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.019 |  |
| 2026-08-26 05:03:42 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-08-26 06:03:41 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.051 |  |
| 2026-08-26 06:01:35 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)