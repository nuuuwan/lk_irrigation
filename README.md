# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_20:19:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 20:19:56 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:12:58 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.009 |  |
| 2025-12-19 20:09:02 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:08:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.028 |  |
| 2025-12-19 20:07:56 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:07:50 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:07:49 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:07:05 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.783 |  |
| 2025-12-19 20:06:19 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.783 |  |
| 2025-12-19 20:06:18 | Nakkala (Kumbukkan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:06:08 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:05:52 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -0.227 |  |
| 2025-12-19 20:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2025-12-19 20:05:50 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-19 20:05:48 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:05:28 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:04:28 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:04:23 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:03:49 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.049 |  |
| 2025-12-19 20:03:47 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-19 20:03:32 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:03:16 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:03:14 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.042 |  |
| 2025-12-19 20:02:46 | Glencourse (Kelani Ganga) | 9.01 | 🟢 Normal | -0.039 |  |
| 2025-12-19 20:02:46 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:02:15 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:02:09 | Manampitiya (Mahaweli Ganga) | 4.16 | 🟡 Alert | -0.042 |  |
| 2025-12-19 20:01:57 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:01:52 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 20:01:49 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:01:33 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:01:24 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:01:19 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:00:41 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:00:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.045 |  |
| 2025-12-19 19:23:28 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-19 19:00:39 | Horowpothana (Yan Oya) | 6.29 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2025-12-19 20:02:09 | Manampitiya (Mahaweli Ganga) | 4.16 | 🟡 Alert | -0.042 |  |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-19 20:05:50 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-19 20:03:47 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-19 20:01:52 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 20:01:19 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:06:18 | Nakkala (Kumbukkan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:01:49 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:19:56 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:01:33 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:07:49 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:02:46 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:00:41 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:01:57 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:06:08 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:05:28 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:05:48 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:04:23 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:09:02 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:02:15 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:03:32 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 20:12:58 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.009 |  |
| 2025-12-19 20:07:50 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:07:56 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:04:28 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:03:16 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:01:24 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | -0.010 |  |
| 2025-12-19 20:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2025-12-19 20:08:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.028 |  |
| 2025-12-19 20:02:46 | Glencourse (Kelani Ganga) | 9.01 | 🟢 Normal | -0.039 |  |
| 2025-12-19 20:03:14 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.042 |  |
| 2025-12-19 20:00:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.045 |  |
| 2025-12-19 20:03:49 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.049 |  |
| 2025-12-19 20:05:52 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -0.227 |  |
| 2025-12-19 20:07:05 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.783 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)