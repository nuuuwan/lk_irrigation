# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_06:11:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,498 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 06:11:53 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.026 |  |
| 2026-01-20 06:10:48 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:06:42 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.180 |  |
| 2026-01-20 06:06:11 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-01-20 06:05:48 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:05:19 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:05:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.088 |  |
| 2026-01-20 06:05:18 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:05:09 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:04:53 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.065 |  |
| 2026-01-20 06:04:38 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-01-20 06:04:34 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:04:32 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:04:32 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:04:13 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-20 06:04:00 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-01-20 06:03:50 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:03:45 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-20 06:03:38 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:03:02 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-20 06:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-01-20 06:02:53 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.074 |  |
| 2026-01-20 06:02:52 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:02:51 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:02:08 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 06:02:07 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:01:55 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:01:39 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-20 06:01:38 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-20 06:01:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-20 06:01:36 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-20 06:01:35 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:01:34 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-20 06:01:28 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:01:17 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-20 06:00:27 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:00:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 06:00:11 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:00:11 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-20 05:56:35 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:28:46 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:20:43 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:19:34 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:18:06 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 06:01:39 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-20 06:02:08 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 06:03:02 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-20 06:03:45 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-20 06:01:17 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-20 06:04:32 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:04:34 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:01:35 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:01:28 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:02:51 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:00:11 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:00:27 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:05:19 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:03:50 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:03:38 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:02:52 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:05:18 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:01:55 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:05:09 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:05:48 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:10:48 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:04:32 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-19 18:02:06 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:28:46 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:02:07 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 06:04:00 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-01-19 18:01:58 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-20 06:04:13 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-20 06:00:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 06:00:11 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-20 06:04:38 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-01-20 06:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-01-20 06:11:53 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.026 |  |
| 2026-01-20 06:06:11 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-01-20 06:04:53 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.065 |  |
| 2026-01-20 06:02:53 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.074 |  |
| 2026-01-20 06:05:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.088 |  |
| 2026-01-20 06:06:42 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)