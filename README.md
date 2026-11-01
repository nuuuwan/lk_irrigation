# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_11:34:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,821 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 11:34:32 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.006 |  |
| 2026-11-01 11:19:24 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.016 |  |
| 2026-11-01 11:17:36 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:16:45 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:13:57 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:12:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.009 |  |
| 2026-11-01 11:09:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:07:18 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:06:04 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-11-01 11:05:55 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-11-01 11:05:32 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-11-01 11:05:28 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.069 |  |
| 2026-11-01 11:04:38 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:04:30 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:04:22 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 11:04:21 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.039 |  |
| 2026-11-01 11:03:58 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.103 |  |
| 2026-11-01 11:03:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-01 11:03:47 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 11:03:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-01 11:03:18 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:02:51 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.052 |  |
| 2026-11-01 11:02:35 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-01 11:02:30 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:25 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:17 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:10 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.061 |  |
| 2026-11-01 11:02:08 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.031 |  |
| 2026-11-01 11:02:08 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.221 |  |
| 2026-11-01 11:02:07 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:01:56 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.052 |  |
| 2026-11-01 11:01:54 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-11-01 11:01:31 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:01:25 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 11:01:20 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:01:05 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:00:10 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 11:01:25 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 11:05:55 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-11-01 11:03:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-01 11:03:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-01 11:02:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-01 11:04:22 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 11:03:47 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 11:00:10 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:09:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:30 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:01:05 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:13:57 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:16:45 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:07 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:02:17 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:07:18 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:04:38 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:01:31 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:17:36 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 11:34:32 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.006 |  |
| 2026-11-01 11:12:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.009 |  |
| 2026-11-01 11:04:30 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:03:38 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:03:18 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:01:20 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 11:06:04 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-11-01 11:19:24 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.016 |  |
| 2026-11-01 11:05:32 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-11-01 11:01:54 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-11-01 10:03:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-11-01 11:02:08 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.031 |  |
| 2026-11-01 11:04:21 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.039 |  |
| 2026-11-01 11:01:56 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.052 |  |
| 2026-11-01 11:02:51 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.052 |  |
| 2026-11-01 11:02:10 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.061 |  |
| 2026-11-01 11:05:28 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.069 |  |
| 2026-11-01 11:03:58 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.103 |  |
| 2026-11-01 11:02:08 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)