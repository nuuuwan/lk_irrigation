# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_20:04:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,033 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 20:04:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:04:07 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 20:03:45 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-10-03 20:03:34 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.031 |  |
| 2026-10-03 20:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.154 |  |
| 2026-10-03 20:03:20 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:03:15 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-03 20:02:57 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.031 |  |
| 2026-10-03 20:02:34 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:02:32 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.806 | 🔺 Rising |
| 2026-10-03 20:02:30 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.050 |  |
| 2026-10-03 20:02:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.034 |  |
| 2026-10-03 20:01:55 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:01:45 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:01:19 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:00:22 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-10-03 20:00:13 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 19:34:59 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:27:03 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 20:02:32 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.806 | 🔺 Rising |
| 2026-10-03 19:06:41 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-10-03 20:03:45 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-10-03 20:03:15 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-03 19:03:17 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-03 19:05:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-03 19:06:49 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-03 20:00:13 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 20:04:07 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 19:06:06 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:12:38 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:01:55 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:02:34 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:02:52 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:34:59 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:02:11 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:01:19 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:05:14 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:04:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:09:51 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:03:53 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:01:45 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-03 20:03:20 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 19:07:24 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-10-03 19:03:50 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-03 19:02:23 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-03 20:00:22 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-10-03 19:08:06 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.019 |  |
| 2026-10-03 19:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-10-03 18:59:20 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-10-03 20:02:57 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.031 |  |
| 2026-10-03 20:03:34 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.031 |  |
| 2026-10-03 20:02:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.034 |  |
| 2026-10-03 19:07:09 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.038 |  |
| 2026-10-03 20:02:30 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.050 |  |
| 2026-10-03 20:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)