# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_13:03:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,689 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 13:03:37 | Manampitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.022 |  |
| 2025-12-14 13:03:35 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:03:34 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2025-12-14 13:03:23 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:03:17 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-12-14 13:03:13 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:03:09 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:42 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | -0.344 |  |
| 2025-12-14 13:02:39 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:37 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2025-12-14 13:02:17 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:15 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:06 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:00 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 13:01:50 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:01:45 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:01:36 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.054 |  |
| 2025-12-14 13:01:23 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.069 |  |
| 2025-12-14 13:01:17 | Thanthirimale (Malwathu Oya) | 4.28 | 🟢 Normal | -0.021 |  |
| 2025-12-14 13:01:13 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-14 13:01:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:01:10 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.020 |  |
| 2025-12-14 13:01:02 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.052 |  |
| 2025-12-14 13:00:53 | Horowpothana (Yan Oya) | 4.42 | 🟢 Normal | -0.059 |  |
| 2025-12-14 13:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.041 |  |
| 2025-12-14 13:00:10 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:12:08 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:10:38 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:09:39 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:09:14 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:08:59 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.069 |  |
| 2025-12-14 12:08:11 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.022 |  |
| 2025-12-14 12:07:51 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:07:42 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:07:25 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:06:53 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:06:01 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:05:52 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2025-12-14 12:05:13 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 13:02:00 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 12:03:39 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 13:02:17 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:00:10 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:06 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:01:45 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:15 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:03:35 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:09:39 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:03:09 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:03:23 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:01:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:01:50 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:09:14 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:03:13 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:39 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:04:22 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:10:38 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 13:02:37 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-14 12:04:01 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:21 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-14 12:02:25 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2025-12-14 13:01:13 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-14 13:01:10 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.020 |  |
| 2025-12-14 13:03:17 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2025-12-14 13:01:17 | Thanthirimale (Malwathu Oya) | 4.28 | 🟢 Normal | -0.021 |  |
| 2025-12-14 12:01:21 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.022 |  |
| 2025-12-14 13:03:37 | Manampitiya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.022 |  |
| 2025-12-14 12:04:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2025-12-14 13:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2025-12-14 13:03:34 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2025-12-14 13:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.041 |  |
| 2025-12-14 13:01:02 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.052 |  |
| 2025-12-14 13:01:36 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.054 |  |
| 2025-12-14 13:00:53 | Horowpothana (Yan Oya) | 4.42 | 🟢 Normal | -0.059 |  |
| 2025-12-14 12:01:35 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.061 |  |
| 2025-12-14 13:01:23 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.069 |  |
| 2025-12-14 12:02:35 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.083 |  |
| 2025-12-14 13:02:42 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | -0.344 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)