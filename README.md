# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_06:28:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,117 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 06:28:14 | Thalgahagoda (Nilwala Ganga) | 1.99 | 🟠 Minor Flood | 0.034 | 🔺 Rising |
| 2026-10-17 06:07:21 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-10-17 06:06:53 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.171 |  |
| 2026-10-17 06:05:30 | Baddegama (Gin Ganga) | 3.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:05:29 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | 0.652 | 🔺 Rising |
| 2026-10-17 06:05:13 | Magura (Kalu Ganga) | 3.79 | 🟢 Normal | -0.088 |  |
| 2026-10-17 06:04:41 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.155 |  |
| 2026-10-17 06:04:22 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:04:01 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.098 |  |
| 2026-10-17 06:03:52 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.006 |  |
| 2026-10-17 06:03:51 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.060 |  |
| 2026-10-17 06:03:48 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-17 06:03:31 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-17 06:03:27 | Dunamale (Aththanagalu Oya) | 3.29 | 🟢 Normal | -0.030 |  |
| 2026-10-17 06:03:23 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-10-17 06:03:13 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 06:03:03 | Ellagawa (Kalu Ganga) | 7.59 | 🟢 Normal | -0.012 |  |
| 2026-10-17 06:02:52 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-10-17 06:02:51 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.081 |  |
| 2026-10-17 06:02:43 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:02:34 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:02:25 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | -0.054 |  |
| 2026-10-17 06:02:24 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-10-17 06:02:16 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.020 |  |
| 2026-10-17 06:02:16 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-17 06:02:11 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-17 06:02:07 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.105 |  |
| 2026-10-17 06:02:03 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-17 06:01:29 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.041 |  |
| 2026-10-17 06:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | -0.012 |  |
| 2026-10-17 06:00:49 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:00:41 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-17 06:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-10-17 06:00:22 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-17 06:00:19 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.210 |  |
| 2026-10-17 06:00:18 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 06:28:14 | Thalgahagoda (Nilwala Ganga) | 1.99 | 🟠 Minor Flood | 0.034 | 🔺 Rising |
| 2026-10-17 05:19:21 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -4.909 |  |
| 2026-10-17 06:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | -0.012 |  |
| 2026-10-17 06:05:29 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | 0.652 | 🔺 Rising |
| 2026-10-17 06:00:41 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-17 06:02:11 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-17 06:03:48 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-17 06:00:22 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-17 06:00:18 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 06:03:13 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 06:04:22 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:00:49 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:05:30 | Baddegama (Gin Ganga) | 3.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:02:43 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:02:34 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 06:03:52 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.006 |  |
| 2026-10-17 06:03:31 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-17 06:02:03 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-17 06:03:03 | Ellagawa (Kalu Ganga) | 7.59 | 🟢 Normal | -0.012 |  |
| 2026-10-17 06:07:21 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-10-17 06:02:16 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-17 06:02:16 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.020 |  |
| 2026-10-17 06:02:52 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-10-17 06:02:24 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-10-17 06:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-17 06:03:27 | Dunamale (Aththanagalu Oya) | 3.29 | 🟢 Normal | -0.030 |  |
| 2026-10-17 06:03:23 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.040 |  |
| 2026-10-17 06:01:29 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.041 |  |
| 2026-10-17 06:02:25 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | -0.054 |  |
| 2026-10-17 06:03:51 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.060 |  |
| 2026-10-17 06:02:51 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.081 |  |
| 2026-10-17 06:05:13 | Magura (Kalu Ganga) | 3.79 | 🟢 Normal | -0.088 |  |
| 2026-10-17 06:04:01 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.098 |  |
| 2026-10-17 06:02:07 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.105 |  |
| 2026-10-17 06:04:41 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.155 |  |
| 2026-10-17 06:06:53 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.171 |  |
| 2026-10-17 06:00:19 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)