# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_07:24:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 07:24:51 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:24:50 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:24:48 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:24:47 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:19:08 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-01 07:13:36 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:13:27 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:13:11 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:11:13 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:08:35 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-01 07:08:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-05-01 07:08:05 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.072 |  |
| 2026-05-01 07:08:01 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-05-01 07:07:19 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.056 |  |
| 2026-05-01 07:05:54 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:05:29 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-05-01 07:05:10 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.140 |  |
| 2026-05-01 07:04:57 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-01 07:04:55 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | -0.016 |  |
| 2026-05-01 07:04:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-01 07:04:37 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-01 07:03:58 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.067 |  |
| 2026-05-01 07:03:54 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.066 |  |
| 2026-05-01 07:03:40 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-01 07:03:33 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 07:03:23 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.025 |  |
| 2026-05-01 07:03:21 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-05-01 07:03:00 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-05-01 07:02:56 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-05-01 07:02:45 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:02:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:02:42 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:02:38 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-05-01 07:02:34 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-05-01 07:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.052 |  |
| 2026-05-01 07:02:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-01 07:02:12 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-05-01 07:01:48 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:01:40 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:01:27 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-01 07:01:26 | Thanthirimale (Malwathu Oya) | 2.73 | 🟢 Normal | -0.023 |  |
| 2026-05-01 07:01:26 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.013 |  |
| 2026-05-01 07:01:19 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 06:38:32 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 07:19:08 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-01 07:04:37 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-01 07:04:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-01 07:01:27 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-01 07:03:40 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-01 07:08:35 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-01 07:03:33 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 07:01:40 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:05:54 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:13:27 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:24:51 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:02:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:01:48 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:01:19 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:11:13 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:13:36 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:02:45 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-01 07:08:01 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-05-01 07:02:34 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-05-01 07:04:57 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-01 07:02:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-05-01 07:02:38 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-05-01 07:01:26 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.013 |  |
| 2026-05-01 07:04:55 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | -0.016 |  |
| 2026-05-01 07:03:21 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-05-01 07:05:29 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-05-01 07:02:12 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-05-01 07:01:26 | Thanthirimale (Malwathu Oya) | 2.73 | 🟢 Normal | -0.023 |  |
| 2026-05-01 07:03:23 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.025 |  |
| 2026-05-01 07:03:00 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-05-01 07:02:56 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-05-01 07:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.052 |  |
| 2026-05-01 07:07:19 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.056 |  |
| 2026-05-01 07:08:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-05-01 07:03:54 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.066 |  |
| 2026-05-01 07:03:58 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.067 |  |
| 2026-05-01 07:08:05 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.072 |  |
| 2026-05-01 07:05:10 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.140 |  |
| 2026-05-01 06:14:42 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)