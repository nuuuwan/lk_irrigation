# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_11:06:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,695 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 11:06:30 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:06:08 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.029 |  |
| 2025-12-13 11:06:04 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.011 |  |
| 2025-12-13 11:05:14 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-13 11:04:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2025-12-13 11:04:40 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.019 |  |
| 2025-12-13 11:04:38 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.031 |  |
| 2025-12-13 11:04:28 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-13 11:04:21 | Weraganthota (Mahaweli Ganga) | -0.78 | 🟢 Normal | -0.147 |  |
| 2025-12-13 11:04:06 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-13 11:03:45 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:03:43 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 11:03:06 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.051 |  |
| 2025-12-13 11:03:06 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2025-12-13 11:02:47 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:02:34 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:02:16 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2025-12-13 11:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | -0.051 |  |
| 2025-12-13 11:02:14 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:02:05 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:01:55 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-13 11:01:45 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.050 |  |
| 2025-12-13 11:01:26 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 11:01:14 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.031 |  |
| 2025-12-13 11:01:09 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:01:08 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2025-12-13 11:01:01 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-13 11:00:57 | Horowpothana (Yan Oya) | 5.88 | 🟢 Normal | -0.040 |  |
| 2025-12-13 10:41:50 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.031 |  |
| 2025-12-13 10:29:20 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.007 |  |
| 2025-12-13 10:13:01 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:12:56 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.045 |  |
| 2025-12-13 10:11:09 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.011 |  |
| 2025-12-13 10:11:02 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2025-12-13 10:09:36 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:09:21 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2025-12-13 10:09:04 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 11:03:43 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 11:01:26 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-13 11:02:47 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:02:34 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:02:14 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:01:14 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:06:30 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:02:05 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-13 11:03:45 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:05:51 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:13:01 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:09:36 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:02:41 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:03:58 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 10:29:20 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.007 |  |
| 2025-12-13 10:05:59 | Thanthirimale (Malwathu Oya) | 4.21 | 🟢 Normal | -0.009 |  |
| 2025-12-13 11:04:06 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-13 11:04:28 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-13 11:01:55 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-13 11:01:01 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-13 11:02:16 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2025-12-13 11:04:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2025-12-13 11:06:04 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.011 |  |
| 2025-12-13 10:11:02 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2025-12-13 11:04:40 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.019 |  |
| 2025-12-13 11:05:14 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-13 11:03:06 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2025-12-13 11:06:08 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.029 |  |
| 2025-12-13 11:04:38 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.031 |  |
| 2025-12-13 11:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.031 |  |
| 2025-12-13 11:00:57 | Horowpothana (Yan Oya) | 5.88 | 🟢 Normal | -0.040 |  |
| 2025-12-13 10:12:56 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.045 |  |
| 2025-12-13 11:01:45 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.050 |  |
| 2025-12-13 11:03:06 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.051 |  |
| 2025-12-13 11:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | -0.051 |  |
| 2025-12-13 11:01:08 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2025-12-13 10:06:16 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.066 |  |
| 2025-12-13 10:04:45 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.147 |  |
| 2025-12-13 11:04:21 | Weraganthota (Mahaweli Ganga) | -0.78 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)