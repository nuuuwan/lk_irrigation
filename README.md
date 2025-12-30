# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_23:17:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,323 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 23:17:33 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.008 |  |
| 2025-12-30 23:11:01 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-30 23:06:45 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:06:32 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2025-12-30 23:06:11 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:05:48 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:04:11 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-30 23:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:03:40 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:03:23 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-30 23:03:22 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-30 23:03:19 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-30 23:03:18 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2025-12-30 23:02:52 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-30 23:02:44 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2025-12-30 23:02:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:29 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:13 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:12 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:08 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 23:01:41 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-30 23:00:51 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-30 23:00:51 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:00:16 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:29:31 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:27:41 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.017 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 23:03:23 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-30 23:02:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-30 22:07:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-30 23:03:19 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-30 23:04:11 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-30 22:06:13 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-30 23:11:01 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-30 23:03:22 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-30 18:04:13 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-30 18:03:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 23:02:08 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 23:02:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:00:51 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:52 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:03:40 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:12 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:06:17 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:02 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:03:30 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:04:05 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:39 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:00:16 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:29:31 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:29 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:05:48 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:06:45 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:06:11 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-30 18:01:08 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:00:38 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:02:13 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:17:33 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.008 |  |
| 2025-12-30 23:06:32 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2025-12-30 23:01:41 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-30 23:00:51 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-30 23:03:18 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2025-12-30 22:02:33 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2025-12-30 23:02:44 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2025-12-30 20:16:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)