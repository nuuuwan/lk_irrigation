# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_01:02:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,307 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 01:02:50 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:02:39 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:02:33 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:02:27 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 01:02:27 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 01:02:08 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:56 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:01:47 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:41 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 01:01:40 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:27 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:01:23 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:00:29 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.105 |  |
| 2025-12-13 00:58:24 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2025-12-13 00:46:00 | Thaldena (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2025-12-13 00:31:30 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.450 |  |
| 2025-12-13 00:16:57 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:16:43 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | -0.017 |  |
| 2025-12-13 00:11:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:10:47 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:09:23 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:09:13 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.105 |  |
| 2025-12-13 00:07:08 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:05:50 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 12.101 | 🔺 Rising |
| 2025-12-13 00:05:42 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:05:15 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 00:04:53 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 00:02:00 | Horowpothana (Yan Oya) | 6.35 | 🟡 Alert | -0.005 |  |
| 2025-12-13 00:05:50 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 12.101 | 🔺 Rising |
| 2025-12-13 00:46:00 | Thaldena (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2025-12-12 23:05:26 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-13 00:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-13 01:02:27 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 23:05:48 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-13 01:02:27 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 01:01:41 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 01:02:39 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 00:04:05 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:02:33 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 00:02:55 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:57 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:47 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:40 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:03:37 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:11:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:02:50 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:02:12 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:02:08 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:04:53 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:07:08 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:05:42 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:56 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:01:23 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:01:27 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 00:01:30 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-13 00:01:03 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2025-12-13 00:16:43 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | -0.017 |  |
| 2025-12-13 00:03:57 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-12-13 00:58:24 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2025-12-13 00:00:56 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.055 |  |
| 2025-12-13 01:00:29 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.105 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-13 00:31:30 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.450 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)