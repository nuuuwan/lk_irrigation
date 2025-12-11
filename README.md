# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_03:26:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,506 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 03:26:49 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:26:47 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:15:18 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:13:31 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.008 |  |
| 2025-12-12 03:11:04 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:09:17 | Panadugama (Nilwala Ganga) | 4.11 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-12 03:08:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2025-12-12 03:08:13 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-12 03:08:12 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | -0.022 |  |
| 2025-12-12 03:07:57 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2025-12-12 03:07:33 | Magura (Kalu Ganga) | 2.94 | 🟢 Normal | -0.074 |  |
| 2025-12-12 03:07:26 | Rathnapura (Kalu Ganga) | 4.12 | 🟢 Normal | 0.706 | 🔺 Rising |
| 2025-12-12 03:07:25 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | -40.000 |  |
| 2025-12-12 03:07:21 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-12 03:07:07 | Padiyathalawa (Maduru Oya) | 2.70 | 🟢 Normal | -40.000 |  |
| 2025-12-12 03:07:05 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -40.000 |  |
| 2025-12-12 03:06:35 | Rathnapura (Kalu Ganga) | 4.11 | 🟢 Normal | 0.706 | 🔺 Rising |
| 2025-12-12 03:06:10 | Rathnapura (Kalu Ganga) | 4.03 | 🟢 Normal | 0.706 | 🔺 Rising |
| 2025-12-12 03:06:07 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:05:57 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2025-12-12 03:05:54 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.038 |  |
| 2025-12-12 03:05:47 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2025-12-12 03:05:30 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2025-12-12 03:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:03:35 | Nakkala (Kumbukkan Oya) | 1.68 | 🟢 Normal | -0.082 |  |
| 2025-12-12 03:03:33 | Horowpothana (Yan Oya) | 4.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-12 03:03:33 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2025-12-12 03:03:29 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2025-12-12 03:03:26 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-12 03:03:21 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:03:16 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.125 |  |
| 2025-12-12 03:02:28 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | -0.083 |  |
| 2025-12-12 03:02:26 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.065 |  |
| 2025-12-12 03:02:26 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:02:23 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-12 03:02:21 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.049 |  |
| 2025-12-12 03:01:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 03:01:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-12 03:01:10 | Moragaswewa (Deduru Oya) | 1.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 03:08:33 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2025-12-12 03:07:26 | Rathnapura (Kalu Ganga) | 4.12 | 🟢 Normal | 0.706 | 🔺 Rising |
| 2025-12-12 03:03:29 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-12 03:03:33 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2025-12-12 03:09:17 | Panadugama (Nilwala Ganga) | 4.11 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-12 03:08:13 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-12 03:02:23 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-12 03:03:26 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-12 03:03:33 | Horowpothana (Yan Oya) | 4.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-12 01:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 03:01:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 03:07:21 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 03:01:10 | Moragaswewa (Deduru Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:26:49 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:02:26 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:06:07 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:15:18 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:03:21 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:11:04 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-12 03:13:31 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.008 |  |
| 2025-12-12 03:05:30 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2025-12-12 03:05:47 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2025-12-12 03:05:57 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2025-12-12 03:01:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-12 03:08:12 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | -0.022 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-12 03:05:54 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.038 |  |
| 2025-12-12 03:02:21 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.049 |  |
| 2025-12-12 03:02:26 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.065 |  |
| 2025-12-12 03:07:33 | Magura (Kalu Ganga) | 2.94 | 🟢 Normal | -0.074 |  |
| 2025-12-12 03:03:35 | Nakkala (Kumbukkan Oya) | 1.68 | 🟢 Normal | -0.082 |  |
| 2025-12-12 03:02:28 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | -0.083 |  |
| 2025-12-12 03:03:16 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.125 |  |
| 2025-12-12 03:07:25 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | -40.000 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)