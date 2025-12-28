# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_08:17:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 08:17:39 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:09:22 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:09:17 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:08:36 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 08:08:16 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-28 08:08:14 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2025-12-28 08:08:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.053 |  |
| 2025-12-28 08:06:28 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:06:26 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:06:21 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2025-12-28 08:06:01 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:05:52 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-28 08:05:32 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.160 |  |
| 2025-12-28 08:05:30 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:05:29 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:04:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.069 |  |
| 2025-12-28 08:04:33 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-28 08:04:31 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:04:07 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:03:56 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:03:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:03:30 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:03:12 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:03:10 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 08:02:54 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:02:49 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:02:49 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-28 08:02:44 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-28 08:02:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:02:34 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:02:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:01:41 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:01:25 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2025-12-28 08:01:20 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 08:01:04 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2025-12-28 08:01:01 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:00:49 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:00:32 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 08:02:44 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-28 08:04:33 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-28 08:08:16 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-28 08:01:20 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 08:05:52 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-28 08:02:49 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-28 08:03:10 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 08:08:36 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 08:02:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:00:49 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:06:28 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:01:41 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:02:34 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:17:39 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:02:49 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:02:54 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:04:07 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:00:32 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:03:56 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:05:30 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:06:26 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:04:31 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:01:01 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:09:17 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:02:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-28 08:06:01 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:09:22 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:03:30 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:03:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:03:12 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:05:29 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.010 |  |
| 2025-12-28 08:01:25 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2025-12-28 08:01:04 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2025-12-28 08:06:21 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2025-12-28 08:08:14 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2025-12-28 08:08:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.053 |  |
| 2025-12-28 08:04:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.069 |  |
| 2025-12-28 08:05:32 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)