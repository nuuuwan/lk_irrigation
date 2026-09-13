# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_05:03:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,334 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 05:03:05 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 05:03:03 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-14 05:02:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:02:24 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-14 05:02:23 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-09-14 05:02:02 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:01:31 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:01:13 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:01:05 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:01:03 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.050 |  |
| 2026-09-14 05:00:34 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:59:45 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:35:00 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-14 04:34:20 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.026 |  |
| 2026-09-14 04:32:22 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.007 |  |
| 2026-09-14 04:20:27 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.024 |  |
| 2026-09-14 04:18:43 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 8.129 | 🔺 Rising |
| 2026-09-14 04:18:12 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 8.129 | 🔺 Rising |
| 2026-09-14 04:17:35 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.006 |  |
| 2026-09-14 04:17:19 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 04:18:43 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 8.129 | 🔺 Rising |
| 2026-09-14 05:03:03 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-14 05:02:24 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-14 04:02:13 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-14 04:02:07 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 05:03:05 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 04:11:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | 0.003 |  |
| 2026-09-14 04:16:23 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.003 |  |
| 2026-09-14 04:02:37 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:05:39 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:00:34 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:02:36 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:01:31 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:02:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:02:58 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:02:02 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:06:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:01:05 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:59:45 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:06:11 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:04:30 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:02:23 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 05:01:13 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 04:17:35 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.006 |  |
| 2026-09-14 04:32:22 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.007 |  |
| 2026-09-14 04:17:19 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-09-14 03:37:03 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.020 |  |
| 2026-09-14 05:02:23 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-09-14 04:20:27 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.024 |  |
| 2026-09-14 04:34:20 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.026 |  |
| 2026-09-14 04:02:51 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.030 |  |
| 2026-09-14 04:12:28 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.035 |  |
| 2026-09-14 04:09:14 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.043 |  |
| 2026-09-14 05:01:03 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.050 |  |
| 2026-09-14 03:16:32 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)