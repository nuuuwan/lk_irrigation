# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_07:40:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 07:40:26 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-05-31 07:36:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.090 |  |
| 2026-05-31 07:22:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:22:26 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.008 |  |
| 2026-05-31 07:19:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:18:29 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:18:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:18:26 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:18:23 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:18:21 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:18:17 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:16:43 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.018 |  |
| 2026-05-31 07:16:15 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.054 |  |
| 2026-05-31 07:14:14 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:14:02 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-31 07:10:40 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:08:04 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.221 |  |
| 2026-05-31 07:07:30 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-05-31 07:07:13 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.019 |  |
| 2026-05-31 07:06:11 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:05:52 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:05:36 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:05:11 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.052 |  |
| 2026-05-31 07:04:18 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.093 |  |
| 2026-05-31 07:03:31 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:03:26 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:03:09 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-31 07:03:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.128 |  |
| 2026-05-31 07:02:51 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:02:23 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-05-31 07:02:11 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.051 |  |
| 2026-05-31 07:02:11 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 07:02:00 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:01:45 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:01:42 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-05-31 07:01:40 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-05-31 07:01:13 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:01:10 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-05-31 07:01:04 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:00:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:00:40 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:00:36 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 07:36:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.090 |  |
| 2026-05-31 07:02:11 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 07:01:40 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:01:04 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:05:52 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:01:45 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:06:11 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:00:40 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:02:00 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:22:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:10:40 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:03:26 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:03:57 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:00:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:02:51 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:19:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:14:14 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:03:31 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 06:05:14 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:01:13 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:05:36 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 07:22:26 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.008 |  |
| 2026-05-31 07:07:30 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-05-31 07:03:09 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-31 07:01:10 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-05-31 07:16:43 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.018 |  |
| 2026-05-31 07:07:13 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.019 |  |
| 2026-05-31 07:01:42 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-05-31 07:40:26 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-05-31 07:14:02 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-31 07:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-05-31 07:02:23 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-05-31 07:02:11 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.051 |  |
| 2026-05-31 07:05:11 | Ellagawa (Kalu Ganga) | 6.22 | 🟢 Normal | -0.052 |  |
| 2026-05-31 07:16:15 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.054 |  |
| 2026-05-31 07:00:36 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.060 |  |
| 2026-05-31 07:04:18 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.093 |  |
| 2026-05-31 07:03:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.128 |  |
| 2026-05-31 07:08:04 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)