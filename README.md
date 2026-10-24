# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_17:04:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,836 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 17:04:52 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:04:32 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-24 17:04:29 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-10-24 17:04:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-10-24 17:04:04 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.988 |  |
| 2026-10-24 17:04:02 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 17:03:20 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.050 |  |
| 2026-10-24 17:03:13 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | -0.082 |  |
| 2026-10-24 17:03:05 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.051 |  |
| 2026-10-24 17:02:58 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-24 17:02:52 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-10-24 17:02:47 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-10-24 17:02:32 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-24 17:02:32 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.042 |  |
| 2026-10-24 17:02:31 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:02:23 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.031 |  |
| 2026-10-24 17:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:02:06 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-10-24 17:01:49 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 17:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-24 17:01:40 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:01:19 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:01:11 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-24 17:01:07 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-24 17:00:42 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.093 |  |
| 2026-10-24 17:00:28 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 16:06:04 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-24 17:04:32 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-24 16:01:33 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 17:01:07 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-24 17:02:23 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 17:01:49 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 17:04:02 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 17:04:52 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:01:22 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:10:21 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:05:02 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:05:00 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:01:19 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:02:31 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:04:55 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:00:28 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 17:01:40 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:06:29 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-10-24 17:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-24 17:02:58 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-24 17:01:11 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-24 17:02:32 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-24 16:08:45 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-10-24 17:02:06 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-10-24 17:02:47 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-10-24 17:04:29 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-10-24 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.031 |  |
| 2026-10-24 17:02:52 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-10-24 17:02:32 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.042 |  |
| 2026-10-24 16:02:06 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.042 |  |
| 2026-10-24 17:03:20 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.050 |  |
| 2026-10-24 17:03:05 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | -0.051 |  |
| 2026-10-24 16:06:15 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.054 |  |
| 2026-10-24 17:04:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-10-24 17:03:13 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | -0.082 |  |
| 2026-10-24 16:02:53 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.085 |  |
| 2026-10-24 17:00:42 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.093 |  |
| 2026-10-24 17:04:04 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.988 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)