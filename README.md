# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_04:33:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,014 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 04:33:57 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:22:28 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:21:40 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.007 |  |
| 2026-09-07 04:13:21 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-07 04:13:03 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.016 |  |
| 2026-09-07 04:12:58 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 04:08:23 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-09-07 04:07:06 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-09-07 04:06:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-07 04:06:28 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.058 |  |
| 2026-09-07 04:05:22 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:04:23 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-07 04:04:07 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-07 04:04:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:03:25 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:03:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:03:23 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:03:22 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:02:31 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:02:06 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:02:03 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.052 |  |
| 2026-09-07 04:01:53 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:48 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 196.800 | 🔺 Rising |
| 2026-09-07 04:01:46 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:43 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:33 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 196.800 | 🔺 Rising |
| 2026-09-07 04:01:16 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:11 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:10 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:00:46 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 03:58:19 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 04:01:48 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 196.800 | 🔺 Rising |
| 2026-09-07 03:05:21 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-07 03:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-07 04:06:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-07 04:04:07 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-07 04:04:23 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-07 04:12:58 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 03:05:02 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-07 04:03:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:00:46 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:11 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 03:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:04:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:46 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:43 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:06:01 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:06:07 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:03:23 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:16 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:33:57 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:05:22 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:03:25 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:02:31 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 03:03:04 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:03:22 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:53 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:01:51 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:22:28 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:01:10 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:02:06 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 04:21:40 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.007 |  |
| 2026-09-07 04:08:23 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-09-07 04:13:21 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-07 03:09:07 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.016 |  |
| 2026-09-07 04:13:03 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.016 |  |
| 2026-09-07 04:07:06 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-09-07 04:02:03 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.052 |  |
| 2026-09-07 04:06:28 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.058 |  |
| 2026-09-06 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)