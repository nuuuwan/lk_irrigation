# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_09:26:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 09:26:43 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-18 09:12:16 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:11:23 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:10:37 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2025-12-18 09:09:49 | Padiyathalawa (Maduru Oya) | 3.20 | 🟢 Normal | -0.387 |  |
| 2025-12-18 09:09:21 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-18 09:09:18 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-18 09:07:45 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 09:07:11 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:07:05 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 09:07:03 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:07:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:06:53 | Thanthirimale (Malwathu Oya) | 4.48 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-18 09:06:00 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:05:20 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:05:18 | Thaldena (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.058 |  |
| 2025-12-18 09:05:11 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:04:28 | Horowpothana (Yan Oya) | 5.45 | 🟢 Normal | -0.019 |  |
| 2025-12-18 09:04:25 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.031 |  |
| 2025-12-18 09:04:23 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:04:16 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-18 09:04:10 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-18 09:04:00 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-18 09:03:55 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:03:17 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 09:03:16 | Manampitiya (Mahaweli Ganga) | 3.63 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2025-12-18 09:02:56 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 09:02:49 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2025-12-18 09:02:35 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2025-12-18 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.050 |  |
| 2025-12-18 09:02:13 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.040 |  |
| 2025-12-18 09:02:12 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 09:01:35 | Yaka Wewa (Ma Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:01:33 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.053 |  |
| 2025-12-18 09:01:11 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:00:55 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-18 09:00:09 | Nakkala (Kumbukkan Oya) | 2.76 | 🟢 Normal | -0.083 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 09:03:16 | Manampitiya (Mahaweli Ganga) | 3.63 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2025-12-18 09:02:49 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2025-12-18 09:06:53 | Thanthirimale (Malwathu Oya) | 4.48 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-18 09:04:00 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-18 09:09:21 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-18 09:26:43 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-18 08:08:08 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-18 09:03:17 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 09:02:12 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 09:02:56 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 09:07:05 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 09:07:45 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 09:01:35 | Yaka Wewa (Ma Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:05:11 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:07:11 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:05:20 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:03:55 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:12:16 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:07:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:07:03 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:06:00 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:11:23 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:04:23 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:01:11 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 09:10:37 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2025-12-18 09:04:10 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-18 09:09:18 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-18 09:00:55 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-18 09:04:28 | Horowpothana (Yan Oya) | 5.45 | 🟢 Normal | -0.019 |  |
| 2025-12-18 09:04:16 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-18 09:04:25 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.031 |  |
| 2025-12-18 09:02:35 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2025-12-18 09:02:13 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.040 |  |
| 2025-12-18 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.050 |  |
| 2025-12-18 09:01:33 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.053 |  |
| 2025-12-18 09:05:18 | Thaldena (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.058 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 09:00:09 | Nakkala (Kumbukkan Oya) | 2.76 | 🟢 Normal | -0.083 |  |
| 2025-12-18 09:09:49 | Padiyathalawa (Maduru Oya) | 3.20 | 🟢 Normal | -0.387 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)