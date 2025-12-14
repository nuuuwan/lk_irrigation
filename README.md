# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_18:08:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,900 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 18:08:28 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:07:26 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:06:51 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:46 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-14 18:05:37 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-14 18:05:22 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.044 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:07 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:04:52 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.087 |  |
| 2025-12-14 18:04:20 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-14 18:04:07 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:04:06 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:03:43 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:03:37 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2025-12-14 18:03:26 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:03:24 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 18:03:23 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:03:11 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.038 |  |
| 2025-12-14 18:03:08 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:02:58 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-14 18:02:54 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:02:43 | Horowpothana (Yan Oya) | 4.26 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:02:35 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:02:28 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 18:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.040 |  |
| 2025-12-14 18:01:59 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.082 |  |
| 2025-12-14 18:01:55 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2025-12-14 18:01:54 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-14 18:01:51 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.030 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:22 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:07 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:05 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2025-12-14 18:01:00 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:00:46 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:00:43 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 18:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 18:00:08 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 18:01:05 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2025-12-14 18:03:37 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2025-12-14 18:05:37 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-14 18:04:20 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-14 18:02:58 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-14 18:05:46 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-14 18:02:28 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 18:00:43 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 18:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 18:03:24 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 18:00:08 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:00:46 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:03:43 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:22 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:08:28 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:02:35 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:07 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:07:26 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:05:07 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:03:26 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:02:43 | Horowpothana (Yan Oya) | 4.26 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:06:51 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:04:06 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:03:08 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:02:54 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:03:23 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:01:00 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:01:54 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-14 18:01:51 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.030 |  |
| 2025-12-14 18:03:11 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.038 |  |
| 2025-12-14 18:01:55 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.040 |  |
| 2025-12-14 18:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.040 |  |
| 2025-12-14 18:05:22 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.044 |  |
| 2025-12-14 18:01:59 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.082 |  |
| 2025-12-14 18:04:52 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)