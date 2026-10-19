# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_12:10:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,157 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 12:10:21 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-10-19 12:09:40 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.102 |  |
| 2026-10-19 12:09:16 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-10-19 12:08:53 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-10-19 12:08:04 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-10-19 12:07:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:06:04 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:05:38 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:05:36 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.030 |  |
| 2026-10-19 12:05:16 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.020 |  |
| 2026-10-19 12:05:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-10-19 12:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.025 |  |
| 2026-10-19 12:04:36 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:04:35 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | -0.039 |  |
| 2026-10-19 12:04:34 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-10-19 12:04:28 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:04:20 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 12:04:02 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-10-19 12:04:01 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:03:50 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:03:43 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:03:31 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:03:23 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-10-19 12:03:06 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.039 |  |
| 2026-10-19 12:03:04 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | -0.048 |  |
| 2026-10-19 12:03:03 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.072 |  |
| 2026-10-19 12:02:54 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.032 |  |
| 2026-10-19 12:02:52 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-10-19 12:02:50 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.038 |  |
| 2026-10-19 12:02:47 | Moragaswewa (Deduru Oya) | 1.66 | 🟢 Normal | -0.073 |  |
| 2026-10-19 12:02:38 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:02:33 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.029 |  |
| 2026-10-19 12:02:31 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-19 12:02:30 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:02:15 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-19 12:01:50 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:01:07 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-10-19 12:00:49 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 12:00:39 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 12:03:04 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | -0.048 |  |
| 2026-10-19 12:04:35 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | -0.039 |  |
| 2026-10-19 12:02:15 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-10-19 12:02:31 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-19 12:00:49 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 12:04:20 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 12:03:50 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:04:36 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:02:30 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:04:01 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:07:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:05:38 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:03:43 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-19 12:08:53 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-10-19 12:08:04 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-10-19 12:04:34 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-10-19 12:01:50 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:06:04 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:03:31 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:02:38 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:04:28 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-19 12:09:16 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-10-19 12:04:02 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.019 |  |
| 2026-10-19 12:05:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-10-19 12:05:16 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.020 |  |
| 2026-10-19 12:10:21 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-10-19 12:03:23 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-10-19 12:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.025 |  |
| 2026-10-19 12:02:33 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.029 |  |
| 2026-10-19 12:05:36 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.030 |  |
| 2026-10-19 12:02:54 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.032 |  |
| 2026-10-19 12:02:50 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.038 |  |
| 2026-10-19 12:03:06 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.039 |  |
| 2026-10-19 12:02:52 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-10-19 12:01:07 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-10-19 12:03:03 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.072 |  |
| 2026-10-19 12:02:47 | Moragaswewa (Deduru Oya) | 1.66 | 🟢 Normal | -0.073 |  |
| 2026-10-19 12:09:40 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)