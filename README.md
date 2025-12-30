# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_22:07:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,295 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 22:07:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-30 22:06:55 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-30 22:06:39 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-30 22:06:32 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 22:06:27 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:06:17 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:06:13 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-30 22:05:12 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:50 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:32 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:10 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:00 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2025-12-30 22:04:00 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2025-12-30 22:03:40 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:03:35 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2025-12-30 22:02:53 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:02:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:02:33 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2025-12-30 22:02:28 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:02:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-30 22:01:39 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:39 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:08 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-30 22:01:02 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:00:54 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.032 |  |
| 2025-12-30 22:00:47 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:00:47 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:00:38 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:00:34 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:19:33 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-30 21:18:39 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 22:04:00 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2025-12-30 22:06:39 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-30 22:07:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-30 22:02:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-30 21:03:41 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-30 22:06:13 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-30 18:04:13 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-30 18:03:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 22:06:32 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 22:02:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:00:47 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:50 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:12 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:39 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:06:17 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:02 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:03:30 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:02:28 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:01:07 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:10 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:04:05 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:39 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:00:47 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 21:06:23 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:06:27 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:04:32 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:03:40 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:05:12 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 18:01:08 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:00:38 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:02:53 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:06:55 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-30 22:01:08 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-30 22:02:33 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2025-12-30 22:03:35 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2025-12-30 22:04:00 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2025-12-30 20:16:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.029 |  |
| 2025-12-30 22:00:54 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.032 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)