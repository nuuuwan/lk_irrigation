# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_18:08:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,806 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 18:08:32 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.023 |  |
| 2025-12-15 18:08:16 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:06:50 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:06:05 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.040 |  |
| 2025-12-15 18:06:03 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:06:01 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:04:44 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2025-12-15 18:04:32 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:04:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:04:04 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2025-12-15 18:03:42 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:03:42 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:03:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-15 18:03:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:03:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 18:02:41 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.053 |  |
| 2025-12-15 18:02:27 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:02:20 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:02:19 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:02:09 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.070 |  |
| 2025-12-15 18:02:05 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |
| 2025-12-15 18:01:43 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:36 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:32 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:32 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:01:31 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:26 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:23 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:18 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:01:17 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:10 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 18:00:44 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:00:43 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:00:13 | Horowpothana (Yan Oya) | 3.72 | 🟢 Normal | -0.074 |  |
| 2025-12-15 18:00:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:00:10 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.021 |  |
| 2025-12-15 17:17:14 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 18:03:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-15 18:02:05 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:03:42 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:23 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:02:19 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:00:44 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:06:50 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:04:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:02:27 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:00:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:31 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:32 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:17 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:02:41 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:08:16 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:43 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:04:32 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:03:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:01:36 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:06:01 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 18:03:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:02:20 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:01:32 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:01:18 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:00:43 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:06:03 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:01:10 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-15 18:04:04 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2025-12-15 18:04:44 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 18:00:10 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.021 |  |
| 2025-12-15 18:08:32 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.023 |  |
| 2025-12-15 18:06:05 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.040 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 18:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.053 |  |
| 2025-12-15 18:02:09 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.070 |  |
| 2025-12-15 18:00:13 | Horowpothana (Yan Oya) | 3.72 | 🟢 Normal | -0.074 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)