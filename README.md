# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_05:40:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,352 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 05:40:53 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-10-14 05:37:19 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-10-14 05:33:35 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.033 | 🔺 Rising |
| 2026-10-14 05:31:56 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.023 |  |
| 2026-10-14 05:27:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.021 |  |
| 2026-10-14 05:16:14 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.027 |  |
| 2026-10-14 05:12:50 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:12:45 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:12:25 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:10:20 | Magura (Kalu Ganga) | 5.42 | 🟡 Alert | 0.054 | 🔺 Rising |
| 2026-10-14 05:08:57 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.010 |  |
| 2026-10-14 05:08:12 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-14 05:08:07 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-14 05:08:04 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:06:21 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.149 |  |
| 2026-10-14 05:05:06 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 05:04:55 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-14 05:04:50 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-14 05:04:23 | Panadugama (Nilwala Ganga) | 6.07 | 🟠 Minor Flood | -0.023 |  |
| 2026-10-14 05:04:07 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-14 05:04:04 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-10-14 05:04:02 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-14 05:03:43 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.100 |  |
| 2026-10-14 05:03:40 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:03:27 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | -48.000 |  |
| 2026-10-14 05:03:24 | Rathnapura (Kalu Ganga) | 4.30 | 🟢 Normal | -48.000 |  |
| 2026-10-14 05:03:17 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.058 |  |
| 2026-10-14 05:02:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:02:38 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:02:36 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-14 05:02:31 | Thawalama (Gin Ganga) | 3.34 | 🟢 Normal | -0.078 |  |
| 2026-10-14 05:02:18 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 05:33:35 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.033 | 🔺 Rising |
| 2026-10-14 05:04:23 | Panadugama (Nilwala Ganga) | 6.07 | 🟠 Minor Flood | -0.023 |  |
| 2026-10-14 05:10:20 | Magura (Kalu Ganga) | 5.42 | 🟡 Alert | 0.054 | 🔺 Rising |
| 2026-10-14 05:04:02 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-14 05:04:50 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-14 05:08:07 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-14 05:04:07 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-14 05:01:17 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 05:05:06 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 05:08:12 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-14 05:02:36 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-14 05:40:53 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-10-14 05:04:04 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-10-14 05:01:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:00:52 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:12:45 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:01:38 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:02:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:12:50 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:03:40 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:02:38 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 05:01:44 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-14 05:04:55 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-14 05:08:57 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.010 |  |
| 2026-10-14 05:02:18 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-10-14 05:01:05 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-10-14 05:27:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.021 |  |
| 2026-10-14 05:37:19 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-10-14 05:31:56 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.023 |  |
| 2026-10-14 05:16:14 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.027 |  |
| 2026-10-14 05:03:17 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.058 |  |
| 2026-10-14 05:02:31 | Thawalama (Gin Ganga) | 3.34 | 🟢 Normal | -0.078 |  |
| 2026-10-14 05:03:43 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.100 |  |
| 2026-10-14 05:06:21 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.149 |  |
| 2026-10-14 05:00:53 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.410 |  |
| 2026-10-14 05:03:27 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | -48.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)