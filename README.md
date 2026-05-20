# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_12:04:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,938 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 12:04:02 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-20 12:03:59 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:52 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:46 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:39 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:36 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:15 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-05-20 12:02:57 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-20 12:02:46 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 12:02:43 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 12:02:21 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-20 12:01:53 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-05-20 12:01:35 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-05-20 12:01:30 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:01:25 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-05-20 12:01:13 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:00:49 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:00:40 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:00:17 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 12:00:06 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 11:18:02 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 11:01:45 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-20 11:06:27 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-20 11:08:59 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-20 12:04:02 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-20 12:00:06 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 12:02:46 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 12:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 12:00:17 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 12:01:13 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:00:40 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:59 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-20 11:01:49 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:52 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:01:30 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:36 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 11:02:09 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:46 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:39 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 11:01:58 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-20 11:02:51 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 11:07:39 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 11:05:30 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:02:43 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:00:49 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 11:04:46 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.005 |  |
| 2026-05-20 12:02:21 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-20 12:02:57 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-20 11:07:17 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-05-20 12:01:53 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-05-20 11:03:54 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-20 12:01:35 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-05-20 11:12:10 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-05-20 11:07:30 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.027 |  |
| 2026-05-20 12:01:25 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-05-20 12:03:15 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-05-20 11:02:31 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.063 |  |
| 2026-05-20 11:04:38 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)