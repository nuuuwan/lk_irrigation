# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_01:47:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,063 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 01:47:04 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:39:01 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.007 |  |
| 2025-12-25 01:33:28 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-25 01:25:29 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:10:10 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2025-12-25 01:08:39 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:08:11 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.038 |  |
| 2025-12-25 01:07:51 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:07:39 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-25 01:06:22 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-25 01:06:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 01:05:15 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:05:13 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:05:10 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 01:04:07 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:04:06 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:04:04 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-25 01:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:03:07 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 01:02:51 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-25 01:02:33 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -8.000 |  |
| 2025-12-25 01:02:25 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-25 01:02:13 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.059 |  |
| 2025-12-25 01:02:08 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:02:06 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -8.000 |  |
| 2025-12-25 01:02:04 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:01:58 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-25 01:01:41 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.995 |  |
| 2025-12-25 01:01:35 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 01:01:24 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:01:09 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2025-12-25 01:01:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:00:39 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2025-12-25 00:59:46 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 00:16:54 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 21.600 | 🔺 Rising |
| 2025-12-25 01:06:22 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-25 01:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-25 01:07:39 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-25 01:01:58 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-25 01:01:35 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 01:03:07 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 01:05:10 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 01:02:51 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-25 01:06:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 01:33:28 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-25 01:25:29 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:02:08 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:04:07 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:01:24 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:05:15 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:01:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:09:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:02:04 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:08:39 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:05:13 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:47:04 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:41:43 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:59:46 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:07:51 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:39:01 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.007 |  |
| 2025-12-25 01:02:25 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-25 01:01:09 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2025-12-25 01:10:10 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 00:02:09 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2025-12-25 01:08:11 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.038 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-25 01:00:39 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2025-12-25 01:02:13 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.059 |  |
| 2025-12-25 01:01:41 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.995 |  |
| 2025-12-25 01:02:33 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -8.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)