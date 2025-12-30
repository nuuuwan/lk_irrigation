# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_06:35:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 06:35:18 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-30 06:31:37 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.027 |  |
| 2025-12-30 06:16:27 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.008 |  |
| 2025-12-30 06:12:57 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:10:06 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.018 |  |
| 2025-12-30 06:09:50 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:09:24 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.027 |  |
| 2025-12-30 06:09:23 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2025-12-30 06:08:42 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.252 |  |
| 2025-12-30 06:08:36 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.029 |  |
| 2025-12-30 06:08:11 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.018 |  |
| 2025-12-30 06:08:07 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:08:07 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:07:40 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-30 06:07:04 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-30 06:06:52 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.009 |  |
| 2025-12-30 06:06:48 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-30 06:06:02 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.720 | 🔺 Rising |
| 2025-12-30 06:05:59 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:05:55 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:05:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.720 | 🔺 Rising |
| 2025-12-30 06:05:12 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-30 06:04:57 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.006 |  |
| 2025-12-30 06:04:54 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:04:53 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:04:28 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-30 06:03:32 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:03:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.085 |  |
| 2025-12-30 06:03:02 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-30 06:02:48 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:02:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-30 06:02:14 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:02:03 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:01:53 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:01:30 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:01:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:01:20 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-30 06:00:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 06:06:02 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.720 | 🔺 Rising |
| 2025-12-30 06:03:02 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-30 06:07:04 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-30 06:05:12 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-30 06:06:48 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-30 06:07:40 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-30 06:35:18 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-30 06:01:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:03:32 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:04:28 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:02:14 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:02:03 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:21:22 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:01:30 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:02:48 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:08:07 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 02:02:12 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:08:07 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:12:57 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:05:59 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:04:54 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:05:55 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:01:53 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:09:50 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 06:04:57 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.006 |  |
| 2025-12-30 06:16:27 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.008 |  |
| 2025-12-30 06:06:52 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.009 |  |
| 2025-12-30 06:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-30 06:01:20 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-30 06:10:06 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.018 |  |
| 2025-12-30 06:08:11 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.018 |  |
| 2025-12-30 06:09:23 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2025-12-30 06:31:37 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.027 |  |
| 2025-12-30 06:08:36 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.029 |  |
| 2025-12-30 06:02:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2025-12-30 06:00:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.066 |  |
| 2025-12-30 06:03:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.085 |  |
| 2025-12-30 06:08:42 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.252 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)