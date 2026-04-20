# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_04:50:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,739 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 04:50:44 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-21 04:35:39 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-21 04:35:11 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-21 04:29:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 25.500 | 🔺 Rising |
| 2026-04-21 04:29:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | 25.500 | 🔺 Rising |
| 2026-04-21 04:22:35 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.004 |  |
| 2026-04-21 04:12:15 | Thanamalwila (Kirindi Oya) | 3.86 | 🟢 Normal | -0.353 |  |
| 2026-04-21 04:11:14 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-21 04:11:06 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.180 |  |
| 2026-04-21 04:08:51 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 04:29:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 25.500 | 🔺 Rising |
| 2026-04-21 04:02:04 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 1.545 | 🔺 Rising |
| 2026-04-21 04:02:48 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-04-21 04:04:04 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-21 04:35:11 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-21 04:06:36 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-21 04:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-21 04:11:14 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-21 04:08:51 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-21 04:03:51 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-21 04:03:48 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 04:50:44 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-21 04:01:52 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 04:01:47 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-21 04:05:48 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 04:03:47 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 04:35:39 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-21 04:22:35 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.004 |  |
| 2026-04-21 03:01:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 04:01:15 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:01:10 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 04:03:45 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-21 04:01:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 04:04:11 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-21 04:01:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-21 04:04:27 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-21 04:00:31 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-04-21 04:02:29 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.031 |  |
| 2026-04-21 04:01:24 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.032 |  |
| 2026-04-21 04:01:19 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-04-21 04:02:25 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.051 |  |
| 2026-04-21 04:04:39 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.059 |  |
| 2026-04-21 04:11:06 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.180 |  |
| 2026-04-21 04:01:26 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.217 |  |
| 2026-04-21 04:12:15 | Thanamalwila (Kirindi Oya) | 3.86 | 🟢 Normal | -0.353 |  |
| 2026-04-21 04:01:13 | Kuda Oya (Kirindi Oya) | 3.11 | 🟢 Normal | -0.502 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)