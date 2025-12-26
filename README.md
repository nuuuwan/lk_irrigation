# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_06:38:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,136 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 06:38:08 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:36:29 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.002 |  |
| 2025-12-26 06:20:28 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.017 |  |
| 2025-12-26 06:16:28 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:16:27 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:16:25 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:14:03 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-26 06:13:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.027 |  |
| 2025-12-26 06:09:19 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-26 06:08:45 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:08:38 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-26 06:08:26 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:08:22 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2025-12-26 06:08:12 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.009 |  |
| 2025-12-26 06:07:51 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-26 06:07:25 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2025-12-26 06:06:09 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:05:59 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 06:05:38 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-26 06:05:28 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-26 06:05:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-26 06:04:41 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-26 06:04:32 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-26 06:03:49 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2025-12-26 06:03:48 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:03:26 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-26 06:03:08 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:02:59 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:02:55 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.054 |  |
| 2025-12-26 06:02:50 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:02:44 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-26 06:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 06:02:42 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.065 |  |
| 2025-12-26 06:02:29 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.098 |  |
| 2025-12-26 06:01:48 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:01:46 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.024 |  |
| 2025-12-26 06:01:07 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.030 |  |
| 2025-12-26 06:00:51 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:00:35 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.254 |  |
| 2025-12-26 06:00:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-26 05:51:50 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.054 |  |
| 2025-12-26 05:47:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | 0.137 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 06:05:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-26 06:00:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-26 06:14:03 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-26 06:05:28 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-26 06:09:19 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-26 06:02:44 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-26 06:03:26 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-26 06:05:59 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 06:04:41 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-26 06:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 06:08:38 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-26 06:00:51 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:03:48 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:03:08 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:16:28 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:10 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:38:08 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:02:59 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:06:09 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:08:45 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:01:48 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:08:26 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-26 06:36:29 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.002 |  |
| 2025-12-26 06:07:25 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2025-12-26 06:08:12 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.009 |  |
| 2025-12-26 06:07:51 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-26 06:04:32 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-26 06:20:28 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.017 |  |
| 2025-12-26 06:03:49 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2025-12-26 06:05:38 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-26 06:01:46 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.024 |  |
| 2025-12-26 06:13:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.027 |  |
| 2025-12-26 06:08:22 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2025-12-26 06:01:07 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.030 |  |
| 2025-12-26 06:02:55 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.054 |  |
| 2025-12-26 06:02:42 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.065 |  |
| 2025-12-26 06:02:29 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.098 |  |
| 2025-12-26 06:00:35 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.254 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)