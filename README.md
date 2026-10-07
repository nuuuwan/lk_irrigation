# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_17:08:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 17:08:17 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-07 17:08:16 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.027 |  |
| 2026-10-07 17:08:16 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-10-07 17:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.030 |  |
| 2026-10-07 17:07:40 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-10-07 17:07:29 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 17:07:27 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-07 17:06:56 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.044 |  |
| 2026-10-07 17:06:14 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:06:10 | Panadugama (Nilwala Ganga) | 4.89 | 🟢 Normal | -1.573 |  |
| 2026-10-07 17:06:07 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.028 |  |
| 2026-10-07 17:06:00 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.019 |  |
| 2026-10-07 17:05:39 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-07 17:05:37 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | -0.094 |  |
| 2026-10-07 17:05:16 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:05:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:04:12 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:03:50 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:03:28 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:03:10 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | -0.080 |  |
| 2026-10-07 17:02:56 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-07 17:02:39 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:02:24 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-07 17:02:17 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.031 |  |
| 2026-10-07 17:01:59 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-07 17:01:48 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:01:36 | Weraganthota (Mahaweli Ganga) | -3.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-07 17:01:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-10-07 17:00:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:00:47 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.025 |  |
| 2026-10-07 17:00:09 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-07 16:56:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:25:44 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | -1.573 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 17:01:59 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-07 17:01:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-10-07 17:07:27 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-07 17:08:17 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-07 17:02:56 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-07 17:01:36 | Weraganthota (Mahaweli Ganga) | -3.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-07 17:07:29 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 17:03:28 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:03:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:04:12 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:03:50 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:00:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:05:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:05:16 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:02:39 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:06:14 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:00:11 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-07 17:01:48 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 16:20:51 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.008 |  |
| 2026-10-07 16:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-07 17:05:39 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-07 17:02:24 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-07 17:00:09 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-07 16:01:13 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-10-07 17:06:00 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.019 |  |
| 2026-10-07 17:07:40 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-10-07 16:05:27 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-10-07 17:00:47 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.025 |  |
| 2026-10-07 17:08:16 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.027 |  |
| 2026-10-07 17:06:07 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.028 |  |
| 2026-10-07 16:03:03 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-10-07 16:03:12 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2026-10-07 17:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.030 |  |
| 2026-10-07 17:02:17 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.031 |  |
| 2026-10-07 17:08:16 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-10-07 17:06:56 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.044 |  |
| 2026-10-07 17:03:10 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | -0.080 |  |
| 2026-10-07 17:05:37 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | -0.094 |  |
| 2026-10-07 17:06:10 | Panadugama (Nilwala Ganga) | 4.89 | 🟢 Normal | -1.573 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)