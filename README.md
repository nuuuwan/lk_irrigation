# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_11:21:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,875 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 11:21:19 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-07-05 11:16:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-07-05 11:12:37 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 11:11:04 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-07-05 11:10:13 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:09:32 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:08:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:08:26 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.053 |  |
| 2026-07-05 11:08:22 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:07:37 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.039 |  |
| 2026-07-05 11:07:25 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.104 |  |
| 2026-07-05 11:07:07 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:06:00 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-07-05 11:04:54 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-05 11:04:45 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.099 |  |
| 2026-07-05 11:04:18 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:04:13 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:03:58 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.125 |  |
| 2026-07-05 11:03:52 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:03:47 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:03:37 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-07-05 11:03:32 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.080 |  |
| 2026-07-05 11:03:26 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.098 |  |
| 2026-07-05 11:02:58 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-07-05 11:02:04 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:01:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:01:38 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:01:37 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-05 11:01:20 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.030 |  |
| 2026-07-05 11:01:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:01:12 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-07-05 11:01:09 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.050 |  |
| 2026-07-05 11:00:49 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.054 |  |
| 2026-07-05 11:00:35 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-05 11:00:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 11:01:37 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-05 11:12:37 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 11:01:38 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:01:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:00:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:03:52 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:01:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:03:47 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:07:07 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:08:22 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 10:05:02 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:01:12 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:04:18 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:08:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 10:04:03 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:09:32 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:10:13 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:04:13 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:02:04 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 11:16:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | -0.009 |  |
| 2026-07-05 11:21:19 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-07-05 11:03:37 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-07-05 11:00:35 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-05 11:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-07-05 11:04:54 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-05 11:11:04 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-07-05 11:01:20 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.030 |  |
| 2026-07-05 11:06:00 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-07-05 11:07:37 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.039 |  |
| 2026-07-05 11:02:58 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-07-05 11:01:09 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.050 |  |
| 2026-07-05 11:08:26 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.053 |  |
| 2026-07-05 11:00:49 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.054 |  |
| 2026-07-05 10:01:17 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.073 |  |
| 2026-07-05 11:03:32 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.080 |  |
| 2026-07-05 11:03:26 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.098 |  |
| 2026-07-05 11:04:45 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.099 |  |
| 2026-07-05 11:07:25 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.104 |  |
| 2026-07-05 11:03:58 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)