# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_17:23:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 17:23:19 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.015 |  |
| 2025-12-27 17:23:16 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:18:03 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:11:31 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:10:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:10:28 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:10:10 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2025-12-27 17:10:02 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2025-12-27 17:08:03 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-27 17:07:21 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 17:06:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2025-12-27 17:05:43 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.009 |  |
| 2025-12-27 17:05:28 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.019 |  |
| 2025-12-27 17:04:21 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-27 17:04:15 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:56 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:48 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:37 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:27 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-27 17:03:26 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:06 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2025-12-27 17:03:01 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-27 17:02:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:32 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:30 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:20 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-27 17:02:02 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2025-12-27 17:01:53 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:50 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:36 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:35 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 17:01:16 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-27 17:01:02 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2025-12-27 17:01:00 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:00:54 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-27 17:00:26 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:00:23 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:51:37 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 17:03:27 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-27 17:02:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-27 17:03:01 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-27 17:04:21 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-27 17:01:35 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 17:07:21 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 17:02:30 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:53 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:00:23 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:23:16 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:32 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:18:03 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:26 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:04:15 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:10:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:00:26 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:36 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:48 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:56 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:11:31 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:03:37 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:10:28 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:20 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:50 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:10:10 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2025-12-27 17:10:02 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2025-12-27 17:05:43 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.009 |  |
| 2025-12-27 17:08:03 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-27 17:00:54 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-27 17:01:16 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-27 17:01:02 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2025-12-27 16:51:37 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.014 |  |
| 2025-12-27 17:23:19 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.015 |  |
| 2025-12-27 17:03:06 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2025-12-27 17:05:28 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.019 |  |
| 2025-12-27 17:06:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2025-12-27 17:02:02 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)