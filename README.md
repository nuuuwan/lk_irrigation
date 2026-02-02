# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_15:13:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,551 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 15:13:38 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.017 |  |
| 2026-02-02 15:11:05 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:07:20 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-02-02 15:07:15 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-02-02 15:06:40 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:06:30 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.018 |  |
| 2026-02-02 15:06:00 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 15:05:43 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:05:39 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:05:32 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:53 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:39 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:37 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-02 15:04:30 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:04:28 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:03 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:03:43 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:03:29 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:03:26 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-02 15:03:15 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-02 15:03:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 15:03:06 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:02:51 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 15:02:49 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:02:49 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:02:36 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-02-02 15:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:02:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-02-02 15:01:46 | Thanthirimale (Malwathu Oya) | 2.45 | 🟢 Normal | -0.039 |  |
| 2026-02-02 15:01:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:01:21 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:01:20 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-02-02 15:01:19 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:01:05 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-02-02 15:00:54 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:00:14 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.041 |  |
| 2026-02-02 15:00:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 15:03:15 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-02 15:03:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 15:06:00 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 15:04:37 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-02 15:02:51 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-02 15:03:26 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-02 15:01:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:00:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:28 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:02:49 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:05:39 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:00:51 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:53 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:03:06 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:39 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:03:29 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:03 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:05:32 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:05:43 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:02:49 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:01:19 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-02 15:04:30 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:03:43 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:06:40 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:11:05 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:01:21 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-02-02 15:07:20 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-02-02 15:01:05 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-02-02 15:02:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-02-02 15:13:38 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.017 |  |
| 2026-02-02 15:06:30 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.018 |  |
| 2026-02-02 15:01:20 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-02-02 14:04:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-02-02 15:02:36 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-02-02 15:07:15 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-02-02 15:01:46 | Thanthirimale (Malwathu Oya) | 2.45 | 🟢 Normal | -0.039 |  |
| 2026-02-02 15:00:14 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)