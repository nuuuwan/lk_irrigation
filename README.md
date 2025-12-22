# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_09:12:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 09:12:01 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2025-12-22 09:11:56 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:10:51 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.017 |  |
| 2025-12-22 09:10:07 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2025-12-22 09:09:35 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:08:11 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:07:33 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:07:12 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:06:25 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 09:05:57 | Thanthirimale (Malwathu Oya) | 4.80 | 🟢 Normal | -0.028 |  |
| 2025-12-22 09:04:29 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-22 09:04:27 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.029 |  |
| 2025-12-22 09:04:22 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2025-12-22 09:03:54 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.091 |  |
| 2025-12-22 09:03:47 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.069 |  |
| 2025-12-22 09:03:22 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:03:13 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.091 |  |
| 2025-12-22 09:03:09 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-22 09:03:08 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.006 |  |
| 2025-12-22 09:03:01 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.045 |  |
| 2025-12-22 09:03:01 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-22 09:02:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-22 09:02:49 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-22 09:02:38 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-22 09:02:33 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-22 09:02:26 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:02:24 | Horowpothana (Yan Oya) | 3.75 | 🟢 Normal | -0.059 |  |
| 2025-12-22 09:02:24 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2025-12-22 09:02:19 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:02:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:01:47 | Manampitiya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.049 |  |
| 2025-12-22 09:01:38 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:01:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 09:01:23 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:01:21 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2025-12-22 09:01:19 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:00:43 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 09:03:01 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-22 09:01:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 09:06:25 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 09:02:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:01:19 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:00:43 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:01:23 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:11:56 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:08:11 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:07:12 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:03:22 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:01:38 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:02:19 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:07:33 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:02:26 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:09:35 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:03:47 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 09:03:08 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.006 |  |
| 2025-12-22 09:04:29 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.009 |  |
| 2025-12-22 09:02:33 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-22 09:02:49 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-22 09:03:09 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-22 09:02:38 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-22 09:10:51 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.017 |  |
| 2025-12-22 09:10:07 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2025-12-22 09:04:22 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2025-12-22 09:01:21 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2025-12-22 09:02:24 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2025-12-22 09:12:01 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2025-12-22 09:05:57 | Thanthirimale (Malwathu Oya) | 4.80 | 🟢 Normal | -0.028 |  |
| 2025-12-22 09:04:27 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.029 |  |
| 2025-12-22 09:02:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2025-12-22 09:03:01 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.045 |  |
| 2025-12-22 09:01:47 | Manampitiya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.049 |  |
| 2025-12-22 09:02:24 | Horowpothana (Yan Oya) | 3.75 | 🟢 Normal | -0.059 |  |
| 2025-12-22 09:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.069 |  |
| 2025-12-22 09:03:13 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.091 |  |
| 2025-12-22 09:03:54 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)