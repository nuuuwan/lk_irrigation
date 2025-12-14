# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_15:03:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,762 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 15:03:38 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2025-12-14 15:03:33 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:03:32 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.038 |  |
| 2025-12-14 15:03:24 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:03:15 | Horowpothana (Yan Oya) | 4.33 | 🟢 Normal | -0.039 |  |
| 2025-12-14 15:02:50 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2025-12-14 15:02:48 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.040 |  |
| 2025-12-14 15:02:20 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | -0.010 |  |
| 2025-12-14 15:02:20 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.030 |  |
| 2025-12-14 15:02:16 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.040 |  |
| 2025-12-14 15:02:09 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | 4.842 | 🔺 Rising |
| 2025-12-14 15:02:00 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:57 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:44 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:40 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2025-12-14 15:01:32 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-14 15:01:23 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-14 15:01:13 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:05 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | -0.060 |  |
| 2025-12-14 15:00:29 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:15:11 | Ellagawa (Kalu Ganga) | 1.63 | 🟢 Normal | 4.842 | 🔺 Rising |
| 2025-12-14 14:10:48 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.017 |  |
| 2025-12-14 14:10:47 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:08:23 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.011 |  |
| 2025-12-14 14:06:15 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.076 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 15:02:09 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | 4.842 | 🔺 Rising |
| 2025-12-14 14:02:25 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 15:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-14 14:05:06 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 15:02:00 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:23 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:03:24 | Moragaswewa (Deduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:13 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:02:48 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:01:25 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:01:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:57 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:01:44 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:03:26 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:03:33 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:04:42 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:10:47 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 14:03:18 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:00:29 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-14 15:02:50 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2025-12-14 15:02:20 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:05:07 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2025-12-14 15:01:32 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:02:39 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:02:24 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-14 14:00:27 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-14 14:08:23 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.011 |  |
| 2025-12-14 14:10:48 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.017 |  |
| 2025-12-14 15:03:38 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2025-12-14 15:01:40 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2025-12-14 15:02:20 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.030 |  |
| 2025-12-14 15:03:32 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.038 |  |
| 2025-12-14 15:03:15 | Horowpothana (Yan Oya) | 4.33 | 🟢 Normal | -0.039 |  |
| 2025-12-14 15:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.040 |  |
| 2025-12-14 15:02:16 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.040 |  |
| 2025-12-14 13:06:16 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.053 |  |
| 2025-12-14 15:01:05 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | -0.060 |  |
| 2025-12-14 14:05:31 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.068 |  |
| 2025-12-14 14:06:15 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)