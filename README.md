# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_12:20:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,063 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 12:20:38 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:17:22 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-01-07 12:13:58 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 12:12:50 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.008 |  |
| 2026-01-07 12:09:05 | Katharagama (Menik Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-01-07 12:08:10 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-01-07 12:07:42 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:07:09 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:07:01 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-07 12:06:35 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:06:29 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:05:33 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-07 12:05:18 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:05:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:05:05 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:04:55 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:04:21 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 12:04:08 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-01-07 12:03:52 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-07 12:03:51 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:03:30 | Manampitiya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.049 |  |
| 2026-01-07 12:03:21 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:03:11 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2026-01-07 12:02:46 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-01-07 12:02:31 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.099 |  |
| 2026-01-07 12:02:26 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.019 |  |
| 2026-01-07 12:02:23 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:02:22 | Weraganthota (Mahaweli Ganga) | -1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:02:21 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.049 |  |
| 2026-01-07 12:02:17 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.080 |  |
| 2026-01-07 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:02:03 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.084 |  |
| 2026-01-07 12:01:24 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:01:21 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:01:20 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:01:11 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:01:11 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:01:08 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 12:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:00:41 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:00:31 | Siyambalanduwa (Heda Oya) | 1.72 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 12:17:22 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-01-07 12:05:33 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-07 12:07:01 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-07 12:04:21 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 12:01:08 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 12:13:58 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 12:06:29 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:02:23 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:01:11 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:05:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:04:55 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:07:42 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:01:11 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:03:21 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:03:51 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:05:05 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:07:09 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:20:38 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 12:12:50 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.008 |  |
| 2026-01-07 12:09:05 | Katharagama (Menik Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-01-07 12:05:18 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:02:22 | Weraganthota (Mahaweli Ganga) | -1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:00:41 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:01:24 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:06:35 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:01:20 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-07 12:03:52 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-07 12:08:10 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-01-07 12:02:26 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.019 |  |
| 2026-01-07 12:02:46 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-01-07 12:03:11 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2026-01-07 12:00:31 | Siyambalanduwa (Heda Oya) | 1.72 | 🟢 Normal | -0.041 |  |
| 2026-01-07 12:02:21 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.049 |  |
| 2026-01-07 12:03:30 | Manampitiya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.049 |  |
| 2026-01-07 12:02:17 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.080 |  |
| 2026-01-07 12:02:03 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.084 |  |
| 2026-01-07 12:02:31 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)