# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_08:26:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,443 measurements** from **39** stations.
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
| 2026-11-04 08:26:28 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:24:39 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.068 |  |
| 2026-11-04 08:09:47 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.069 |  |
| 2026-11-04 08:09:46 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:07:39 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.018 |  |
| 2026-11-04 08:07:21 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-04 08:07:17 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.064 |  |
| 2026-11-04 08:05:55 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | -0.239 |  |
| 2026-11-04 08:05:39 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:05:33 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 08:05:10 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:05:07 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 08:04:59 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:04:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 08:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 08:04:23 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | -0.106 |  |
| 2026-11-04 08:04:19 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | 2.011 | 🔺 Rising |
| 2026-11-04 08:04:04 | Galgamuwa (Mee Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-04 08:04:04 | Moragaswewa (Deduru Oya) | 4.17 | 🟢 Normal | 0.020 | 🔺 Rising |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 08:04:19 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | 2.011 | 🔺 Rising |
| 2026-11-04 08:04:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 08:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 08:03:38 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 08:05:07 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 08:04:04 | Moragaswewa (Deduru Oya) | 4.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 08:07:21 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-04 08:05:33 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 08:01:14 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:01:59 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:00:21 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:04:59 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:05:39 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:04:04 | Galgamuwa (Mee Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-04 08:01:16 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 08:03:53 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-11-04 08:07:39 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.018 |  |
| 2026-11-04 08:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-04 08:02:45 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-11-04 08:01:42 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.025 |  |
| 2026-11-04 08:05:10 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:26:28 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:00:24 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:02:37 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-11-04 08:03:22 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:09:46 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:03:42 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:02:54 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:02:36 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.051 |  |
| 2026-11-04 08:07:17 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.064 |  |
| 2026-11-04 08:24:39 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.068 |  |
| 2026-11-04 08:09:47 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.069 |  |
| 2026-11-04 08:01:36 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.088 |  |
| 2026-11-04 08:03:12 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.103 |  |
| 2026-11-04 08:04:23 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | -0.106 |  |
| 2026-11-04 08:03:23 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.107 |  |
| 2026-11-04 08:02:10 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.112 |  |
| 2026-11-04 08:00:41 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.117 |  |
| 2026-11-04 08:05:55 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)