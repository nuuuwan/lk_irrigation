# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_18:20:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,266 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 18:20:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-29 18:13:13 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-29 18:10:45 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:08:24 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 18:07:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:39 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 18:07:39 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 18:07:25 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:07 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-29 18:05:37 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:05:08 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.005 |  |
| 2025-12-29 18:04:58 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:04:14 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-29 18:04:02 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:03:53 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.031 |  |
| 2025-12-29 18:03:49 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:03:21 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 18:03:06 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:03:00 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-29 18:02:57 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 18:02:46 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 18:02:36 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:02:15 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:02:09 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.041 |  |
| 2025-12-29 18:02:02 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:01:53 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.079 |  |
| 2025-12-29 18:01:43 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-29 18:01:37 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:01:18 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:01:09 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:00:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:00:31 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:00:26 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 18:00:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 18:07:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-29 18:01:43 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-29 18:13:13 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-29 18:20:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-29 18:08:24 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 18:07:39 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 18:00:26 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 18:02:46 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 18:02:57 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 18:07:07 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 18:07:39 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 18:02:02 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:00:31 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:02:36 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:00:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:01:18 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:02:15 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:03:21 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:03:49 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:04:02 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:05:37 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:00:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:03:06 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:25 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:04:58 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:10:45 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:01:37 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:01:09 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:05:08 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.005 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-29 17:02:53 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-29 18:04:14 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-29 18:03:00 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2025-12-29 18:03:53 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.031 |  |
| 2025-12-29 18:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.041 |  |
| 2025-12-29 18:01:53 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)