# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_08:06:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,399 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 08:06:35 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:06:02 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | -108.000 |  |
| 2025-12-15 08:06:01 | Galgamuwa (Mee Oya) | 1.59 | 🟢 Normal | -108.000 |  |
| 2025-12-15 08:05:55 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2025-12-15 08:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.070 |  |
| 2025-12-15 08:05:24 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.084 |  |
| 2025-12-15 08:05:17 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.041 |  |
| 2025-12-15 08:05:15 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:05:02 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2025-12-15 08:05:01 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 08:04:53 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:04:27 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-15 08:04:02 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 08:03:49 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.052 |  |
| 2025-12-15 08:03:21 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-15 08:03:11 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-15 08:03:09 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | -0.016 |  |
| 2025-12-15 08:02:51 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:48 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:40 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:39 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:25 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:23 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:20 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:16 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:10 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:01 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:01:48 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2025-12-15 08:01:31 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-15 08:01:09 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-15 08:01:08 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.023 |  |
| 2025-12-15 08:01:05 | Horowpothana (Yan Oya) | 4.10 | 🟢 Normal | -0.020 |  |
| 2025-12-15 08:00:40 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2025-12-15 08:00:21 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:39:16 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:22:35 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.038 |  |
| 2025-12-15 07:19:31 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.045 |  |
| 2025-12-15 07:09:51 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 07:09:44 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.023 |  |
| 2025-12-15 07:08:17 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | -0.084 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 06:10:00 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2025-12-15 08:04:27 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-15 08:01:09 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-15 08:03:21 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-15 08:03:11 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-15 08:01:31 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-15 08:04:02 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 08:02:25 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:16 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:00:21 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:01 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:40 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:39 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:23 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:51 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:20 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:05:15 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:06:35 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:04:53 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:10 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:02:48 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 08:05:55 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2025-12-15 08:05:01 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 08:03:09 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | -0.016 |  |
| 2025-12-15 07:03:48 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-15 08:00:40 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2025-12-15 08:01:05 | Horowpothana (Yan Oya) | 4.10 | 🟢 Normal | -0.020 |  |
| 2025-12-15 07:05:47 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2025-12-15 08:05:02 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2025-12-15 08:01:48 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2025-12-15 08:01:08 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.023 |  |
| 2025-12-15 07:02:31 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.035 |  |
| 2025-12-15 07:22:35 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.038 |  |
| 2025-12-15 08:05:17 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.041 |  |
| 2025-12-15 07:19:31 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.045 |  |
| 2025-12-15 08:03:49 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.052 |  |
| 2025-12-15 08:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.070 |  |
| 2025-12-15 08:05:24 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.084 |  |
| 2025-12-15 08:06:02 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)