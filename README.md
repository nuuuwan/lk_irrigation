# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_01:43:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,325 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 01:43:26 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.014 |  |
| 2025-12-13 01:32:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-13 01:10:23 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2025-12-13 01:07:32 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:07:17 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:07:08 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:06:13 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:06:12 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:06:10 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -3.005 |  |
| 2025-12-13 01:05:47 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:05:47 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:05:42 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:05:23 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:05:16 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -4.696 |  |
| 2025-12-13 01:04:30 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -4.696 |  |
| 2025-12-13 01:04:26 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:03:35 | Horowpothana (Yan Oya) | 6.31 | 🟡 Alert | -0.039 |  |
| 2025-12-13 01:03:17 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:02:50 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:02:39 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:02:33 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:02:27 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 01:02:27 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 01:02:08 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:56 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:01:47 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:41 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 01:01:40 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:27 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:01:23 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:00:29 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.105 |  |
| 2025-12-13 00:58:24 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 01:03:35 | Horowpothana (Yan Oya) | 6.31 | 🟡 Alert | -0.039 |  |
| 2025-12-12 23:05:26 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-13 00:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-13 01:32:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-13 01:02:27 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 01:02:27 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 01:01:41 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 01:02:39 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:02:33 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:07:08 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 01:05:47 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:57 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:07:32 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:47 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:06:13 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:01:40 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:05:23 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:07:17 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:02:08 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:04:53 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:05:47 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:06:12 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-13 00:05:42 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-13 01:10:23 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2025-12-13 01:01:56 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:03:17 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:01:23 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:01:27 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:43:26 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.014 |  |
| 2025-12-13 00:03:57 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-12-13 00:58:24 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2025-12-13 00:00:56 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.055 |  |
| 2025-12-13 01:00:29 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.105 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-13 00:31:30 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.450 |  |
| 2025-12-13 01:06:10 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -3.005 |  |
| 2025-12-13 01:05:16 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)