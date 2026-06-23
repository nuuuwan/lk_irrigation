# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_03:13:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,717 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 03:13:07 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:11:57 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.061 |  |
| 2026-06-24 03:11:05 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:09:16 | Ellagawa (Kalu Ganga) | 7.45 | 🟢 Normal | -270.000 |  |
| 2026-06-24 03:09:14 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 03:09:14 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -270.000 |  |
| 2026-06-24 03:08:46 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:08:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-06-24 03:07:18 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.333 |  |
| 2026-06-24 03:07:15 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -144.000 |  |
| 2026-06-24 03:07:14 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -144.000 |  |
| 2026-06-24 03:07:12 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -144.000 |  |
| 2026-06-24 03:07:03 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.018 |  |
| 2026-06-24 03:06:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:06:21 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.030 |  |
| 2026-06-24 03:06:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:06:02 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:05:57 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:05:17 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.024 |  |
| 2026-06-24 03:05:05 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:04:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:04:11 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 03:04:04 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.057 |  |
| 2026-06-24 03:04:02 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.020 |  |
| 2026-06-24 03:03:50 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-06-24 03:03:43 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-06-24 03:03:39 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.126 |  |
| 2026-06-24 03:03:11 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:03:08 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:02:58 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.045 |  |
| 2026-06-24 03:02:55 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:02:35 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.060 |  |
| 2026-06-24 03:02:30 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.031 |  |
| 2026-06-24 03:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | -0.024 |  |
| 2026-06-24 03:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:01:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-06-24 03:01:30 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:01:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:00:56 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:00:34 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:00:34 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.045 |  |
| 2026-06-24 02:50:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:39:53 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.126 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 03:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | -0.024 |  |
| 2026-06-24 03:02:35 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.060 |  |
| 2026-06-24 03:04:11 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 03:03:08 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:06:02 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:06:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:00:56 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:03:11 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:01:30 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:05:05 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:04:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:01:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:05:57 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:02:55 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:13:07 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:11:05 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:08:46 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:09:14 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 03:01:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-06-24 03:07:03 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.018 |  |
| 2026-06-24 03:04:02 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.020 |  |
| 2026-06-24 03:03:43 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-06-24 03:05:17 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.024 |  |
| 2026-06-24 03:08:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-06-24 03:06:21 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.030 |  |
| 2026-06-24 03:03:50 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-06-24 03:02:30 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.031 |  |
| 2026-06-24 03:00:34 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.045 |  |
| 2026-06-24 03:02:58 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.045 |  |
| 2026-06-24 03:04:04 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.057 |  |
| 2026-06-24 03:11:57 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.061 |  |
| 2026-06-24 03:03:39 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.126 |  |
| 2026-06-24 03:07:18 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.333 |  |
| 2026-06-24 03:07:15 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -144.000 |  |
| 2026-06-24 03:09:16 | Ellagawa (Kalu Ganga) | 7.45 | 🟢 Normal | -270.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)