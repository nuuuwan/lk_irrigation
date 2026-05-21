# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_09:10:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,725 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 09:10:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:08:20 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.256 |  |
| 2026-05-21 09:08:04 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:07:16 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.047 |  |
| 2026-05-21 09:06:38 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:06:38 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-05-21 09:06:31 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:06:03 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:06:00 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:05:49 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:05:46 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:05:22 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-21 09:05:21 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:05:20 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 09:05:01 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:04:17 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.015 |  |
| 2026-05-21 09:04:16 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-21 09:04:05 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-05-21 09:03:58 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.101 |  |
| 2026-05-21 09:03:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:03:31 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-21 09:03:26 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-21 09:03:24 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:03:11 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-05-21 09:03:00 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-21 09:02:46 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:02:41 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:02:37 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-05-21 09:02:36 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.010 |  |
| 2026-05-21 09:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 09:02:06 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.028 |  |
| 2026-05-21 09:01:58 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-05-21 09:01:53 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:01:24 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:52 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:46 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:32 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:23 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:17 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:10 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.030 |  |
| 2026-05-21 08:51:27 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 08:50:04 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 08:25:39 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 08:23:17 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 09:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 09:03:00 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-21 09:05:20 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 09:01:24 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:23 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:17 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:10:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:02:46 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:03:24 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:05:21 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:01:53 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:02:41 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:06:03 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:52 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:03:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:00:46 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:05:46 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:05:01 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:08:04 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 08:05:26 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:05:49 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:06:38 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:06:00 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 09:04:16 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-21 09:02:36 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.010 |  |
| 2026-05-21 09:03:26 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-21 09:05:22 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-21 09:03:11 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-05-21 09:04:17 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.015 |  |
| 2026-05-21 09:02:37 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-05-21 09:03:31 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-21 09:04:05 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-05-21 09:06:38 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-05-21 09:02:06 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.028 |  |
| 2026-05-21 09:00:10 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.030 |  |
| 2026-05-21 09:07:16 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.047 |  |
| 2026-05-21 09:01:58 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-05-21 09:03:58 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.101 |  |
| 2026-05-21 09:08:20 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)