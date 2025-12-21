# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_04:05:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,469 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 04:05:19 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-22 04:04:41 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:04:40 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 04:04:31 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:04:24 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:03:50 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.040 |  |
| 2025-12-22 04:03:45 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:03:43 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.006 |  |
| 2025-12-22 04:03:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:03:03 | Horowpothana (Yan Oya) | 4.10 | 🟢 Normal | -0.082 |  |
| 2025-12-22 04:02:29 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2025-12-22 04:02:26 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | -0.013 |  |
| 2025-12-22 04:02:14 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:02:13 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.030 |  |
| 2025-12-22 04:01:45 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:01:28 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:01:21 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:01:07 | Manampitiya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.042 |  |
| 2025-12-22 04:00:59 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:00:23 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2025-12-22 03:35:16 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-22 03:16:55 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.016 |  |
| 2025-12-22 03:16:41 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.024 |  |
| 2025-12-22 03:16:40 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:16:07 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.013 |  |
| 2025-12-22 03:11:18 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:09:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.046 |  |
| 2025-12-22 03:08:17 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-22 03:35:16 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-22 04:04:40 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 04:01:21 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:00:50 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:58 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:01:45 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:11:18 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:08:17 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:01:28 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:03:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:14 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:08:21 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:05:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:03:43 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.006 |  |
| 2025-12-22 04:04:41 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:04:24 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:03:45 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:04:31 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:00:59 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:02:14 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-22 04:02:26 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | -0.013 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-22 03:16:55 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.016 |  |
| 2025-12-22 04:05:19 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-22 03:16:41 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.024 |  |
| 2025-12-22 04:02:13 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.030 |  |
| 2025-12-22 04:02:29 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2025-12-22 03:05:54 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.035 |  |
| 2025-12-22 04:03:50 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.040 |  |
| 2025-12-22 03:01:59 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2025-12-22 04:01:07 | Manampitiya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.042 |  |
| 2025-12-22 03:09:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.046 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-22 02:04:26 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2025-12-22 04:00:23 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2025-12-22 03:02:58 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.061 |  |
| 2025-12-22 04:03:03 | Horowpothana (Yan Oya) | 4.10 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)