# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_11:21:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,132 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 11:21:04 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.008 |  |
| 2026-11-26 11:17:05 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-26 11:14:35 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:11:38 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.025 |  |
| 2026-11-26 11:11:07 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.039 |  |
| 2026-11-26 11:08:51 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.029 |  |
| 2026-11-26 11:08:34 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:07:53 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.001 |  |
| 2026-11-26 11:07:04 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | -0.080 |  |
| 2026-11-26 11:06:02 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.085 |  |
| 2026-11-26 11:05:34 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.058 |  |
| 2026-11-26 11:05:05 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.064 |  |
| 2026-11-26 11:05:04 | Moragaswewa (Deduru Oya) | 4.37 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-26 11:04:50 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.070 |  |
| 2026-11-26 11:04:36 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-11-26 11:04:23 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-26 11:04:21 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-11-26 11:04:11 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.040 |  |
| 2026-11-26 11:03:50 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.060 |  |
| 2026-11-26 11:03:43 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:03:43 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 11:03:30 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-26 11:03:26 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-26 11:03:05 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.035 |  |
| 2026-11-26 11:02:49 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.100 |  |
| 2026-11-26 11:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | -0.010 |  |
| 2026-11-26 11:02:33 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.020 |  |
| 2026-11-26 11:02:27 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.100 |  |
| 2026-11-26 11:01:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-26 11:01:45 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-11-26 11:01:45 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:01:40 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:01:27 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-11-26 11:01:12 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.157 |  |
| 2026-11-26 11:01:11 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-11-26 11:01:06 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:00:30 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-26 11:00:16 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 11:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | -0.010 |  |
| 2026-11-26 11:03:50 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.060 |  |
| 2026-11-26 11:05:04 | Moragaswewa (Deduru Oya) | 4.37 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-26 11:01:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-26 11:03:30 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-26 11:03:43 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 11:07:53 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.001 |  |
| 2026-11-26 11:01:11 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:01:45 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:01:40 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:03:43 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:14:35 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:08:34 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:01:06 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-26 11:21:04 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.008 |  |
| 2026-11-26 11:04:23 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-26 11:17:05 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-26 11:03:26 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-26 11:00:30 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-26 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-11-26 11:04:21 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-11-26 11:01:45 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-11-26 11:02:33 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.020 |  |
| 2026-11-26 11:01:27 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-11-26 11:11:38 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.025 |  |
| 2026-11-26 11:08:51 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.029 |  |
| 2026-11-26 11:00:16 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.030 |  |
| 2026-11-26 11:03:05 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.035 |  |
| 2026-11-26 11:04:36 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-11-26 11:11:07 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.039 |  |
| 2026-11-26 11:04:11 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.040 |  |
| 2026-11-26 11:05:34 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.058 |  |
| 2026-11-26 11:05:05 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.064 |  |
| 2026-11-26 11:04:50 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.070 |  |
| 2026-11-26 11:07:04 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | -0.080 |  |
| 2026-11-26 11:06:02 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.085 |  |
| 2026-11-26 11:02:49 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.100 |  |
| 2026-11-26 11:02:27 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.100 |  |
| 2026-11-26 11:01:12 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)