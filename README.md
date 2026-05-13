# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_13:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 13:13:45 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-05-13 13:08:30 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-13 13:08:13 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:07:58 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:07:57 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-05-13 13:06:58 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-13 13:06:45 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 13:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-05-13 13:05:58 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 13:05:46 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 13:05:45 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.028 |  |
| 2026-05-13 13:05:37 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.018 |  |
| 2026-05-13 13:05:24 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 1.129 | 🔺 Rising |
| 2026-05-13 13:05:16 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-13 13:05:10 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-13 13:04:02 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-13 13:03:45 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 13:03:33 | Rathnapura (Kalu Ganga) | 6.25 | 🟡 Alert | 0.114 | 🔺 Rising |
| 2026-05-13 13:03:12 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:03:01 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:02:59 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-13 13:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.147 |  |
| 2026-05-13 13:02:39 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.080 |  |
| 2026-05-13 13:02:38 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-13 13:02:31 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-13 13:02:22 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-05-13 13:02:21 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:02:13 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-05-13 13:02:05 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-13 13:02:00 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.140 |  |
| 2026-05-13 13:01:48 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:01:43 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-05-13 13:01:35 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-13 13:01:30 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:01:21 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.029 |  |
| 2026-05-13 13:01:08 | Ellagawa (Kalu Ganga) | 7.53 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-13 13:01:04 | Galgamuwa (Mee Oya) | 2.72 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-05-13 13:00:58 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-05-13 13:00:53 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | -0.086 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 13:03:33 | Rathnapura (Kalu Ganga) | 6.25 | 🟡 Alert | 0.114 | 🔺 Rising |
| 2026-05-13 13:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-05-13 13:07:57 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-05-13 13:05:24 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 1.129 | 🔺 Rising |
| 2026-05-13 13:13:45 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-05-13 13:02:22 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-05-13 13:01:43 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-05-13 13:01:04 | Galgamuwa (Mee Oya) | 2.72 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-05-13 13:00:58 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-05-13 13:01:08 | Ellagawa (Kalu Ganga) | 7.53 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-13 13:05:16 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-13 13:04:02 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-13 13:02:31 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-13 13:08:30 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-13 13:02:59 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-13 13:02:05 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-13 13:01:35 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-13 13:06:58 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-13 13:03:45 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 13:05:58 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 13:05:46 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 13:05:10 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-13 13:06:45 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 13:02:21 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:01:48 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:01:30 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:03:12 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:08:13 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:07:58 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:03:01 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 13:05:37 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.018 |  |
| 2026-05-13 13:02:38 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-13 13:05:45 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.028 |  |
| 2026-05-13 13:01:21 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.029 |  |
| 2026-05-13 13:02:13 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-05-13 13:02:39 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.080 |  |
| 2026-05-13 13:00:53 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | -0.086 |  |
| 2026-05-13 13:02:00 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.140 |  |
| 2026-05-13 13:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)