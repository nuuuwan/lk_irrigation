# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_06:35:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,008 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 06:35:57 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.001 |  |
| 2026-09-08 06:26:23 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:13:49 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.026 |  |
| 2026-09-08 06:08:43 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.183 |  |
| 2026-09-08 06:07:48 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:07:43 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-09-08 06:06:45 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-09-08 06:06:26 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.057 |  |
| 2026-09-08 06:06:22 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:05:50 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 06:05:38 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 06:05:19 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.033 |  |
| 2026-09-08 06:05:05 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-08 06:05:02 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:04:17 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 06:04:04 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:41 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:36 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:22 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:20 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:20 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:16 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.193 |  |
| 2026-09-08 06:03:16 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2026-09-08 06:03:12 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-09-08 06:03:12 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 06:02:46 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-08 06:02:44 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:41 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-08 06:02:40 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-09-08 06:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:23 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:11 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:01:29 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-08 06:01:23 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:01:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.544 | 🔺 Rising |
| 2026-09-08 06:01:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-08 06:01:09 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:00:57 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.031 |  |
| 2026-09-08 06:00:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 06:01:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.544 | 🔺 Rising |
| 2026-09-08 06:02:46 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-08 06:01:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-08 06:05:05 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-08 06:01:29 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-07 18:10:27 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-08 06:03:12 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 06:05:50 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 06:05:38 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 06:04:17 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 06:35:57 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.001 |  |
| 2026-09-08 06:01:23 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:04:04 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:01:09 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:00:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:26:23 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:11 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:07:48 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:36 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:41 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:05:02 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:02:23 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:20 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:03:20 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:06:22 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-08 06:06:45 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-09-08 06:02:41 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-08 06:02:40 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-09-08 06:13:49 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.026 |  |
| 2026-09-08 06:00:57 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.031 |  |
| 2026-09-08 06:05:19 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.033 |  |
| 2026-09-08 06:03:16 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2026-09-08 06:06:26 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.057 |  |
| 2026-09-08 06:03:12 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-09-08 06:07:43 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-09-08 06:08:43 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.183 |  |
| 2026-09-08 06:03:16 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)