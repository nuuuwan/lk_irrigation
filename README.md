# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_14:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 14:20:37 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.046 |  |
| 2026-05-14 14:13:17 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-14 14:13:15 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.037 |  |
| 2026-05-14 14:11:25 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:10:22 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-14 14:09:24 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.009 |  |
| 2026-05-14 14:08:49 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-14 14:07:52 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-14 14:07:44 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.085 |  |
| 2026-05-14 14:06:57 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-14 14:06:41 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-14 14:06:27 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:06:20 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 14:05:50 | Thanthirimale (Malwathu Oya) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:05:25 | Putupaula (Kalu Ganga) | 2.69 | 🟢 Normal | -0.011 |  |
| 2026-05-14 14:04:53 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.324 | 🔺 Rising |
| 2026-05-14 14:04:38 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-14 14:04:26 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:04:06 | Rathnapura (Kalu Ganga) | 4.23 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-14 14:03:51 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.023 |  |
| 2026-05-14 14:03:50 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-05-14 14:03:36 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:03:30 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:03:26 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-14 14:03:23 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:03:06 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-14 14:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-14 14:02:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:02:26 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-14 14:02:23 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | -0.011 |  |
| 2026-05-14 14:02:18 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:02:15 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.42 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 14:02:02 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.031 |  |
| 2026-05-14 14:01:59 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:01:57 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:01:55 | Galgamuwa (Mee Oya) | 2.18 | 🟢 Normal | -0.101 |  |
| 2026-05-14 14:01:32 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:59:17 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 14:04:53 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.324 | 🔺 Rising |
| 2026-05-14 14:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.42 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 14:03:50 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-05-14 14:04:38 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-14 14:07:52 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-14 14:04:06 | Rathnapura (Kalu Ganga) | 4.23 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-14 14:10:22 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-14 14:06:57 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-14 14:13:17 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-14 14:02:26 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-14 14:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-14 14:03:06 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-14 14:08:49 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-14 14:06:41 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-14 14:06:20 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 13:59:17 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:11:25 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:02:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:02:15 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:04:26 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:06:27 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:01:57 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-14 14:09:24 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.009 |  |
| 2026-05-14 14:03:23 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:05:50 | Thanthirimale (Malwathu Oya) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:01:32 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:01:59 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:03:36 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:02:18 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:03:30 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-14 14:02:23 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | -0.011 |  |
| 2026-05-14 14:05:25 | Putupaula (Kalu Ganga) | 2.69 | 🟢 Normal | -0.011 |  |
| 2026-05-14 14:03:26 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-14 14:03:51 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.023 |  |
| 2026-05-14 14:02:02 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.031 |  |
| 2026-05-14 14:13:15 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.037 |  |
| 2026-05-14 14:20:37 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.046 |  |
| 2026-05-14 14:07:44 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.085 |  |
| 2026-05-14 14:01:55 | Galgamuwa (Mee Oya) | 2.18 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)