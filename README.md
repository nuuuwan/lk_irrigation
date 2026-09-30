# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_01:27:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,521 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 01:27:21 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.016 |  |
| 2026-10-01 01:20:59 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-10-01 01:16:31 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:14:45 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.064 |  |
| 2026-10-01 01:13:57 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-01 01:12:44 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:09:04 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.039 |  |
| 2026-10-01 01:08:58 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:08:13 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:07:15 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:07:00 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-01 01:06:43 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.019 |  |
| 2026-10-01 01:05:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-01 01:05:29 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-10-01 01:05:17 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-01 01:04:42 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:04:04 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:03:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:03:52 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:03:38 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:03:26 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:03:06 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.042 |  |
| 2026-10-01 01:02:55 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-10-01 01:02:35 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:02:27 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:01:55 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:01:23 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.032 |  |
| 2026-10-01 01:01:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:01:16 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 01:02:55 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-10-01 01:05:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-01 01:05:17 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-01 01:13:57 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-01 01:07:00 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-01 01:01:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:01:55 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:08:58 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:12:44 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:03:26 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:03:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:00:12 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:02:27 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:04:04 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:40:54 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-01 01:16:31 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:09:18 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-10-01 01:08:13 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:02:35 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:04:42 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:03:52 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:07:15 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:03:38 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-10-01 01:05:29 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-10-01 01:27:21 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.016 |  |
| 2026-10-01 01:06:43 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.019 |  |
| 2026-09-30 23:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-10-01 01:20:59 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-10-01 01:01:23 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.032 |  |
| 2026-10-01 01:09:04 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.039 |  |
| 2026-10-01 01:03:06 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.042 |  |
| 2026-10-01 01:14:45 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.064 |  |
| 2026-09-30 23:05:48 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.111 |  |
| 2026-10-01 00:06:25 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -3.051 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)