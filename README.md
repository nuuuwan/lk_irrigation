# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_23:12:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,165 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 23:12:48 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-13 23:10:04 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-13 23:07:36 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-13 23:06:51 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:06:47 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 23:06:05 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2025-12-13 23:05:51 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-13 23:05:48 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2025-12-13 23:05:02 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2025-12-13 23:04:57 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2025-12-13 23:04:46 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-13 23:04:22 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-13 23:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:55 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2025-12-13 23:03:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:48 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:46 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:45 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:09 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:08 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:04 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-13 23:03:03 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:02:54 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:02:48 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-13 23:02:22 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2025-12-13 23:02:18 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:01:53 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:01:45 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:01:24 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.020 |  |
| 2025-12-13 23:01:19 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:01:07 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:00:56 | Horowpothana (Yan Oya) | 5.34 | 🟢 Normal | -0.050 |  |
| 2025-12-13 23:00:26 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-13 22:34:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2025-12-13 22:19:41 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.080 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 23:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2025-12-13 23:05:51 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-13 23:00:26 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-13 23:04:46 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-13 23:10:04 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-13 22:16:05 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 23:06:47 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 23:12:48 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-13 23:02:48 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-13 23:07:36 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-13 23:03:09 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:08 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:03 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:01:53 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:04:13 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:01:19 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:45 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:01:07 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:48 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:02:18 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:05:48 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:01:45 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:02:54 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:03:46 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:06:51 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 23:04:57 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2025-12-13 23:05:02 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2025-12-13 23:04:22 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-13 23:03:04 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-13 22:03:11 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-13 23:01:24 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.020 |  |
| 2025-12-13 23:02:22 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2025-12-13 23:03:55 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2025-12-13 23:06:05 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-13 23:00:56 | Horowpothana (Yan Oya) | 5.34 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)