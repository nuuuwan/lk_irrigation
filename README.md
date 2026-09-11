# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_07:15:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **257,747 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-11 07:15:48 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.016 |  |
| 2026-09-11 07:15:22 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-09-11 07:12:50 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:10:21 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-09-11 07:10:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:09:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-11 07:09:48 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:09:42 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:09:16 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:08:31 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.083 |  |
| 2026-09-11 07:08:16 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:07:44 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-09-11 07:07:13 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-11 07:07:09 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:05:28 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-11 07:05:17 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:04:33 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-11 07:04:32 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:03:51 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:03:48 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-09-11 07:03:46 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:03:45 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.146 |  |
| 2026-09-11 07:03:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:03:03 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:02:59 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-11 07:02:51 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.132 |  |
| 2026-09-11 07:02:42 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:02:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.131 |  |
| 2026-09-11 07:02:18 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-11 07:02:15 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:02:14 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:01:46 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-11 07:01:38 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.002 |  |
| 2026-09-11 07:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-09-11 07:01:06 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:00:29 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:00:14 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-11 07:02:59 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-11 07:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-11 07:09:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-11 06:06:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-11 07:01:46 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-11 07:07:13 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-11 07:04:33 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-11 06:01:30 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 07:09:16 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:05:17 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:00:29 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:04:32 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:02:14 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:01:06 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:10:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:09:48 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:03:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:03:03 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:07:09 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:03:51 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:02:18 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:12:50 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:03:46 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:02:15 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:08:16 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:09:42 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-11 07:01:38 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.002 |  |
| 2026-09-11 07:15:22 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-09-11 07:10:21 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-09-11 07:05:28 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-11 07:07:44 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-09-11 07:00:14 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-09-11 07:15:48 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.016 |  |
| 2026-09-11 07:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-09-11 07:03:48 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-09-11 07:08:31 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.083 |  |
| 2026-09-11 07:02:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.131 |  |
| 2026-09-11 07:02:51 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.132 |  |
| 2026-09-11 07:03:45 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)