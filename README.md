# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_16:17:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 16:17:07 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.009 |  |
| 2025-12-22 16:16:03 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:15:23 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-22 16:09:18 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:08:38 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:07:23 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2025-12-22 16:06:04 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:05:56 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:05:22 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:05:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:39 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:39 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.029 |  |
| 2025-12-22 16:04:33 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:28 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:04 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:04:02 | Thanthirimale (Malwathu Oya) | 4.45 | 🟢 Normal | -0.049 |  |
| 2025-12-22 16:03:52 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2025-12-22 16:03:36 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:03:02 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-22 16:02:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:38 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2025-12-22 16:02:38 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:02:28 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:27 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-22 16:02:26 | Horowpothana (Yan Oya) | 3.35 | 🟢 Normal | -0.049 |  |
| 2025-12-22 16:02:24 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:23 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:16 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:02 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:01:51 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:01:40 | Manampitiya (Mahaweli Ganga) | 2.37 | 🟢 Normal | -0.031 |  |
| 2025-12-22 16:01:27 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2025-12-22 16:01:25 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:00:22 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:00:11 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:00:10 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 16:02:38 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2025-12-22 16:03:02 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-22 16:02:27 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-22 16:15:23 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-22 16:16:03 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-22 15:02:30 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:23 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:24 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:28 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:05:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:02 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:00:11 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:28 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:01:51 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:09:18 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:05:22 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:05:56 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:39 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:33 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:16 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:39 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:17:07 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.009 |  |
| 2025-12-22 16:06:04 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:04:04 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:08:38 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:01:25 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:00:10 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:02:38 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:00:22 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:03:36 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:01:27 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2025-12-22 16:07:23 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2025-12-22 16:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.029 |  |
| 2025-12-22 16:03:52 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2025-12-22 16:01:40 | Manampitiya (Mahaweli Ganga) | 2.37 | 🟢 Normal | -0.031 |  |
| 2025-12-22 16:04:02 | Thanthirimale (Malwathu Oya) | 4.45 | 🟢 Normal | -0.049 |  |
| 2025-12-22 16:02:26 | Horowpothana (Yan Oya) | 3.35 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)