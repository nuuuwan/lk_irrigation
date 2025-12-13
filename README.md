# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_05:09:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,375 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 05:09:00 | Horowpothana (Yan Oya) | 4.98 | 🟢 Normal | -0.093 |  |
| 2025-12-14 05:08:32 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-14 05:08:22 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 05:07:50 | Manampitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.036 |  |
| 2025-12-14 05:07:48 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.052 |  |
| 2025-12-14 05:06:54 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2025-12-14 05:06:52 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.109 |  |
| 2025-12-14 05:06:41 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -4.500 |  |
| 2025-12-14 05:06:40 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-14 05:06:09 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -4.500 |  |
| 2025-12-14 05:06:00 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 05:05:39 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:05:18 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:04:52 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:04:42 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.059 |  |
| 2025-12-14 05:04:38 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:04:13 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 05:03:30 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.036 |  |
| 2025-12-14 05:02:35 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:02:33 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-14 05:02:26 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:02:16 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:02:08 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:02:01 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:55 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:41 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.062 |  |
| 2025-12-14 05:01:16 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-14 05:01:09 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:01 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-14 05:00:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 04:43:52 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 04:20:33 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 13.714 | 🔺 Rising |
| 2025-12-14 04:20:12 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 13.714 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 04:20:33 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 13.714 | 🔺 Rising |
| 2025-12-14 05:06:54 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2025-12-14 05:08:32 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-14 05:01:16 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-14 05:06:40 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-14 05:01:01 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-14 04:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-14 05:02:33 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-14 05:06:00 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 05:08:22 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 05:04:13 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 05:02:26 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:02:16 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:41 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:04:38 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:00:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:09 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:02:01 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:04:52 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-14 05:01:55 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:05:25 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:05:39 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:02:35 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:02:08 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-14 05:05:18 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-14 04:02:23 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2025-12-14 05:03:30 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.036 |  |
| 2025-12-14 05:07:50 | Manampitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.036 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-14 05:07:48 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.052 |  |
| 2025-12-14 05:04:42 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.059 |  |
| 2025-12-14 05:01:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.062 |  |
| 2025-12-14 04:08:30 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.067 |  |
| 2025-12-14 05:09:00 | Horowpothana (Yan Oya) | 4.98 | 🟢 Normal | -0.093 |  |
| 2025-12-14 05:06:52 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.109 |  |
| 2025-12-14 05:06:41 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -4.500 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)