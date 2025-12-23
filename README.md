# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_11:15:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,649 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 11:15:46 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:12:36 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:09:00 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:05:35 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:05:17 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:05:11 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:05:08 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.019 |  |
| 2025-12-23 11:04:58 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 11:04:52 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.040 |  |
| 2025-12-23 11:04:39 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 11:04:36 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:04:31 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:04:02 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.013 |  |
| 2025-12-23 11:03:58 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.082 |  |
| 2025-12-23 11:03:47 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2025-12-23 11:03:43 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2025-12-23 11:03:39 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:03:32 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:03:22 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:03:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:03:03 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:03:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:03:00 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-23 11:02:46 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:02:39 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:02:34 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-23 11:02:07 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:02:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.078 |  |
| 2025-12-23 11:01:53 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:01:43 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:01:30 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.129 |  |
| 2025-12-23 11:01:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.057 |  |
| 2025-12-23 11:00:30 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:00:29 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:00:27 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2025-12-23 10:29:03 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 11:03:47 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2025-12-23 11:03:00 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-23 11:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-23 11:04:39 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 11:04:58 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 11:00:30 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:04:36 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:15:46 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:03:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:03:22 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:01:53 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:09:00 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:12:36 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:02:34 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:02:46 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:02:07 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:03:32 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:01:43 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:04:31 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:05:35 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:03:03 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:05:11 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 11:05:17 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:03:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:03:39 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:02:39 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:00:29 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-23 11:04:02 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.013 |  |
| 2025-12-23 11:05:08 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.019 |  |
| 2025-12-23 11:00:27 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2025-12-23 11:03:43 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2025-12-23 10:01:25 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.031 |  |
| 2025-12-23 11:04:52 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.040 |  |
| 2025-12-23 11:01:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.057 |  |
| 2025-12-23 11:02:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.078 |  |
| 2025-12-23 11:03:58 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.082 |  |
| 2025-12-23 11:01:30 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)