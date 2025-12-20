# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_09:06:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,931 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 09:06:52 | Weraganthota (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-20 09:06:44 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:06:23 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:06:17 | Padiyathalawa (Maduru Oya) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-20 09:05:11 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-20 09:05:10 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:05:08 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.021 |  |
| 2025-12-20 09:05:01 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-20 09:04:52 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 09:04:41 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:04:11 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:03:54 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:03:53 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:03:18 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:03:03 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-20 09:02:57 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:57 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2025-12-20 09:02:41 | Manampitiya (Mahaweli Ganga) | 4.07 | 🟡 Alert | -0.062 |  |
| 2025-12-20 09:02:41 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | -0.020 |  |
| 2025-12-20 09:02:38 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:38 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2025-12-20 09:02:36 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:34 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:29 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:02:26 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:17 | Horowpothana (Yan Oya) | 6.32 | 🟡 Alert | -0.023 |  |
| 2025-12-20 09:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.060 |  |
| 2025-12-20 09:02:09 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:01:49 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:01:33 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:01:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:01:17 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:01:04 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:00:20 | Galgamuwa (Mee Oya) | 1.75 | 🟢 Normal | -0.024 |  |
| 2025-12-20 08:31:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2025-12-20 08:14:11 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:12:52 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:12:20 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:10:39 | Horowpothana (Yan Oya) | 6.34 | 🟡 Alert | -0.023 |  |
| 2025-12-20 08:10:37 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-20 08:10:35 | Galgamuwa (Mee Oya) | 1.77 | 🟢 Normal | -0.024 |  |
| 2025-12-20 08:10:33 | Galgamuwa (Mee Oya) | 1.77 | 🟢 Normal | -0.024 |  |
| 2025-12-20 08:08:50 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 08:04:30 | Thanthirimale (Malwathu Oya) | 5.60 | 🟡 Alert | 0.000 |  |
| 2025-12-20 09:02:17 | Horowpothana (Yan Oya) | 6.32 | 🟡 Alert | -0.023 |  |
| 2025-12-20 09:02:41 | Manampitiya (Mahaweli Ganga) | 4.07 | 🟡 Alert | -0.062 |  |
| 2025-12-20 09:06:52 | Weraganthota (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-20 09:05:11 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-20 09:06:17 | Padiyathalawa (Maduru Oya) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-20 09:04:52 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 09:05:01 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-20 09:01:17 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:01:33 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:12:52 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:38 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:03:18 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-20 08:06:17 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:01:49 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:04:41 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:05:10 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:03:54 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:57 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:01:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:26 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:34 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:02:36 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:03:53 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:06:44 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:06:23 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:04:11 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:02:29 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-20 09:02:09 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2025-12-20 08:04:52 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | -0.011 |  |
| 2025-12-20 09:03:03 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-20 09:02:41 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | -0.020 |  |
| 2025-12-20 09:02:57 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2025-12-20 09:05:08 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.021 |  |
| 2025-12-20 09:00:20 | Galgamuwa (Mee Oya) | 1.75 | 🟢 Normal | -0.024 |  |
| 2025-12-20 09:02:38 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2025-12-20 08:31:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.050 |  |
| 2025-12-20 09:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.060 |  |
| 2025-12-20 08:05:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)