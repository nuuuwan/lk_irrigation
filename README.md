# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_01:18:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 01:18:40 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:14:40 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:10:32 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-05-20 01:10:03 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.007 |  |
| 2026-05-20 01:08:54 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-20 01:07:47 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:07:13 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:06:38 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:06:19 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:06:05 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 01:04:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-20 01:04:16 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.005 |  |
| 2026-05-20 01:04:16 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:04:12 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:04:07 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:03:45 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-05-20 01:03:37 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.011 |  |
| 2026-05-20 01:03:36 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-20 01:03:15 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:02:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:02:41 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 01:02:35 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:02:29 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-05-20 01:02:04 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:01:45 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:01:39 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.011 |  |
| 2026-05-20 01:01:21 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-20 01:01:03 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-05-20 01:00:48 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:00:36 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:00:29 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:00:15 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:59:40 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:56:35 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 01:03:45 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-05-20 01:04:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-20 01:01:21 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-20 01:03:36 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-20 01:02:41 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 01:06:05 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:00:29 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:18:40 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:02:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:06:38 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:04:07 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:14:40 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:02:04 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:00:15 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:00:48 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:01:45 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:51 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:03:23 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:04:16 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-20 01:04:16 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.005 |  |
| 2026-05-20 01:10:03 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.007 |  |
| 2026-05-20 01:08:54 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-20 01:06:19 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:04:12 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:07:47 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:02:35 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:00:36 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-20 01:01:03 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-05-20 01:03:37 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.011 |  |
| 2026-05-20 01:01:39 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.011 |  |
| 2026-05-20 00:38:09 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.012 |  |
| 2026-05-20 01:02:29 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-05-20 01:10:32 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.017 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 21:18:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.052 |  |
| 2026-05-20 00:02:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)