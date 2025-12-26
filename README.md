# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_10:09:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,291 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 10:09:46 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.028 |  |
| 2025-12-26 10:09:11 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:08:46 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.046 |  |
| 2025-12-26 10:08:44 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:08:11 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.131 |  |
| 2025-12-26 10:07:29 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.012 |  |
| 2025-12-26 10:07:21 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.042 |  |
| 2025-12-26 10:06:52 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:06:11 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:06:10 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:06:00 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.035 |  |
| 2025-12-26 10:05:38 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.019 |  |
| 2025-12-26 10:05:32 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:05:16 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-26 10:05:09 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:05:04 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-26 10:04:46 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.021 |  |
| 2025-12-26 10:04:36 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.050 |  |
| 2025-12-26 10:04:22 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-26 10:04:22 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:04:14 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-26 10:03:50 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.012 |  |
| 2025-12-26 10:03:46 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:03:46 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:03:28 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:03:21 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:03:19 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:03:16 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:02:27 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:02:25 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:02:21 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2025-12-26 10:01:53 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:01:38 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.046 |  |
| 2025-12-26 10:01:33 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2025-12-26 10:00:57 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 09:16:57 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.012 |  |
| 2025-12-26 09:16:13 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.046 |  |
| 2025-12-26 09:14:12 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.035 |  |
| 2025-12-26 09:14:08 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 10:05:04 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-26 10:05:16 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-26 10:04:22 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-26 09:14:08 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-26 10:03:16 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:05:09 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:03:46 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:02:25 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:03:28 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:06:52 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:06:11 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:09:11 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:05:32 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:06:10 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:03:21 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:00:57 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 10:03:19 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:03:46 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:02:21 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:01:53 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:02:27 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:04:22 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:01:33 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:08:44 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-26 10:04:14 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-26 10:07:29 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.012 |  |
| 2025-12-26 10:03:50 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.012 |  |
| 2025-12-26 10:05:38 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.019 |  |
| 2025-12-26 09:02:53 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.019 |  |
| 2025-12-26 10:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2025-12-26 10:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2025-12-26 10:04:46 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.021 |  |
| 2025-12-26 10:09:46 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.028 |  |
| 2025-12-26 10:06:00 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.035 |  |
| 2025-12-26 10:07:21 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.042 |  |
| 2025-12-26 10:08:46 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.046 |  |
| 2025-12-26 10:01:38 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | -0.046 |  |
| 2025-12-26 10:04:36 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.050 |  |
| 2025-12-26 10:08:11 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)