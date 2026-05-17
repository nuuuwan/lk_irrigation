# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_01:38:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,758 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 01:38:25 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:37:52 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:16:38 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:16:06 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.025 |  |
| 2026-05-18 01:12:27 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -11.726 |  |
| 2026-05-18 01:09:06 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-05-18 01:08:10 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:07:20 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | -11.726 |  |
| 2026-05-18 01:06:08 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-05-18 01:06:02 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:05:48 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:05:33 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.060 |  |
| 2026-05-18 01:05:31 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:04:41 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:03:30 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:03:23 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:03:17 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-05-18 01:02:53 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:02:35 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-18 01:02:32 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:02:20 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:02:18 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:02:13 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:02:09 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 01:02:06 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:01:57 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:01:31 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 01:01:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:01:10 | Ellagawa (Kalu Ganga) | 6.91 | 🟢 Normal | -0.081 |  |
| 2026-05-18 01:00:57 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:00:16 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 21:00:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | -0.064 |  |
| 2026-05-18 00:04:52 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-05-18 00:06:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-18 01:02:35 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-18 00:17:17 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-18 01:02:09 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 01:01:31 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 01:00:16 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 01:02:13 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:05:31 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:03:23 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:38:25 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:01:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:16:38 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:02:20 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:03:30 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:02:32 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 01:08:10 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:02:18 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:02:06 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:01:57 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:00:57 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-18 01:09:06 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-05-17 22:05:40 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.019 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-18 01:05:48 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:06:02 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:04:41 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-18 01:16:06 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.025 |  |
| 2026-05-18 01:06:08 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-05-18 00:00:25 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.045 |  |
| 2026-05-18 00:04:14 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.048 |  |
| 2026-05-18 01:03:17 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-05-18 01:05:33 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.060 |  |
| 2026-05-18 01:01:10 | Ellagawa (Kalu Ganga) | 6.91 | 🟢 Normal | -0.081 |  |
| 2026-05-18 01:12:27 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -11.726 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)