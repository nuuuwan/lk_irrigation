# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_14:12:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,560 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 14:12:11 | Rathnapura (Kalu Ganga) | 4.44 | 🟢 Normal | -0.048 |  |
| 2026-05-15 14:12:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-05-15 14:10:55 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-05-15 14:10:49 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-05-15 14:10:01 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.036 |  |
| 2026-05-15 14:07:46 | Badalgama (Maha Oya) | 4.31 | 🟢 Normal | -0.067 |  |
| 2026-05-15 14:07:23 | Glencourse (Kelani Ganga) | 12.22 | 🟢 Normal | -0.195 |  |
| 2026-05-15 14:07:10 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | -0.029 |  |
| 2026-05-15 14:07:05 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.117 |  |
| 2026-05-15 14:06:53 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.256 |  |
| 2026-05-15 14:06:52 | Moragaswewa (Deduru Oya) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:06:33 | Giriulla (Maha Oya) | 3.15 | 🟢 Normal | -0.074 |  |
| 2026-05-15 14:05:50 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 14:05:22 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.063 |  |
| 2026-05-15 14:03:58 | Hanwella (Kelani Ganga) | 5.62 | 🟢 Normal | -0.118 |  |
| 2026-05-15 14:03:49 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 14:03:44 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-15 14:03:18 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:02:57 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.213 |  |
| 2026-05-15 14:02:44 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:02:41 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:02:39 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-15 14:02:31 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2026-05-15 14:02:30 | Galgamuwa (Mee Oya) | 3.92 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-15 14:02:21 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-05-15 14:02:21 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.044 |  |
| 2026-05-15 14:02:08 | Moragaswewa (Deduru Oya) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:02:04 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | -0.031 |  |
| 2026-05-15 14:01:56 | Magura (Kalu Ganga) | 4.54 | 🟡 Alert | -0.069 |  |
| 2026-05-15 14:01:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-05-15 14:01:45 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:01:37 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:01:35 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:01:17 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 14:01:06 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:00:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-05-15 14:00:45 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-05-15 14:00:41 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-05-15 14:00:17 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 14:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 14:03:49 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 14:02:04 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | -0.031 |  |
| 2026-05-15 14:01:56 | Magura (Kalu Ganga) | 4.54 | 🟡 Alert | -0.069 |  |
| 2026-05-15 14:02:30 | Galgamuwa (Mee Oya) | 3.92 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-15 14:02:39 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-15 14:01:17 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 14:00:17 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 14:02:41 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:01:06 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:06:52 | Moragaswewa (Deduru Oya) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:01:45 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:01:35 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:03:18 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:05:50 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:02:44 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:01:37 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 14:01:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-05-15 14:12:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-05-15 14:03:44 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-15 14:02:31 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2026-05-15 14:10:55 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-05-15 14:10:49 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-05-15 14:02:21 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-05-15 14:00:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-05-15 14:07:10 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | -0.029 |  |
| 2026-05-15 14:00:45 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-05-15 14:10:01 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.036 |  |
| 2026-05-15 14:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-05-15 14:02:21 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.044 |  |
| 2026-05-15 14:12:11 | Rathnapura (Kalu Ganga) | 4.44 | 🟢 Normal | -0.048 |  |
| 2026-05-15 14:05:22 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.063 |  |
| 2026-05-15 14:07:46 | Badalgama (Maha Oya) | 4.31 | 🟢 Normal | -0.067 |  |
| 2026-05-15 14:06:33 | Giriulla (Maha Oya) | 3.15 | 🟢 Normal | -0.074 |  |
| 2026-05-15 14:07:05 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.117 |  |
| 2026-05-15 14:03:58 | Hanwella (Kelani Ganga) | 5.62 | 🟢 Normal | -0.118 |  |
| 2026-05-15 14:07:23 | Glencourse (Kelani Ganga) | 12.22 | 🟢 Normal | -0.195 |  |
| 2026-05-15 14:02:57 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.213 |  |
| 2026-05-15 14:06:53 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)