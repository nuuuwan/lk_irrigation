# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_20:28:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 20:28:04 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.378 |  |
| 2025-12-24 20:23:58 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:13:06 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.023 |  |
| 2025-12-24 20:10:32 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-24 20:10:27 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:08:22 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-24 20:06:50 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:06:23 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.118 |  |
| 2025-12-24 20:06:07 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-24 20:06:04 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.028 |  |
| 2025-12-24 20:05:44 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 20:05:31 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-24 20:05:26 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:05:18 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-24 20:05:13 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:04:51 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.040 |  |
| 2025-12-24 20:04:47 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:04:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.087 |  |
| 2025-12-24 20:04:04 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 20:03:39 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:03:24 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.096 |  |
| 2025-12-24 20:03:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 20:03:14 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:02:44 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-24 20:02:42 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.029 |  |
| 2025-12-24 20:02:33 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:02:11 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:02:10 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-24 20:02:01 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-24 20:01:33 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:01:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:01:20 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 20:01:16 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:00:31 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:00:21 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-24 20:00:07 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:46:28 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.023 |  |
| 2025-12-24 19:42:41 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 20:06:07 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-24 20:08:22 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-24 20:10:32 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-24 20:01:20 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 20:04:04 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 20:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 20:02:01 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-24 20:05:44 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 20:00:21 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-24 20:03:39 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:02:33 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:23:58 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:02:11 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:01:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:00:31 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:05:13 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:00:07 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:10:27 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:05:26 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:06:50 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:04:47 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:01:33 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:03:14 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 20:02:44 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-24 20:05:18 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-24 20:02:10 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-24 20:05:31 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-24 20:13:06 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.023 |  |
| 2025-12-24 20:06:04 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.028 |  |
| 2025-12-24 20:02:42 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.029 |  |
| 2025-12-24 20:04:51 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.040 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-24 20:04:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.087 |  |
| 2025-12-24 20:03:24 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.096 |  |
| 2025-12-24 20:06:23 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.118 |  |
| 2025-12-24 20:28:04 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.378 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)