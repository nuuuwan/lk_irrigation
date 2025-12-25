# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_11:07:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,437 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 11:07:17 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:07:08 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | -0.009 |  |
| 2025-12-25 11:06:29 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:06:12 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2025-12-25 11:05:40 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:05:22 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:04:06 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -0.070 |  |
| 2025-12-25 11:03:53 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.052 |  |
| 2025-12-25 11:03:48 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-25 11:03:46 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:03:45 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.078 |  |
| 2025-12-25 11:03:18 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-25 11:03:14 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 11:03:00 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.064 |  |
| 2025-12-25 11:02:58 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2025-12-25 11:02:49 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.084 |  |
| 2025-12-25 11:02:43 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.011 |  |
| 2025-12-25 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 11:02:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-25 11:02:10 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:02:09 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.070 |  |
| 2025-12-25 11:02:00 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2025-12-25 11:01:56 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:01:51 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-25 11:01:46 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-25 11:01:38 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:01:29 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 11:01:18 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2025-12-25 11:01:11 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2025-12-25 11:01:10 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.037 |  |
| 2025-12-25 11:00:15 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:25:19 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.078 |  |
| 2025-12-25 10:17:44 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.114 |  |
| 2025-12-25 10:16:44 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:16:02 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.034 |  |
| 2025-12-25 10:15:56 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:15:34 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.009 |  |
| 2025-12-25 10:14:39 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:13:12 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-25 10:12:53 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.037 |  |
| 2025-12-25 10:11:54 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 11:02:00 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2025-12-25 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 11:03:18 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-25 11:02:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-25 11:01:46 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-25 11:03:14 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 11:01:29 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 11:02:10 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:00:15 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:01:26 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:16:44 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:06:29 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:01:38 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:14:39 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:01:56 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:03:46 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:05:22 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:05:40 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:07:17 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-25 10:15:34 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.009 |  |
| 2025-12-25 11:07:08 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | -0.009 |  |
| 2025-12-25 11:03:48 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-25 11:01:51 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-25 11:02:43 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.011 |  |
| 2025-12-25 11:02:58 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2025-12-25 10:05:02 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.013 |  |
| 2025-12-25 11:06:12 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2025-12-25 11:01:11 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2025-12-25 11:01:18 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2025-12-25 10:16:02 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.034 |  |
| 2025-12-25 11:01:10 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.037 |  |
| 2025-12-25 11:03:53 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.052 |  |
| 2025-12-25 11:03:00 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.064 |  |
| 2025-12-25 11:04:06 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -0.070 |  |
| 2025-12-25 11:02:09 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.070 |  |
| 2025-12-25 10:06:45 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.072 |  |
| 2025-12-25 11:03:45 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.078 |  |
| 2025-12-25 11:02:49 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.084 |  |
| 2025-12-25 10:17:44 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)