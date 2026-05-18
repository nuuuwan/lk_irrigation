# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_05:21:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,898 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 05:21:53 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:20:07 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:18:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.173 |  |
| 2026-05-18 05:16:07 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-05-18 05:13:58 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:13:56 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:11:01 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-05-18 05:07:33 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | -3.429 |  |
| 2026-05-18 05:06:51 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -3.429 |  |
| 2026-05-18 05:05:58 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-05-18 05:05:55 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:05:45 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.022 |  |
| 2026-05-18 05:05:39 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:05:37 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:05:00 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.019 |  |
| 2026-05-18 05:04:32 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:03:41 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.029 |  |
| 2026-05-18 05:03:12 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.081 |  |
| 2026-05-18 05:03:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-18 05:03:06 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:03:02 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-18 05:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-05-18 05:02:39 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.080 |  |
| 2026-05-18 05:02:23 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-05-18 05:02:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:02:00 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-05-18 05:01:46 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:01:46 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 05:01:41 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:01:28 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.102 |  |
| 2026-05-18 05:01:26 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-18 05:01:17 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.18 | 🟡 Alert | 0.000 |  |
| 2026-05-18 05:00:34 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 05:00:19 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 05:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.18 | 🟡 Alert | 0.000 |  |
| 2026-05-18 05:03:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-18 05:00:19 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-18 05:03:02 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-18 05:00:34 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 05:01:46 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 04:03:30 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:01:41 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-18 03:02:43 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:03:06 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 04:12:24 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:13:58 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:21:53 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:01:46 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:05:39 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:05:37 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 04:11:45 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-18 04:00:55 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:02:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:20:07 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-18 05:05:58 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-05-18 05:16:07 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-05-18 05:11:01 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-05-18 05:02:00 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-05-18 05:05:00 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.019 |  |
| 2026-05-18 05:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-18 05:02:23 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-05-18 05:01:26 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-18 05:05:45 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.022 |  |
| 2026-05-18 05:03:41 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.029 |  |
| 2026-05-18 05:02:39 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.080 |  |
| 2026-05-18 05:03:12 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.081 |  |
| 2026-05-18 05:01:28 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.102 |  |
| 2026-05-18 05:18:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.173 |  |
| 2026-05-18 04:09:21 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | -0.335 |  |
| 2026-05-18 05:07:33 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | -3.429 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)