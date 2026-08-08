# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_15:14:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,954 measurements** from **39** stations.
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
| 2026-08-08 15:14:23 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-08 15:13:20 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:10:37 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-08 15:09:35 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-08 15:09:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.081 |  |
| 2026-08-08 15:08:53 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:07:41 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-08 15:06:35 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:05:12 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:05:06 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-08-08 15:04:26 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:04:16 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:04:14 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:03:39 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:03:33 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.029 |  |
| 2026-08-08 15:03:28 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-08 15:03:22 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:03:13 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.011 |  |
| 2026-08-08 15:03:06 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:03:02 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:02:58 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.032 |  |
| 2026-08-08 15:02:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:02:28 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 15:02:19 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-08 15:02:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:02:01 | Thanthirimale (Malwathu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:56 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:48 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:01:38 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:22 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 15:01:17 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:06 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-08 15:01:00 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:00:58 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:00:24 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-08 15:00:11 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:00:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 15:14:23 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-08-08 15:09:35 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-08 15:00:24 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-08 15:03:28 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-08 15:07:41 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-08 15:02:19 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-08 15:10:37 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-08 15:01:06 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-08 15:01:22 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 15:02:28 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 15:13:20 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:04:26 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:17 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:00:58 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:56 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:08:53 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:02:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:05:12 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:04:16 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:02:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:00:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:03:06 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:04:14 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:03:39 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:03:02 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:02:01 | Thanthirimale (Malwathu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:38 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:00 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:48 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:03:22 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:06:35 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:00:11 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:03:13 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.011 |  |
| 2026-08-08 15:05:06 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-08-08 15:03:33 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.029 |  |
| 2026-08-08 15:02:58 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.032 |  |
| 2026-08-08 15:09:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)