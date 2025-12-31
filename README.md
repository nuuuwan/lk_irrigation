# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_16:06:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,962 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 16:06:48 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:06:24 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:57 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:57 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:06 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:04:30 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:04:17 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:04:01 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:22 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:22 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:03:18 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.038 |  |
| 2025-12-31 16:03:14 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:13 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:08 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.035 |  |
| 2025-12-31 16:02:43 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.108 |  |
| 2025-12-31 16:02:35 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-31 16:02:32 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 16:02:09 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:02:06 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:01:59 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:01:53 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:01:41 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2025-12-31 16:01:36 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 16:00:52 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:51 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.517 |  |
| 2025-12-31 16:00:30 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:00:27 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:25 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:08 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:34:10 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.517 |  |
| 2025-12-31 15:12:05 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 16:02:35 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-31 16:02:32 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 15:05:21 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 15:08:25 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 16:01:59 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:02:06 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:08 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:01:53 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:02:09 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:04:01 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:57 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:45 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:13 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:01:36 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2025-12-31 15:04:06 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:06:24 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:25 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:22 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:06:48 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:57 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:52 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:04:30 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:27 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:03:14 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:06 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:04:17 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:00:30 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:03:22 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-31 15:03:44 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.011 |  |
| 2025-12-31 16:01:41 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2025-12-31 16:03:08 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.035 |  |
| 2025-12-31 16:03:18 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.038 |  |
| 2025-12-31 15:02:00 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.052 |  |
| 2025-12-31 16:02:43 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.108 |  |
| 2025-12-31 16:00:51 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.517 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)