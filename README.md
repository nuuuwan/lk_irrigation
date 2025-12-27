# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_08:34:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,107 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 08:34:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:26:25 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-27 08:16:59 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:14:05 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:11:56 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:10:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.060 |  |
| 2025-12-27 08:08:55 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:08:22 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.018 |  |
| 2025-12-27 08:08:19 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.018 |  |
| 2025-12-27 08:07:51 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.011 |  |
| 2025-12-27 08:07:16 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:06:52 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:06:30 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:05:29 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.058 |  |
| 2025-12-27 08:05:15 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:05:07 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:04:47 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:04:47 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.042 |  |
| 2025-12-27 08:04:39 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.087 |  |
| 2025-12-27 08:04:28 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 08:04:14 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.021 |  |
| 2025-12-27 08:03:47 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:03:20 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-27 08:03:01 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:03:00 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 08:02:46 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:02:33 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2025-12-27 08:02:17 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:01:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 08:01:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.013 |  |
| 2025-12-27 08:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:01:17 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:43 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:00:41 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:31 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:10 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:07 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 08:03:20 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-27 08:26:25 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-27 08:03:00 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-27 08:01:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 08:04:28 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 06:07:12 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.004 |  |
| 2025-12-27 08:00:07 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:16:59 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:07:16 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:02:46 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:10 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:01:17 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:41 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:34:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:05:15 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:05:07 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:03:47 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:00:31 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:14:05 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:08:55 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:03:01 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 07:18:30 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2025-12-27 08:06:30 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:02:17 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:00:43 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:04:47 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:11:56 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-27 07:02:15 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-27 08:07:51 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.011 |  |
| 2025-12-27 08:01:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.013 |  |
| 2025-12-27 08:08:22 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.018 |  |
| 2025-12-27 08:08:19 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.018 |  |
| 2025-12-27 08:04:14 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.021 |  |
| 2025-12-27 08:02:33 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2025-12-27 08:04:47 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.042 |  |
| 2025-12-27 08:05:29 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.058 |  |
| 2025-12-27 08:10:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.060 |  |
| 2025-12-27 08:04:39 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)