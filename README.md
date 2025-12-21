# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_18:37:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,148 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 18:37:54 | Horowpothana (Yan Oya) | 4.63 | 🟢 Normal | -0.052 |  |
| 2025-12-21 18:28:04 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.023 |  |
| 2025-12-21 18:08:28 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-21 18:06:05 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.037 |  |
| 2025-12-21 18:05:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2025-12-21 18:05:26 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-21 18:05:10 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2025-12-21 18:04:33 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.057 |  |
| 2025-12-21 18:04:32 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | -0.030 |  |
| 2025-12-21 18:04:25 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-21 18:04:16 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:04:11 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2025-12-21 18:03:46 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:44 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:33 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:18 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:10 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2025-12-21 18:02:52 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.030 |  |
| 2025-12-21 18:02:51 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.051 |  |
| 2025-12-21 18:02:47 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.053 |  |
| 2025-12-21 18:02:45 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2025-12-21 18:02:32 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:02:22 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 18:02:17 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.023 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-21 18:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:02:05 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:01:43 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 18:01:35 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 18:01:27 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:01:25 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:01:25 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.092 |  |
| 2025-12-21 18:01:08 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2025-12-21 18:01:07 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2025-12-21 18:00:43 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:00:39 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 17:59:57 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 18:02:45 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2025-12-21 18:04:25 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 18:01:35 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 18:01:43 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 17:59:57 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 18:00:43 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:02:32 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:00:39 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:33 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:10 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:46 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:02:22 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:44 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:04:16 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:01:27 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:18 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:08:28 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:01:25 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:02:05 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:05:26 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-21 18:01:08 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2025-12-21 18:05:10 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2025-12-21 18:04:11 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-21 18:28:04 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.023 |  |
| 2025-12-21 18:02:52 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.030 |  |
| 2025-12-21 18:04:32 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | -0.030 |  |
| 2025-12-21 18:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2025-12-21 18:01:07 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2025-12-21 18:06:05 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.037 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-21 18:02:51 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.051 |  |
| 2025-12-21 18:37:54 | Horowpothana (Yan Oya) | 4.63 | 🟢 Normal | -0.052 |  |
| 2025-12-21 18:02:47 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.053 |  |
| 2025-12-21 18:04:33 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.057 |  |
| 2025-12-21 18:05:35 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.058 |  |
| 2025-12-21 18:01:25 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)