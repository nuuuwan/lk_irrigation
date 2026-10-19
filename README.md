# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_23:30:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,574 measurements** from **39** stations.
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
| 2026-10-19 23:30:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:20:01 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.009 |  |
| 2026-10-19 23:13:46 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-10-19 23:12:55 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-19 23:11:35 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-19 23:10:29 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-10-19 23:06:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:05:42 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:04:52 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-10-19 23:04:46 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:04:34 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.095 |  |
| 2026-10-19 23:04:33 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.029 |  |
| 2026-10-19 23:04:04 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-10-19 23:04:01 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-10-19 23:03:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | -0.023 |  |
| 2026-10-19 23:03:28 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.012 |  |
| 2026-10-19 23:03:09 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-10-19 23:03:05 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:03:05 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.291 |  |
| 2026-10-19 23:02:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:02:37 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.021 |  |
| 2026-10-19 23:02:21 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.049 |  |
| 2026-10-19 23:02:05 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-19 23:02:04 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 1.480 | 🔺 Rising |
| 2026-10-19 23:01:45 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:01:36 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.040 |  |
| 2026-10-19 23:01:27 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.051 |  |
| 2026-10-19 23:01:15 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-10-19 23:01:14 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-19 23:00:28 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.079 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 23:12:55 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-19 23:13:46 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-10-19 23:02:04 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 1.480 | 🔺 Rising |
| 2026-10-19 23:03:09 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-10-19 22:02:56 | Kithulgala (Kelani Ganga) | 2.56 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-10-19 23:02:05 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-19 23:11:35 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-19 23:02:43 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:03:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:01:45 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:03:05 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:02:21 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:30:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:06:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:05:42 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:04:46 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 23:20:01 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.009 |  |
| 2026-10-19 22:06:11 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-10-19 23:01:14 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-19 23:04:04 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-10-19 23:04:01 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-10-19 23:03:28 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.012 |  |
| 2026-10-19 23:04:52 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-10-19 23:10:29 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-10-19 23:02:37 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.021 |  |
| 2026-10-19 23:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | -0.023 |  |
| 2026-10-19 23:04:33 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.029 |  |
| 2026-10-19 23:01:36 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.040 |  |
| 2026-10-19 23:01:15 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-10-19 22:02:25 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.041 |  |
| 2026-10-19 23:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.049 |  |
| 2026-10-19 23:01:27 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.051 |  |
| 2026-10-19 22:04:43 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.067 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-19 23:00:28 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.079 |  |
| 2026-10-19 23:04:34 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.095 |  |
| 2026-10-19 23:03:05 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.291 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)