# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_11:15:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,084 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 11:15:55 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:11:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:11:39 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:10:46 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.027 |  |
| 2026-09-19 11:07:27 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.031 |  |
| 2026-09-19 11:07:05 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-19 11:07:01 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.070 |  |
| 2026-09-19 11:06:46 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-09-19 11:06:29 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-09-19 11:06:04 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.028 |  |
| 2026-09-19 11:05:51 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-09-19 11:05:29 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 11:05:25 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-19 11:04:57 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.031 |  |
| 2026-09-19 11:04:43 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.031 |  |
| 2026-09-19 11:04:37 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:04:27 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-19 11:04:26 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:04:16 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-09-19 11:03:24 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:03:21 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-19 11:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:03:12 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:02:48 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:02:46 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-19 11:02:40 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:02:40 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-09-19 11:02:27 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:02:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-19 11:02:06 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-19 11:01:47 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:45 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:40 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:37 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:33 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.042 |  |
| 2026-09-19 11:01:28 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:25 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:00:38 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:00:34 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 11:02:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-19 11:05:29 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 11:05:25 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-19 11:01:47 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:00:34 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:25 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:03:24 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:00:38 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:40 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:02:48 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:04:26 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:03:12 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:11:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:02:40 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:02:27 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:15:55 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:45 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:11:39 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:37 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:01:28 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 11:07:05 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-19 11:02:46 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-19 11:04:27 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-19 11:02:06 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-19 11:04:16 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-09-19 11:06:46 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-09-19 11:02:40 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-09-19 11:03:21 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-19 11:10:46 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | -0.027 |  |
| 2026-09-19 11:06:04 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.028 |  |
| 2026-09-19 11:06:29 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-09-19 11:05:51 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-09-19 11:07:27 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.031 |  |
| 2026-09-19 11:04:43 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.031 |  |
| 2026-09-19 11:04:57 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.031 |  |
| 2026-09-19 11:01:33 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.042 |  |
| 2026-09-19 11:07:01 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)