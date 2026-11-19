# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_10:33:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,969 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 10:33:30 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:20:14 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:13:16 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.017 |  |
| 2026-11-19 10:13:02 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.018 |  |
| 2026-11-19 10:12:36 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:09:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | -0.027 |  |
| 2026-11-19 10:08:22 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:07:12 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:07:12 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:07:05 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.009 |  |
| 2026-11-19 10:06:59 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:06:52 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:06:50 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:06:08 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:05:32 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.519 |  |
| 2026-11-19 10:04:37 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2026-11-19 10:04:20 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-11-19 10:04:00 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:03:59 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 10:03:56 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:03:51 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:03:46 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:03:35 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-11-19 10:03:17 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:02:51 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:02:31 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-11-19 10:02:14 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:02:09 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.052 |  |
| 2026-11-19 10:02:03 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:02:00 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:01:21 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:01:20 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:01:16 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 10:01:11 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:00:24 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:00:16 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-19 10:00:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 10:00:16 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-19 10:03:59 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 10:01:16 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 09:02:20 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:02:00 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:00:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:02:03 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:02:14 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:03:46 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:33:30 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:12:36 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:06:52 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:04:00 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:06:50 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:08:22 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:01:21 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:01:11 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:03:51 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:06:59 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:00:24 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:20:14 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:06:08 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:01:20 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:07:12 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 10:07:05 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.009 |  |
| 2026-11-19 10:07:12 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:02:51 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:03:17 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:03:56 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-19 10:04:20 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-11-19 10:13:16 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.017 |  |
| 2026-11-19 10:13:02 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.018 |  |
| 2026-11-19 10:02:31 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-11-19 10:09:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | -0.027 |  |
| 2026-11-19 10:04:37 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2026-11-19 10:03:35 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-11-19 10:02:09 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.052 |  |
| 2026-11-19 10:05:32 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.519 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)