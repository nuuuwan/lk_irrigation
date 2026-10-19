# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_21:07:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,500 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 21:07:35 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-19 21:07:19 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-10-19 21:06:30 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-10-19 21:06:24 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-10-19 21:06:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-19 21:05:52 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 21:05:31 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | -0.413 |  |
| 2026-10-19 21:05:21 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | -0.075 |  |
| 2026-10-19 21:04:56 | Panadugama (Nilwala Ganga) | 5.05 | 🟡 Alert | -0.033 |  |
| 2026-10-19 21:04:40 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-19 21:04:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 21:04:01 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-19 21:03:44 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-10-19 21:03:32 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.031 |  |
| 2026-10-19 21:03:28 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-19 21:03:23 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-19 21:03:11 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.039 |  |
| 2026-10-19 21:02:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 21:02:48 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 21:02:45 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-10-19 21:02:40 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.040 |  |
| 2026-10-19 21:02:30 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-10-19 21:02:26 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-10-19 21:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.061 |  |
| 2026-10-19 21:02:12 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.013 |  |
| 2026-10-19 21:02:10 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-19 21:01:48 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-19 21:01:43 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-10-19 21:01:24 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.112 |  |
| 2026-10-19 21:01:20 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.064 |  |
| 2026-10-19 21:01:16 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 21:00:59 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | 0.138 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 20:07:34 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | -0.025 |  |
| 2026-10-19 21:04:56 | Panadugama (Nilwala Ganga) | 5.05 | 🟡 Alert | -0.033 |  |
| 2026-10-19 21:04:01 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-19 21:00:59 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-19 21:01:48 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-19 21:03:23 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-19 21:03:28 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-19 21:01:16 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 20:06:06 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-19 21:02:48 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 21:02:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-19 21:05:52 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 21:06:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-19 21:04:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 21:03:44 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-10-19 21:04:40 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-19 21:07:35 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-19 21:07:19 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-10-19 21:01:43 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-10-19 21:02:12 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.013 |  |
| 2026-10-19 21:06:30 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-10-19 21:02:45 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-10-19 21:02:10 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-19 21:06:24 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-10-19 20:18:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.55 | 🟢 Normal | -0.025 |  |
| 2026-10-19 21:03:32 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.031 |  |
| 2026-10-19 21:02:30 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-10-19 21:02:26 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-10-19 20:01:39 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.033 |  |
| 2026-10-19 21:03:11 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.039 |  |
| 2026-10-19 21:02:40 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.040 |  |
| 2026-10-19 21:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.061 |  |
| 2026-10-19 21:01:20 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.064 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-19 21:05:21 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | -0.075 |  |
| 2026-10-19 21:01:24 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.112 |  |
| 2026-10-19 21:05:31 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | -0.413 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)