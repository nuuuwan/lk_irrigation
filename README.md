# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_06:39:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,938 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 06:39:09 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.005 |  |
| 2026-05-18 06:23:01 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:12:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:08:30 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-18 06:07:37 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:07:13 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:06:52 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.151 |  |
| 2026-05-18 06:06:39 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.030 |  |
| 2026-05-18 06:06:18 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:05:56 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-05-18 06:05:51 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.038 |  |
| 2026-05-18 06:05:18 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.024 |  |
| 2026-05-18 06:04:56 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-18 06:04:51 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:04:35 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:04:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.005 |  |
| 2026-05-18 06:03:46 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:03:26 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-18 06:03:23 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-05-18 06:03:03 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-18 06:02:48 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.023 |  |
| 2026-05-18 06:02:47 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.014 |  |
| 2026-05-18 06:02:24 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-05-18 06:02:15 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-05-18 06:02:10 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-05-18 06:01:59 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.061 |  |
| 2026-05-18 06:01:51 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | -0.079 |  |
| 2026-05-18 06:01:45 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-18 06:01:42 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.071 |  |
| 2026-05-18 06:01:19 | Putupaula (Kalu Ganga) | 2.27 | 🟢 Normal | -0.096 |  |
| 2026-05-18 06:01:12 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-18 06:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.06 | 🟡 Alert | -0.120 |  |
| 2026-05-18 06:00:52 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:00:42 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-18 06:00:41 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-18 06:00:38 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:00:12 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 06:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.06 | 🟡 Alert | -0.120 |  |
| 2026-05-18 06:03:03 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-18 06:08:30 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-18 06:04:56 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-18 06:00:12 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 06:00:42 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-18 06:39:09 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.005 |  |
| 2026-05-18 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:06:18 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:03:46 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:04:51 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:00:38 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:07:13 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:04:35 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:00:52 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:12:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:07:37 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:23:01 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 06:04:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.005 |  |
| 2026-05-18 06:05:56 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-05-18 06:01:12 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-18 06:00:41 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-18 06:03:26 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-18 06:03:23 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-05-18 06:02:47 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.014 |  |
| 2026-05-18 06:01:45 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-18 06:02:15 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-18 06:02:10 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-05-18 06:02:48 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.023 |  |
| 2026-05-18 06:05:18 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.024 |  |
| 2026-05-18 06:06:39 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.030 |  |
| 2026-05-18 06:02:24 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-05-18 06:05:51 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.038 |  |
| 2026-05-18 06:01:59 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.061 |  |
| 2026-05-18 06:01:42 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.071 |  |
| 2026-05-18 06:01:51 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | -0.079 |  |
| 2026-05-18 06:01:19 | Putupaula (Kalu Ganga) | 2.27 | 🟢 Normal | -0.096 |  |
| 2026-05-18 06:06:52 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)