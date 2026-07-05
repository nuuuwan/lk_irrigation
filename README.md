# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_07:11:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,710 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 07:11:40 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:09:10 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.103 |  |
| 2026-07-05 07:08:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:08:45 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:07:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.095 |  |
| 2026-07-05 07:07:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:07:33 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 07:06:39 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.298 |  |
| 2026-07-05 07:06:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-07-05 07:06:18 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.050 |  |
| 2026-07-05 07:06:13 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:06:12 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-07-05 07:06:00 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:05:20 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.022 |  |
| 2026-07-05 07:05:15 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:04:50 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:04:49 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.095 |  |
| 2026-07-05 07:04:44 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-05 07:04:19 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-07-05 07:04:05 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.066 |  |
| 2026-07-05 07:03:04 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.060 |  |
| 2026-07-05 07:02:38 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-07-05 07:02:32 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:02:06 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:02:03 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.022 |  |
| 2026-07-05 07:01:42 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.023 |  |
| 2026-07-05 07:01:30 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.010 |  |
| 2026-07-05 07:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.041 |  |
| 2026-07-05 07:01:12 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-05 07:01:12 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:00:52 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:00:47 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.004 |  |
| 2026-07-05 07:00:40 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:34:19 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 07:06:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-07-05 06:07:33 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-07-05 07:01:12 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-05 07:07:33 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 07:01:12 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:00:40 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:02:32 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:03:28 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:00:52 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:04:50 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:09:45 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:07:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:08:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:06:13 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:02:06 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:06:00 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:05:15 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:08:45 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:11:40 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:00:47 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.004 |  |
| 2026-07-05 07:04:44 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-05 07:01:30 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.010 |  |
| 2026-07-05 06:09:18 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-07-05 07:06:12 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-07-05 07:04:19 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-07-05 07:05:20 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.022 |  |
| 2026-07-05 07:02:03 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.022 |  |
| 2026-07-05 07:01:42 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.023 |  |
| 2026-07-05 07:02:38 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-07-05 07:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.041 |  |
| 2026-07-05 06:05:53 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.047 |  |
| 2026-07-05 07:06:18 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.050 |  |
| 2026-07-05 07:03:04 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.060 |  |
| 2026-07-05 07:04:05 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.066 |  |
| 2026-07-05 07:04:49 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.095 |  |
| 2026-07-05 07:07:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.095 |  |
| 2026-07-05 07:09:10 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.103 |  |
| 2026-07-05 07:06:39 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.298 |  |
| 2026-07-05 06:03:28 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)