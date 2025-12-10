# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_14:08:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,204 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 14:08:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-10 14:07:26 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:06:03 | Thanthirimale (Malwathu Oya) | 3.76 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-10 14:05:55 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.057 |  |
| 2025-12-10 14:05:52 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.025 |  |
| 2025-12-10 14:05:49 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.020 |  |
| 2025-12-10 14:05:49 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2025-12-10 14:05:28 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.039 |  |
| 2025-12-10 14:04:28 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2025-12-10 14:04:11 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:04:02 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:03:44 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-10 14:03:38 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 14:03:29 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:03:11 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2025-12-10 14:03:04 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-10 14:03:04 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-10 14:02:49 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:02:47 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 14:02:46 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-10 14:02:44 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:02:40 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:02:35 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 14:02:26 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 14:02:21 | Horowpothana (Yan Oya) | 5.21 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-10 14:02:15 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:01:51 | Manampitiya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.040 |  |
| 2025-12-10 14:01:48 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:01:27 | Pitabeddara (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.043 |  |
| 2025-12-10 14:01:24 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-10 14:01:23 | Weraganthota (Mahaweli Ganga) | -0.48 | 🟢 Normal | -0.374 |  |
| 2025-12-10 14:01:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.050 |  |
| 2025-12-10 14:01:22 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.012 |  |
| 2025-12-10 14:01:21 | Yaka Wewa (Ma Oya) | 2.40 | 🟢 Normal | -0.080 |  |
| 2025-12-10 14:00:52 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-10 13:17:12 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.025 |  |
| 2025-12-10 13:12:32 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 14:08:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-10 14:01:24 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-10 14:02:21 | Horowpothana (Yan Oya) | 5.21 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-10 14:06:03 | Thanthirimale (Malwathu Oya) | 3.76 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-10 14:02:35 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 14:02:26 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 14:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 14:03:38 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 14:02:47 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:04:02 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:02:40 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:01:48 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:02:44 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:07:26 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:03:29 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:02:49 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:04:11 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 14:02:15 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:04:40 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-10 14:03:04 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-10 14:03:44 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-10 14:03:04 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-10 14:05:49 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2025-12-10 14:04:28 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2025-12-10 14:01:22 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.012 |  |
| 2025-12-10 14:02:46 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-10 14:05:49 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.020 |  |
| 2025-12-10 14:03:11 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2025-12-10 14:00:52 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-10 14:05:52 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.025 |  |
| 2025-12-10 14:05:28 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.039 |  |
| 2025-12-10 14:01:51 | Manampitiya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.040 |  |
| 2025-12-10 14:01:27 | Pitabeddara (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.043 |  |
| 2025-12-10 14:01:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.050 |  |
| 2025-12-10 14:05:55 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.057 |  |
| 2025-12-10 14:01:21 | Yaka Wewa (Ma Oya) | 2.40 | 🟢 Normal | -0.080 |  |
| 2025-12-10 14:01:23 | Weraganthota (Mahaweli Ganga) | -0.48 | 🟢 Normal | -0.374 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)