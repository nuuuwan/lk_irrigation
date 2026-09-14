# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_06:18:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 06:18:53 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:18:16 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.002 |  |
| 2026-09-14 06:11:39 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.053 |  |
| 2026-09-14 06:09:56 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-14 06:09:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:07:22 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-14 06:06:23 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.031 |  |
| 2026-09-14 06:05:37 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:05:31 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:05:23 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.021 |  |
| 2026-09-14 06:05:14 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.023 |  |
| 2026-09-14 06:05:13 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:04:56 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.077 |  |
| 2026-09-14 06:04:38 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.156 |  |
| 2026-09-14 06:04:33 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-14 06:04:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-09-14 06:03:55 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.101 |  |
| 2026-09-14 06:03:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:03:46 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 06:03:23 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:03:18 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-14 06:02:48 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-14 06:02:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:02:39 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.271 |  |
| 2026-09-14 06:02:33 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-09-14 06:02:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-09-14 06:02:14 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-14 06:02:12 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:02:10 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 06:02:14 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-14 06:04:33 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-14 06:09:56 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-14 06:07:22 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-14 06:03:18 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-14 06:03:46 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 06:01:56 | Weraganthota (Mahaweli Ganga) | -3.57 | 🟢 Normal | 0.003 |  |
| 2026-09-14 06:18:16 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.002 |  |
| 2026-09-14 06:18:53 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:01:43 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:01:08 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:02:12 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:02:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:09:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:03:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:00:21 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:03:23 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:05:31 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:05:13 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:01:27 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:05:37 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:01:18 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 06:00:45 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-14 06:02:33 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-09-14 06:02:48 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-14 06:02:10 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.015 |  |
| 2026-09-14 06:04:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-09-14 06:05:23 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.021 |  |
| 2026-09-14 06:05:14 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.023 |  |
| 2026-09-14 06:06:23 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.031 |  |
| 2026-09-14 06:02:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-09-14 06:11:39 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.053 |  |
| 2026-09-14 06:04:56 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.077 |  |
| 2026-09-14 06:03:55 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.101 |  |
| 2026-09-14 06:04:38 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.156 |  |
| 2026-09-14 06:02:39 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.271 |  |
| 2026-09-14 06:01:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -1.132 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)