# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_08:03:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,424 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 08:03:53 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-11-04 08:03:42 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:03:38 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 08:03:23 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.107 |  |
| 2026-11-04 08:03:22 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-04 08:03:12 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.103 |  |
| 2026-11-04 08:02:54 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:02:45 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-11-04 08:02:37 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-11-04 08:02:36 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.051 |  |
| 2026-11-04 08:02:10 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.112 |  |
| 2026-11-04 08:01:59 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:01:42 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.025 |  |
| 2026-11-04 08:01:36 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.088 |  |
| 2026-11-04 08:01:16 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 08:01:14 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:00:41 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.117 |  |
| 2026-11-04 08:00:24 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:00:21 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:40:13 | Pitabeddara (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.117 |  |
| 2026-11-04 07:37:54 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.025 |  |
| 2026-11-04 07:23:13 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 07:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-04 07:03:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-04 07:04:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-04 07:04:27 | Ellagawa (Kalu Ganga) | 6.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 08:03:38 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 07:04:30 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 07:02:50 | Moragaswewa (Deduru Oya) | 4.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 08:01:14 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:01:59 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:04:26 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:12:10 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:00:21 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-04 07:23:13 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:01:16 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 07:02:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 08:03:53 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-11-04 08:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-04 08:02:45 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-11-04 08:01:42 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.025 |  |
| 2026-11-04 07:08:51 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.027 |  |
| 2026-11-04 08:00:24 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-11-04 07:01:46 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.032 |  |
| 2026-11-04 07:01:45 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-11-04 08:02:37 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-11-04 08:03:22 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:03:42 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:02:54 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.042 |  |
| 2026-11-04 07:05:29 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.043 |  |
| 2026-11-04 07:07:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.047 |  |
| 2026-11-04 08:02:36 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.051 |  |
| 2026-11-04 07:05:43 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.074 |  |
| 2026-11-04 08:01:36 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.088 |  |
| 2026-11-04 08:03:12 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.103 |  |
| 2026-11-04 08:03:23 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.107 |  |
| 2026-11-04 08:02:10 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.112 |  |
| 2026-11-04 08:00:41 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.117 |  |
| 2026-11-04 07:02:06 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.121 |  |
| 2026-11-04 07:05:47 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.203 |  |
| 2026-11-04 07:05:33 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -1.878 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)