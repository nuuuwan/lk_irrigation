# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--28_10:08:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **245,428 measurements** from **39** stations.
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
| 2026-08-28 10:08:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-08-28 10:07:09 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-08-28 10:06:51 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:06:46 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:06:11 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.066 |  |
| 2026-08-28 10:05:56 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:05:52 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-28 10:05:09 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:05:04 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-08-28 10:04:14 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-08-28 10:04:13 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 10:03:52 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 10:03:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:03:42 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:03:34 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-28 10:03:12 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.020 |  |
| 2026-08-28 10:02:43 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:02:40 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:02:39 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:02:11 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-28 10:02:07 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 10:01:48 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:01:45 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.029 |  |
| 2026-08-28 10:01:39 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.032 |  |
| 2026-08-28 10:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:01:17 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.092 |  |
| 2026-08-28 10:01:17 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:01:11 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-28 10:00:53 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.013 |  |
| 2026-08-28 10:00:42 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:00:35 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:00:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-28 09:04:33 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.414 | 🔺 Rising |
| 2026-08-28 10:01:11 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-28 10:02:11 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-28 10:05:52 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-28 10:02:07 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 10:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 10:03:52 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 10:03:42 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:00:07 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:04:13 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:00:35 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:02:40 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:00:42 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-28 09:03:44 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:05:56 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:03:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:06:46 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:03:12 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:02:43 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:05:09 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-28 09:05:02 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:02:39 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:06:51 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:01:48 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:01:17 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-28 10:03:34 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-28 10:05:04 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-08-28 10:00:53 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.013 |  |
| 2026-08-28 10:07:09 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-08-28 10:04:14 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-08-28 10:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.020 |  |
| 2026-08-28 09:02:07 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.025 |  |
| 2026-08-28 10:08:16 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-08-28 09:10:45 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.029 |  |
| 2026-08-28 10:01:45 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.029 |  |
| 2026-08-28 10:01:39 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.032 |  |
| 2026-08-28 10:06:11 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.066 |  |
| 2026-08-28 10:01:17 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)