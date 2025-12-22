# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_12:11:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,796 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 12:11:25 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.058 |  |
| 2025-12-22 12:09:15 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:08:34 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:08:03 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:07:08 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:06:29 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:05:29 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:05:28 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:05:11 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:05:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-22 12:04:49 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:04:45 | Weraganthota (Mahaweli Ganga) | -0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-22 12:04:31 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:04:25 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:04:23 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:04:22 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 12:04:21 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:04:14 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:04:09 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-22 12:04:09 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.029 |  |
| 2025-12-22 12:03:52 | Manampitiya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.068 |  |
| 2025-12-22 12:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-22 12:03:32 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.014 |  |
| 2025-12-22 12:03:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:02:43 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:02:41 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2025-12-22 12:02:39 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:02:17 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:02:16 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:02:07 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2025-12-22 12:01:56 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | -0.012 |  |
| 2025-12-22 12:01:56 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:01:41 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2025-12-22 12:01:22 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:01:11 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:00:54 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:00:41 | Thanthirimale (Malwathu Oya) | 4.65 | 🟢 Normal | -0.082 |  |
| 2025-12-22 12:00:22 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:00:10 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2025-12-22 11:57:55 | Horowpothana (Yan Oya) | 3.57 | 🟢 Normal | -0.073 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 12:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-22 12:05:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-22 12:04:22 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 12:01:22 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:05:28 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:03:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:02:39 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:01:11 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:00:22 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:00:54 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:08:34 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:05:11 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:02:16 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:08:03 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:09:15 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:06:29 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:07:08 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:02:43 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:04:49 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 12:04:14 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:04:23 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:02:17 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:01:56 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:04:31 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:04:25 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2025-12-22 12:00:10 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2025-12-22 12:01:41 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2025-12-22 12:01:56 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | -0.012 |  |
| 2025-12-22 12:03:32 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.014 |  |
| 2025-12-22 12:04:45 | Weraganthota (Mahaweli Ganga) | -0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-22 12:02:41 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2025-12-22 12:04:09 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-22 12:02:07 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2025-12-22 12:04:09 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.029 |  |
| 2025-12-22 12:11:25 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.058 |  |
| 2025-12-22 12:03:52 | Manampitiya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.068 |  |
| 2025-12-22 11:57:55 | Horowpothana (Yan Oya) | 3.57 | 🟢 Normal | -0.073 |  |
| 2025-12-22 12:00:41 | Thanthirimale (Malwathu Oya) | 4.65 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)