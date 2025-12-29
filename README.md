# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_06:34:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,804 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 06:34:50 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-29 06:33:48 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2025-12-29 06:33:47 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2025-12-29 06:27:39 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:20:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:19:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:18:21 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:16:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:16:22 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:10:19 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -2.323 |  |
| 2025-12-29 06:09:48 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -2.323 |  |
| 2025-12-29 06:09:32 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-29 06:08:59 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.018 |  |
| 2025-12-29 06:08:34 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:07:12 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-29 06:06:23 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:06:12 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-29 06:06:01 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:05:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.064 |  |
| 2025-12-29 06:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.030 |  |
| 2025-12-29 06:05:15 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 06:04:44 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-29 06:04:06 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 06:04:02 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:03:34 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:03:00 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 06:02:57 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:02:47 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-29 06:02:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:02:22 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-29 06:02:14 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:02:10 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2025-12-29 06:02:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 06:01:59 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:01:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:01:54 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.022 |  |
| 2025-12-29 06:01:37 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:01:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:00:45 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.105 |  |
| 2025-12-29 06:00:17 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.021 |  |
| 2025-12-29 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 06:33:48 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2025-12-29 06:07:12 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-29 06:09:32 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-29 06:06:12 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-29 06:04:44 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-29 06:02:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 06:03:00 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 06:05:15 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 06:04:06 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 06:34:50 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-29 06:02:47 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-29 06:02:57 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:08:34 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:01:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:04:02 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:01:37 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:06:01 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:02:14 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:18:21 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:20:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:03:34 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:01:59 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:19:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:02:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:16:22 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:06:23 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:27:39 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:01:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:02:22 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-29 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-29 06:02:10 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2025-12-29 06:08:59 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.018 |  |
| 2025-12-29 06:00:17 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.021 |  |
| 2025-12-29 06:01:54 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.022 |  |
| 2025-12-29 06:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.030 |  |
| 2025-12-29 06:05:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.064 |  |
| 2025-12-29 06:00:45 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.105 |  |
| 2025-12-29 06:10:19 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -2.323 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)