# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_04:05:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,035 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 04:05:59 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -1.200 |  |
| 2025-12-17 04:05:29 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -1.200 |  |
| 2025-12-17 04:05:17 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-17 04:05:02 | Yaka Wewa (Ma Oya) | 1.27 | 🟢 Normal | -108.000 |  |
| 2025-12-17 04:05:01 | Yaka Wewa (Ma Oya) | 1.30 | 🟢 Normal | -108.000 |  |
| 2025-12-17 04:04:58 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | -108.000 |  |
| 2025-12-17 04:04:53 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:04:48 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-17 04:04:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-17 04:03:57 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:03:45 | Horowpothana (Yan Oya) | 6.08 | 🟡 Alert | 0.000 |  |
| 2025-12-17 04:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:03:12 | Horowpothana (Yan Oya) | 6.08 | 🟡 Alert | 0.000 |  |
| 2025-12-17 04:03:09 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 04:03:01 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:02:43 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2025-12-17 04:02:32 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.106 |  |
| 2025-12-17 04:02:18 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:01:46 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | -0.010 |  |
| 2025-12-17 04:01:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2025-12-17 04:01:17 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-17 04:00:13 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:28:43 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:26:17 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.029 |  |
| 2025-12-17 03:23:03 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:17:06 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-17 03:16:50 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-17 03:11:49 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.106 |  |
| 2025-12-17 03:10:24 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.005 |  |
| 2025-12-17 03:08:16 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:08:03 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 03:07:43 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 04:03:45 | Horowpothana (Yan Oya) | 6.08 | 🟡 Alert | 0.000 |  |
| 2025-12-17 03:03:52 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2025-12-17 03:06:04 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.604 | 🔺 Rising |
| 2025-12-17 00:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2025-12-17 04:01:17 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-17 04:04:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-17 04:05:17 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-17 03:16:50 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-17 03:01:11 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 03:17:06 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-17 03:03:40 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 03:08:03 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 04:03:01 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:02:50 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:02:18 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:08:16 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:03:57 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:01:37 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 02:33:23 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:07:43 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:04:53 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:28:43 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:00:13 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 03:10:24 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.005 |  |
| 2025-12-17 04:04:48 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-17 02:03:31 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-17 04:03:09 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 04:01:46 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | -0.010 |  |
| 2025-12-17 03:03:59 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2025-12-17 04:02:43 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2025-12-17 03:26:17 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.029 |  |
| 2025-12-17 04:01:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-17 04:02:32 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.106 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |
| 2025-12-17 04:05:59 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -1.200 |  |
| 2025-12-17 04:05:02 | Yaka Wewa (Ma Oya) | 1.27 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)