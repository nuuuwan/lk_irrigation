# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_20:05:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,949 measurements** from **39** stations.
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
| 2026-10-24 20:05:00 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:04:53 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.050 |  |
| 2026-10-24 20:04:05 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.010 |  |
| 2026-10-24 20:03:46 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-10-24 20:03:36 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.022 |  |
| 2026-10-24 20:03:28 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.059 |  |
| 2026-10-24 20:03:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-24 20:03:25 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-24 20:03:13 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | -0.020 |  |
| 2026-10-24 20:02:57 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-24 20:02:46 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 20:02:41 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-10-24 20:02:29 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-10-24 20:02:28 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-24 20:02:19 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:02:10 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:01:56 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.020 |  |
| 2026-10-24 20:01:46 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:01:36 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:01:33 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:01:00 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.024 |  |
| 2026-10-24 20:00:43 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-24 20:00:36 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:00:14 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 19:33:37 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:24:44 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 20:02:57 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-24 20:03:25 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-24 20:00:43 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-24 19:00:57 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-24 20:00:14 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 20:02:46 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 20:01:33 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:05:00 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:04:05 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:01:46 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:02:19 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:00:36 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:02:10 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:02:39 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-24 20:01:36 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-24 19:07:55 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:10:00 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:01:05 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-24 20:02:28 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:03:52 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-10-24 20:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | -0.010 |  |
| 2026-10-24 19:05:09 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-10-24 20:03:13 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | -0.020 |  |
| 2026-10-24 19:24:44 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-10-24 20:01:56 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.020 |  |
| 2026-10-24 19:02:23 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-24 18:00:25 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |
| 2026-10-24 19:03:48 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-24 20:02:29 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-10-24 20:03:36 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.022 |  |
| 2026-10-24 20:01:00 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.024 |  |
| 2026-10-24 18:02:58 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-24 20:03:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-24 20:03:46 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-10-24 20:02:41 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-10-24 18:01:50 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-10-24 20:04:53 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.050 |  |
| 2026-10-24 20:03:28 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.059 |  |
| 2026-10-24 19:00:50 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)