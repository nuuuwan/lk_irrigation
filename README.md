# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_15:08:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,084 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 15:08:17 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:08:02 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-11 15:07:31 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:07:02 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:06:20 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-11 15:06:12 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:05:47 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:05:46 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-11 15:05:44 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:05:30 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-11 15:05:11 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-11 15:05:06 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:04:50 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:04:23 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 15:03:55 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.030 |  |
| 2025-12-11 15:03:44 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.010 |  |
| 2025-12-11 15:03:42 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-11 15:03:39 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 15:03:26 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-11 15:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-11 15:03:21 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-11 15:03:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 15:03:13 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2025-12-11 15:03:09 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.031 |  |
| 2025-12-11 15:03:02 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2025-12-11 15:02:59 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.060 |  |
| 2025-12-11 15:02:06 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 15:01:36 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:01:15 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 15:01:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-11 15:01:09 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 15:00:15 | Horowpothana (Yan Oya) | 4.50 | 🟢 Normal | -0.032 |  |
| 2025-12-11 14:26:42 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 14:18:30 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-11 14:12:12 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | -0.031 |  |
| 2025-12-11 14:10:30 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 15:06:20 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-11 15:05:30 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-11 15:01:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-11 15:03:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 15:05:46 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-11 15:03:42 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-11 15:03:26 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-11 15:04:23 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 15:08:02 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-11 15:02:06 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 15:01:09 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 15:03:39 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 15:02:59 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 15:08:17 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:04:50 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:06:12 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:10:30 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:06:20 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:05:44 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:05:06 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:05:47 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:07:31 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:07:02 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:01:36 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-11 15:03:44 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.010 |  |
| 2025-12-11 15:01:15 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:06:15 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-11 15:05:11 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-11 15:03:02 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2025-12-11 15:03:21 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-11 14:01:23 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2025-12-11 15:03:13 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2025-12-11 15:03:55 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.030 |  |
| 2025-12-11 14:12:12 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | -0.031 |  |
| 2025-12-11 15:03:09 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.031 |  |
| 2025-12-11 15:00:15 | Horowpothana (Yan Oya) | 4.50 | 🟢 Normal | -0.032 |  |
| 2025-12-11 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)