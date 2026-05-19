# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_21:18:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,410 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 21:18:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.052 |  |
| 2026-05-19 21:16:32 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.008 |  |
| 2026-05-19 21:15:30 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:13:00 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-05-19 21:10:21 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:08:49 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.018 |  |
| 2026-05-19 21:07:16 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:06:51 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:06:27 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:06:16 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-05-19 21:06:06 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:06:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.085 |  |
| 2026-05-19 21:06:00 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:05:46 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-05-19 21:05:32 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:05:25 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:05:19 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:04:48 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.123 |  |
| 2026-05-19 21:04:31 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:04:13 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:03:57 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:03:56 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-19 21:03:55 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:03:16 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:03:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:02:45 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:02:42 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:02:35 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-19 21:02:08 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:01:11 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.035 |  |
| 2026-05-19 21:01:08 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-19 21:01:08 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.023 |  |
| 2026-05-19 21:01:03 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:00:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 21:00:44 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:00:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 21:02:35 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-19 21:01:08 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-19 21:03:56 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-19 21:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:00:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:00:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:07:16 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:15:30 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:05:19 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:03:16 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:04:31 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:00:44 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:03:55 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:03:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:10:21 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:01:03 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:06:51 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:06:00 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:04:13 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:02:45 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 21:16:32 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.008 |  |
| 2026-05-19 21:13:00 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-05-19 21:03:57 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:05:25 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:02:42 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:02:08 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:06:06 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:06:27 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-05-19 21:05:46 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-05-19 21:08:49 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.018 |  |
| 2026-05-19 21:06:16 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 21:01:08 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.023 |  |
| 2026-05-19 21:01:11 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.035 |  |
| 2026-05-19 21:18:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.052 |  |
| 2026-05-19 21:06:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.085 |  |
| 2026-05-19 21:04:48 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)