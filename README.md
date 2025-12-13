# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_03:46:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,307 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 03:46:35 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:46:01 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:42:41 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:34:51 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -2.017 |  |
| 2025-12-14 03:10:53 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:10:46 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.018 |  |
| 2025-12-14 03:09:15 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2025-12-14 03:08:02 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:07:27 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2025-12-14 03:06:59 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-14 03:06:57 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-14 03:06:57 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-14 03:06:45 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2025-12-14 03:06:43 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 03:05:53 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.019 |  |
| 2025-12-14 03:05:43 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.041 |  |
| 2025-12-14 03:05:25 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-14 03:05:03 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-14 03:04:39 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:03:53 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:03:51 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:03:48 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 03:03:48 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-14 03:03:42 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -1.286 |  |
| 2025-12-14 03:03:30 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2025-12-14 03:03:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -1.286 |  |
| 2025-12-14 03:03:01 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-14 03:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -1.286 |  |
| 2025-12-14 03:02:39 | Horowpothana (Yan Oya) | 5.12 | 🟢 Normal | -6.750 |  |
| 2025-12-14 03:02:27 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:02:07 | Horowpothana (Yan Oya) | 5.18 | 🟢 Normal | -6.750 |  |
| 2025-12-14 03:02:05 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-14 03:02:03 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:01:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2025-12-14 03:01:18 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:01:06 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 03:06:59 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-14 03:03:30 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2025-12-14 03:01:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2025-12-14 03:06:45 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2025-12-14 03:06:57 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-14 03:05:03 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-14 01:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-14 03:02:05 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-14 02:08:15 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-14 03:03:48 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-14 03:03:48 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 03:03:53 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:02:03 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:03:51 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:08:02 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:01:18 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:03:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:02:27 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:04:39 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:01:06 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:10:53 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:46:35 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:42:41 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 03:09:15 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2025-12-14 03:07:27 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2025-12-14 03:05:25 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-14 03:06:43 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-14 03:03:01 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-14 01:02:44 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.012 |  |
| 2025-12-14 03:10:46 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.018 |  |
| 2025-12-14 03:05:53 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.019 |  |
| 2025-12-14 03:05:43 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.041 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-14 02:03:02 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.079 |  |
| 2025-12-14 03:03:42 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -1.286 |  |
| 2025-12-14 03:34:51 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -2.017 |  |
| 2025-12-14 03:02:39 | Horowpothana (Yan Oya) | 5.12 | 🟢 Normal | -6.750 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)