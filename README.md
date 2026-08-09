# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_15:18:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,861 measurements** from **39** stations.
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
| 2026-08-09 15:18:22 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.008 |  |
| 2026-08-09 15:12:40 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-09 15:11:59 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:10:56 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-09 15:08:47 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-09 15:07:45 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:07:42 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:06:55 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.093 |  |
| 2026-08-09 15:06:46 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.028 |  |
| 2026-08-09 15:06:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.067 |  |
| 2026-08-09 15:06:14 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-08-09 15:05:48 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 15:05:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.114 |  |
| 2026-08-09 15:05:15 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:04:57 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:04:56 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:49 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:46 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-08-09 15:03:39 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:32 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:27 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.005 |  |
| 2026-08-09 15:03:25 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-09 15:03:19 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:18 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.010 |  |
| 2026-08-09 15:03:00 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:02:44 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-09 15:02:34 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-08-09 15:02:30 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-08-09 15:02:27 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-08-09 15:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-08-09 15:01:39 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.011 |  |
| 2026-08-09 15:01:37 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.061 |  |
| 2026-08-09 15:01:19 | Peradeniya (Mahaweli Ganga) | 3.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 15:01:19 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 15:01:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.042 |  |
| 2026-08-09 15:00:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:00:33 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:46:38 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 14:03:53 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-09 15:03:25 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-09 15:12:40 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-09 15:08:47 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-09 15:01:19 | Peradeniya (Mahaweli Ganga) | 3.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 15:01:19 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 15:05:48 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 15:10:56 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-09 15:00:33 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:01:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:19 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:07:45 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:04:57 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:00:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:49 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:32 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:04:56 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:39 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:05:15 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:11:59 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 14:10:28 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 15:03:27 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.005 |  |
| 2026-08-09 15:18:22 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.008 |  |
| 2026-08-09 15:06:14 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-08-09 15:03:18 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.010 |  |
| 2026-08-09 15:02:30 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-08-09 15:02:44 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-09 15:01:39 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.011 |  |
| 2026-08-09 15:02:27 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-08-09 15:02:34 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-08-09 15:03:46 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-08-09 15:06:46 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.028 |  |
| 2026-08-09 15:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-08-09 15:01:05 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.042 |  |
| 2026-08-09 15:01:37 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.061 |  |
| 2026-08-09 15:06:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.067 |  |
| 2026-08-09 15:06:55 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.093 |  |
| 2026-08-09 15:05:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)