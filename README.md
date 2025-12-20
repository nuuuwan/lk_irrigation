# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_08:01:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,861 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 08:01:12 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:01:10 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2025-12-20 08:00:56 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-20 08:00:52 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-20 08:00:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:20:18 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-20 07:16:07 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:13:52 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:10:37 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.059 |  |
| 2025-12-20 07:10:28 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:09:24 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:08:52 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:08:01 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-20 07:07:54 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-20 07:07:31 | Weraganthota (Mahaweli Ganga) | -0.52 | 🟢 Normal | -0.373 |  |
| 2025-12-20 07:07:21 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2025-12-20 07:07:18 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-20 07:07:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2025-12-20 07:06:49 | Padiyathalawa (Maduru Oya) | 1.62 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-20 07:06:22 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.020 |  |
| 2025-12-20 07:06:06 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.019 |  |
| 2025-12-20 07:05:46 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-20 07:05:43 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:04:37 | Manampitiya (Mahaweli Ganga) | 4.16 | 🟡 Alert | -0.038 |  |
| 2025-12-20 07:04:10 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-20 07:03:58 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-20 07:03:49 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:03:33 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:03:10 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:03:05 | Thanthirimale (Malwathu Oya) | 5.60 | 🟡 Alert | 0.005 |  |
| 2025-12-20 07:03:00 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:02:46 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2025-12-20 07:02:43 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 07:03:05 | Thanthirimale (Malwathu Oya) | 5.60 | 🟡 Alert | 0.005 |  |
| 2025-12-20 07:00:40 | Horowpothana (Yan Oya) | 6.35 | 🟡 Alert | 0.000 |  |
| 2025-12-20 07:04:37 | Manampitiya (Mahaweli Ganga) | 4.16 | 🟡 Alert | -0.038 |  |
| 2025-12-20 07:07:54 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-20 07:03:58 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-20 07:06:49 | Padiyathalawa (Maduru Oya) | 1.62 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-20 07:08:01 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-20 08:00:56 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-20 07:01:56 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:01:12 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:02:25 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:03:10 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:08:52 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:10:28 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:03:33 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:03:49 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:02:43 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:16:07 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:00:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:00:09 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:02:26 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:05:43 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:13:52 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-20 07:09:24 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:31:39 | Galgamuwa (Mee Oya) | 1.77 | 🟢 Normal | -0.007 |  |
| 2025-12-20 07:04:10 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-20 07:05:46 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-20 07:01:20 | Nakkala (Kumbukkan Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-20 07:07:21 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:00:52 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-20 07:01:42 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | -0.011 |  |
| 2025-12-20 07:06:06 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.019 |  |
| 2025-12-20 07:06:22 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.020 |  |
| 2025-12-20 07:02:46 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2025-12-20 07:07:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2025-12-20 06:07:52 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.046 |  |
| 2025-12-20 08:01:10 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2025-12-20 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.119 |  |
| 2025-12-20 07:07:31 | Weraganthota (Mahaweli Ganga) | -0.52 | 🟢 Normal | -0.373 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)