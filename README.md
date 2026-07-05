# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_13:24:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,957 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 13:24:13 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:22:40 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:14:18 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.036 |  |
| 2026-07-05 13:14:00 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-07-05 13:13:37 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.047 |  |
| 2026-07-05 13:11:20 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:10:44 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:09:36 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.194 |  |
| 2026-07-05 13:09:15 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:09:12 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.063 |  |
| 2026-07-05 13:08:30 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-07-05 13:06:56 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.100 |  |
| 2026-07-05 13:06:52 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-07-05 13:06:26 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:05:50 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-07-05 13:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.29 | 🟢 Normal | -0.043 |  |
| 2026-07-05 13:05:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-07-05 13:05:07 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-07-05 13:04:38 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-07-05 13:03:50 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:03:22 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.094 |  |
| 2026-07-05 13:02:54 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-05 13:02:44 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | -0.081 |  |
| 2026-07-05 13:02:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-07-05 13:02:36 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:02:36 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.040 |  |
| 2026-07-05 13:02:21 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:02:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:01:48 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:01:37 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.021 |  |
| 2026-07-05 13:01:24 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:01:16 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 13:01:10 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:01:04 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-05 13:01:00 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-07-05 13:00:31 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 13:00:31 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 13:05:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-07-05 13:02:54 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-05 13:00:31 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 13:01:16 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 13:01:10 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:02:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:06:26 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:24:13 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:09:15 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:02:36 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:03:50 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:04:38 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:01:48 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:10:44 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:02:21 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:11:20 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:00:31 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:22:40 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:01:24 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:14:00 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-07-05 13:05:50 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-07-05 13:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-07-05 13:06:52 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-07-05 13:02:37 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-07-05 13:01:00 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-07-05 13:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.011 |  |
| 2026-07-05 13:08:30 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-07-05 13:05:07 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-07-05 13:01:04 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-05 13:01:37 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.021 |  |
| 2026-07-05 13:14:18 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.036 |  |
| 2026-07-05 13:02:36 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.040 |  |
| 2026-07-05 13:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.29 | 🟢 Normal | -0.043 |  |
| 2026-07-05 13:13:37 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.047 |  |
| 2026-07-05 13:09:12 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.063 |  |
| 2026-07-05 13:02:44 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | -0.081 |  |
| 2026-07-05 13:03:22 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.094 |  |
| 2026-07-05 13:06:56 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.100 |  |
| 2026-07-05 13:09:36 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)