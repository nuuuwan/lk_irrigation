# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_09:11:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,038 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 09:11:05 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-10-19 09:09:14 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.019 |  |
| 2026-10-19 09:09:10 | Panadugama (Nilwala Ganga) | 5.41 | 🟡 Alert | -0.029 |  |
| 2026-10-19 09:09:00 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:08:59 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:07:15 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.075 |  |
| 2026-10-19 09:06:16 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-19 09:06:08 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-10-19 09:05:58 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.118 |  |
| 2026-10-19 09:05:55 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-10-19 09:05:44 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:05:18 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.049 |  |
| 2026-10-19 09:05:00 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.070 |  |
| 2026-10-19 09:04:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:04:28 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:04:23 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-19 09:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.85 | 🟢 Normal | -0.032 |  |
| 2026-10-19 09:04:07 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | -0.061 |  |
| 2026-10-19 09:04:06 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-19 09:04:04 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.058 |  |
| 2026-10-19 09:04:03 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:04:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:03:50 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.062 |  |
| 2026-10-19 09:03:47 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.019 |  |
| 2026-10-19 09:03:41 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:03:38 | Pitabeddara (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.039 |  |
| 2026-10-19 09:03:28 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:03:16 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-10-19 09:03:07 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:02:47 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.060 |  |
| 2026-10-19 09:02:29 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 09:02:23 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.040 |  |
| 2026-10-19 09:02:21 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.015 |  |
| 2026-10-19 09:02:06 | Manampitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-10-19 09:01:40 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-10-19 09:01:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.024 |  |
| 2026-10-19 09:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:00:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:00:46 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:00:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 09:00:22 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:36:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 09:02:29 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 09:09:10 | Panadugama (Nilwala Ganga) | 5.41 | 🟡 Alert | -0.029 |  |
| 2026-10-19 09:04:23 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-19 09:06:16 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-19 09:00:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 09:00:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:04:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:04:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:09:00 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:05:44 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-19 09:04:03 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-19 08:18:26 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-10-19 09:01:40 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-10-19 09:11:05 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-10-19 09:06:08 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-10-19 09:02:21 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.015 |  |
| 2026-10-19 09:05:55 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-10-19 09:09:14 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.019 |  |
| 2026-10-19 09:03:16 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-10-19 09:03:47 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.019 |  |
| 2026-10-19 09:04:28 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:03:07 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:00:46 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:03:41 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:01:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | -0.024 |  |
| 2026-10-19 09:04:06 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-19 09:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.85 | 🟢 Normal | -0.032 |  |
| 2026-10-19 09:03:38 | Pitabeddara (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.039 |  |
| 2026-10-19 09:02:06 | Manampitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-10-19 09:02:23 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.040 |  |
| 2026-10-19 09:05:18 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.049 |  |
| 2026-10-19 09:04:04 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.058 |  |
| 2026-10-19 09:02:47 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.060 |  |
| 2026-10-19 09:04:07 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | -0.061 |  |
| 2026-10-19 09:03:50 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.062 |  |
| 2026-10-19 09:05:00 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.070 |  |
| 2026-10-19 09:07:15 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.075 |  |
| 2026-10-19 09:05:58 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)