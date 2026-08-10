# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_04:19:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 04:19:49 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:13:47 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:09:56 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-11 04:09:19 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:09:02 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-08-11 04:06:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-08-11 04:05:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:04:45 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:04:41 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2026-08-11 04:04:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:53 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:44 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-08-11 04:03:22 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:19 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.061 |  |
| 2026-08-11 04:03:16 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-08-11 04:03:09 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:03 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:02:54 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:02:38 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-11 04:02:25 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:02:23 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-08-11 04:02:04 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-11 04:02:03 | Peradeniya (Mahaweli Ganga) | 3.47 | 🟢 Normal | -0.021 |  |
| 2026-08-11 04:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-08-11 04:01:38 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 04:01:22 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 04:01:16 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:01:14 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:01:13 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.020 |  |
| 2026-08-11 04:01:10 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:01:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:00:20 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-11 03:59:13 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 04:09:02 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-08-11 04:09:56 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-11 04:02:38 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-11 04:01:22 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 04:01:38 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 04:00:20 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:13:47 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:01:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-08-11 03:06:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:53 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:02:17 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:02:25 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:04:45 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:22 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:01:16 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:04:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:09:19 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:03:03 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-11 03:01:02 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:05:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:02:54 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:19:49 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:01:10 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:01:14 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:02:04 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-10 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-11 04:01:13 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.020 |  |
| 2026-08-11 04:03:16 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-08-11 04:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-08-11 04:02:03 | Peradeniya (Mahaweli Ganga) | 3.47 | 🟢 Normal | -0.021 |  |
| 2026-08-11 03:01:08 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.022 |  |
| 2026-08-11 04:02:23 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-08-11 04:03:44 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-08-11 04:04:41 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2026-08-11 04:06:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-08-11 04:03:19 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.061 |  |
| 2026-08-11 03:10:48 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -6.353 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)