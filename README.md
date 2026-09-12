# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_14:06:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **258,904 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 14:06:28 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-12 14:05:36 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:05:17 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-09-12 14:04:44 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:04:38 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:04:29 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:04:23 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:04:22 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-09-12 14:04:10 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-09-12 14:03:54 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-12 14:03:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:48 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:03:35 | Moragaswewa (Deduru Oya) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:29 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:09 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:06 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:50 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 14:02:42 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:42 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:39 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:02:25 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-12 14:02:20 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:08 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.020 |  |
| 2026-09-12 14:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:01:46 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:01:42 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | -0.013 |  |
| 2026-09-12 14:01:42 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.029 |  |
| 2026-09-12 14:01:21 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:01:12 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:00:38 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:00:09 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-09-12 14:00:09 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 14:03:54 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-12 14:04:22 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-09-12 14:02:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-12 14:06:28 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-12 14:02:50 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 13:01:58 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:42 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:04:38 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:35 | Moragaswewa (Deduru Oya) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:25 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:05:36 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:42 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-12 13:00:55 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:06 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-09-12 13:07:05 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:01:21 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:01:12 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:00:09 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:04:44 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:29 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:03:09 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:01:46 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:04:29 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-12 14:02:20 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:04:23 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:02:39 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:00:38 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:03:48 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-12 14:00:09 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-09-12 14:01:42 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | -0.013 |  |
| 2026-09-12 14:02:08 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.020 |  |
| 2026-09-12 14:05:17 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-09-12 14:04:10 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-09-12 14:01:42 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.029 |  |
| 2026-09-12 13:08:32 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)