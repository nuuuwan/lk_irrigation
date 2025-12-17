# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_08:01:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,173 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 08:01:45 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:39 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:25 | Horowpothana (Yan Oya) | 5.94 | 🟢 Normal | -0.046 |  |
| 2025-12-17 08:01:16 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:13 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-17 08:01:10 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2025-12-17 08:01:08 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:00:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.046 |  |
| 2025-12-17 07:53:15 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.006 |  |
| 2025-12-17 07:26:20 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:25:23 | Moragaswewa (Deduru Oya) | 1.33 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-17 07:24:08 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:13:43 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:11:59 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:11:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:09:36 | Horowpothana (Yan Oya) | 5.98 | 🟢 Normal | -0.046 |  |
| 2025-12-17 07:09:17 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2025-12-17 07:08:47 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:08:44 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:08:29 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.046 |  |
| 2025-12-17 07:07:56 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:06:40 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2025-12-17 07:05:54 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:05:53 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 07:05:39 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-17 07:05:20 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.021 |  |
| 2025-12-17 07:05:08 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:04:22 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:04:13 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-17 07:04:13 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.016 |  |
| 2025-12-17 07:04:11 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.019 |  |
| 2025-12-17 07:03:58 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.065 |  |
| 2025-12-17 07:03:47 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:03:46 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.030 |  |
| 2025-12-17 07:03:13 | Thanthirimale (Malwathu Oya) | 3.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-17 07:03:12 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 07:03:11 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:03:10 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 07:04:13 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-17 07:05:39 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-17 07:25:23 | Moragaswewa (Deduru Oya) | 1.33 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-17 07:03:13 | Thanthirimale (Malwathu Oya) | 3.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-17 07:05:53 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 07:03:12 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 07:01:13 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:01:20 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:24:08 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:01:22 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:45 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:13:43 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:05:08 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:11:59 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:39 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:08:44 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:11:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:03:11 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:08 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:08:47 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:01:16 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:02:20 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:26:20 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:03:47 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:05:54 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 07:53:15 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.006 |  |
| 2025-12-17 07:09:17 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2025-12-17 07:03:10 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.010 |  |
| 2025-12-17 08:01:13 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-17 07:04:13 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.016 |  |
| 2025-12-17 07:04:11 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.019 |  |
| 2025-12-17 08:01:10 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2025-12-17 07:03:46 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.030 |  |
| 2025-12-17 08:01:25 | Horowpothana (Yan Oya) | 5.94 | 🟢 Normal | -0.046 |  |
| 2025-12-17 08:00:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.046 |  |
| 2025-12-17 07:03:58 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.065 |  |
| 2025-12-17 07:02:15 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.084 |  |
| 2025-12-17 07:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.110 |  |
| 2025-12-17 07:01:11 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | -14.400 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)