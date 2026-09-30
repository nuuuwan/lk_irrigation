# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_18:27:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:19:58 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:11:07 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-09-30 18:11:04 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-30 18:07:54 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-09-30 18:06:22 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:06:05 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:06:05 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 18:04:07 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.010 |  |
| 2026-09-30 18:03:56 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-30 18:03:46 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:03:35 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:03:23 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:03:22 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 18:03:14 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:03:12 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.019 |  |
| 2026-09-30 18:03:08 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:02:59 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.147 |  |
| 2026-09-30 18:02:57 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.060 |  |
| 2026-09-30 18:02:42 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-09-30 18:02:29 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 18:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-09-30 18:02:27 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:02:23 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.043 |  |
| 2026-09-30 18:01:58 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-09-30 18:01:47 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:01:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:01:28 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-09-30 18:01:21 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-30 18:01:18 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 18:01:07 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:01:07 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-30 18:00:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:00:24 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:00:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.123 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 18:02:42 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-30 18:11:04 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-30 18:03:56 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-30 18:01:18 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 18:02:29 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 18:06:05 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 18:03:22 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 18:01:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:09:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:01:47 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:19:58 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:01:07 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:01:07 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:02:57 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:06:22 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:03:14 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:06:05 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:03:35 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:00:24 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:04:07 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.010 |  |
| 2026-09-30 18:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-09-30 18:01:21 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-30 18:07:54 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-09-30 18:03:12 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.019 |  |
| 2026-09-30 18:11:07 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-09-30 18:00:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:03:46 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:02:27 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:03:23 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:03:08 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.021 |  |
| 2026-09-30 18:01:58 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-09-30 18:01:28 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-09-30 18:02:23 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.043 |  |
| 2026-09-30 18:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.060 |  |
| 2026-09-30 18:00:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.123 |  |
| 2026-09-30 18:02:59 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)