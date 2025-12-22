# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_10:27:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,716 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 10:27:34 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:23:43 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:16:44 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:14:57 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.067 |  |
| 2025-12-22 10:12:47 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:11:00 | Padiyathalawa (Maduru Oya) | 1.26 | 🟢 Normal | -0.018 |  |
| 2025-12-22 10:07:56 | Manampitiya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.045 |  |
| 2025-12-22 10:07:08 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2025-12-22 10:06:48 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:06:46 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-22 10:06:40 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:06:37 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2025-12-22 10:06:15 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2025-12-22 10:05:51 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.009 |  |
| 2025-12-22 10:05:49 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-22 10:05:13 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-22 10:05:07 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:05:03 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.078 |  |
| 2025-12-22 10:04:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2025-12-22 10:04:36 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:04:02 | Weraganthota (Mahaweli Ganga) | -1.11 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-22 10:03:35 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.156 |  |
| 2025-12-22 10:03:34 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-22 10:03:29 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:03:09 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:02:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:02:44 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2025-12-22 10:02:32 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-22 10:02:26 | Thanthirimale (Malwathu Oya) | 4.78 | 🟢 Normal | -0.021 |  |
| 2025-12-22 10:02:26 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-22 10:02:17 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:01:27 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-22 10:01:17 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-22 10:01:11 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:00:47 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.010 |  |
| 2025-12-22 10:00:33 | Horowpothana (Yan Oya) | 3.70 | 🟢 Normal | -0.052 |  |
| 2025-12-22 10:00:28 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 10:04:02 | Weraganthota (Mahaweli Ganga) | -1.11 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-22 10:06:46 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-22 10:02:26 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-22 10:05:13 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-22 10:02:17 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:00:28 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:06:48 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:03:09 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:08:11 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:12:47 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:04:36 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:02:32 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:02:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:01:11 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:16:44 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:05:07 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:06:40 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:27:34 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 10:03:29 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:03:08 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.006 |  |
| 2025-12-22 10:05:51 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.009 |  |
| 2025-12-22 10:05:49 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-22 10:01:17 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-22 10:00:47 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.010 |  |
| 2025-12-22 10:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-22 10:03:34 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-22 10:11:00 | Padiyathalawa (Maduru Oya) | 1.26 | 🟢 Normal | -0.018 |  |
| 2025-12-22 10:06:37 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2025-12-22 10:06:15 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2025-12-22 10:07:08 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2025-12-22 10:01:27 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2025-12-22 10:02:26 | Thanthirimale (Malwathu Oya) | 4.78 | 🟢 Normal | -0.021 |  |
| 2025-12-22 10:04:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2025-12-22 10:02:44 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2025-12-22 10:07:56 | Manampitiya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.045 |  |
| 2025-12-22 10:00:33 | Horowpothana (Yan Oya) | 3.70 | 🟢 Normal | -0.052 |  |
| 2025-12-22 10:14:57 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.067 |  |
| 2025-12-22 10:05:03 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.078 |  |
| 2025-12-22 10:03:35 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)