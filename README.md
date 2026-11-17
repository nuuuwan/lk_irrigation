# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_11:15:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,228 measurements** from **39** stations.
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
| 2026-11-17 11:15:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.040 |  |
| 2026-11-17 11:14:29 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.026 |  |
| 2026-11-17 11:12:19 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:10:13 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:08:16 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-11-17 11:07:02 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2026-11-17 11:06:27 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.012 |  |
| 2026-11-17 11:05:47 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:05:40 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.035 |  |
| 2026-11-17 11:05:29 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:05:27 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.020 |  |
| 2026-11-17 11:05:23 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:05:08 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.022 |  |
| 2026-11-17 11:04:50 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:04:38 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-11-17 11:04:14 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-17 11:03:57 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:03:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:03:51 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:03:45 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:03:32 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:03:11 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-17 11:02:48 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-11-17 11:02:44 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.011 |  |
| 2026-11-17 11:02:44 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:02:38 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-11-17 11:02:36 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 11:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:02:19 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:02:11 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:02:03 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:02:00 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:01:43 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:01:30 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 11:01:01 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:00:41 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.099 |  |
| 2026-11-17 11:00:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-17 10:47:40 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 11:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 11:01:30 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 11:01:43 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:02:19 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:03:51 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:03:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:03:32 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:05:47 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:10:13 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:03:57 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:02:00 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:01:01 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:00:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:04:50 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:02:03 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:12:19 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 11:05:23 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-17 10:16:12 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | -0.008 |  |
| 2026-11-17 11:05:29 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:02:11 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:02:44 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:02:36 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:03:45 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.010 |  |
| 2026-11-17 11:02:48 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-11-17 11:08:16 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-11-17 11:02:44 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.011 |  |
| 2026-11-17 11:03:11 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-17 11:06:27 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.012 |  |
| 2026-11-17 11:02:38 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-11-17 11:05:27 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.020 |  |
| 2026-11-17 11:05:08 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.022 |  |
| 2026-11-17 11:14:29 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.026 |  |
| 2026-11-17 11:04:14 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-17 11:04:38 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-11-17 11:05:40 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.035 |  |
| 2026-11-17 11:15:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.040 |  |
| 2026-11-17 11:07:02 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2026-11-17 11:00:41 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)