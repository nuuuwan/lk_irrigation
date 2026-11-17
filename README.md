# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_16:21:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 16:21:39 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:19:11 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.017 |  |
| 2026-11-17 16:14:43 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:13:47 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:09:18 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:07:51 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:07:45 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.054 |  |
| 2026-11-17 16:06:54 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:06:23 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-17 16:06:06 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 16:05:29 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:04:52 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:04:51 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-11-17 16:03:48 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:48 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:03:45 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:40 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-17 16:03:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:24 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:03:20 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:03:17 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.021 |  |
| 2026-11-17 16:03:12 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:11 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:08 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:02:59 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-17 16:02:51 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-17 16:02:44 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:02:31 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-17 16:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:02:26 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-17 16:02:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:02:09 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:01:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-17 16:01:21 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:01:13 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:00:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:00:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:58:45 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 16:01:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-17 16:02:51 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-17 16:03:40 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-17 16:06:23 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-17 16:02:26 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-17 15:06:15 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 16:06:06 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 15:03:30 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:00:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:48 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:05:29 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:04:52 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:13:47 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:12 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:11 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.000 |  |
| 2026-11-17 15:58:45 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:01:21 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:14:43 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:00:08 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:02:44 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:08 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:45 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:06:54 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:21:39 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:01:13 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-17 16:03:48 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:09:18 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:03:24 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:02:09 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:03:20 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-17 16:02:31 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-17 16:19:11 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.017 |  |
| 2026-11-17 16:02:59 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-17 16:03:17 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.021 |  |
| 2026-11-17 16:04:51 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-11-17 16:07:45 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)