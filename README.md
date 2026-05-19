# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_20:11:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 20:11:59 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:11:18 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-05-19 20:10:18 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.021 |  |
| 2026-05-19 20:09:37 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.057 |  |
| 2026-05-19 20:08:58 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-05-19 20:08:43 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:08:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.055 |  |
| 2026-05-19 20:07:59 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:07:16 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-05-19 20:06:30 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:06:27 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-19 20:06:18 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.101 |  |
| 2026-05-19 20:05:56 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-05-19 20:05:51 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.094 |  |
| 2026-05-19 20:05:24 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:04:24 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:04:16 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-05-19 20:04:00 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-19 20:03:38 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-19 20:03:14 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:03:04 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-19 20:02:56 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:02:53 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-05-19 20:02:53 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-05-19 20:02:36 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:02:29 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:02:28 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:02:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-05-19 20:01:52 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.025 |  |
| 2026-05-19 20:01:51 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:01:38 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:01:33 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-05-19 20:01:20 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.103 |  |
| 2026-05-19 20:01:11 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.022 |  |
| 2026-05-19 20:01:09 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-19 20:00:57 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-05-19 20:00:21 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 19:37:58 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | -0.057 |  |
| 2026-05-19 19:33:17 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.022 |  |
| 2026-05-19 19:25:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 20:04:00 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-19 20:03:04 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:04:24 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:07:59 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:01:51 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:02:28 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:08:43 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:03:14 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:02:56 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:11:59 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:02:29 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:05:24 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:01:38 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:00:21 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 20:11:18 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-05-19 20:08:58 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-05-19 20:01:09 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-19 20:06:27 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-19 20:03:38 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-19 20:07:16 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-05-19 20:02:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.011 |  |
| 2026-05-19 20:00:57 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-05-19 20:04:16 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-05-19 20:05:56 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 20:10:18 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.021 |  |
| 2026-05-19 20:02:53 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-05-19 20:01:11 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.022 |  |
| 2026-05-19 20:01:52 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.025 |  |
| 2026-05-19 20:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-05-19 20:01:33 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-05-19 20:08:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.055 |  |
| 2026-05-19 20:09:37 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.057 |  |
| 2026-05-19 20:05:51 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.094 |  |
| 2026-05-19 20:06:18 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.101 |  |
| 2026-05-19 20:01:20 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)