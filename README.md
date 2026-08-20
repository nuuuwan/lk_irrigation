# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_03:14:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,138 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 03:14:11 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:12:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:12:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-08-21 03:09:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-21 03:07:17 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 03:06:55 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:06:39 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 03:06:30 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:05:49 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-21 03:05:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:05:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:44 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:40 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:29 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:26 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:24 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.079 |  |
| 2026-08-21 03:04:22 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:03:59 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.039 |  |
| 2026-08-21 03:03:45 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:03:37 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-21 03:03:32 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:03:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-21 03:03:24 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-08-21 03:02:55 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 03:02:39 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:33 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:13 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:01:43 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-21 03:01:03 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:00:55 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:00:55 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 03:01:43 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-21 03:03:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-21 03:03:37 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-21 03:09:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-21 02:05:26 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-21 01:03:53 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 03:02:55 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 03:07:17 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 03:05:49 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-21 03:06:39 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:33 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:00:55 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:01:03 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:22 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:03:45 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:29 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:26 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:12:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:06:55 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:44 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:14:11 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:13 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:05:15 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:04:40 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:05:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:02:19 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:02:39 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 03:12:42 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-08-21 02:21:18 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.016 |  |
| 2026-08-21 03:03:24 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-08-21 03:03:59 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.039 |  |
| 2026-08-21 02:01:43 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.040 |  |
| 2026-08-21 03:00:55 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.043 |  |
| 2026-08-21 00:14:30 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.063 |  |
| 2026-08-21 03:04:24 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)