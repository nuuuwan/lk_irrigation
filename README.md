# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_08:36:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,818 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 08:36:54 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.051 |  |
| 2025-12-11 08:14:39 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.012 |  |
| 2025-12-11 08:11:29 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.012 |  |
| 2025-12-11 08:10:55 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.038 |  |
| 2025-12-11 08:09:54 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:08:54 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.037 |  |
| 2025-12-11 08:08:04 | Weraganthota (Mahaweli Ganga) | -1.06 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-11 08:07:32 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:06:41 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2025-12-11 08:06:14 | Horowpothana (Yan Oya) | 4.65 | 🟢 Normal | -0.020 |  |
| 2025-12-11 08:06:00 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:05:48 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 08:05:18 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2025-12-11 08:05:05 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-11 08:05:04 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:05:04 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.050 |  |
| 2025-12-11 08:04:42 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:04:39 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.029 |  |
| 2025-12-11 08:04:08 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:04:05 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:03:51 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.049 |  |
| 2025-12-11 08:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.097 |  |
| 2025-12-11 08:03:20 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:03:19 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:03:17 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:03:11 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-11 08:02:55 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-11 08:02:47 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 08:02:37 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:02:34 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.061 |  |
| 2025-12-11 08:02:22 | Thanthirimale (Malwathu Oya) | 4.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-11 08:02:11 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:01:58 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-11 08:01:49 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:01:48 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:01:38 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.040 |  |
| 2025-12-11 08:01:35 | Yaka Wewa (Ma Oya) | 1.42 | 🟢 Normal | -0.021 |  |
| 2025-12-11 08:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 08:08:04 | Weraganthota (Mahaweli Ganga) | -1.06 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-11 08:02:22 | Thanthirimale (Malwathu Oya) | 4.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-11 08:02:47 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 08:05:48 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 08:02:11 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:03:17 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:01:49 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:03:19 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:03:20 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:04:08 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:02:37 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:06:00 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:04:05 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:05:04 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:09:54 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:04:42 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:07:32 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:01:48 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 08:03:11 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-11 08:02:55 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-11 08:01:58 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-11 08:11:29 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.012 |  |
| 2025-12-11 08:14:39 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.012 |  |
| 2025-12-11 08:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.017 |  |
| 2025-12-11 08:06:41 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2025-12-11 08:05:05 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2025-12-11 08:06:14 | Horowpothana (Yan Oya) | 4.65 | 🟢 Normal | -0.020 |  |
| 2025-12-11 08:05:18 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2025-12-11 08:01:35 | Yaka Wewa (Ma Oya) | 1.42 | 🟢 Normal | -0.021 |  |
| 2025-12-11 08:04:39 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.029 |  |
| 2025-12-11 08:08:54 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.037 |  |
| 2025-12-11 08:10:55 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.038 |  |
| 2025-12-11 08:01:38 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.040 |  |
| 2025-12-11 08:03:51 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.049 |  |
| 2025-12-11 08:05:04 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.050 |  |
| 2025-12-11 08:36:54 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.051 |  |
| 2025-12-11 08:02:34 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.061 |  |
| 2025-12-11 08:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)