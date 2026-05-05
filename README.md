# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_12:29:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,513 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 12:29:29 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.015 |  |
| 2026-05-05 12:12:41 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:11:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-05 12:09:34 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:08:00 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:07:46 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:07:45 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-05-05 12:07:28 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:07:09 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:05:45 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:04:53 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-05-05 12:04:42 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:04:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:04:01 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:57 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:40 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.069 |  |
| 2026-05-05 12:03:37 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:36 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:33 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-05 12:03:31 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.112 |  |
| 2026-05-05 12:03:25 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-05 12:03:25 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:25 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:12 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:02:54 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 12:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:02:39 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:02:27 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.030 |  |
| 2026-05-05 12:02:26 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:02:20 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-05 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-05 12:02:08 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:01:45 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-05-05 12:01:32 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-05 12:01:32 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 12:01:26 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-05-05 12:01:21 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:01:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:01:15 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-05 12:01:13 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:01:11 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-05-05 12:00:42 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 12:11:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-05 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-05 12:03:33 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-05 12:01:15 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-05 12:02:54 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-05 12:01:32 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 12:03:37 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:04:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:57 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:02:08 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:04:42 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:08:00 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:12 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:05:45 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:36 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:02:39 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:01:21 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:25 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:04:01 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:07:46 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:02:26 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:03:25 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:01:13 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:09:34 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:12:41 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:07:09 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:07:45 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-05-05 12:01:32 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-05 12:03:25 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-05 12:01:45 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-05-05 12:01:11 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-05-05 12:02:20 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-05 12:29:29 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.015 |  |
| 2026-05-05 12:01:26 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-05-05 12:02:27 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.030 |  |
| 2026-05-05 12:04:53 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-05-05 12:03:40 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.069 |  |
| 2026-05-05 12:03:31 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)