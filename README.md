# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_08:20:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 08:20:44 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:12:14 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | -0.009 |  |
| 2026-08-13 08:12:02 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.027 |  |
| 2026-08-13 08:10:43 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-13 08:09:47 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.036 |  |
| 2026-08-13 08:07:53 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:07:40 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.107 |  |
| 2026-08-13 08:07:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:07:27 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-13 08:06:41 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:05:50 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.030 |  |
| 2026-08-13 08:05:50 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:05:14 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:04:50 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:04:43 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:04:19 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.044 |  |
| 2026-08-13 08:04:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:03:54 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.205 |  |
| 2026-08-13 08:03:45 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:03:41 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 08:03:39 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 08:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:03:13 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-08-13 08:03:08 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-08-13 08:03:03 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-13 08:02:51 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:02:50 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:02:27 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:02:17 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-08-13 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.101 |  |
| 2026-08-13 08:02:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:01:49 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.076 |  |
| 2026-08-13 08:01:24 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:01:18 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.039 |  |
| 2026-08-13 08:01:12 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:01:06 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:00:57 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.168 |  |
| 2026-08-13 08:00:12 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 07:59:41 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:33:53 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 08:07:27 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-13 08:00:12 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 08:03:39 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 08:03:41 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 08:10:43 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-13 08:01:12 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:20:44 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:07:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:02:27 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:01:06 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:07:53 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:02:51 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:02:50 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:00:22 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:06:41 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:03:45 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:02:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:04:43 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:05:50 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:01:24 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:04:50 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:05:14 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:04:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 08:12:14 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | -0.009 |  |
| 2026-08-13 08:03:03 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-13 08:03:08 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-08-13 08:03:13 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-08-13 08:02:17 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-08-13 08:12:02 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.027 |  |
| 2026-08-13 08:05:50 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.030 |  |
| 2026-08-13 08:09:47 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.036 |  |
| 2026-08-13 08:01:18 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.039 |  |
| 2026-08-13 08:04:19 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.044 |  |
| 2026-08-13 08:01:49 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.076 |  |
| 2026-08-13 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.101 |  |
| 2026-08-13 08:07:40 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.107 |  |
| 2026-08-13 08:00:57 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.168 |  |
| 2026-08-13 08:03:54 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)