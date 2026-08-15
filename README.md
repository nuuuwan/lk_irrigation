# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_05:17:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 05:17:26 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:12:45 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:11:55 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:09:37 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:07:28 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.019 |  |
| 2026-08-15 05:06:36 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 05:05:55 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-08-15 05:05:46 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.980 |  |
| 2026-08-15 05:05:39 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-15 05:05:17 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-08-15 05:05:00 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:04:11 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:03:55 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.091 |  |
| 2026-08-15 05:03:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:03:15 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:02:43 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:02:26 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-15 05:02:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:02:20 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:02:17 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.071 |  |
| 2026-08-15 05:02:11 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:01:47 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-15 05:01:18 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:01:17 | Peradeniya (Mahaweli Ganga) | 3.13 | 🟢 Normal | -0.047 |  |
| 2026-08-15 05:01:03 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:00:42 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:00:34 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-15 05:00:04 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.052 |  |
| 2026-08-15 04:59:27 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 04:34:07 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.486 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 05:05:55 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-08-15 05:05:17 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-08-15 04:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-15 03:05:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-15 05:02:26 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-15 05:01:47 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-15 05:05:39 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-15 05:06:36 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 05:00:34 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-15 04:01:43 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-15 05:00:42 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:01:18 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:02:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:03:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:03:15 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:02:43 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 18:02:32 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-15 03:06:03 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:17:26 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-15 04:59:27 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:01:03 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-15 04:01:15 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:02:20 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:05:00 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:04:11 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:12:45 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:09:37 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:11:55 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:02:11 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 05:07:28 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.019 |  |
| 2026-08-14 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-08-15 05:01:17 | Peradeniya (Mahaweli Ganga) | 3.13 | 🟢 Normal | -0.047 |  |
| 2026-08-15 05:00:04 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.052 |  |
| 2026-08-15 04:07:18 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.053 |  |
| 2026-08-14 18:01:00 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.055 |  |
| 2026-08-15 05:02:17 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.071 |  |
| 2026-08-15 05:03:55 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.091 |  |
| 2026-08-15 04:34:07 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.486 |  |
| 2026-08-15 05:05:46 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.980 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)