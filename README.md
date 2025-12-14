# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_11:10:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,621 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 11:10:51 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.053 |  |
| 2025-12-14 11:08:15 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:07:58 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:07:54 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.076 |  |
| 2025-12-14 11:07:17 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:07:13 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:06:17 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:05:41 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:05:26 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | -0.029 |  |
| 2025-12-14 11:05:12 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.010 |  |
| 2025-12-14 11:04:49 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.156 |  |
| 2025-12-14 11:03:59 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:03:45 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:03:39 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.032 |  |
| 2025-12-14 11:03:30 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2025-12-14 11:03:28 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2025-12-14 11:03:16 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-14 11:03:09 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:02:51 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.084 |  |
| 2025-12-14 11:02:49 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:02:44 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | -0.016 |  |
| 2025-12-14 11:02:39 | Weraganthota (Mahaweli Ganga) | -1.11 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2025-12-14 11:02:24 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:02:23 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-14 11:02:12 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-14 11:02:10 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2025-12-14 11:02:08 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.050 |  |
| 2025-12-14 11:02:07 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-14 11:02:05 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:01:47 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.020 |  |
| 2025-12-14 11:01:33 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:01:26 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.011 |  |
| 2025-12-14 11:01:19 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:01:13 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 11:00:57 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2025-12-14 11:00:56 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:00:42 | Horowpothana (Yan Oya) | 4.53 | 🟢 Normal | -0.040 |  |
| 2025-12-14 11:00:33 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:25:59 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.016 |  |
| 2025-12-14 10:23:23 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 10:19:27 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 11:02:39 | Weraganthota (Mahaweli Ganga) | -1.11 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2025-12-14 11:02:07 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-14 11:01:13 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 11:01:19 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:00:33 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:01:33 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:02:05 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:03:45 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:06:17 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:00:56 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:03:59 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:07:13 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:03:09 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:02:24 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:02:49 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:05:26 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:07:58 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:08:15 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:05:41 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-14 11:03:16 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-14 11:02:12 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-14 11:02:23 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-14 11:05:12 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.010 |  |
| 2025-12-14 11:01:26 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.011 |  |
| 2025-12-14 11:02:44 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | -0.016 |  |
| 2025-12-14 11:01:47 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.020 |  |
| 2025-12-14 11:03:30 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2025-12-14 11:02:10 | Manampitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2025-12-14 11:00:57 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2025-12-14 11:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | -0.029 |  |
| 2025-12-14 11:03:39 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.032 |  |
| 2025-12-14 11:00:42 | Horowpothana (Yan Oya) | 4.53 | 🟢 Normal | -0.040 |  |
| 2025-12-14 11:03:28 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2025-12-14 11:02:08 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.050 |  |
| 2025-12-14 11:10:51 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.053 |  |
| 2025-12-14 11:07:54 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.076 |  |
| 2025-12-14 11:02:51 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.084 |  |
| 2025-12-14 11:04:49 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)