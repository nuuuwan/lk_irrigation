# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_18:05:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,727 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 18:05:19 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:05:08 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:05:08 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:04:57 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | 17.561 | 🔺 Rising |
| 2026-11-05 18:04:57 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-05 18:04:27 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:04:20 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:04:13 | Thanamalwila (Kirindi Oya) | 1.96 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-05 18:04:13 | Moragaswewa (Deduru Oya) | 3.30 | 🟢 Normal | -0.030 |  |
| 2026-11-05 18:03:53 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:19 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.040 |  |
| 2026-11-05 18:03:14 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.084 |  |
| 2026-11-05 18:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | -0.060 |  |
| 2026-11-05 18:02:40 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:02:39 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 18:02:39 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:02:37 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.070 |  |
| 2026-11-05 18:02:22 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.025 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-05 18:01:50 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-05 18:01:45 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:38 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.031 |  |
| 2026-11-05 18:01:37 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:36 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:33 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:32 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 17.561 | 🔺 Rising |
| 2026-11-05 18:01:29 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:25 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:15 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:10 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-05 18:01:06 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:00:29 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:00:11 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-05 17:27:48 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 18:04:57 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | 17.561 | 🔺 Rising |
| 2026-11-05 18:01:50 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-05 17:06:04 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-05 18:04:57 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-05 18:04:13 | Thanamalwila (Kirindi Oya) | 1.96 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-05 18:02:39 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 18:01:10 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-05 18:01:15 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:33 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:06 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:53 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:07:56 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:25 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:29 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:01:36 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:02:39 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:04:20 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:02:40 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:05:19 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:05:08 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-05 17:17:33 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:05:08 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:00:29 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:37 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:45 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-05 18:00:11 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-05 18:02:22 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.025 |  |
| 2026-11-05 18:04:13 | Moragaswewa (Deduru Oya) | 3.30 | 🟢 Normal | -0.030 |  |
| 2026-11-05 17:27:48 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.030 |  |
| 2026-11-05 18:01:38 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.031 |  |
| 2026-11-05 18:03:19 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.040 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-05 18:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | -0.060 |  |
| 2026-11-05 17:08:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-11-05 18:02:37 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.070 |  |
| 2026-11-05 18:03:14 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)