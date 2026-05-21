# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_13:26:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,884 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 13:26:12 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-05-21 13:18:44 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 13:14:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-21 13:11:54 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 13:07:00 | Glencourse (Kelani Ganga) | 9.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-21 13:06:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:05:55 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-05-21 13:05:42 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-05-21 13:05:24 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 13:04:48 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:04:46 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:04:46 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-21 13:04:39 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-21 13:04:35 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:04:18 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.047 |  |
| 2026-05-21 13:04:01 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:03:56 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.060 |  |
| 2026-05-21 13:03:46 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:03:31 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:03:10 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 13:03:08 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:02:49 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:02:48 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:02:48 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:02:38 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.030 |  |
| 2026-05-21 13:01:59 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:01:47 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:01:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:00:53 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:00:43 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:00:43 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:00:19 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.013 |  |
| 2026-05-21 13:00:18 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:56:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 13:14:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-21 13:04:46 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-21 13:04:39 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-21 13:07:00 | Glencourse (Kelani Ganga) | 9.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-21 13:03:10 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 13:05:24 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 13:11:54 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 13:18:44 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 13:00:43 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:56:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:01:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:04:35 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:02:48 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:14:43 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:04:48 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:02:49 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:06:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:02:38 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 13:01:59 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-21 12:05:35 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-05-21 13:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:04:46 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:03:08 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:04:01 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:03:31 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:00:18 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:00:43 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:01:47 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:02:48 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:03:46 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:00:53 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-05-21 13:00:19 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.013 |  |
| 2026-05-21 13:05:42 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-05-21 13:05:55 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-05-21 13:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.030 |  |
| 2026-05-21 13:26:12 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-05-21 13:04:18 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.047 |  |
| 2026-05-21 13:03:56 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)